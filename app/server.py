# server.py - run our web service

import socket # contains low level network functions
import threading

class HandleConnection (threading.Thread):
    def __init__(self, conn, addr, create):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.create = create
    def run(self):
        handle_connection(conn, addr, create)


def handle_connection(conn, addr, create):
    """handle connection from the address"""
    print 'connection recieved from:', addr
    server = create()
    server.startup()
    while True:
        data = conn.recv(1024) # read data from the connection / raw input
        if not data:
            break
        print 'from client:', data
        response = server.process(data)
        conn.send(response)
        server.finish()
    conn.close()
    

def run_server(port, create):
    """run our server on the given port"""
    host = '' # all available network interfaces
    # create an internet socket for TCP protocol
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(True) # listen for incoming connections
    print 'listening on port', port
    while True:
        conn, addr = s.accept() # accept a connection
        new_connection = HandleConnection(conn, addr, create)
        new_connection.start()
        # handle_connection(conn, addr, create)
    s.close() # can't get here
