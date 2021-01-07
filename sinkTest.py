from ums.sink import Sink
import socket

def handler(obj):
    obj.content()

sinker = Sink(handler, '192.168.0.17')
sinker.run()