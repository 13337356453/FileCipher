import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from FileCipherEvent import FileCipherEvent
from windows.FileCipher import Ui_MainWindow


class FileCipher(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(FileCipher,self).__init__()
        self.setupUi(self)
        self.init()
    def init(self):
        self.bind()

    def bind(self):
        self.controller=FileCipherEvent(self)
        self.choiceFileBtn.clicked.connect(self.controller.choiceFile)
        self.makeKeybtn.clicked.connect(self.controller.makeKey)
        self.copyKeybtn.clicked.connect(self.controller.copyKey)
        self.choiceOutBtn.clicked.connect(self.controller.choiceOut)
        self.startBtn.clicked.connect(self.controller.start)

if __name__ == '__main__':
    app=QApplication(sys.argv)
    fc=FileCipher()
    fc.show()
    sys.exit(app.exec_())
