from threading import Thread
def server():
    host1 = input ("Enter the host1 : ")
    host2 = input ("Enter the host2 : ")
    hostsock1 = server(host1, 10000)
    hostsock2 = server(host2, 10000)
    hostsock1.connect()
    hostsock2.connect()
    Thread.spleep(2)
    for i in range(10):
        hostsock1.send('OS')
        hostsock2.send('CPU')
    hostsock1.close()
    hostsock2.close()