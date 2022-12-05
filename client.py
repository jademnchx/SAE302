import socket, threading, sys

class Client(threading.Thread):
    
    host = 'localhost'
    port = 10000
    
    def __init__(self, host, port):
        super().__init__()
        self.__host = host
        self.__port = port
        self.__sock = socket.socket()
    
    def __connect(self) -> int:
        try :
            self.__sock.connect((self.__host,self.__port))
        except ConnectionRefusedError:
            print ("connection refused")
            return -1
        except ConnectionError:
            print ("connection error")
            return -1
        else :
            print ("connection done")
            return 0
        
    def __dialogue(self):
        msg = ""
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = input("client: ")
            self.__sock.send(msg.encode())
            msg = self.__sock.recv(1024).decode()
            print(msg)
        self.__sock.close()


    def run(self):
        if (self.__connect() ==0):
            self.__dialogue()

if __name__=="__main__":
    if len(sys.argv) < 3:
        client = Client("127.0.0.1",15001)
    else :
        host = sys.argv[1]
        port = int(sys.argv[2])
        # création de l'objet client qui est aussi un thread
        client = Client(host,port)
    #démarrage de la thread client
    client.start()
    client.join()