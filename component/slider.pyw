import sys
from PyQt4 import QtCore, QtGui
app=QtGui.QApplication(sys.argv)
window=QtGui.QWidget()
setnumber=QtGui.QSpinBox()
setnumber.setRange(0,130)
slider=QtGui.QSlider(QtCore.Qt.Horizontal)
#numberlabel=QtGui.QLabel("number")
#numberlabel.setBuddy(setnumber)


slider.setRange(0,130)
#sliderlabel=QtGui.QLabel("range")
#sliderlabel.setBuddy(slider)
QtCore.QObject.connect(setnumber,QtCore.SIGNAL("valueChanged(int)"),slider,QtCore.SLOT("setValue(int)"))
QtCore.QObject.connect(slider,QtCore.SIGNAL("valueChanged(int)"),setnumber,QtCore.SLOT("setValue(int)"))

setnumber.setValue(3)
buttonbox=QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Close)
window.setWindowTitle("slider")
layout=QtGui.QVBoxLayout()
layout.addWidget(setnumber)
layout.addWidget(slider)
layout.addWidget(buttonbox)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
