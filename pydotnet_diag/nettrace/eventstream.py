from .eventobject import BlockFactories, EventTag, EventObject
from . import parsers
import io

class EventStream:

    def __init__(self):
        self.object_depth = 0
        self.trace = None
        self.metadata = {}
        self.events = []
        self.stacks = []
        self.sequence_points = []

    def read(self, buf):
        while obj := self.read_objects(buf):
            if obj.name == 'Trace':
                self.trace = obj
            elif obj.name == 'EventBlock':
                self.events.extend(obj.events)
            elif obj.name == 'MetadataBlock':
                for evt in obj.events:
                    self.metadata[evt.payload.id] = evt.payload
            elif obj.name == 'StackBlock':
                self.stacks.extend(obj.stacks)
            elif obj.name == 'SPBlock':
                self.sequence_points.extend(obj.threads)

        for event in self.events:
            if event.payload_decoded: continue
            metadata = self.metadata[event.metadata_id]
            parser = f"read_{metadata.provider_name.replace('-', '_')}_{metadata.event_id}_payload"
            if hasattr(parsers, parser):
                event.payload = eval(f"parsers.{parser}")(io.BytesIO(event.payload))

        for id in self.metadata.keys():
            metadata = self.metadata[id]
            if metadata.event_name is None or metadata.event_name == '':
                parser = f"get_{metadata.provider_name.replace('-', '_')}_{metadata.event_id}_op_code"
                if hasattr(parsers, parser):
                    metadata.event_name = eval(f"parsers.{parser}")()



    def read_objects(self, buf, obj=None):
        tag = int.from_bytes(buf.read(1), byteorder='little')

        if tag == EventTag.BEGIN_PRIVATE_OBJECT:
            self.object_depth += 1
            return self.read_objects(buf, obj)
        elif tag == EventTag.NULL_REFERENCE:
            if self.object_depth == 0: return None

            version = int.from_bytes(buf.read(4), byteorder='little')
            min_reader_ver = int.from_bytes(buf.read(4), byteorder='little')
            name_len = int.from_bytes(buf.read(4), byteorder='little')
            name = buf.read(name_len).decode()

            return self.read_objects(buf, EventObject(name, version, min_reader_ver))

        elif tag == EventTag.END_OBJECT:
            self.object_depth -= 1
            if self.object_depth == 0: return obj
            if obj is not None and obj.name in BlockFactories.keys():
                    obj = BlockFactories[obj.name](name=obj.name, version=obj.version, min_reader_ver=obj.min_reader_ver)
                    obj.read(buf)
            return self.read_objects(buf, obj)
        else:
            raise Exception("Unknown EventObject Tag!")

