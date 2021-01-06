import socket

class BasePacket():
    def __init__(
            self, 
            action, 
            content=None, 
            host=socket.gethostname(), 
            port=6969,
            name=socket.gethostname()):
        self.action = action
        self.host = host
        self.port = port
        self.content = content
        self.name = name
