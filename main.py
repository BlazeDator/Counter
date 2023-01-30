import sys, os, re, csv
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags( QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.X11BypassWindowManagerHint )
        self.font = QtGui.QFont()
        self.sizeP = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)

        # Start UI
        self.textTotal = QtWidgets.QLabel("Total: ")
        self.counterTotal = QtWidgets.QLabel("00")
        self.textReworks = QtWidgets.QLabel("Reworks: ")
        self.counterReworks = QtWidgets.QLabel("00")
        self.newButton = QtWidgets.QPushButton("Novo")
        self.newButton.setStyleSheet("background:#81B38E;")
        self.deleteButton = QtWidgets.QPushButton("Apagar Ultimo")
        self.deleteButton.setStyleSheet("background:#b3818e;")
        
        # Logic
        self.selected = None

        # Storage
        self.labels = [self.textTotal, self.counterTotal, self.textReworks, self.counterReworks]
        self.buttons = [self.newButton, self.deleteButton]
        self.lines = []
        self.linesToLabels = {}

        self.layout = QtWidgets.QFormLayout(self)
        self.layout.addRow(self.textTotal, self.counterTotal)
        self.layout.addRow(self.textReworks, self.counterReworks)
        self.layout.addRow(self.newButton)
        self.layout.addRow(self.deleteButton)

        # Buttons
        self.newButton.clicked.connect(self.new)
        self.deleteButton.clicked.connect(self.delete)

        # First Entry
        if self.loadData():
            print("[LOG] Load Sucessful")
        else:
            self.new()


        # Window Size
        self.resize(384, 192)
        self.resizeEvent(self)


    def new(self, name=None, count=None):
        text = None
        line = myLineEdit(self)
        line.setSizePolicy(self.sizeP)
        if not name:
            text = QtWidgets.QLabel("00")
        else:
            line.setText(name)            
            text = QtWidgets.QLabel(count)

        self.lines.append(line)

        self.labels.append(text)

        self.linesToLabels[line] = text
            
        self.select(x=self.selected)

        self.layout.addRow(line, text)
        self.resizeEvent(self)


    def delete(self):
        if len(self.lines) > 1:
            self.counterTotal.setText(str(int(self.counterTotal.text()) - int(self.linesToLabels[self.lines[-1]].text())).zfill(2))
            if self.lines[-1] is self.selected:
                self.select(x=self.lines[-2])

            self.linesToLabels.pop(self.lines[-1])
            self.lines.pop().deleteLater()
            self.labels.pop().deleteLater()
            self.resizeEvent(self)

            self.resize(self.width(), (self.height() - self.width()))     
        else:
            self.counterTotal.setText("00")
            self.linesToLabels[self.lines[0]].setText("00")  

    def select(self,x=None):
        if self.selected:
            self.selected.setStyleSheet("background:white;")

        if x:
            self.selected = x
        else:
            self.selected = self.lines[-1]
            
        self.selected.setStyleSheet("background:#81B38E;")

    def resizeEvent(self, event):
        width = self.frameGeometry().width()*1.4
        #height = self.frameGeometry().height()*.30
        size = width

        # Control Sizes here
        labelSize = int(size/26)
        buttonSize = int(size/32)
        lineSize = int(size/32)

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

    def saveData(self):
        with open("data/history.csv","w") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "counter"])
            writer.writeheader()
            for row in self.linesToLabels:
                writer.writerow({"name": row.text(), "counter" : self.linesToLabels[row].text()})

    def loadData(self):
        if os.path.isfile("data/history.csv"):
            with open("data/history.csv","r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.new(name=row["name"], count=row["counter"])

            count = 0
            for c in self.linesToLabels:
                count += int(self.linesToLabels[c].text())
            self.counterTotal.setText(str(count).zfill(2))

            return True
        return False

class myLineEdit(QtWidgets.QLineEdit):
    def __init__(self, widget):
        super().__init__()
        self.setText("Inserir Nome")
        self.widget = widget

    def mousePressEvent(self, event):
        self.widget.select(x=self)


def main():
    # Start Application
    app = QtWidgets.QApplication([])

    # Main Window/Widget
    widget = MyWidget()
    widget.setWindowTitle("Contador V0.7")
    icon = QtGui.QIcon("data/icon.png")
    widget.setWindowIcon(icon)

    # Timer for counters - Update every 128ms
    timer = QtCore.QTimer(widget)
    timer.setInterval(128) 

    # Timer to save file
    saveTimer = QtCore.QTimer(widget)
    saveTimer.setInterval(1024) 

    # Connect the timer's timeout signal to a slot that updates the label's content
    def updateLabel():
        counter = 0
        counter_reworks = 0

        dir = os.listdir("..\\")
        for file in dir:
            if re.match(r"^\d+_V1_\d+.*$", file):
                counter += 1
            if re.match(r"^\d+_V1_\w+_\d+.*$", file):
                counter_reworks += 1

        # Count
        total = int(widget.counterTotal.text())
        if counter > total:
            widget.linesToLabels[widget.selected].setText(str(
                int(widget.linesToLabels[widget.selected].text()) + counter - total).zfill(2))
            widget.counterTotal.setText(str(counter).zfill(2))

        # Count Reworks
        widget.counterReworks.setText(str(counter_reworks).zfill(2))
        
    timer.timeout.connect(updateLabel)
    def saveHistory():
        widget.saveData()
    saveTimer.timeout.connect(saveHistory)

    # Start the timer
    timer.start()
    saveTimer.start()

    widget.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()


# PROXIMAS FEATURES

# Salvar o contador atual 
# Contar os reworks a parte "19621617_V1_Rework_29256250"