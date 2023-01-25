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
                QtCore.QSize(128, 128),
                QtWidgets.qApp.desktop().availableGeometry()
        ))
    """
    #def mousePressEvent(self, event):
        #label.setText(str(count("..\\")))
    def resizeEvent(self, event):
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        fontsize = int((width + height)/3)
        font.setPointSize(fontsize)
        label.setFont(font)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setGeometry(-int(width*.005),-int(height*.1),width, height)
    """    

def main():
    # Creating Qt Window
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("background-color: black;")
    window.setWindowTitle("Contador V0.5.1")
    icon = QtGui.QIcon("icon.png")
    window.setWindowIcon(icon)

    # Central Widget
    central = QtWidgets.QWidget()
    
    QtWidgets.QFormLayout.

    # Counter Showing
    label = QLabel("", window)
    font = QtGui.QFont()
    font.setPointSize(window.height())
    label.setFont(font)
    label.setAlignment(QtCore.Qt.AlignCenter)
    label.setStyleSheet("color: white;")
    label.setGeometry(0, 0, window.width(), window.height())

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