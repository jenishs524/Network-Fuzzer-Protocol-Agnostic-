#!/usr/bin/env python3
"""
Simple TCP echo server – used as a target for fuzzing.
"""
import socket

HOST = "0.0.0.0"
PORT = 9999

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"[*] Echo server listening on {PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"[*] Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)  # echo back

if __name__ == "__main__":
    main()