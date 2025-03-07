import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os
import time
from usb_port import USB_PORT
import ui_mode

ui = ui_mode.Ui_MainWindow()


class label_set_stylesheet(PyQt5.QtCore.QObject):
    signal_update = pyqtSignal(QtWidgets.QLabel, str)

    def sloat_update_label(self, label: QtWidgets.QLabel, sytlesheet: str):
        label.setStyleSheet(sytlesheet)

    def __init__(self, label: QtWidgets.QLabel, stylesheet: str):
        super().__init__()
        self.signal_update.connect(self.sloat_update_label)
        self.signal_update.emit(label, stylesheet)


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


class USB_PROGRESS:
    usb: USB_PORT
    label: QtWidgets.QLabel
    textEdit: textEdit_ops
    flag_working = False
    callback = None

    def print(self, text: str):
        self.textEdit.append(f'{time.strftime("%H:%M:%S", time.localtime())}: {text}')

    def __callback_connected(self, port: USB_PORT):
        print("USB插入", port.description)
        self.print("插入")
        self.flag_working = True
        if self.callback != None:
            self.callback(port, self)
        self.flag_working = False

    def __callback_disconnect(self, port: USB_PORT):
        self.flag_working = True
        print("USB拔出", port.description)
        self.print("拔出")
        label_set_stylesheet(self.label, ui.label_color_free.styleSheet())
        self.flag_working = False

    def __init__(
        self, usb: USB_PORT, label: QtWidgets.QLabel, textEdit: QtWidgets.QTextEdit
    ):
        self.label = label
        self.textEdit = textEdit_ops(textEdit)
        self.usb = usb
        self.usb.regester_callback_connected(self.__callback_connected)
        self.usb.regester_callback_disconnect(self.__callback_disconnect)

    def run(self):
        self.usb.start_detection()
        # self.timer = threading.Timer(0.3, self.usb.start_detection)
        # self.timer.start()

    def exit(self):
        while self.flag_working:
            time.sleep(0.1)
        self.usb.stop_detection()


class PAGE_MODE(QtWidgets.QMainWindow):
    usb1: USB_PROGRESS
    usb2: USB_PROGRESS
    usb3: USB_PROGRESS

    signal_return = pyqtSignal()

    def sloat_return_click(self):
        self.usb1.exit()
        self.usb2.exit()
        self.usb3.exit()
        self.hide()
        self.signal_return.emit()

    def __init__(
        self,
        usb1: USB_PORT,
        usb2: USB_PORT,
        usb3: USB_PORT,
    ):
        super().__init__()
        ui.setupUi(self)
        ui.pushButton_return.clicked.connect(self.sloat_return_click)
        self.usb1 = USB_PROGRESS(usb1, ui.label_usb_1, ui.textEdit_usb_1)
        self.usb2 = USB_PROGRESS(usb2, ui.label_usb_2, ui.textEdit_usb_2)
        self.usb3 = USB_PROGRESS(usb3, ui.label_usb_3, ui.textEdit_usb_3)

    def showEvent(self, event):
        super().showEvent(event)
        self.usb1.run()
        self.usb2.run()
        self.usb3.run()
