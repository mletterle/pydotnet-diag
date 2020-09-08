### THIS IS AUTOGENERATED CODE
### Generated: 20200908 16:06:12
### Generated by: evtparsergen.py-23526ee
### Generated from: https://github.com/microsoft/perfview/blob/P2.0.59/src/TraceEvent/Parsers/w3core.man.xml

from .utils import *

def read_IIS_Trace_10000_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['SiteId'] = read_win_type(buf, 'win:UInt32')
	ret['AppPoolId'] = read_win_type(buf, 'win:UnicodeString')
	ret['ConnId'] = read_win_type(buf, 'win:UInt64')
	ret['RawConnId'] = read_win_type(buf, 'win:UInt64')
	ret['RequestURL'] = read_win_type(buf, 'win:UnicodeString')
	ret['RequestVerb'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10001_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['BytesSent'] = read_win_type(buf, 'win:UInt32')
	ret['BytesReceived'] = read_win_type(buf, 'win:UInt32')
	ret['HttpStatus'] = read_win_type(buf, 'win:UInt32')
	ret['HttpSubStatus'] = read_win_type(buf, 'win:UInt16')

def read_IIS_Trace_10002_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['FileName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10003_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10004_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10005_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ProcessId'] = read_win_type(buf, 'win:UInt32')
	ret['TotalReqs'] = read_win_type(buf, 'win:UInt32')
	ret['CurrentReqs'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10006_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['RedirectedURL'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10007_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['FileName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10008_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10009_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10010_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['PhysicalPath'] = read_win_type(buf, 'win:UnicodeString')
	ret['AccessPerms'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10011_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['SiteId'] = read_win_type(buf, 'win:UInt32')
	ret['RequestURL'] = read_win_type(buf, 'win:UnicodeString')
	ret['RequestVerb'] = read_win_type(buf, 'win:AnsiString')
	ret['RecursiveLevel'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10012_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['BytesSent'] = read_win_type(buf, 'win:UInt32')
	ret['HttpStatus'] = read_win_type(buf, 'win:UInt32')
	ret['HttpSubStatus'] = read_win_type(buf, 'win:UInt16')

def read_IIS_Trace_10013_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['HttpStatus'] = read_win_type(buf, 'win:UInt32')
	ret['HttpSubStatus'] = read_win_type(buf, 'win:UInt16')
	ret['FileNameOrURL'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10014_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10015_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10016_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['BytesSent'] = read_win_type(buf, 'win:UInt32')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10017_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10018_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['BytesReceived'] = read_win_type(buf, 'win:UInt32')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10019_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['FilePath'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10020_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ConfigPath'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10021_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Name'] = read_win_type(buf, 'win:UnicodeString')
	ret['Type'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10022_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['OldUrl'] = read_win_type(buf, 'win:UnicodeString')
	ret['NewUrl'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10023_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['OldHandlerName'] = read_win_type(buf, 'win:UnicodeString')
	ret['NewHandlerName'] = read_win_type(buf, 'win:UnicodeString')
	ret['NewHandlerModules'] = read_win_type(buf, 'win:UnicodeString')
	ret['NewHandlerScriptProcessor'] = read_win_type(buf, 'win:UnicodeString')
	ret['NewHandlerType'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10024_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['AuthType'] = read_win_type(buf, 'win:UnicodeString')
	ret['UserName'] = read_win_type(buf, 'win:UnicodeString')
	ret['SupportsIsInRole'] = read_win_type(buf, 'win:Boolean')

def read_IIS_Trace_10025_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Name'] = read_win_type(buf, 'win:UnicodeString')
	ret['Precondition'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10026_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Name'] = read_win_type(buf, 'win:UnicodeString')
	ret['Precondition'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10027_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Headers'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10028_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['FileName'] = read_win_type(buf, 'win:UnicodeString')
	ret['Offset'] = read_win_type(buf, 'win:UInt64')
	ret['Size'] = read_win_type(buf, 'win:UInt64')

def read_IIS_Trace_10029_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Buffer'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10030_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Headers'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10031_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Buffer'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10032_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Reason'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10033_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['HeaderName'] = read_win_type(buf, 'win:AnsiString')
	ret['HeaderValue'] = read_win_type(buf, 'win:AnsiString')
	ret['Replace'] = read_win_type(buf, 'win:Boolean')

def read_IIS_Trace_10034_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10035_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['RemoteAddress'] = read_win_type(buf, 'win:AnsiString')
	ret['RemotePort'] = read_win_type(buf, 'win:AnsiString')
	ret['LocalAddress'] = read_win_type(buf, 'win:AnsiString')
	ret['LocalPort'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10036_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['AuthTypeSupported'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10037_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['AuthType'] = read_win_type(buf, 'win:UInt32')
	ret['NTLMUsed'] = read_win_type(buf, 'win:Boolean')
	ret['RemoteUserName'] = read_win_type(buf, 'win:UnicodeString')
	ret['AuthUserName'] = read_win_type(buf, 'win:UnicodeString')
	ret['TokenImpersonationLevel'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10038_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10039_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10040_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10041_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10042_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10043_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10044_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10045_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10046_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10047_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10048_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10049_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['PackageName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10050_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['KMUsed'] = read_win_type(buf, 'win:Boolean')
	ret['APUserName'] = read_win_type(buf, 'win:UnicodeString')
	ret['SPNName'] = read_win_type(buf, 'win:UnicodeString')
	ret['ADConfigIsOK'] = read_win_type(buf, 'win:Boolean')
	ret['KerberosInfo'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10051_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10052_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['RequestAuthType'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10053_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10054_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['FileName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10055_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['IPAddress'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10056_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['HostName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10057_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10058_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['FileName'] = read_win_type(buf, 'win:UnicodeString')
	ret['AccountName'] = read_win_type(buf, 'win:UnicodeString')
	ret['DomainName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10059_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['FileName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10060_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ImageName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10061_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ImageName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10062_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['CurrentFlags'] = read_win_type(buf, 'win:UInt32')
	ret['NeededFlags'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10063_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['FilterName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10064_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['NotificationStatus'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10065_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10066_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10067_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10068_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['OrigURL'] = read_win_type(buf, 'win:AnsiString')
	ret['OrigPath'] = read_win_type(buf, 'win:AnsiString')
	ret['AccessPerms'] = read_win_type(buf, 'win:UInt32')
	ret['MatchingPath'] = read_win_type(buf, 'win:UInt32')
	ret['MatchingURL'] = read_win_type(buf, 'win:UInt32')
	ret['ScriptMapEntry'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10069_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['FinalURL'] = read_win_type(buf, 'win:AnsiString')
	ret['FinalPath'] = read_win_type(buf, 'win:AnsiString')
	ret['AccessPerms'] = read_win_type(buf, 'win:UInt32')
	ret['MatchingPath'] = read_win_type(buf, 'win:UInt32')
	ret['MatchingURL'] = read_win_type(buf, 'win:UInt32')
	ret['ScriptMapEntry'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10070_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['OrigUserName'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10071_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['FinalUserName'] = read_win_type(buf, 'win:AnsiString')
	ret['PasswordChanged'] = read_win_type(buf, 'win:Boolean')

def read_IIS_Trace_10072_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10073_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10074_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['HttpStatus'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10075_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10076_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10077_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10078_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['OrigClientHostName'] = read_win_type(buf, 'win:AnsiString')
	ret['OrigClientUserName'] = read_win_type(buf, 'win:AnsiString')
	ret['OrigServerName'] = read_win_type(buf, 'win:AnsiString')
	ret['OrigOperation'] = read_win_type(buf, 'win:AnsiString')
	ret['OrigTarget'] = read_win_type(buf, 'win:AnsiString')
	ret['OrigParameters'] = read_win_type(buf, 'win:AnsiString')
	ret['OrigHttpStatus'] = read_win_type(buf, 'win:UInt32')
	ret['OrigWin32Status'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10079_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['FinalClientHostName'] = read_win_type(buf, 'win:AnsiString')
	ret['FinalClientUserName'] = read_win_type(buf, 'win:AnsiString')
	ret['FinalServerName'] = read_win_type(buf, 'win:AnsiString')
	ret['FinalOperation'] = read_win_type(buf, 'win:AnsiString')
	ret['FinalTarget'] = read_win_type(buf, 'win:AnsiString')
	ret['FinalParameters'] = read_win_type(buf, 'win:AnsiString')
	ret['FinalHttpStatus'] = read_win_type(buf, 'win:UInt32')
	ret['FinalWin32Status'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10080_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10081_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10082_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['RequestedURL'] = read_win_type(buf, 'win:AnsiString')
	ret['PhysicalPath'] = read_win_type(buf, 'win:AnsiString')
	ret['DenialReason'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10083_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10084_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['HeaderName'] = read_win_type(buf, 'win:AnsiString')
	ret['HeaderValue'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10085_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['HeaderName'] = read_win_type(buf, 'win:AnsiString')
	ret['HeaderValue'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10086_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['HeaderName'] = read_win_type(buf, 'win:AnsiString')
	ret['HeaderValue'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10087_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['HeaderName'] = read_win_type(buf, 'win:AnsiString')
	ret['HeaderValue'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10088_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10089_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10090_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10091_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10092_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['CommandLine'] = read_win_type(buf, 'win:UnicodeString')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')
	ret['ProcessId'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10093_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Headers'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10094_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Headers'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10095_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10096_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10097_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10098_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10099_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10100_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10101_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10102_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10103_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10104_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10105_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10106_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10107_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10108_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10109_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Message'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10110_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Message'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10111_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Message'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10112_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['PositionInQueue'] = read_win_type(buf, 'win:UInt32')
	ret['MaxInstances'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10113_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['CommandLine'] = read_win_type(buf, 'win:UnicodeString')
	ret['IsNewProcess'] = read_win_type(buf, 'win:Boolean')
	ret['ProcessId'] = read_win_type(buf, 'win:UInt32')
	ret['RequestNumber'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10114_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10115_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10116_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10117_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10118_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10119_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10120_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['BufferSize'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10121_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10122_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['BytesReceived'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10123_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10124_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['DataType'] = read_win_type(buf, 'win:UInt32')
	ret['DataSize'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10125_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10126_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['BytesSent'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10127_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10128_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10129_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Reason'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10130_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10131_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10132_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Status'] = read_win_type(buf, 'win:UInt32')
	ret['Reason'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10133_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Status'] = read_win_type(buf, 'win:UInt32')
	ret['Reason'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10134_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10135_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10136_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10137_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10138_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Reason'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10139_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['OriginalFileName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10140_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')
	ret['OriginalFileName'] = read_win_type(buf, 'win:UnicodeString')
	ret['OriginalFileSize'] = read_win_type(buf, 'win:UInt32')
	ret['CompressedFileName'] = read_win_type(buf, 'win:UnicodeString')
	ret['CompressedFileSize'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10141_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10142_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10143_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Reason'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10144_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['OriginalSize'] = read_win_type(buf, 'win:UInt32')
	ret['CompressedSize'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10145_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10146_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10147_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['FileName'] = read_win_type(buf, 'win:UnicodeString')
	ret['UserName'] = read_win_type(buf, 'win:UnicodeString')
	ret['DomainName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10148_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Successful'] = read_win_type(buf, 'win:Boolean')
	ret['FileFromCache'] = read_win_type(buf, 'win:Boolean')
	ret['FileAddedToCache'] = read_win_type(buf, 'win:Boolean')
	ret['FileDirmoned'] = read_win_type(buf, 'win:Boolean')
	ret['LastModCheckErrorIgnored'] = read_win_type(buf, 'win:Boolean')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')
	ret['LastModifiedTime'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10149_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['RequestURL'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10150_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['PhysicalPath'] = read_win_type(buf, 'win:UnicodeString')
	ret['URLInfoFromCache'] = read_win_type(buf, 'win:Boolean')
	ret['URLInfoAddedToCache'] = read_win_type(buf, 'win:Boolean')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10151_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['HttpsysCacheable'] = read_win_type(buf, 'win:Boolean')
	ret['Reason'] = read_win_type(buf, 'win:UInt32')
	ret['CachePolicy'] = read_win_type(buf, 'win:UInt32')
	ret['TimeToLive'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10152_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10153_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Result'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10154_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['CachePolicy'] = read_win_type(buf, 'win:UInt32')
	ret['TimeToLive'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10155_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['Result'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10156_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')

def read_IIS_Trace_10157_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['Notification'] = read_win_type(buf, 'win:UInt32')
	ret['fIsPostNotification'] = read_win_type(buf, 'win:Boolean')

def read_IIS_Trace_10158_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['Notification'] = read_win_type(buf, 'win:UInt32')
	ret['fIsPostNotificationEvent'] = read_win_type(buf, 'win:Boolean')
	ret['NotificationStatus'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10159_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['Notification'] = read_win_type(buf, 'win:UInt32')
	ret['fIsPostNotificationEvent'] = read_win_type(buf, 'win:Boolean')
	ret['CompletionBytes'] = read_win_type(buf, 'win:UInt32')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10160_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10161_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['NotificationStatus'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10162_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['Notification'] = read_win_type(buf, 'win:UInt32')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10163_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['Notification'] = read_win_type(buf, 'win:UInt32')
	ret['HttpStatus'] = read_win_type(buf, 'win:UInt32')
	ret['HttpReason'] = read_win_type(buf, 'win:AnsiString')
	ret['HttpSubStatus'] = read_win_type(buf, 'win:UInt16')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')
	ret['ConfigExceptionInfo'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10164_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['Notification'] = read_win_type(buf, 'win:UInt32')
	ret['HttpStatus'] = read_win_type(buf, 'win:UInt32')
	ret['HttpReason'] = read_win_type(buf, 'win:AnsiString')

def read_IIS_Trace_10165_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ErrorDescription'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Trace_10166_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['Data1'] = read_win_type(buf, 'win:UnicodeString')
	ret['Data2'] = read_win_type(buf, 'win:UnicodeString')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10167_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['Data1'] = read_win_type(buf, 'win:UnicodeString')
	ret['Data2'] = read_win_type(buf, 'win:UnicodeString')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10168_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['Data1'] = read_win_type(buf, 'win:UnicodeString')
	ret['Data2'] = read_win_type(buf, 'win:UnicodeString')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10169_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['Data1'] = read_win_type(buf, 'win:UnicodeString')
	ret['Data2'] = read_win_type(buf, 'win:UnicodeString')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10170_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['Data1'] = read_win_type(buf, 'win:UnicodeString')
	ret['Data2'] = read_win_type(buf, 'win:UnicodeString')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10171_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['Data1'] = read_win_type(buf, 'win:UnicodeString')
	ret['Data2'] = read_win_type(buf, 'win:UnicodeString')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Trace_10172_payload(buf):
	ret = {}
	ret['ContextId'] = read_win_type(buf, 'win:GUID')
	ret['ModuleName'] = read_win_type(buf, 'win:UnicodeString')
	ret['Data1'] = read_win_type(buf, 'win:UnicodeString')
	ret['Data2'] = read_win_type(buf, 'win:UnicodeString')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Global_Trace_10000_payload(buf):
	ret = {}
	ret['CommandLineArgs'] = read_win_type(buf, 'win:UnicodeString')
	ret['IIS5CompatMode'] = read_win_type(buf, 'win:Boolean')
	ret['UserName'] = read_win_type(buf, 'win:UnicodeString')
	ret['ProcessAffinityMask'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Global_Trace_10001_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10002_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10003_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10004_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10005_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10006_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10007_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10008_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10009_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10010_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10011_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10012_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10013_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10014_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10015_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10016_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10017_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10018_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10019_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10020_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10021_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10022_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10023_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10024_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10025_payload(buf):
	ret = {}
	ret['InitStatus'] = read_win_type(buf, 'win:UInt32')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Global_Trace_10026_payload(buf):
	ret = {}
	ret['FilterName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Global_Trace_10027_payload(buf):
	ret = {}
	ret['FilterName'] = read_win_type(buf, 'win:UnicodeString')
	ret['ErrorCode'] = read_win_type(buf, 'win:UInt32')

def read_IIS_Global_Trace_10028_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10029_payload(buf):
	ret = {}
	ret['ShutdownImmediate'] = read_win_type(buf, 'win:Boolean')
	ret['AllCGIKilled'] = read_win_type(buf, 'win:Boolean')

def read_IIS_Global_Trace_10030_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10031_payload(buf):
	ret = {}

def read_IIS_Global_Trace_10032_payload(buf):
	ret = {}
	ret['FilterName'] = read_win_type(buf, 'win:UnicodeString')

def read_IIS_Global_Trace_10033_payload(buf):
	ret = {}
	ret['FilterName'] = read_win_type(buf, 'win:UnicodeString')

