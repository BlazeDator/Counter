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
                QtCore.QSize(256, 96),
                QtWidgets.qApp.desktop().availableGeometry()
        ))

    #def mousePressEvent(self, event):
        #label.setText(str(count("..\\")))
    #def paintEvent(self, event):
        #label.setText(str(count("..\\")))

def main():
    # Creating Qt Window
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("background-color: black;")
    window.setWindowTitle("Contador V0.3")
    icon = QtGui.QIcon("icon.png")
    window.setWindowIcon(icon)

    # Counter Showing
    global label
    label = QLabel("", window)
    font = QtGui.QFont()
    font.setPointSize(64)
    label.setFont(font)
    label.setStyleSheet("color: white;")
    label.setGeometry(80,0,200, 100)

    #Timer with a refresh rate of 60 FPS
    timer = QtCore.QTimer(window)
    timer.setInterval(256) 

    # Connect the timer's timeout signal to a slot that updates the label's content
    def updateLabel():
        counter = 0
        dir = os.listdir("..\\")
        for file in dir:
            if re.match(r"^\d+_V1_\d+.*$", file):
                counter += 1
        label.setText(str(counter))

    timer.timeout.connect(updateLabel)

    # Start the timer
    timer.start()
    window.show()
    window.update()
    app.exec_()

if __name__ == '__main__':
    main()