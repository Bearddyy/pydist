import pickle 
import socket

class Server():
    def __init__(self, onReceive, port=6969, headersize=10):
        self.onReceive = onReceive
        self.host = ''
        self.port = port
        self.headersize = headersize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
    
    def run(self):
        while True:
            print("Waiting for next message")
            message = ''
            clientsocket, address = self.sock.accept()
            print(f"Connection from {address} ...")
            
            header = clientsocket.recv(self.headersize)
            length = int(header.strip())
            print(f"Expected Length of data:{length + self.headersize}...")
            message = clientsocket.recv(length)

            print("Full message received.")

            try:
                obj = pickle.loads(message)

                try:
                    if obj.host == None:
                        obj.host = address

                    self.onReceive(obj)
                except:
                    print("Error Actioning message")
            except:
                print("Error Parsing message")

            print("Message Handled.")
            clientsocket.close()
            

if __name__ == '__main__':
    def callback(obj):
        print(obj)

    server = Server(callback)
    server.run()
