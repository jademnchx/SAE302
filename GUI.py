
from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialisation
        widget = QWidget()
        self.setCentralWidget(widget)
        self.setWindowTitle("Test")
        self.resize(400, 300)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.textEdit = QTextEdit()
        self.textEdit.setEnabled(False)

        # Blocks
        block1 = QGroupBox("Commande")
        cmd1 = QComboBox()
        cmd2 = QComboBox()
        cmd3 = QComboBox()

        # Constructeur
        self.__cmd1 = cmd1
        self.__cmd2 = cmd2
        self.__cmd3 = cmd3

         # ComboBox
        cmd1.addItem("disconnect")
        cmd1.addItem("connect info")
        cmd1.addItem("kill")
        cmd1.addItem("reset")

        cmd2.addItem("OS")
        cmd2.addItem("CPU")
        cmd2.addItem("Name")
        cmd2.addItem("RAM")

        cmd3.addItem("DOS:dir")
        cmd3.addItem("DOS:mkdir toto")
        cmd3.addItem("Linux:ls -la")
        cmd3.addItem("Powershell:get-process")
        cmd3.addItem("python --version")
        cmd3.addItem("ping 192.157.65.78")       

        # Placement blocks
        grid.addWidget(self.__cmd1, 0, 0)
        grid.addWidget(self.__cmd2, 2, 0)
        grid.addWidget(self.__cmd3, 4, 0)
        grid.addWidget(self.textEdit, 5, 0)
        
        # Actions blocks
        self.__cmd1.currentIndexChanged.connect(self.cmd1_Clicked)
        self.__cmd2.currentIndexChanged.connect(self.cmd2_Clicked)
        self.__cmd3.currentIndexChanged.connect(self.cmd3_Clicked)
        
        
    def cmd1_Clicked(self):
        t = self.__cmd1.currentText()
        self.textEdit.append(f"cmd1 : {t}")
    
    def cmd2_Clicked(self):
        t = self.__cmd2.currentText()
        self.textEdit.append(f"cmd2 : {t}")
        
    def cmd3_Clicked(self):
        t = self.__cmd2.currentText()
        self.textEdit.append(f"cmd3 : {t}")
        
        
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()