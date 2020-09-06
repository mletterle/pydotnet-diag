import struct

class DiagnosticMsg:
    magic_str = "DOTNET_IPC_V1"
    _header_bytes = struct.Struct("<14sHBBH")

    def __init__(self, msg=None):
        if msg != None:
            self.magic, self.size, self.command_set, self.command_id, self.reserved = DiagnosticMsg._header_bytes.unpack_from(msg)
            self.payload = msg[20:]
        else:
            self.magic = DiagnosticMsg.magic_str
            self.size = DiagnosticMsg._header_bytes.size
            self.command_set = 0x00
            self.command_id = 0x00
            self.reserved = 0x0000
            self.payload = None

    @property
    def payload(self):
        return self.__payload

    @payload.setter
    def payload(self, value):
        self.__payload = value
        self.size = DiagnosticMsg._header_bytes.size + len(self.payload or [])

    def to_bytes(self):
        return DiagnosticMsg._header_bytes.pack(str.encode(self.magic), self.size, self.command_set, self.command_id, self.reserved) + (self.payload or bytes(0))

