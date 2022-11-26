import socket

BYE = 'bye'
EXIT = 'exit'
msg = ''
data = ''

if __name__ == '__main__':
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 10000))
    print ("Connected to server")
    while msg != BYE and data != BYE :
        msg = input('Enter a message to send: ')
        client_socket.send(msg.encode())
        data = client_socket.recv(1024).decode()
        print ("Received from server: ", data)
    client_socket.close()
    print ("Connection closed")
