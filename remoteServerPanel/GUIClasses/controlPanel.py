#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
import os
import Properties
sys.path.append(r"/home/srdl/serverPanel/remoteServerPanel/Application")
import hashlib
import SSHConnection
import fileTransfer
from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import * #Qt, QStringList
from PyQt4.QtGui import * #QAbstractItemDelegate, QApplication, QBrush, \
     #QCheckBox, QComboBox, QGridLayout, QImage, QLabel, QSpinBox, QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QMessageBox

  
from PyQt4.QtGui import QApplication, QDialog, QListWidgetItem, QListWidget, QIcon


class ControlPanel(QtGui.QWidget):
    def __init__(self,hostIP,hostUser,hostPass, parent=None):
        self.host=hostIP
        self.user=hostUser
        self.password=hostPass 
        print(self.host)
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(10, 10, 700, 700)
        self.setWindowTitle('server connection panel')
        self.connection=SSHConnection.SSHConnection(self.host,self.user,self.password)

        if not self.connection.userClient.login(self.host,self.user,self.password):
           print("connection filed")

        treeWidget = QTreeWidget()
        self.treeWidget = QTreeWidget(self)
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.openMenu)


        self.header=QtGui.QTreeWidgetItem(["name","size","owner","premission"])
        self.treeWidget.setHeaderItem(self.header)

        self.treeWidget.move(220,60)
        self.treeWidget.resize(500,600)
   
        self.treeWidget.itemDoubleClicked.connect(self.getTreeItem)

        self.ownerRead = QtGui.QCheckBox('', self)
        self.ownerRead.move(70, 100)
       
        self.ownerWrite = QtGui.QCheckBox('', self)
        self.ownerWrite.move(110, 100)
       
        self.ownerExe = QtGui.QCheckBox('', self)
        self.ownerExe.move(150, 100)
       
        self.grupRead = QtGui.QCheckBox('', self)
        self.grupRead.move(70, 130)
       
        self.grupWrite = QtGui.QCheckBox('', self)
        self.grupWrite.move(110, 130)
        
        self.grupExe = QtGui.QCheckBox('', self)
        self.grupExe.move(150, 130)
        
        self.otherRead = QtGui.QCheckBox('', self)
        self.otherRead.move(70, 160)
                

        self.otherWrite = QtGui.QCheckBox('', self)
        self.otherWrite.move(110, 160)
        

        self.otherExe = QtGui.QCheckBox('', self)
        self.otherExe.move(150, 160)
        

        self.geri = QtGui.QPushButton('BACK', self)
        self.geri.setFocusPolicy(QtCore.Qt.NoFocus)
        self.geri.move(5, 5)
        self.geri.clicked.connect(self.turnBack)
       
        self.suankiDizin = QtGui.QLabel("CURRENT DIR", self)
        self.geri.setFocusPolicy(QtCore.Qt.NoFocus)
        self.suankiDizin.move(100,10)
        
        self.dizinIslemleri = QtGui.QLabel("PERMISSIONS", self)
        self.dizinIslemleri.move(10,60)
       
        self.owner = QtGui.QLabel("OWNER", self)
        self.owner.move(10,100)

        self.grup = QtGui.QLabel("GRUP", self)
        self.grup.move(10,130)

        self.other = QtGui.QLabel("OTHER", self)
        self.other.move(10,160)

        self.read = QtGui.QLabel("R", self)
        self.read.move(70,85)
        
        self.write = QtGui.QLabel("W", self)
        self.write.move(110,85)

        self.execute = QtGui.QLabel("EX", self)
        self.execute.move(150,85)
       
        self.premission = QtGui.QPushButton('CHANGE PREMISSION',self)
        self.premission.setFocusPolicy(QtCore.Qt.NoFocus)
        self.premission.move(10, 180)
        self.premission.clicked.connect(self.changePremission)
         

        self.dizinIslemleri = QtGui.QLabel("DIR-FOLDER OPERATIONS", self)
        self.dizinIslemleri.move(10,240)

        self.create = QtGui.QPushButton('CREATE NEW DIR',self)
        self.create.setFocusPolicy(QtCore.Qt.NoFocus)
        self.create.move(10, 260)
        self.create.clicked.connect(self.createDir)
   
        self.remove = QtGui.QPushButton('REMOVE DIR',self)
        self.remove.setFocusPolicy(QtCore.Qt.NoFocus)
        self.remove.move(25, 290)
        self.remove.clicked.connect(self.removeDir)
       
       
        self.upload = QtGui.QPushButton('UPLOAD FOLDER',self)
        self.upload.setFocusPolicy(QtCore.Qt.NoFocus)
        self.upload.move(15, 320)
        self.upload.clicked.connect(self.uploadFolder)
        
      
        self.download = QtGui.QPushButton('DOWNLOAD  FOLDER',self)
        self.download.setFocusPolicy(QtCore.Qt.NoFocus)
        self.download.move(10, 350)
        self.download.clicked.connect(self.downloadFolder)


        self.editbutton = QtGui.QPushButton('EDIT FILE',self)
        self.editbutton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.editbutton.move(10, 380)
        self.editbutton.clicked.connect(self.editFile)
    

    @pyqtSlot()
    def properties(self):
    	print"its in"
    	global ex;
    	ex = Properties.Example()
    	ex.show()
    	print "isnt in"
        #sys.exit(app.exec_())

    def openMenu(self, position):
        print self.treeWidget.currentItem().text(0)
            
        menu = QMenu()
        
        if '.' in self.treeWidget.currentItem().text(0):
            action1 = menu.addAction("edit file")
            self.connect(action1,SIGNAL("triggered()"),
					self,SLOT("editFile()"))
            action3 = menu.addAction("copy to")  
            
            action2 = menu.addAction("rename file")
            #self.connect(action1,SIGNAL("triggered()"),
			#		self,SLOT("removeDir()"))
        action4 = menu.addAction("move to")
        action5 = menu.addAction("move to trash")
        self.connect(action5,SIGNAL("triggered()"),
					self,SLOT("removeDir()"))
        action6 = menu.addAction("properties")
        self.connect(action6,SIGNAL("triggered()"),
					self,SLOT("properties()"))

        
           
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            print "right pressed."
            #event.accept()
            #self.rightClickMenu(event)
        else:
        	print "other pressed."
            #event.ignore()

        
    @pyqtSlot()
    def rightClickMenu(self,  event):
        pos = event.pos
        self.gui.ui.menuEdit.popup(QtGui.QCursor.pos())


    def uploadFolder(self):
        localPath=""
        for localPath in QtGui.QFileDialog.getOpenFileNames(self, "selcet file"):
            print localPath
        if localPath:
            reply = QtGui.QMessageBox.question(self, 'Message',
                "Are you sure you want to upluad  "+localPath+" ?", QtGui.QMessageBox.Yes |
                QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                fileName=localPath.split("/")  
                remotePath=str(self.serverCurrentDir[1]+"/"+fileName[len(fileName)-1])
                server=fileTransfer.Server(self.user, self.password, self.host)
                
                server.upload(str(localPath),str(remotePath))
                server.close()
                #QMessageBox.information(self, 'Info Message', "its done correctly",
                #QMessageBox.Ok)
                #else:
                #    QMessageBox.information(self, 'Info Message', "An error accoured.",
                #    QMessageBox.Ok)

                self.getServerDirList();
            else:
                print "didnt done"
        else:
            QMessageBox.information(self, 'Info Message', "You didnt selected anything",
            QMessageBox.Ok)




    def downloadFolder(self):
        if self.treeWidget.currentItem():
            dirName=self.treeWidget.currentItem().text(0)
            reply = QtGui.QMessageBox.question(self, 'Message',
                "Are you sure you want to download "+dirName+" ?", QtGui.QMessageBox.Yes |
                QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                remotePath=str(self.serverCurrentDir[1]+"/"+dirName)
                localPath=str("/home/srdl/"+dirName)
                server=fileTransfer.Server(self.user, self.password, self.host)
                server.download(str(remotePath), str(localPath))
                server.close()
                print "its done"
            else:
                print "didnt done"
        else:
            QMessageBox.information(self, 'Info Message', "You didnt selected anything",
            QMessageBox.Ok)

    def reNameFile(self):
        if self.treeWidget.currentItem():
            dirName=self.treeWidget.currentItem().text(0)
            reply = QtGui.QMessageBox.question(self, 'Message',
                "Are you sure you want to rename "+dirName+" ?", QtGui.QMessageBox.Yes |
                QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                pass	
                #remotePath=str(self.serverCurrentDir[1]+"/"+dirName)
                #localPath=str("/home/srdl/"+dirName)
                #server=fileTransfer.Server(self.user, self.password, self.host)
                #server.download(str(remotePath), str(localPath))
                #server.close()
                #print "its done"
            #else:
            #    print "didnt done"
        #else:
        #    QMessageBox.information(self, 'Info Message', "You didnt selected anything",
        #    QMessageBox.Ok) 


          
    @pyqtSlot()
    def editFile(self):
        if self.treeWidget.currentItem():
            dirName=self.treeWidget.currentItem().text(0)
            reply = QtGui.QMessageBox.question(self, 'Message',
                "Are you sure you want to edit "+dirName+" ?", QtGui.QMessageBox.Yes |
                QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                self.remotePath=str(self.serverCurrentDir[1]+"/"+dirName)
                self.localPath= os.getcwd()  #str("/home/srdl/serverPanel/remoteServerPanel/GUIClasses/cache"+dirName)
                self.localPath=self.localPath+"/cache"
            
                if not os.path.isdir(self.localPath):
       	            os.makedirs(self.localPath)
                server=fileTransfer.Server(self.user, self.password, self.host)
                server.download(str(self.remotePath), str(self.localPath+dirName))
                server.close()
            self.localPath=self.localPath+dirName

            if os.path.isfile(self.localPath):
                self.filehash1 = hashlib.md5(open(self.localPath,'rb').read())
             	print self.filehash1.hexdigest() ;
             	os.system("gedit "+str(self.localPath))
                self.filehash2 = hashlib.md5(open(self.localPath,'rb').read())

                if self.filehash1.hexdigest()==self.filehash2.hexdigest():
                 	print "esit"
                 	QMessageBox.information(self, 'Info Message', "You didnt selected anything",
                    QMessageBox.Ok)

                if self.filehash1.hexdigest()!=self.filehash2.hexdigest():
                    print "esit  degil  "
                    reply = QtGui.QMessageBox.question(self, 'Message',
                    "Are you sure you want to edit "+dirName+" ?", QtGui.QMessageBox.Yes |
                    QtGui.QMessageBox.No, QtGui.QMessageBox.No)

                    if reply == QtGui.QMessageBox.Yes:
                        server=fileTransfer.Server(self.user, self.password, self.host)
                        server.upload(str(self.localPath),str(self.remotePath))
                        server.close()
                        self.getServerDirList(); 


 
    @pyqtSlot()
    def removeDir(self):
        if self.treeWidget.currentItem():
            dirName=self.treeWidget.currentItem().text(0)
            reply = QtGui.QMessageBox.question(self, 'Message',
                "Are you sure you want to remove "+dirName+" ?", QtGui.QMessageBox.Yes |
                QtGui.QMessageBox.No, QtGui.QMessageBox.No)

            if reply == QtGui.QMessageBox.Yes:
                command= "rm -r "+dirName
                self.handleCommand(command)
            else:
                print "didnt done"
        else:
            QMessageBox.information(self, 'Info Message', "You didnt selected anything",
            QMessageBox.Ok)





    def createDir(self):
        dirName, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 
            'Enter dir name:')
        
        if ok:
            command="mkdir "+dirName
            self.handleCommand(command)


       
    def connectionBuilder(self):
        
        self.connection=SSHConnection.SSHConnection(self.host,self.user,self.password)

        if not self.connection.userClient.login(self.host,self.user,self.password):
            print("connection filed")
        else:
            print ("ssh session login  successfuly")
            self.getServerDirList();



      
    def getTreeItem(self):
    	if '.' in self.treeWidget.currentItem().text(0):
    		self.editFile()
   
        else :
        	self.handleCommand("cd "+self.treeWidget.currentItem().text(0));
        #print self.treeWidget.currentItem().text(1);




    def turnBack(self):
        self.handleCommand("cd ..");





    def changePremission(self):
        #text=self.treeWidget.currentItem().text(0)
        if self.treeWidget.currentItem():
            text=self.treeWidget.currentItem().text(0)
            print "yes it is"
            reply = QtGui.QMessageBox.question(self, 'Message',
                "Are you sure you want to change premission of "+text+" ?", QtGui.QMessageBox.Yes |
                QtGui.QMessageBox.No, QtGui.QMessageBox.No) 

            if reply == QtGui.QMessageBox.Yes:
                print "its done"
                self.setPremission(text)
            else:
                print "didnt done"
        else:
            print "you didnt selected anything " 
            QMessageBox.information(self, 'Info Message', '''You didnt selected anything''',
            QMessageBox.Ok)           

                       

    def setPremission(self,text):
        r= self.ownerRead.checkState()
        w=self.ownerWrite.checkState()
        e=self.ownerExe.checkState()
        owner=0;
        if r!=0:
            owner+=4
            self.ownerRead.setCheckState( QtCore.Qt.Unchecked )
        if w!=0:
            owner+=2
            self.ownerWrite.setCheckState( QtCore.Qt.Unchecked )

        if e!=0:
            owner+=1
            self.ownerExe.setCheckState( QtCore.Qt.Unchecked )

        grup=0;
        r= self.grupRead.checkState()
        w=self.grupWrite.checkState()
        e=self.grupExe.checkState()
        if r!=0:
            grup+=4
            self.grupRead.setCheckState( QtCore.Qt.Unchecked )

        if w!=0:    
            grup+=2
            self.grupWrite.setCheckState( QtCore.Qt.Unchecked )

        if e!=0:    
            grup+=1
            self.grupExe.setCheckState( QtCore.Qt.Unchecked )

        r= self.otherRead.checkState()
        w=self.otherWrite.checkState()
        e=self.otherExe.checkState()
        other=0;
        if r!=0:
            other+=4
            self.otherRead.setCheckState( QtCore.Qt.Unchecked )

        if w!=0:    
            other+=2
            self.otherWrite.setCheckState( QtCore.Qt.Unchecked )

        if e!=0:    
            other+=1
            self.otherExe.setCheckState( QtCore.Qt.Unchecked )

    
        premission=str(owner)+str(grup)+str(other)
        chmodCommand="chmod "+premission+" "+text 
        self.handleCommand(chmodCommand)



        
    def setServerFileList(self, serverFileList):
        self.treeWidget.clear()
        itemList=[]; i=0;
        while i <(len(serverFileList)-3):
            a=QStringList([str(serverFileList[i]),str(serverFileList[i+1]),str(serverFileList[i+2]),str(serverFileList[i+3])]);
            item = QTreeWidgetItem(self.treeWidget, a)
            itemList.append(item); i=i+4
        self.treeWidget.insertTopLevelItems(0,itemList)




    def setCurrentDir(self, currentDir):
        self.suankiDizin.setText(currentDir)   
        self.suankiDizin.setWordWrap(True)




    def getServerDirList(self):
        self.connection.userClient.sendline("ls -l --color=none")
        self.connection.userClient.prompt()

        fileArray=str(self.connection.userClient.before)
        self.serverFiles=fileArray.split( )
        i=5;
        self.serverFiles1=[]

        self.connection.userClient.sendline("pwd");
        self.connection.userClient.prompt()

        currentDir=str(self.connection.userClient.before)
        
        self.serverCurrentDir=currentDir.split( )
        self.setCurrentDir(self.serverCurrentDir[1])
        while (i+8)<len(self.serverFiles):
            self.serverFiles1.append(self.serverFiles[i+8]);
            self.serverFiles1.append(self.serverFiles[i+4]);
            self.serverFiles1.append(self.serverFiles[i+2]);
            self.serverFiles1.append(self.serverFiles[i]);
            i=i+9
        self.setServerFileList(self.serverFiles1)




    def handleCommand(self,cmd):
       
        self.connection.userClient.sendline(cmd)
        print "it s done"
        self.connection.userClient.prompt()
        self.getServerDirList();        
   



if __name__ == "__main__":
  app = QApplication(sys.argv)
  con=ControlPanel("192.168.1.45", "srdl","ser21")
  con.show()
  con.connectionBuilder()
  app.exec_()

