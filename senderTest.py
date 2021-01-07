import socket
from ums.sender import Sender
from ums.basePacket import BasePacket

from randomStuff import doStuff

if __name__ == '__main__':
    SENDER = Sender('192.168.0.17')
    testPacket = BasePacket('post', doStuff)
    SENDER.send(testPacket)