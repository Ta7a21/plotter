from PyQt5.QtWidgets import QMessageBox

def raiseError(self, txt):
    QMessageBox.critical(self, "Error", txt)