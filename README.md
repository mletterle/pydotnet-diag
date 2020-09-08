# PyDotNet-Diag

A python library and client implementing the .NET Core [Diagnostic IPC Protocol](https://github.com/dotnet/diagnostics/blob/3.1.141901/documentation/design-docs/ipc-protocol.md).

It also supports parsing the [EventPipe File Format](https://github.com/microsoft/perfview/blob/T2.0.59/src/TraceEvent/EventPipe/EventPipeFormat.md).

## Current Limitations
 - Only V4 of the NetTrace format is supported
 - Only Unix Sockets are supported at this time.

