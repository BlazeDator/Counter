import sys, os, re

from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication,QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.WindowCloseButtonHint |
            #QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.X11BypassWindowManagerHint
        )
        self.setGeometry(
            QtWidgets.QStyle.alignedRect(
                QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter,
                QtCore.QSize(96, 96),
                QtWidgets.qApp.desktop().availableGeometry()
        ))

    #def mousePressEvent(self, event):
        #label.setText(str(count("..\\")))
    def resizeEvent(self, event):
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        fontsize = int(width*.40 + height*.20)
        font.setPointSize(fontsize)
        label.setFont(font)
        label.setGeometry(int(width/16),-int(height/9),width, height)
        

def main():
    # Creating Qt Window
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("background-color: black;")
    window.setWindowTitle("Contador V0.5")
    icon = QtGui.QIcon("icon.png")
    window.setWindowIcon(icon)

    # Counter Showing
    global label
    label = QLabel("", window)
    global font
    font = QtGui.QFont()
    label.setStyleSheet("color: white;")

    #Timer - Update every 128ms
    timer = QtCore.QTimer(window)
    timer.setInterval(128) 

    # Connect the timer's timeout signal to a slot that updates the label's content
    def updateLabel():
        counter = 0
        dir = os.listdir("..\\")
        for file in dir:
            if re.match(r"^\d+_V1_\d+.*$", file):
                counter += 1
        label.setText(str(counter).zfill(2))

    timer.timeout.connect(updateLabel)

    # Start the timer
    timer.start()
    
    # Qt Window
    window.show()
    window.update()
    app.exec_()

if __name__ == '__main__':
    main()