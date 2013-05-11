#!/usr/bin/python
# inputdialog.py
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
class InputDialog(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('server connection panel')
        self.button = QtGui.QPushButton('CONNECT', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20, 20)
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.connectToServer)
        self.setFocus()
        self.ipEdit = QtGui.QLineEdit(self)
        self.ipEdit.move(130, 22)
    def connectToServer(self):
        ip= self.ipEdit.text()
        if ip=="":
            reply = QtGui.QMessageBox.warning(self, 'didnt connect','you should enter server ip to enter aria')
	    
 
app = QtGui.QApplication(sys.argv)
icon = InputDialog()
icon.show()
app.exec_()
