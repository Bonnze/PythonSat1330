#pyqt 1.0 
# https://docs.google.com/presentation/d/1yKphcke3fU9ngtN5ob5EMkL-21DzqxBD5uNaZNJwhWo/edit?usp=sharing
#calculator
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class Mywindow(QMainWindow):
    def init(self):
        super(Mywindow,self).init()
        self.counter = 0
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Calculator")


        
app = QApplication(sys.argv)
window  = Mywindow()
window.show()
sys.exit(app.exec_())
