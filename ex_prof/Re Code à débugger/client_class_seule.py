import socket, threading, sys


class Client():

    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        self.__sock = socket.socket()
        self.__thread = None

    # fonction de connection.
    def connect(self) -> int:
        try :
            self.__sock.connect((self.__host,self.__port))
        except ConnectionRefusedError:
            print ("serveur non lancé ou mauvaise information")
            return -1
        except ConnectionError:
            print ("erreur de connection")
            return -1
        else :
            print ("connexion réalisée")
            return 0

    """ 
        fonction qui gére le dialogue
        -> lance une thread pour la partie reception 
        -> lance une boucle pour la partie emission. la boucle s'arréte si le message est kill, reset ou disconnect
        cette méthode attend la fin de la thread et ferme la socket à l'issue de son exécution
    """
    def dialogue(self):
        msg = ""
        self.__thread = threading.Thread(target=self.__reception, args=[self.__sock,])
        self.__thread.start()
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = self.__envoi()
        self.__thread.join()
        self.__sock.close()

    # méthode d'envoi d'un message au travers la socket. Le résultat de cette methode est le message envoyé.
    def __envoi(self):
        msg = input("client: ")
        try:
            self.__sock.send(msg.encode())
        except BrokenPipeError:
            print ("erreur, socket fermée")
        return msg
    """
     méthode de recpetion, passée à la thread, la connection étant passée en argument.
     cette méthode s'arréte quand le message reçu est kill, reset ou disconnect.
    """
    def __reception(self, conn):
        msg =""
        while msg != "kill" and msg != "disconnect" and msg != "reset":
            msg = conn.recv(1024).decode()
            print(msg)


if __name__=="__main__":
    # argument de la ligne de commande
    # argv[0] = nom_application
    # argv[1] = host
    # argv[2] = port
    # exemple : python3 client_class_seule.py 127.0.0.1 15001
    print (sys.argv)
    if len(sys.argv) < 3:
        client = Client("127.0.0.1",15001)
    else :
        host = sys.argv[1]
        port = int(sys.argv[2])
        client = Client(host,port)
    client.connect()
    client.dialogue()