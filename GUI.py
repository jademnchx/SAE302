
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
        test = QComboBox()
        
                
        # Constructeur
        self.__test = test
        
        # ComboBox
        test.addItem("CPU")
        test.addItem("RAM")
        
        # Placement blocks
        grid.addWidget(self.__test, 0, 0)
        
        
        
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()