import io
from enum import IntEnum
from uuid import UUID
from .nettypecode import NetTypeCode
from . import utils
from . import parsers

BlockFactories = {}

class EventTag(IntEnum):
    NULL_REFERENCE = 0x01
    BEGIN_PRIVATE_OBJECT = 0x05
    END_OBJECT = 0x06

class EventObject:

    def __init_subclass__(cls, is_factory=True, factory_name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if not is_factory: return
        factory_name = factory_name or cls.__name__
        if factory_name not in BlockFactories.keys(): BlockFactories[factory_name] = cls

    def __init__(self, name=None, version=0, min_reader_ver=0):
        self.name = name or self.__class__.__name__
        self.version = version
        self.min_reader_ver = min_reader_ver


class TraceObject(EventObject, factory_name='Trace'):

    def __init__(self, name=None, version=0, min_reader_ver=0):
        super().__init__(name, version, min_reader_ver)
        self.year = 0
        self.month = 0
        self.day_of_week = 0
        self.day = 0
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.millisecond = 0
        self.sync_time_qpc = 0
        self.qpc_freq = 0
        self.pointer_size = 0
        self.process_id = 0
        self.number_of_proc = 0
        self.expected_cpu_sampling_rate = 0

    def read(self, buf):
        self.year = int.from_bytes(buf.read(2), byteorder='little')
        self.month = int.from_bytes(buf.read(2), byteorder='little')
        self.day_of_week = int.from_bytes(buf.read(2), byteorder='little')
        self.day = int.from_bytes(buf.read(2), byteorder='little')
        self.hour = int.from_bytes(buf.read(2), byteorder='little')
        self.minute = int.from_bytes(buf.read(2), byteorder='little')
        self.second = int.from_bytes(buf.read(2), byteorder='little')
        self.millisecond = int.from_bytes(buf.read(2), byteorder='little')
        self.sync_time_qpc = int.from_bytes(buf.read(8), byteorder='little')
        self.qpc_freq = int.from_bytes(buf.read(8), byteorder='little')
        self.pointer_size = int.from_bytes(buf.read(4), byteorder='little')
        self.process_id = int.from_bytes(buf.read(4), byteorder='little')
        self.number_of_proc = int.from_bytes(buf.read(4), byteorder='little')
        self.expected_cpu_sampling_rate = int.from_bytes(buf.read(4), byteorder='little')


class Block(EventObject, is_factory=False):

    def __init__(self, name=None, version=0, min_reader_ver=0):
        super().__init__(name, version, min_reader_ver)

    def read(self, buf):
        self.block_size = int.from_bytes(buf.read(4), byteorder='little')
        self.align(buf, 4)
        self.end_of_block = buf.tell() + self.block_size

    def align(self, buf, bound):
        align = buf.tell() % bound
        if align != 0: buf.seek(bound - align, io.SEEK_CUR)

    def decode_payload(self, payload):
        pass

    @staticmethod
    def read_var_int(buf):
        ret = 0
        shift = 0
        while True:
            b = buf.read(1)[0]
            ret |= ((b & 0x7F) << shift)
            shift += 7
            if not (b & 0x80): break
        return ret

class EventBlob:

    def __init__(self):
        self.event_size = 0
        self.metadata_id = 0
        self.seq = 0
        self.thread_id = 0
        self.capture_thread_id = 0
        self.processor_num = 0
        self.stack_id = 0
        self.timestamp = 0
        self.activity_id = UUID(int=0)
        self.related_activity_id = UUID(int=0)
        self.is_sorted = False
        self.payload_size = 0
        self.payload = None
        self.payload_decoded = False

class EventBlock(Block):

    def __init__(self, name=None, version=0, min_reader_ver=0):
        super().__init__(name, version, min_reader_ver)
        self.flags = 0x00
        self.min_timestamp = 0
        self.max_timestamp = 0
        self.events = []

    def read(self, buf):
        super().read(buf)
        header_size = int.from_bytes(buf.read(2), byteorder='little')
        end_of_header = (buf.tell() - 2) + header_size
        self.flags = int.from_bytes(buf.read(2), byteorder='little')
        self.header_compressed = self.flags & 0x01 == 0x01
        self.min_timestamp = int.from_bytes(buf.read(8), byteorder='little')
        self.max_timestamp = int.from_bytes(buf.read(8), byteorder='little')

        buf.seek(end_of_header, io.SEEK_SET)

        while buf.tell() < self.end_of_block:
            prev_event = self.events[-1] if len(self.events) != 0 else EventBlob()
            if self.header_compressed:
                 self.events.append(self.read_compressed_event(buf, prev_event))
            else:
                 self.events.append(self.read_event(buf))

    def read_event(self, buf):
        event = EventBlob()
        event.event_size = int.from_bytes(buf.read(4), byteorder='little')
        event.metadata_id = int.from_bytes(buf.read(4), byteorder='little')
        event.is_sorted = event.metadata_id & 0x80000000
        event.metadata_id &= 0x7FFFFFFF
        event.seq = int.from_bytes(buf.read(4), byteorder='little')
        event.thread_id = int.from_bytes(buf.read(8), byteorder='little')
        event.capture_thread_id = int.from_bytes(buf.read(8), byteorder='little')
        event.processor_num = int.from_bytes(buf.read(4), byteorder='little')
        event.stack_id = int.from_bytes(buf.read(4), byteorder='little')
        event.timestamp = int.from_bytes(buf.read(8), byteorder='little')
        event.activity_id = UUID(bytes_le=buf.read(16))
        event.related_activity_id = UUID(bytes_le=buf.read(16))
        event.payload_size = int.from_bytes(buf.read(4), byteorder='little')
        event.payload = self.decode_payload(buf.read(event.payload_size))
        event.align(buf, 4)
        return event


    def read_compressed_event(self, buf, prev_event):
        event = EventBlob()
        flags = buf.read(1)[0]
        event.metadata_id = Block.read_var_int(buf) if flags & 0x01 else prev_event.metadata_id
        event.seq = prev_event.seq + Block.read_var_int(buf) if flags & 0x02 else prev_event.seq
        if not flags & 0x02 and event.metadata_id != 0: event.seq += 1
        event.capture_thread_id = Block.read_var_int(buf) if flags & 0x02 else prev_event.capture_thread_id
        event.processor_num = Block.read_var_int(buf) if flags & 0x02 else prev_event.processor_num
        event.thread_id = Block.read_var_int(buf) if flags & 0x04 else prev_event.thread_id
        event.stack_id = Block.read_var_int(buf) if flags & 0x08 else prev_event.stack_id
        event.timestamp = prev_event.timestamp + Block.read_var_int(buf)
        event.activity_id = UUID(bytes_le=buf.read(16)) if flags & 0x10 else prev_event.activity_id
        event.related_activity_id = UUID(bytes_le=buf.read(16)) if flags & 0x20 else prev_event.related_activity_id
        if flags & 0x40: event.is_sorted = True
        event.payload_size = Block.read_var_int(buf) if flags & 0x80 else prev_event.payload_size
        event.payload = self.decode_payload(buf.read(event.payload_size))
        return event

    def decode_payload(self, buf):
        return buf

class Metadata:

    def __init__(self):
        self.id = 0
        self.provider_name = None
        self.event_id = 0
        self.event_name = None
        self.keywords = 0
        self.version = 0
        self.level = 0
        self.field_count = 0
        self.fields = []

class MetadataField:

    def __init__(self):
        self.type_code = None
        self.name = None
        self.field_count = 0
        self.fields = []

    def read(self, buf):
        self.type_code = int.from_bytes(buf.read(4), byteorder='little')
        if self.type_code == NetTypeCode.OBJECT:
            self.read_fields(buf)
        self.name = utils.bytes_to_nuluni(buf)

    def read_fields(self, buf):
        self.field_count = int.from_bytes(buf.read(4), byteorder='little')
        for i in range(self.field_count):
            fields.append(MetadataField())
            fields[-1].read(buf)

class MetadataBlock(EventBlock):

    def __init__(self, name=None, version=0, min_reader_ver=0):
        super().__init__(name, version, min_reader_ver)

    def read(self, buf):
        super().read(buf)

    def decode_payload(self, payload):
        metadata = Metadata()
        buf = io.BytesIO(payload)
        metadata.id = int.from_bytes(buf.read(4), byteorder='little')
        metadata.provider_name = utils.bytes_to_nuluni(buf)
        metadata.event_id = int.from_bytes(buf.read(4), byteorder='little')
        metadata.event_name = utils.bytes_to_nuluni(buf)
        metadata.keywords = int.from_bytes(buf.read(8), byteorder='little')
        metadata.version = int.from_bytes(buf.read(4), byteorder='little')
        metadata.level = int.from_bytes(buf.read(4), byteorder='little')
        metadata.field_count = int.from_bytes(buf.read(4), byteorder='little')

        for i in range(metadata.field_count):
            field = MetadataField()
            field.read(buf)
            metadata.fields.append(field)

        if metadata.field_count > 0:
            #Add a dynamicly created parser function
            code = f"def temp_meth(buf):\n"
            code += "\tret = {}\n"
            for field in metadata.fields:
                code += self.get_metadata_field_code(field)
            code += "\treturn ret\n"
            code += f"parsers.read_{metadata.provider_name.replace('-', '_')}_{metadata.event_id}_payload = temp_meth"
            exec(code)
        self.payload_decoded = True
        return metadata

    def get_metadata_field_code(self, field, in_object=False):
        code = ""
        if field.type_code == NetTypeCode.OBJECT:
            code += f"\tret['{field.name}'] = {{"
            for subfield in field.fields:
               code += self.get_metadata_field_code(subfield, in_object=True) + ","
            code = code[:-1] + "}\n"
        elif in_object:
            code += f"'{field.name}': utils.read_type({field.type_code}, buf)"
        else:
            code += f"\tret['{field.name}'] = utils.read_type({field.type_code}, buf)\n"

        return code


class StackBlock(Block):

    def __init__(self, name=None, version=0, min_reader_ver=0):
        super().__init__(name, version, min_reader_ver)
        self.first_id = 0
        self.stack_count = 0
        self.stacks = []

    def read(self, buf):
        super().read(buf)
        self.first_id = int.from_bytes(buf.read(4), byteorder='little')
        self.stack_count = int.from_bytes(buf.read(4), byteorder='little')
        for i in range(self.stack_count):
            stack_size = int.from_bytes(buf.read(4), byteorder='little')
            self.stacks.append(buf.read(stack_size))
        buf.seek(self.end_of_block, io.SEEK_SET)

class SPThread:

    def __init__(self, thread_id, seq_num):
        self.thread_id = thread_id
        self.seq_num = seq_num

class SequencePointBlock(Block, factory_name='SPBlock'):

    def __init__(self, name=None, version=0, min_reader_ver=0):
        super().__init__(name, version, min_reader_ver)
        self.timestamp = 0
        self.thread_count = 0
        self.threads = []

    def read(self, buf):
        super().read(buf)
        self.timestamp = int.from_bytes(buf.read(8), byteorder='little')
        self.thread_count = int.from_bytes(buf.read(4), byteorder='little')
        for t in range(self.thread_count):
            self.threads.append(SPThread(int.from_bytes(buf.read(8), byteorder='little'), int.from_bytes(buf.read(4), byteorder='little')))
