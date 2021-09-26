from PyQt5 import QtWidgets, uic, QtGui
import sys
from plot import plot


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("app.ui", self)
        self.plotButton.clicked.connect(lambda: plot(self))


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()
