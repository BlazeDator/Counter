import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags( QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.X11BypassWindowManagerHint )
        self.font = QtGui.QFont()

        self.textTotal = QtWidgets.QLabel("Total: ")
        self.counterTotal = QtWidgets.QLabel("00")
        self.newButton= QtWidgets.QPushButton("Novo")

        # Storage
        self.labels = [self.textTotal, self.counterTotal]
        self.buttons = [self.newButton]
        self.lines = []

        self.layout = QtWidgets.QFormLayout(self)
        self.layout.addRow(self.textTotal, self.counterTotal)
        self.layout.addRow(self.newButton)
        self.magic()

        self.resizeEvent(self)
        self.newButton.clicked.connect(self.magic)
        

    @QtCore.Slot()
    def magic(self):
        line = QtWidgets.QLineEdit("Nome")
        self.lines.append(line)

        text = QtWidgets.QLabel("00")
        self.labels.append(text)

        self.layout.addRow(line, text)
        self.resizeEvent(self)

    def resizeEvent(self, event):
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()

        # Control Sizes here
        labelSize = int((width + height)/24)
        buttonSize = int((width + height)/32)
        lineSize = int((width + height)/32)

        self.font.setPointSize(labelSize)
        for label in self.labels:
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setFont(self.font)

        self.font.setPointSize(buttonSize)    
        for button in self.buttons:
            button.setFont(self.font)

        self.font.setPointSize(lineSize)    
        for line in self.lines:
            line.setFont(self.font)

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