from PyQt5 import QtWidgets, uic, QtGui
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi("app.ui", self)

    def closeEvent(self, event):
        # Confirmation message when the user closes the app
        reply = QtWidgets.QMessageBox()
        reply.setText("Do you really want to close the app?")
        reply.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        reply.setWindowTitle("Close")
        reply = reply.exec()

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()
