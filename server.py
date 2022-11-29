import socket

class Serveur() :
    def serveur():
        msg = ""
        while msg != "kill" :
            server_socket = socket.socket()
            server_socket.bind(("localhost", 10000))
            while msg != "kill" and msg != "reset":
                conn = server_socket.accept()
                while msg != "kill"  and msg != "reset" and msg != "disconect":
                    # Executer les cmd
                    data = conn.recv(1024).decode()
                    print ("Received from client: ", data)
                    msg = input('Enter a message to send: ')
                    conn.send(msg.encode())
                    #
            conn.close()
            print ("Connection closed")
        server_socket.close()
        print ("Server closed")

# Coder les commande ici

if __name__ == '__main__':
    pass