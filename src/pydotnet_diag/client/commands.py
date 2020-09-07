from enum import IntEnum

class CommandSet(IntEnum):
    # RESERVED = 0x00
    DUMP = 0x01
    EVENTPIPE = 0x02
    PROFILER = 0x03
    PROCESS = 0x04
    SERVER = 0xFF

class ServerCommandId(IntEnum):
    OK = 0x00
    ERROR = 0xFF

class EventPipeCommandId(IntEnum):
    # RESERVED = 0x00
    STOP_TRACING = 0x01
    COLLECT_TRACING = 0x02
    COLLECT_TRACING_2 = 0x03

class DumpCommandId(IntEnum):
    # RESERVED = 0x00
    CREATE_CORE_DUMP = 0x01

class ProfilerCommandId(IntEnum):
    # RESERVED = 0x00
    ATTACH_PROFILER = 0x01
