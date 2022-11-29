import threading, socket

class Client():
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__sock = None
        
    def is_connected(self):
        print('Socket is connected')
        return(self.__sock != None)
    
    
    def connect():
        sock = socket.socket()
        sock.bind(('localhost', 10000))
        sock.listen(5)
        conn, address = sock.accept()
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
    Client.connect()

    Client.send()
    