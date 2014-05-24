# proxy

class NameService:
    """name service for procied connections"""

    def __init__(self):
        self.names = {}

    def add(self, name, conn):
        """return true if name is not used; bind name"""
        if name in self.names:
            return False
        else:
            self.names[name] = conn
            return True

    def get(self, name):
        """return the connection for name"""
        if name in self.names:
            return self.names[name]
        else:
            return None
