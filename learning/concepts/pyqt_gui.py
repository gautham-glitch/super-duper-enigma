import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,
QVBoxLayout,QHBoxLayout,QWidget,QGridLayout,QPushButton,QCheckBox,QRadioButton,QButtonGroup,QLineEdit)
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt
class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my first widget")
        self.setGeometry(700,300,1000,200)
        self.setWindowIcon(QIcon("C:\\Users\\kaart\\OneDrive\\Desktop\\Screenshot 2025-04-20 141046.jpg"))

        self.txtbox = QLineEdit(self)
        self.button = QPushButton("submit",self)

        self.initui()
    def initui(self):
        self.txtbox.setGeometry(10,10,200,40)
        self.txtbox.setStyleSheet("font-size: 25px;"
                                    "font-family: Comic sans ms;")
        self.button.setGeometry(210,10,200,40)
        self.button.setStyleSheet("font-size: 25px;"
                                    "font-family: Comic sans ms;")
        self.button.clicked.connect(self.submit)

        self.txtbox.setPlaceholderText("enter your name")
    def submit(self):
        text = self.txtbox.text()
        print(f"hello, {text}")

def main():
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()