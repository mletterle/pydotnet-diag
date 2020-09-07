import struct
from .eventstream import EventStream

class NetTrace:
    Magic = b'Nettrace'
    StreamHeader = b'\x14\x00!FastSerialization.1'

    def __init__(self):
        self.event_stream = None

    def read(self, buf):
        self.magic = buf.read(len(NetTrace.Magic)).decode()
        str_len = int.from_bytes(buf.read(4), byteorder='little')
        self.stream_name = buf.read(str_len).decode()

        if self.magic != 'Nettrace' or self.stream_name != '!FastSerialization.1':
            raise Exception('Not a NetTrace file!')

        es = EventStream()
        es.read(buf)
        self.event_stream = es
