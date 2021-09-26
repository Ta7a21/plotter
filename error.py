from PyQt5.QtWidgets import QMessageBox


def error(self, error_message):
    QMessageBox.critical(self, "Error", error_message)
