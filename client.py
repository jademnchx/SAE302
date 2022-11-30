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
        self.__sock = socket.socket()
        self.__sock.connect((self.__host, self.__port))
        self.__sock.send('connected')
        
    def send(self):
        threading.Thread(target=self.__send).start()
    
    def __send(self, msg):
        if self.is_connected():
            self.__sock.send(msg)
            msg = self.__sock.recv (1024).decode()
            print(msg)
        else:
            print("error __send")
    
    def close(self):
        self.__sock.close()