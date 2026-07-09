📁 Network Fuzzer (Protocol Agnostic)

Description
Uses Boofuzz to fuzz any TCP protocol. The protocol is defined using Boofuzz primitives; it sends mutated inputs to a target and monitors for crashes.

Key Features

    Protocol‑agnostic – define your own messages.

    Mutation‑based fuzzing (byte flipping, length overflows).

    Web interface for monitoring (port 26000).

    Logs test cases and crashes.

Technologies

    Boofuzz, Scapy (optional).

Prerequisites

    Python 3, Boofuzz.

Installation
bash

pip install boofuzz scapy

Usage

    Start a target server (e.g., echo server).

    Run the fuzzer:
    bash

python fuzzer.py

    Watch output and visit http://localhost:26000 for live status.

Sample Output
text

[*] Starting fuzzer against 127.0.0.1:9999 (TCP)
[2026-07-09 19:29:09,061] Test Case: 1: SimpleCommand:[SimpleCommand.String1:0]
...

Notes

    Modify fuzzer.py to define your own protocol structures.

    Use TCPSocketConnection instead of deprecated SocketConnection.
