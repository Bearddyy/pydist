from ums.sink import Sink
import socket

def handler(obj):
    obj.content()

sinker = Sink(handler, socket.gethostname())
sinker.run()