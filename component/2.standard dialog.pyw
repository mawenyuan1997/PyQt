import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

class StandardDialog(QDialog):
    def __init__(self,parent=None):
        super(StandardDialog,self).__init__(parent)
        
        self.setWindowTitle("Standard Dialog")
        
        filebutton=QPushButton(self.tr("文件对话框"))
        colorbutton=QPushButton(self.tr("颜色对话框"))
        fontbutton=QPushButton(self.tr("字体对话框"))
        
        self.directory=QLineEdit()
        self.colorframe=QFrame()
        self.colorframe.setFrameShape(QFrame.Box)
        self.colorframe.setAutoFillBackground(True)
        self.fontlineedit=QLineEdit("hello")
        
        layout=QGridLayout()
        layout.addWidget(filebutton,0,0)
        layout.addWidget(self.directory,0,1)
        layout.addWidget(colorbutton,1,0)
        layout.addWidget(self.colorframe,1,1)
        layout.addWidget(fontbutton,2,0)
        layout.addWidget(self.fontlineedit,2,1)
        self.setLayout(layout)
        
        self.connect(filebutton,SIGNAL("clicked()"),self.openfile)
        self.connect(colorbutton,SIGNAL("clicked()"),self.opencolor)
        self.connect(fontbutton,SIGNAL("clicked()"),self.openfont)
    def openfile(self):
        s=QFileDialog.getOpenFileName(self,"Open file Dialog","/","Python files(*.py)")
        self.directory.setText(str(s))
    def opencolor(self):
        c=QColorDialog.getColor(Qt.blue)
        if c.isValid():
            self.colorframe.setPalette(QPalette(c))
    def openfont(self):
        f,ok=QFontDialog.getFont()
        if ok:
            self.fontlineedit.setFont(f)
app=QApplication(sys.argv)
form=StandardDialog()
form.show()
app.exec_()
