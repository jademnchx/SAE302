
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
        cpu = QPushButton("CPU")
        os = QPushButton("OS")
        memory = QPushButton("Memory")
        ram = QPushButton("RAM")
        ip = QPushButton("IP")
        name = QPushButton("Name")
        python = QPushButton("Python")

        block2 = QGroupBox("Client")
        block2.setLayout(QGridLayout())
        connect = QPushButton("Connect")
        message = QLineEdit("Commande")


        block3 = QGroupBox("Serveur")
        block3.setLayout(QGridLayout())
        start = QPushButton("Start")
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

        ''' Constructeur '''
        self.histo = histo
        self.res = res
        self.start = start
        self.connect = connect
        self.message = message


        ''' Grid blocks '''
        grid.addWidget(block1, 0, 0, 3, 2)
        grid.addWidget(block2, 3, 0, 2, 2)
        grid.addWidget(block3, 0, 2, 3, 2)
        grid.addWidget(block4, 3, 2, 2, 2)
        grid.addWidget(block5, 5, 0, 2, 4)


        ''' Layout blocks '''
        block1.layout().addWidget(cpu, 0, 0)
        block1.layout().addWidget(os, 0, 1)
        block1.layout().addWidget(memory, 0, 2)
        block1.layout().addWidget(ram, 0, 3)
        block1.layout().addWidget(ip, 1, 0)
        block1.layout().addWidget(name, 1, 1)
        block1.layout().addWidget(python, 1, 2)
        
        block2.layout().addWidget(connect, 0, 0)
        block2.layout().addWidget(message, 1, 0)

        block3.layout().addWidget(start, 0, 0)
        block3.layout().addWidget(kill, 0, 1)
        block3.layout().addWidget(reset, 0, 2)
        block3.layout().addWidget(disconnect, 0, 3)

        block4.layout().addWidget(histo, 0, 0)
        block5.layout().addWidget(res, 0, 0)


        ''' Actions blocks '''

        start.clicked.connect(self.__serveur_Clicked)


    ''' Fonctions blocks '''
    def __serveur_Clicked(self):
        if self.start.text() == "Start":
            self.start.setText("Stop")
            Server.serveur()
            print('Serveur démarré')
        else:
            print('Serveur arrêté')

    def __connect_Clicked(self):
        Client.run()
    def __message_Clicked(self):
        Client.__envoi(self.message.text())

if __name__ == '__main__':
    '''Create the Qt Application'''
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()