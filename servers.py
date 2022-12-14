import socket, psutil, sys

class Server():
        
    def __init__(self):
        pass
        
    def serveur(self, msg):
        conn = None
        server_socket = None
        while msg != "kill" :
            msg = ""
            server_socket = socket.socket()
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind(("localhost", 15001))
            server_socket.listen(1)
            print('Server waiting for connection')
            while msg != "kill" and msg != "reset":
                msg = ""
                try :
                    conn, addr = server_socket.accept()
                    print (addr)
                except ConnectionError:
                    print ("connection error")
                    break
                else :
                    while msg != "kill" and msg != "reset" and msg != "disconnect":
                        msg = conn.recv(1024).decode()
                        if msg == "cpu":
                            cpu = str(psutil.cpu_percent())
                            conn.send(cpu.encode())
                            print('cpu : ', cpu)

                        elif msg == "os" :
                            os = str(sys.platform)
                            conn.send(os.encode())
                            print('os : ', os)
                        
                        elif msg == "memory":
                            memory = str(psutil.virtual_memory().total)
                            conn.send(memory.encode())
                            print ('memory : ', memory)
                            
                        elif msg == "ram":
                            ram = str(psutil.disk_usage('/'))
                            conn.send(ram.encode())
                            print('ram : ', ram)
                        
                        elif msg == "ip":
                            ip = socket.gethostbyname(socket.gethostname())
                            conn.send(ip.encode())
                            print('ip : ', ip)
                        
                        elif msg == "name":
                            name = socket.gethostname()
                            conn.send(name.encode())
                            print('name : ', name)
                            
                        elif msg == "python":
                            python = str(sys.version)
                            conn.send(python.encode())
                            print('version : ', python)
                            
                        else :
                            conn.send(msg.encode())
                            print('Receive from client : ', msg)
                    conn.close()
                    print ("Connection closed")
        server_socket.close()
        print ("Server closed")

if __name__ == '__main__':
    serv = Server()
    serv.serveur()