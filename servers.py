import socket, subprocess, os
class Server:
        
    def __init__(self):
        pass
        
    def serveur(self):
        msg = ""
        conn = None
        server_socket = None
        while msg != "kill" :
            msg = ""
            server_socket = socket.socket()
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind(("localhost", 15001))
            server_socket.listen(1)
            print('Server waiting for connection')
            while msg != "kill" and msg != "reset":
                msg = ""
                try :
                    conn, addr = server_socket.accept()
                    print (addr)
                except ConnectionError:
                    print ("connection error")
                    break
                else :
                    while msg != "kill" and msg != "reset" and msg != "disconnect":
                        msg = conn.recv(1024).decode()
                        print ("Received from client: ", msg)
                        rep = self.cmds(msg)
                        conn.send(rep.encode())
                    conn.close()
        print ("Connection closed")
        server_socket.close()
        print ("Server closed")

    # Coder les commande ici

    def cmds(self, msg):
        if msg == "ipconfig" or msg == "hostname" :
            p = subprocess.Popen(msg, stdout = subprocess.PIPE, stderr=subprocess.STDOUT, encoding='cp850', shell=True)
            rep = p.stdout.read()
            print("rep=",rep)
            return rep
        else :
            return "Commande inconnue"

if __name__ == '__main__':
    serv = Server()
    serv.serveur()