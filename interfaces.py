from PyQt5.QtWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialize the main window
        widget = QWidget()
        self.setCentralWidget(widget)
        
        grid = QGridLayout()
        widget.setLayout(grid)
        
        # Blocks
        test=QLabel("Test")
        
        # Constructeur
        self.__test = test
        
        # Placement blocks
        grid.addWidget(self.__test, 0, 0)
        
        # Actions
        self.setWindowTitle("Test")
        
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
        
        