from .eventobject import EventObject, TraceObject, EventBlock, MetadataBlock, StackBlock, SequencePointBlock, EventTag

class EventStream:

    Factories = { 'Trace': TraceObject, 'EventBlock': EventBlock, 'MetadataBlock': MetadataBlock, 'StackBlock': StackBlock,  'SPBlock': SequencePointBlock }

    def __init__(self):
        self.object_depth = 0

    def read(self, buf, obj=None):
        tag = int.from_bytes(buf.read(1), byteorder='little')

        if tag == EventTag.BEGIN_PRIVATE_OBJECT:
            self.object_depth += 1
            return self.read(buf, obj)
        elif tag == EventTag.NULL_REFERENCE:
            if self.object_depth == 0: return None

            version = int.from_bytes(buf.read(4), byteorder='little')
            min_reader_ver = int.from_bytes(buf.read(4), byteorder='little')
            name_len = int.from_bytes(buf.read(4), byteorder='little')
            name = buf.read(name_len).decode()

            return self.read(buf, EventObject(name, version, min_reader_ver))

        elif tag == EventTag.END_OBJECT:
            self.object_depth -= 1
            if self.object_depth == 0: return obj
            if obj is not None and obj.name in EventStream.Factories.keys():
                    obj = EventStream.Factories[obj.name](name=obj.name, version=obj.version, min_reader_ver=obj.min_reader_ver)
                    obj.read(buf)
            return self.read(buf, obj)
        else:
            raise Exception("Unknown EventObject Tag!")

