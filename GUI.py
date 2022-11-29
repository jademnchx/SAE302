
from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialisation
        widget = QWidget()
        self.setCentralWidget(widget)
        
        grid = QGridLayout()
        widget.setLayout(grid)
        
        self.setWindowTitle("Test")
        self.resize(250,250)
        
        # Blocks
        add = QPushButton('Add')
        cmd = QComboBox()
    
        # Constructeur
        self.__cmd = cmd
        self.__add = add
        
        # ComboBox
        cmd.addItem("disconect")
        cmd.addItem("connect info")
        cmd.addItem("kill")
        cmd.addItem("reset")
        
        # Placement blocks
        grid.addWidget(self.__cmd, 0, 0)
        grid.addWidget(self.__add, 0, 1)
        
        # Actions blocks
        add.clicked.connect(self.__actionadd)
        
    def __actionadd(self):
        print("Add")
        
    def __actiontest(self):
        print("test")
        
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()