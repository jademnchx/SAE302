import socket
REST = 'reset'
BYE = 'disconnect'
EXIT = 'kill'
msg = ''

if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 10000))
    print ("Server started")
    server_socket.listen(2)
        
    while msg != EXIT :
        conn, address = server_socket.accept()
        
        while msg != BYE and msg != EXIT :
            data = conn.recv(1024).decode()
            print ("Received from client: ", data)
            
            if msg == BYE :
                conn.send(BYE.encode())
            else :
                msg = input('Enter a message to send: ')
                conn.send(msg.encode())
        conn.close()
        print ("Connection closed")
    server_socket.close()
    print ("Server closed")