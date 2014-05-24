# server.py - run our web service

import socket # contains low level network functions
import guess # contains our guessing game

def handle_connection(conn, addr):
    """handle connection from the address"""
    print 'connection recieved from:', addr
    number = guess.get_number(100)
    print '(our number is ' + str(number) + ')'
    while True:
        data = conn.recv(1024) # read data from the connection / raw input
        if not data:
            break
        print 'from client:', data
        playing, response = guess.one_turn(number, data)
        conn.send(response)
    conn.close()
    

def server(port):
    """run our server on the given port"""
    host = '' # all available network interfaces
    # create an internet socket for TCP protocol
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(True) # listen for incoming connections
    print 'listening on port', port
    while True:
        conn, addr = s.accept() # accept a connection
        handle_connection(conn, addr)
    s.close() # can't get here
