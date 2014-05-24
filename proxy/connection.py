# connections
#
# a connection is a real socket connection

class Connection(object):
    """a socket connection between two processes"""

    def __init__(self, conn):
        """initialize with the acutal socket connection"""
        self.conn = conn

    def send(self, s):
        self.conn.send(s)

    def recv(self):
        return self.conn.recv(1024)

    def close(self):
        self.conn.close()
        
