import socket

class Client():
    host = 'localhost'
    port = 10000
    
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__sock = None
        
    def is_connected(self):
        print('Socket is connected')
        return(self.__sock != None)
    
    def connected(self):
        sock = socket.socket()
        sock.connect(self.__host, self.__port)
        print("Socket is connected")
        
    def send(self, msg):
        if self.is_connected():
            sock = socket.socket()
            sock.send(msg)
            msg = sock.recv (1024).decode()
            print(msg)
        else:
            print("Socket is not connected")
    
    def close(self):
        sock = socket.socket()
        sock.close()
        print("Socket is closed")

if __name__ == '__main__':
    Client.connected()
    Client.send()
