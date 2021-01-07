import socket
from ums.basePacket import BasePacket
from ums.sender     import Sender
from ums.server     import Server

class Sink():
    def __init__(self, onReceive, serverHost, ourPort=9696, serverPort=6969, headersize=10):
        self.serverHost = serverHost
        self.serverPort = serverPort
        self.ourPort = ourPort
        self.onReceive = onReceive

        #Coms to server
        self.theirServer = Sender(self.serverHost, self.serverPort)

        # set up receive server
        self.ourServer = Server(self.onReceive, port=ourPort)


    def run(self):
        registrationPacket = BasePacket('register', port=self.ourPort)
        self.theirServer.send(registrationPacket)
        self.ourServer.run()
