#!/usr/bin/env python3

import sys
from pydotnet_diag.nettrace import NetTrace

def print_field(field, indent=0):
    tabs = "\t" * indent
    print(f"{tabs}Name: {field.name}\n{tabs}Type: {field.type_code}")
    for subfield in field.fields:
        print_field(subfield, indent+1)


def read_file(ntfile):
    nt = None
    with open(ntfile, 'rb') as ntfile:
        nt = NetTrace()
        nt.read(ntfile)
    return nt

def print_trace(nt):
    trace = nt.event_stream.trace

    print(f"Trace of PID:{trace.process_id} from {trace.year}{trace.month:02}{trace.day:02} - {trace.hour:02}:{trace.minute:02}:{trace.second:02}")

    for evt in nt.event_stream.events:
        print(f"{evt.seq}: {evt.metadata_id:04} TimeStamp: {evt.timestamp}\n\t{evt.payload}")


def main():
    f = sys.argv[1]
    print_trace(read_file(f))

if __name__ == "__main__":
    main()
