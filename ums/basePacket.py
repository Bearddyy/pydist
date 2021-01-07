import socket

class BasePacket():
    def __init__(
            self, 
            action, 
            content=None, 
            host='', 
            port=9696,
            name=socket.gethostname()):
        self.action = action
        self.host = host
        self.port = port
        self.content = content
        self.name = name
