import socket, subprocess, os

def serveur():
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
                    conn.send(msg.encode())
            conn.close()
            print ("Connection closed")
        server_socket.close()
        print ("Server closed")

# Coder les commande ici

def cmd(self, cmd):
    msg = ""
    if msg == "IP":
        cmd = "ipconfig"
        p = subprocess.Popen(cmd,stdout = subprocess.PIPE, stderr=subprocess.PIPE, encoding='cp850', shell=True)
        print (f"résultat commande : \n {p.stdout.read()}")
        print (f"erreur commande : \n {p.stderr.read()}")

if __name__ == '__main__':
    serveur()