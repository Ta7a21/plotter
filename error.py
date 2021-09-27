from PyQt5.QtWidgets import QMessageBox


def errorPOPUP(self, error_message):
    QMessageBox.critical(self, "Error", error_message)
