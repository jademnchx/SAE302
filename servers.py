import socket

def serveur():
    msg = ""
    while msg != "kill" :
        server_socket = socket.socket()
        server_socket.bind(("localhost", 10000))
        server_socket.listen(1)
        print('Serveur en attente de connexion')
        while msg != "kill" and msg != "reset":
            conn, addr = server_socket.accept()
            print (addr)
            while msg != "kill"  and msg != "reset" and msg != "disconect":
                data = conn.recv(1024).decode()
                print ("Received from client: ", data)
                msg = input('Enter a message to send: ')
                conn.send(msg.encode())
        conn.close()
        print ("Connection closed")
    server_socket.close()
    print ("Server closed")

# Coder les commande ici

if __name__ == '__main__':
    serveur()