
from client import Client

def server():
    host = 'localhost'
    port = 10000
    heirm = Client(host, port)
    heirm.connected()
    print ("Connected to server")
    rep=heirm.send('error __send')
    if rep == 'Socket is connected':
        print ("Socket is not connected")
    else :
        print(rep)