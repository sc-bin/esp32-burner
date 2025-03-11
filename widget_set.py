import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class textEdit_ops(PyQt5.QtCore.QObject):
    textEdit: QtWidgets.QTextEdit
    signal_update = pyqtSignal(QtWidgets.QTextEdit, str)

    def sloat_update(self, textEdit: QtWidgets.QTextEdit, text: str):
        textEdit.append(text)

    def __init__(self, textEdit: QtWidgets.QTextEdit):
        super().__init__()
        self.textEdit = textEdit
        self.signal_update.connect(self.sloat_update)

    def append(self, text: str):
        self.signal_update.emit(self.textEdit, text)


class label_ops(PyQt5.QtCore.QObject):
    label: QtWidgets.QLabel
    signal_setText = pyqtSignal(QtWidgets.QLabel, str)
    signal_setStyleSheet = pyqtSignal(QtWidgets.QLabel, str)

    def sloat_setText(self, label: QtWidgets.QLabel, text: str):
        label.setText(text)

    def sloat_setStyleSheet(self, label: QtWidgets.QLabel, sytlesheet: str):
        label.setStyleSheet(sytlesheet)

    def __init__(self, label: QtWidgets.QLabel):
        super().__init__()
        self.label = label
        self.signal_setText.connect(self.sloat_setText)
        self.signal_setStyleSheet.connect(self.sloat_setStyleSheet)

    def setText(self, text: str):
        self.signal_setText.emit(self.label, text)

    def setStyleSheet(self, sytlesheet: str):
        self.signal_setStyleSheet.emit(self.label, sytlesheet)


class run_at_sloat(PyQt5.QtCore.QObject):
    signal_run = pyqtSignal()

    def sloat_run(self):
        print("在草里运行回调")
        self.func()
        print("在草里运行回调 func")

    def __init__(self, func):
        super().__init__()
        self.func = func
        self.signal_run.connect(self.func)
        self.signal_run.emit()
