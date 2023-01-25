import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags( QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowCloseButtonHint )
        self.font = QtGui.QFont()



        self.textTotal = QtWidgets.QLabel("Total: ")
        self.counterTotal = QtWidgets.QLabel("0")
        self.newButton= QtWidgets.QPushButton("Novo")
        self.prompt = QtWidgets.QLineEdit("Nome")

        # Storage
        self.labels = [self.textTotal, self.counterTotal]
        self.buttons = []

        self.layout = QtWidgets.QFormLayout(self)
        self.layout.addRow(self.textTotal, self.counterTotal)
        self.layout.addRow(self.prompt, self.newButton)
        

        self.resizeEvent(self)
        self.newButton.clicked.connect(self.magic)
        self.newButton.setFont(self.font)

    @QtCore.Slot()
    def magic(self):
        button = QtWidgets.QPushButton(self.prompt.text())
        self.buttons.append(button)

        text = QtWidgets.QLabel("0")
        self.labels.append(text)

        self.layout.addRow(button, text)
        self.resizeEvent(self)

    def resizeEvent(self, event):
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        fontsize = int((width + height)/24)
        self.font.setPointSize(fontsize)
        for label in self.labels:
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setFont(self.font)

def main():
    # Start Application
    app = QtWidgets.QApplication([])

    # Main Window/Widget
    widget = MyWidget()
    widget.resize(256, 256)
    widget.setWindowTitle("Contador V0.6")
    icon = QtGui.QIcon("icon.png")
    widget.setWindowIcon(icon)


    widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()