
from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        widget = QWidget()
        self.setCentralWidget(widget)
        
        grid = QGridLayout()
        widget.setLayout(grid)
        
        # Blocks
        test = QComboBox()
        
                
        # Constructeur
        self.__test = test
        
        # ComboBox
        test.addItem("C -> K")
        test.addItem("K -> C")
        
        # Placement blocks
        grid.addWidget(self.__test, 0, 0)
        
        # Actions blocks
        self.setWindowTitle("One")
        
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()