import socket, threading

class Client():
    
    host = 'localhost'
    port = 10000
    
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__sock = None
        
    def is_connected(self):
        return(self.__sock != None)
    
    def connected(self):
        threading.Thread(target=self.__connected).start()
    
    def __connected(self):
        try :
            self.__sock = socket.socket()
            self.__sock.connect((self.__host, self.__port))
        except ConnectionRefusedError :
            print("error __connected")
        else :
            print("win __connected")
        
    def send(self):
        threading.Thread(target=self.__send).start()
    
    def __send(self, msg):
        if self.is_connected():
            sock = socket.socket()
            sock.send(msg)
            msg = sock.recv (1024).decode()
            print(msg)
        else:
            print("error __send")
    
    def close(self):
        sock = socket.socket()
        if sock.close():
            print("win close")
        else:
            print("error close")
