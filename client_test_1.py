
from client import Client
def server():
    host = 'localhost'
    port = 10000
    heirm = server(host, port)
    heirm.connect()
    rep=heirm.send('connected')
    if rep == 'Socket is connected':
        print ("Server is not connected")
    else :
        print(rep)