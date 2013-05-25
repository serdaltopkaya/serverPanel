#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QAbstractItemDelegate, QApplication, QBrush, \
     QCheckBox, QComboBox, QGridLayout, QImage, QLabel, QSpinBox
  
from PyQt4.QtGui import QApplication, QDialog, QListWidgetItem, QListWidget, QIcon


class ControlPanel(QtGui.QWidget):
    def __init__(self,hostIP,hostUser,hostPass, parent=None):
        self.host=hostIP
        self.user=hostUser
        self.password=hostPass 
        print(self.host)
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('server connection panel')

        self.listW = QListWidget(self)
        self.listW.move(220,20)
        self.listW.resize(300,300)
        for i in range(10):
            self.listW.addItem('Item %s' % (i + 1))

        self.listW.itemDoubleClicked.connect(self.getListItem)		 


        self.cb1 = QtGui.QCheckBox('', self)
        self.cb1.move(70, 100)
       # self.cb.togagle()
        

        self.cb2 = QtGui.QCheckBox('', self)
        self.cb2.move(110, 100)
       # self.cb.togagle()


        self.cb3 = QtGui.QCheckBox('', self)
        self.cb3.move(150, 100)
        #self.cb.togagle()

        self.cb4 = QtGui.QCheckBox('', self)
        self.cb4.move(70, 130)
        #self.cb.togagle()
        

        self.cb5 = QtGui.QCheckBox('', self)
        self.cb5.move(110, 130)
        #self.cb.togagle()


        self.cb6 = QtGui.QCheckBox('', self)
        self.cb6.move(150, 130)
        #self.cb.togagle()

        self.cb7 = QtGui.QCheckBox('', self)
        self.cb7.move(70, 160)
        #self.cb.togagle()
        

        self.cb8 = QtGui.QCheckBox('', self)
        self.cb8.move(110, 160)
        #self.cb.togagle()


        self.cb9 = QtGui.QCheckBox('', self)
        self.cb9.move(150, 160)
        #self.cb.togagle()




        self.geri = QtGui.QPushButton('GERI', self)
        self.geri.setFocusPolicy(QtCore.Qt.NoFocus)
        self.geri.move(5, 5)

        self.suankiDizin = QtGui.QLabel("DIZIN", self)
        self.suankiDizin.move(100,10)


        self.dizinIslemleri = QtGui.QLabel("IZIN ISLEMLERI", self)
        self.dizinIslemleri.move(10,50)
       
        self.sahip = QtGui.QLabel("SAHIP", self)
        self.sahip.move(10,100)

        self.grup = QtGui.QLabel("GRUP", self)
        self.grup.move(10,130)

        self.diger = QtGui.QLabel("DIGER", self)
        self.diger.move(10,160)

        self.oku = QtGui.QLabel("OKU", self)
        self.oku.move(70,85)
 
       
        self.yaz = QtGui.QLabel("YAZ", self)
        self.yaz.move(110,85)

        self.calistir = QtGui.QLabel("CALSTR", self)
        self.calistir.move(150,85)

       
        self.klasor = QtGui.QLabel(" KLASOR", self)
        self.klasor.move(520,10)

        self.yeniKlasor = QtGui.QPushButton('YENI', self)
        self.yeniKlasor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.yeniKlasor.move(520, 25)

        self.silKlasor = QtGui.QPushButton('SIL', self)
        self.silKlasor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.silKlasor.move(520, 55)

        self.indirKlasor = QtGui.QPushButton('INDIR', self)
        self.indirKlasor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.indirKlasor.move(520, 85)
        
        self.yukleKlasor = QtGui.QPushButton('YUKLE', self)
        self.yukleKlasor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.yukleKlasor.move(520, 115)
          
    def getListItem(self):
        items = self.listW.selectedItems()
        x=[]
        for i in range(len(items)):
            x.append(str(self.listW.selectedItems()[i].text()))
        print x

    #def Start(self):
     #   panel = ControlPanel()
      #  panel.show()

if __name__ == "__main__":
  app = QApplication(sys.argv)
  con=ControlPanel()
  con.show()
  app.exec_()
