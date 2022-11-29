import threading, socket

class Client():
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__sock = None
        
    def is_connected(self):
        print('Socket is connected')
        return(self.__sock != None)
        
    
    def connect(self):
        threading.Thread(target = self.__connect)
        
    def __connect(self):
        sock = socket.socket()
        sock.connect(self.__host, self.__port)
        
    def send(self):
        threading.Thread(target = self.__send)
        
    def __send(self, msg):
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
    pass