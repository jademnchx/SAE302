import socket

BYE = 'bye'
EXIT = 'exit'
msg = ''
data = ''

class Client():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))
        print ("Connected to server")
        
    def action(self):
        BYE = 'bye'
        msg = ''
        data = ''
        while msg != BYE and data != BYE :
            msg = input('Enter a message to send: ')
            self.send(msg.encode())
            print ("message sent")
            data = self.socket.recv(1024).decode()
            print ("Received from server: ", data)
        else :
            self.socket.send(BYE.encode())
            print ("message sent")
            self.socket.close()
            print ("Connection closed")

if __name__ == '__main__':
    Client.action()
