from enum import IntEnum

class NetTypeCode(IntEnum):
    '''
    TypeCodes from: https://docs.microsoft.com/en-us/dotnet/api/system.typecode
    Additions from: https://github.com/microsoft/perfview/blob/T2.0.59/src/TraceEvent/EventPipe/EventPipeEventSource.cs#L819
    '''
    EMPTY     = 0
    OBJECT    = 1
    DB_NULL   = 2
    BOOLEAN   = 3
    CHAR      = 4
    SBYTE     = 5
    BYTE      = 6
    INT16     = 7
    UINT16    = 8
    INT32     = 9
    UINT32    = 10
    INT64     = 11
    UINT64    = 12
    SINGLE    = 13
    DOUBLE    = 14
    DECIMAL   = 15
    DATE_TIME = 16
    GUID      = 17
    STRING    = 18
    ARRAY     = 19
