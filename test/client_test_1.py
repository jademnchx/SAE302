
def server():
    host = input ("Enter the host : ")
    port = input ("Enter the port : ")
    heirm = server(host, port)
    heirm.connect()
    rep=heirm.send('connected')
    if rep == 'Socket is connected':
        print ("Server is not connected")
    else :
        print(rep)