#!/usr/bin/env python3
"""
Project 20 – Network Fuzzer (Protocol Agnostic)
Fuzzes any TCP protocol using Boofuzz.
"""

import sys
from boofuzz import *
from boofuzz.connections import TCPSocketConnection

# ---------- CONFIG ----------
TARGET_HOST = "127.0.0.1"
TARGET_PORT = 9999

def get_session():
    """Define the protocol and create a fuzzing session."""
    connection = TCPSocketConnection(TARGET_HOST, TARGET_PORT)
    session = Session(target=Target(connection=connection))

    # Define a simple protocol: e.g., a command string
    s_initialize("SimpleCommand")
    s_string("HELLO")
    s_delim(" ")
    s_string("WORLD", fuzzable=True)   # fuzz this field
    s_delim("\r\n")

    session.connect(s_get("SimpleCommand"))
    return session

def main():
    print(f"[*] Starting fuzzer against {TARGET_HOST}:{TARGET_PORT} (TCP)")
    session = get_session()
    try:
        session.fuzz()
    except KeyboardInterrupt:
        print("\n[*] Stopped by user.")
    print("[+] Fuzzing complete. Check the console output for results.")

if __name__ == "__main__":
    main()