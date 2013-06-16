
#! /usr/bin/python
import hashlib
import sys
import os
from PyQt4 import QtGui

class Notepad(QtGui.QMainWindow):

    def __init__(self):
        super(Notepad, self).__init__()
        self.initUI()
        
    def initUI(self): 
        self.filedata=""
        saveAction = QtGui.QAction('Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save current file')
        saveAction.triggered.connect(self.saveFile)
         
        closeAction = QtGui.QAction('Close', self)
        closeAction.setShortcut('Ctrl+Q')
        closeAction.setStatusTip('Close Notepad')
        closeAction.triggered.connect(self.close)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
       
        fileMenu.addAction(saveAction)
        
        fileMenu.addAction(closeAction)
        self.text = QtGui.QTextEdit(self)
        
        self.setCentralWidget(self.text)
        self.setGeometry(300,300,600,600)
        self.setWindowTitle('Notepad')
        self.show()
       
    def openFile(self):
        self.path =os.getcwd()
        self.path1=self.path+"/cache"
        if not os.path.isdir(self.path1):
        	os.makedirs(self.path1)
        	print "folder yaratildi."
        if os.path.isfile(self.path1+"/a.py"):
        	self.path2=self.path1+"/a.py"
        	self.filehash1 = hashlib.md5(open(self.path2,'rb').read())
        	print self.filehash1.hexdigest() ;
        os.system("gedit "+self.path2)
        self.filehash2 = hashlib.md5(open(self.path2,'rb').read())
        print self.filehash2.hexdigest() 
        
        if self.filehash1.hexdigest()==self.filehash2.hexdigest():
            print "esit"
        if self.filehash1.hexdigest()!=self.filehash2.hexdigest():
            print "esit  degil  "

            #f = open(self.path1+"/a.py", 'r')
            #self.filedata = f.read()
            #self.text.setText(self.filedata)
            #f.close()
 
    def saveFile(self):
        #filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        print "girdi"
        if self.text == self.filedata:
        	print "ayni"
        if self.text  != self.filedata:
        	print self.text

       #import hashlib
       #>>> filehash = hashlib.md5(open('denme1.py','rb').read())
       #>>> print "FILE HASH: " + filehash.hexdigest() 

        f = open(self.path1+"/a.py", 'w')
        self.filedata = self.text.toPlainText()
       
        f.write(self.filedata)
        f.close()
        
def main():
    app = QtGui.QApplication(sys.argv)
    notepad = Notepad()
    notepad.openFile();
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()