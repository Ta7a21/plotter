from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QWidget
import sys
from plot import plot


class Ui(QWidget):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("app.ui", self)
        self.graph.setBackground("w")
        self.graph.showGrid(x=True, y=True, alpha=0.8)
        self.plotButton.clicked.connect(lambda: plot(self))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
