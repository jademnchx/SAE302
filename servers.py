import socket, psutil, sys

class Server():

    def serveur(self):
        msg = ""
        conn = None
        server_socket = None
        while msg != "kill" :
            msg = ""
            server_socket = socket.socket()
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind(("localhost", 17671)) #Le serveur écoute sur le port 17671
            server_socket.listen(1) #Le serveur écoute une seule connexion
            print('Server waiting for connection')
            while msg != "kill" and msg != "reset":
                msg = ""
                try :
                    conn, addr = server_socket.accept() #Le serveur accepte la connexion
                    print (addr) #Affiche l'adresse du client
                except ConnectionError:
                    print ("connection error")
                    break
                else :
                    while msg != "kill" and msg != "reset" and msg != "disconnect":
                        try :
                            msg = conn.recv(1024).decode() #Le message est reçu du client
                        except ConnectionAbortedError:
                            print ("connection aborted error")
                            
                        # Commandes du serveur
                        if msg == "cpu":
                            msg = 'cpu : ' + str(psutil.cpu_percent())
                        elif msg == "os" :
                            msg = 'os : ' + str(sys.platform)
                        elif msg == "memory":
                            msg = 'memory : ' + str(psutil.virtual_memory().total)
                        elif msg == "ram":
                            msg = 'ram : ' + str(psutil.disk_usage('/'))
                        elif msg == "ip":
                            msg = 'ip : ' + socket.gethostbyname(socket.gethostname())
                        elif msg == "name":
                            msg = 'name : ' + socket.gethostname()
                        elif msg == "python":
                            msg = 'python : ' + str(sys.version)
                        elif msg != "kill" and msg != "reset" and msg != "disconnect":
                            msg = "Commande inconnue"
                        conn.send(msg.encode()) #Le message est envoyé au client
                        print (msg)
                    conn.close() # La connexion est fermée
                    print ("Connection closed")
        server_socket.close() #Le serveur est fermé
        print ("Server closed")
        
if __name__=="__main__":
    server = Server()
    server.serveur()