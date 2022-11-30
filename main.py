from client import Client
import sys

def __main__():
    client = Client(Client.host, Client.port)
    client.connected()
    client.close()
    
if __name__ == '__main__':
    sys.exit(__main__())
    