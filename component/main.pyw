import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
class Form(QDialog):
    def __init__(self,parent=None):
        super(Form,self).__init__(parent)
        self.browser=QTextBrowser()
        self.addline=QLineEdit()
        self.deleteline=QLineEdit()
        self.addlabel=QLabel("Add")
        self.deletelabel=QLabel("Delete")
        grid=QGridLayout()
        grid.addWidget(self.browser,0,0)
        grid.addWidget(self.addlabel,5,0)
        grid.addWidget(self.addline,5,2)
        grid.addWidget(self.deletelabel,6,0)
        grid.addWidget(self.deleteline,6,2)
        self.setLayout(grid)
        self.connect(self.addline,SIGNAL("returnPressed()"),self.updateUi)
        self.setWindowTitle("fruit")
    def updateUi(self):
        try:
            text=str(self.addline.text())
            self.browser.append("%s"%text)
        except:
            self.browser.append("%s is invalid!"%s)
app=QApplication(sys.argv)
form=Form()
form.show()
app.exec_()
            
