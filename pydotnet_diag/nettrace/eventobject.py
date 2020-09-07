from enum import IntEnum
import io

class EventTag(IntEnum):
    NULL_REFERENCE = 0x01
    BEGIN_PRIVATE_OBJECT = 0x05
    END_OBJECT = 0x06

class EventObject:

    def __init__(self, name=None, version=0, min_reader_ver=0):
        self.name = name or self.__class__.__name__
        self.version = version
        self.min_reader_ver = min_reader_ver


class TraceObject(EventObject):

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

class Block(EventObject):

    def __init__(self, name=None, version=0, min_reader_ver=0):
        super().__init__(name, version, min_reader_ver)

    def read(self, buf):
        self.block_size = int.from_bytes(buf.read(4), byteorder='little')
        align = buf.tell() % 4
        if align != 0: buf.seek(4 - align, io.SEEK_CUR)
        self.end_of_block = buf.tell() + self.block_size

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
        self.flags = int.from_bytes(buf.read(2), byteorder='little')
        self.compressed = self.flags & 0x0001 == 0x0001
        self.min_timestamp = int.from_bytes(buf.read(8), byteorder='little')
        self.max_timestamp = int.from_bytes(buf.read(8), byteorder='little')
        while buf.tell() < self.end_of_block:
            if self.compressed:
                 self.read_compressed_block(buf)
            else:
                 self.read_block(buf)

    def read_block(self, buf):
        buf.read(1)

    def read_compressed_block(self, buf):
        buf.read(1)

class MetadataBlock(EventBlock):

    def __init__(self, name=None, version=0, min_reader_ver=0):
        super().__init__(name, version, min_reader_ver)

    def read(self, buf):
        super().read(buf)

    def read_block(self, buf):
        super().read_block(buf)

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

class SequencePointBlock(Block):

    def __init__(self, name=None, version=0, min_reader_ver=0):
        super().__init__(name, version, min_reader_ver)
        self.timestamp = 0
        self.thread_count = 0
        self.threads = []

    def read(self, buf):
        super().read(buf)
        while buf.tell() < self.end_of_block:
            self.threads.append(SPThread(int.from_bytes(buf.read(8), byteorder='little'), int.from_bytes(buf.read(4), byteorder='little')))
