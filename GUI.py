
from PyQt5.QtWidgets import *
import sys
from servers import cmd

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialisation
        widget = QWidget()
        self.setCentralWidget(widget)
        
        grid = QGridLayout()
        widget.setLayout(grid)
        
        self.setWindowTitle("Test")
        self.resize(400, 300)
        
        # Blocks
        add = QPushButton('Add')
        valid = QPushButton('OK')
        cmd = QComboBox()
        cmd2 = QComboBox()
        
        # Constructeur
        self.__cmd = cmd
        self.__valid = valid
        self.__cmd2 = cmd2
        self.__add = add
        # ComboBox
        cmd.addItem("disconnect")
        cmd.addItem("connect info")
        cmd.addItem("kill")
        cmd.addItem("reset")
        
        cmd2.addItem("OS")
        cmd2.addItem("CPU")
        cmd2.addItem("Name")
        cmd2.addItem("RAM")
        
        # Placement blocks
        grid.addWidget(self.__cmd, 0, 0)
        grid.addWidget(self.__valid, 0, 1)
        grid.addWidget(self.__cmd2, 2, 0)
        grid.addWidget(self.__add, 2, 1)
        
        # Actions blocks
        add.clicked.connect(self.__actionadd)
        valid.clicked.connect(self.__actionvalid)
        
    def __actionadd(self):
        print("Add")
    
    def __actionvalid(self):
        cmd()
        print("Valid")
        
        
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()