
from PyQt5.QtWidgets import *
import sys
from client import Client
from servers import Server

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
        cmd = QComboBox()
        cmd.addItems(["cpu", "os", "memory", "ram", "ip", "name", "python"])

        block2 = QGroupBox("Client")
        block2.setLayout(QGridLayout())
        connect = QPushButton("Connect")
        com = QComboBox()
        com.addItems(["kill", "reset", "disconnect"])
        comm = QPushButton("Envoyer")

        block3 = QGroupBox("Serveur")
        block3.setLayout(QGridLayout())
        start = QPushButton("Start")

        block4 = QGroupBox("Historique")
        block4.setLayout(QGridLayout())
        histo = QTextEdit()
        histo.setEnabled(False)

        block5 = QGroupBox("Résultat")
        block5.setLayout(QGridLayout())
        res = QTextEdit()
        res.setEnabled(False)
        result = QPushButton("Valider")

        block6 = QGroupBox("Fichier")
        block6.setLayout(QGridLayout())
        fichier = QLabel("Lecture de fichier")
        nomfichier = QLineEdit()
        lire = QPushButton("Lire")


        ''' Constructeur '''
        self.cmd = cmd
        self.histo = histo
        self.res = res
        self.nomfichier = nomfichier


        ''' Grid blocks '''
        grid.addWidget(block1, 0, 0, 3, 2)
        grid.addWidget(block2, 3, 0, 2, 2)
        grid.addWidget(block3, 0, 2, 3, 2)
        grid.addWidget(block4, 3, 2, 2, 2)
        grid.addWidget(block5, 5, 0, 2, 4)
        grid.addWidget(block6, 7, 0, 2, 4)
        


        ''' Layout blocks '''
        block1.layout().addWidget(cmd, 1, 0)
        block1.layout().addWidget(result, 1, 1)
        block2.layout().addWidget(connect, 0, 0)
        block2.layout().addWidget(com, 2, 0)
        block2.layout().addWidget(comm, 2, 1)
        block3.layout().addWidget(start, 0, 0)
        block4.layout().addWidget(histo, 0, 0)
        block5.layout().addWidget(res, 0, 0)
        block6.layout().addWidget(fichier, 0, 0)
        block6.layout().addWidget(nomfichier, 1, 0)
        block6.layout().addWidget(lire, 2, 0)


        ''' Actions blocks '''
        cmd.currentIndexChanged.connect(self.__cmd_Clicked)
        lire.clicked.connect(self.__lire_Clicked)
        connect.clicked.connect(self.__connect_Clicked)
        start.clicked.connect(self.__start_Clicked)


    ''' Fonctions blocks '''

    def __lire_Clicked(self):
        print ("lire : ", self.nomfichier.text())
        clientlist = []
        IP = []
        IP.append("localhost")
        for ip in IP:
            print ("connexion à ", ip, "port 10958")
            clientlist.append(Client(ip, 10958))
        
    def __cmd_Clicked(self):    
        self.res.append(f"cmd : {self.cmd.currentText()}")

    def __connect_Clicked(self):
        clientlist = []
        IP = []
        IP.append("localhost")
        for ip in IP:
            print ("connexion à ", ip, "port 10958")
            clientlist.append(Client(ip, 10958))
        self.histo.append(f"connect : {ip}")

    def __disconnect_Clicked(self):
        Server.serveur(self)
        self.histo.append("disconnect")
        

    def __reset_Clicked(self):
        Server.serveur(self)
        self.histo.append("reset")
        

    def __kill_Clicked(self):
        self.histo.append("kill")
        Server.serveur(self)
        print ("kill success")
        

    def __start_Clicked(self):
        self.histo.append("start")
        Server.serveur(self)
        
        
        



if __name__ == '__main__':
    '''Create the Qt Application'''
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()