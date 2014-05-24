# client.py

import socket
import sys

# start up stuff
# while True:
#   processing on input
#   possible quit
#   send request to server
#   recieve response from server
# finish up stuff

class Client(object):
    """guessing game client class"""

    def startup(self):
        """startup guessing game client"""
        self.playing = True
        self.num_guesses = 0
        print "guess a number between 1 and 100"

    def running(self):
        """return true if we are running"""
        return self.playing

    def process(self, data):
        """process data in client, initially None"""
        if not data is None:
            print data
            if data == "you won.":
                self.playing = False
                return
        guess = raw_input('Your guess? ')
        self.num_guesses += 1
        return guess

    def finish(self):
        """finish the client guessing game"""
        print "you used " + str(self.num_guesses) + " guesses."


        
def run_client(host, port):
    """connect the client to the server host:port"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port)) # connect client to host:port
    client = Client()
    client.startup()
    data = None
    while True:
        request = client.process(data)
        if not client.running():
            break
        s.send(request) #send information to server
        data = s.recv(1024) # read information from the server
    client.finish()
    s.close() # close socket


if __name__ == "__main__":
    port = None
    host = None
    # should be run as: python client.py <port>
    try:
        host = sys.argv[1]
        port = int(sys.argv[2]) # get port argument
        run_guess_server(port) # runs on that port
    except:
        print 'usage', sys.argv[0], '<host> <port>'
    if port and host:
        run_client(host, port)
