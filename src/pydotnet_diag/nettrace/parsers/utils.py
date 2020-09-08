import struct

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
    return str_bytes.decode('ansi')

def read_winType(winType, buf):
    if winType == "win:UnicodeString":
        return bytes_to_nuluni(buf)
    elif winType == "win:AnsiString":
        return bytes_to_nulans(buf)
    elif winType == "win:Int8" or winType == "win:UInt8":
        return int.from_bytes(buf.read(1), byteorder='little')
    elif winType == "win:Int16" or winType == "win:UInt16":
        return int.from_bytes(buf.read(2), byteorder='little')
    elif winType == "win:Int32" or winType == "win:UInt32":
        return int.from_bytes(buf.read(4), byteorder='little')
    elif winType == "win:Float":
        return struct.unpack('<f', buf.read(4))
    elif winType == "win:Double":
        return struct.unpack('<d', buf.read(8))
    elif winType == "win:Boolean":
        return int.from_bytes(buf.read(4), byteorder='little') == 1
