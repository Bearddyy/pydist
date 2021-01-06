import socket
from ums.sender import Sender
from ums.basePacket import BasePacket

from randomStuff import doStuff

if __name__ == '__main__':
    SENDER = Sender(socket.gethostname())
    testPacket = BasePacket('post', doStuff)
    SENDER.send(testPacket)