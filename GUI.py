
from PyQt5.QtWidgets import *
import sys
from client import Client
from servers import Server

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialisation
        widget = QWidget()
        self.setCentralWidget(widget)
        self.setWindowTitle("SAE302")
        
        grid = QGridLayout()
        widget.setLayout(grid)
        
        self.textEdit = QTextEdit()
        self.textEdit.setEnabled(False)

        # Blocks
        block1 = QGroupBox("Commande") 
        block1.setLayout(QGridLayout())
        cmd1 = QComboBox()
        cmd2 = QComboBox()
        
        block2 = QGroupBox("Connection")
        block2.setLayout(QGridLayout())
        connect = QPushButton("Connect")
        disconnect = QPushButton("Disconnect")
        reset = QPushButton("Reset")
        kill = QPushButton("Kill")
        
        # Constructeur
        self.block1 = block1
        self.block2 = block2
        self.__cmd2 = cmd2
        self.__connect = connect
        self.__disconnect = disconnect
        self.__reset = reset
        self.__kill = kill
        
         # ComboBox

        cmd2.addItem("OS")
        cmd2.addItem("CPU")
        cmd2.addItem("Name")
        cmd2.addItem("RAM")

        # Placement blocks
        grid.addWidget(block1, 0, 0, 3, 2)
        grid.addWidget(block2, 3, 0, 2, 2)
        grid.addWidget(self.textEdit, 5, 0)
        
        block1.layout().addWidget(cmd2, 1, 0)
        block2.layout().addWidget(connect, 0, 0)
        
        # Actions blocks
        self.__cmd2.currentIndexChanged.connect(self.cmd2_Clicked)
        
   
    def cmd2_Clicked(self):
        t = self.__cmd2.currentText()
        self.textEdit.append(f"cmd2 : {t}")
        
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()