import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication, QDialog, QListWidgetItem, QListWidget, QIcon, QTextEdit, QTextDocumentFragment

def main():

    app = QtGui.QApplication(sys.argv)
    window = QDialog()

    list = QListWidget( window )

    textEditor = QTextEdit( window );
    textEditor.setReadOnly( True )
    tick_icon = QTextDocumentFragment.fromHtml(r"<img src='tick.png'>");

    textEditor.insertPlainText ( " ValiumKnight writes: " )
    textEditor.textCursor().insertFragment(tick_icon);
    textEditor.insertPlainText ( " Hello World " )
    textEditor.textCursor().insertFragment(tick_icon);
    textEditor.textCursor().insertFragment(tick_icon);
    textEditor.textCursor().insertFragment(tick_icon);

    window.show( )
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
