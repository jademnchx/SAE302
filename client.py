import socket, threading, sys

class Connect():
    
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 10000))
    print ("Connected to server")
    
    def __init__(self):
        pass
    
    def send (self, msg):
        self.client_socket.send(msg.encode())
        print ("Message sent")
        
    def receive (self):
        data = self.client_socket.recv(1024).decode()
        print ("Message received")
        return data
    
    def __receive_thread(self):
        pass
    
    def __connect_thread(self):
        pass
        
        
if __name__ == '__main__':
    pass