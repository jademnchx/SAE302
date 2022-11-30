from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QVBoxLayout, QPushButton
import sys


class TextEditDemo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.i = 0
        self.setWindowTitle("QTextEdit")
        self.resize(300, 270)

        self.textEdit = QTextEdit()
        self.textEdit.setEnabled(False)
        self.btnPress1 = QPushButton("Add message")
        self.btnPress2 = QPushButton("Clear")

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        self.setLayout(layout)

        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)

    def btnPress1_Clicked(self):
        self.textEdit.append(f"Nouveau texte {self.i}")
        self.i += 1
#        self.textEdit.setPlainText("Hello PyQt5!\nfrom pythonpyqt.com")

    def btnPress2_Clicked(self):
        self.textEdit.setPlainText("")
#        self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\nHello</font>")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TextEditDemo()
    win.show()
    sys.exit(app.exec_())
    
    
################################
#   def closeEvent(self, _e: QCloseEvent): # <--- Fermeture de l'application depuis la croix Windows
#        box = QMessageBox()
#        box.setWindowTitle("Quitter ?")
#        box.setText("Voulez vous quitter ?")
#        box.addButton(QMessageBox.Yes)
#        box.addButton(QMessageBox.No)
#
#        ret = box.exec()

#        if ret == QMessageBox.Yes:
#            QCoreApplication.exit(0)
#        else:
#            _e.ignore()
            
################################
