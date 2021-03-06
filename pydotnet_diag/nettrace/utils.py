import struct
from uuid import UUID
from .nettypecode import NetTypeCode

def bytes_to_nuluni(buf):
    str_bytes = b''
    while True:
        b = buf.read(2)
        if b == b'\x00\x00': break
        str_bytes += b
    return str_bytes.decode('utf-16')

def bytes_to_nulans(buf):
    str_bytes = b''
    while True:
        b = buf.read(1)
        if b == b'\x00': break
        str_bytes += b
    return str_bytes.decode('utf-8')

def read_type(type_code, buf):
    if type_code == NetTypeCode.BOOLEAN:
        return int.from_bytes(buf.read(4), byteorder='little') == 1
    if type_code == NetTypeCode.CHAR:
        return int.from_bytes(buf.read(1), byteorder='little')
    if type_code == NetTypeCode.SBYTE:
        return int.from_bytes(buf.read(1), byteorder='little', signed=True)
    if type_code == NetTypeCode.BYTE:
        return int.from_bytes(buf.read(1), byteorder='little')
    if type_code == NetTypeCode.INT16:
        return int.from_bytes(buf.read(2), byteorder='little', signed=True)
    if type_code == NetTypeCode.UINT16:
        return int.from_bytes(buf.read(2), byteorder='little')
    if type_code == NetTypeCode.INT32:
        return int.from_bytes(buf.read(4), byteorder='little', signed=True)
    if type_code == NetTypeCode.UINT32:
        return int.from_bytes(buf.read(4), byteorder='little')
    if type_code == NetTypeCode.INT64:
        return int.from_bytes(buf.read(8), byteorder='little', signed=True)
    if type_code == NetTypeCode.UINT64:
        return int.from_bytes(buf.read(8), byteorder='little')
    if type_code == NetTypeCode.SINGLE:
        return struct.unpack('<f', buf.read(4))[0]
    if type_code == NetTypeCode.DOUBLE:
        return struct.unpack('<d', buf.read(8))[0]
    if type_code == NetTypeCode.STRING:
        return bytes_to_nuluni(buf)
    if type_code == NetTypeCode.GUID:
        return UUID(bytes_le=buf.read(16))

def read_win_type(buf, win_type):
    if win_type == "win:UnicodeString": return read_type(NetTypeCode.STRING, buf)
    elif win_type == "win:AnsiString": return bytes_to_nulans(buf)
    elif win_type == "win:Int8": return read_type(NetTypeCode.SBYTE, buf)
    elif win_type == "win:UInt8": return read_type(NetTypeCode.BYTE, buf)
    elif win_type == "win:Int16": return read_type(NetTypeCode.INT16, buf)
    elif win_type == "win:UInt16": return read_type(NetTypeCode.UINT16, buf)
    elif win_type == "win:Int32": return read_type(NetTypeCode.INT32, buf)
    elif win_type == "win:UInt32": return read_type(NetTypeCode.UINT32, buf)
    elif win_type == "win:Int64": return read_type(NetTypeCode.INT64, buf)
    elif win_type == "win:UInt64": return read_type(NetTypeCode.UINT64, buf)
    elif win_type == "win:Float": return read_type(NetTypeCode.SINGLE, buf)
    elif win_type == "win:Double": return read_type(NetTypeCode.DOUBLE, buf)
    elif win_type == "win:Boolean": return read_type(NetTypeCode.BOOLEAN, buf)
    elif win_type == "win:GUID": return read_type(NetTypeCode.GUID, buf)
    elif win_type == "win:Pointer": return read_type(NetTypeCode.UINT64, buf) #Nobody uses 32-bit CPUs anymore ...
