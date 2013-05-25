#!/usr/bin/python
# inputdialog.py
import sys
import controlPanel
from PyQt4 import QtGui
from PyQt4 import QtCore

class ConnectionPanel(QtGui.QWidget):
    def __init__(self, parent=None):
   
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('server connection panel')
   
        self.serverLabel = QtGui.QLabel("SERVER IP      :", self)
        self.serverLabel.move(20,20)
       
        self.userLabel = QtGui.QLabel("USER NAME   :", self)
        self.userLabel.move(20,60)

        self.passLabel = QtGui.QLabel("PASSWORD    :", self)
        self.passLabel.move(20,100)

        self.button = QtGui.QPushButton('CONNECT', self)
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(130, 150)
   
        self.connect(self.button, QtCore.SIGNAL('clicked()'), self.connectToServer)
        self.setFocus()
   
        self.ipEdit = QtGui.QLineEdit(self)
        self.ipEdit.move(130, 20)
   
        self.userName = QtGui.QLineEdit(self)
        self.userName.move(130, 60)
     
        self.password=QtGui.QLineEdit(self)
        self.password.setEchoMode (QtGui.QLineEdit.Password)
        self.password.move(130,100) 
   
    
    def closeEvent(self): 
        self.destory()  


    def connectToServer(self):
        ip= self.ipEdit.text()
        if ip=="":
            reply = QtGui.QMessageBox.warning(self, 'didnt connect','you should enter server ip to enter aria')
	
        else: 
            self.getConInform()
            self.panel = controlPanel.ControlPanel(self.hostIP,self.hostUser,self.hostPass)
            self.panel.show()
      

    def getConInform(self):
            self.hostIP=shost = self.ipEdit.text()
            self.hostUser=self.userName.text()	 
            self.hostPass=self.password.text()
   
def Start():
    global panel
    panel = ConnectionPanel()
    panel.show()
                            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Start()
    app.exec_()
