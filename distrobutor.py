from ums.server import Server
from ums.sender import Sender

class Distributor():
    def __init__(self):
        self.server = Server(self.on_receive)
        self.registered = dict()
        self.stored = dict()

    def run(self):
        self.server.run()

    def on_receive(self, obj):
        print("Distributor received ", obj.action, " request")

        if(obj.action == 'register'):
            self.register(obj)
        elif(obj.action == 'fetch'):
            self.fetch(obj)
        elif(obj.action == 'post'):
            self.post(obj)

    def register(self, obj):
        self.registered[obj.name] = obj

    def distrobute(self, obj):
        print("Distributing...")
        for sinkName in self.registered:
            print(f"Sending to {sinkName}")
            sink = self.registered[sinkName]
            tempSender = Sender(sink.host, sink.port)
            tempSender.send(obj)
        print("Finished Sending")

    def store(self, obj):
        pass

    def fetch(self, obj):
        stored = self.stored[obj.name]
        tempSender = Sender(obj.host, obj.port)
        tempSender.send(stored)
        self.stored[obj.name] = []
        pass

    def post(self, obj):
        self.distrobute(obj)

if __name__ == "__main__":
    distro = Distributor()
    distro.run()
    