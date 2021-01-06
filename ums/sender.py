import pickle 
import socket


class Sender():
    def __init__(self, host, port=6969, headersize=10):
        self.host = host
        self.port = port
        self.headersize = headersize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def send(self, obj):
        message = pickle.dumps(obj)

        #First part of message is the size, padded to headersize
        message = bytes(f"{len(message):<{self.headersize}}", 'utf-8') + message
        print(f"Sending {len(message)} bytes to {self.host}")
        
        try:
            self.sock.connect((self.host, self.port))
            self.sock.send(message)
            self.sock.close()
            print("Message Sent.")
        except:
            print("Could not connect to {self.host}")
            print("Please check connection")
        
