import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.closebutton=QPushButton("Hello")
        self.connect(self.closebutton,SIGNAL("clicked()"),self,SLOT("close()"))
        layout=QVBoxLayout()
        layout.addWidget(self.closebutton)
        self.setLayout(layout)
        self.setWindowTitle("hello")
        self.resize(800, 500)
app=QApplication(sys.argv)
form=Form()
form.show()
app.exec_()
        
        
