# proxy test

import socket
import sys
import connection

def run_test(host, port, name):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    conn = connection.Connection(sock)
    conn.send(name)
    print conn.recv()
    conn.close()

if __name__ == "__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])
    name = sys.argv[3]
    run_test(host, port, name)
