
from PyQt5.QtWidgets import *
import sys
from client import Client

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        ''' Initialisation '''
        widget = QWidget()
        self.setCentralWidget(widget)
        self.setWindowTitle("SAE302")
        grid = QGridLayout()
        widget.setLayout(grid)


        ''' Blocks '''
        block1 = QGroupBox("Commande") 
        block1.setLayout(QGridLayout())
        cpu = QPushButton("CPU")
        os = QPushButton("OS")
        memory = QPushButton("Memory")
        ram = QPushButton("RAM")
        ip = QPushButton("IP")
        name = QPushButton("Name")
        python = QPushButton("Python")

        block2 = QGroupBox("Client")
        block2.setLayout(QGridLayout())
        ipserv = QLineEdit("")
        portserv = QLineEdit("")
        connect = QPushButton("Connect")
        message = QLineEdit("")
        send = QPushButton("Send")


        block3 = QGroupBox("Serveur")
        block3.setLayout(QGridLayout())
        kill = QPushButton("Kill")
        reset = QPushButton("Reset")
        disconnect = QPushButton("Disconnect")
        
        block4 = QGroupBox("Historique")
        block4.setLayout(QGridLayout())
        histo = QTextEdit()
        histo.setEnabled(False)

        block5 = QGroupBox("Résultat")
        block5.setLayout(QGridLayout())
        res = QTextEdit()
        res.setEnabled(False)
        
        block6 = QGroupBox("Fichier")
        block6.setLayout(QGridLayout())
        fichier = QLabel("Lecture de fichier")
        nomfichier = QLineEdit()
        lire = QPushButton("Lire")

        ''' Constructeur '''
        self.histo = histo
        self.res = res
        self.connect = connect
        self.message = message
        self.nomfichier = nomfichier
        self.ipserv = ipserv
        self.portserv = portserv



        ''' Grid blocks '''
        grid.addWidget(block1, 0, 0, 3, 2)
        grid.addWidget(block2, 3, 0, 2, 2)
        grid.addWidget(block3, 0, 2, 3, 2)
        grid.addWidget(block4, 3, 2, 2, 2)
        grid.addWidget(block5, 5, 0, 2, 4)
        grid.addWidget(block6, 7, 0, 2, 4)

        ''' Layout blocks '''
        block1.layout().addWidget(cpu, 0, 0)
        block1.layout().addWidget(os, 0, 1)
        block1.layout().addWidget(memory, 0, 2)
        block1.layout().addWidget(ram, 0, 3)
        block1.layout().addWidget(ip, 1, 0)
        block1.layout().addWidget(name, 1, 1)
        block1.layout().addWidget(python, 1, 2)
        
        block2.layout().addWidget(ipserv, 0, 0)
        block2.layout().addWidget(portserv, 0, 1)
        block2.layout().addWidget(connect, 1, 0)
        block2.layout().addWidget(message, 2, 0)
        block2.layout().addWidget(send, 2, 1)

        block3.layout().addWidget(kill, 0, 1)
        block3.layout().addWidget(reset, 0, 2)
        block3.layout().addWidget(disconnect, 0, 3)

        block4.layout().addWidget(histo, 0, 0)
        block5.layout().addWidget(res, 0, 0)
        

        block6.layout().addWidget(fichier, 0, 0)
        block6.layout().addWidget(nomfichier, 1, 0)
        block6.layout().addWidget(lire, 2, 0)


        ''' Actions blocks '''
        # cpu.clicked.connect(self.__cpu)
        # os.clicked.connect(self.__os)
        # memory.clicked.connect(self.__memory)
        # ram.clicked.connect(self.__ram)
        # ip.clicked.connect(self.__ip)
        # name.clicked.connect(self.__name)
        # python.clicked.connect(self.__python)

        kill.clicked.connect(self.__kill)
        reset.clicked.connect(self.__reset)
        disconnect.clicked.connect(self.__disconnect)

        # send.clicked.connect(Client.__dialogue)
        connect.clicked.connect(self.__connect)
        lire.clicked.connect(self.__lire_Clicked)


        '''Client'''
    def __connect(self):
        clientlist = []
        IP = []
        IP.append(self.ipserv.text())
        for ip in IP:
            print ('connecté à : ', ip)
            clientlist.append(Client(ip, self.portserv.text()))
        self.histo.append(f"connect : {ip}")
        self.connect.setEnabled(False)
        
         
        '''Server'''
    def __kill(self):
        msg = "kill"
        Client.envoi(msg)
        self.histo.append(msg)
    def __reset(self):
        msg = "reset"
        Client.envoi(msg)
        self.histo.append(msg)
    def __disconnect(self):
        msg = "disconnect"
        Client.envoi(msg)
        self.histo.append(msg)
        
        
        ''' Commandes'''
    # def __cpu(self):
    #     msg = "cpu"
    #     Client.__dialogue(msg)
    #     self.histo.append(msg)
    # def __os(self):
    #     msg = "os"
    #     Client.__dialogue(msg)
    #     self.histo.append(msg)
    # def __memory(self):
    #     msg = "memory"
    #     Client.__dialogue(msg)
    #     self.histo.append(msg)
    # def __ram(self):
    #     msg = "ram"
    #     Client.__dialogue(msg)
    #     self.histo.append(msg)
    # def __ip(self):
    #     msg = "ip"
    #     Client.__dialogue(msg)
    #     self.histo.append(msg)
    # def __name(self):
    #     msg = "name"
    #     Client.__dialogue(msg)
    #     self.histo.append(msg)
    # def __python(self):
    #     msg = "python"
    #     Client.__dialogue(msg)
    #     self.histo.append(msg)

        '''Fichier'''
    def __lire_Clicked(self):
        print ("lire : ", self.nomfichier.text())
        clientlist = []
        IP = []
        IP.append("localhost")
        for ip in IP:
            print ("connexion à ", ip, "port 10958")
            clientlist.append(Client(ip, 10958))

if __name__ == '__main__':
    '''Create the Qt Application'''
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()