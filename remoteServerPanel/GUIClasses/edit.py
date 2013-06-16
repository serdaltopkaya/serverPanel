
#! /usr/bin/python

import sys
import os
from PyQt4 import QtGui

class Notepad(QtGui.QMainWindow, filename):

    def __init__(self):
        super(Notepad, self).__init__()
        self.initUI()
        
    def initUI(self):
       
        f = open(filename, 'r')
        filedata = f.read()
        self.text.setText(filedata)

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
       
        
    def saveFile(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        f = open(filename, 'w')
        filedata = self.text.toPlainText()
        f.write(filedata)
        f.close()
        
def main():
    app = QtGui.QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
