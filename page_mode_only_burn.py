import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os
import time
from usb_port import USB_PORT
import transfer
import ui_only_burn

ui = ui_only_burn.Ui_MainWindow()


class label_set_stylesheet(PyQt5.QtCore.QObject):
    signal_update = pyqtSignal(QtWidgets.QLabel, str)

    def sloat_update_label(self, label: QtWidgets.QLabel, sytlesheet: str):
        label.setStyleSheet(sytlesheet)

    def __init__(self, label: QtWidgets.QLabel, stylesheet: str):
        super().__init__()
        self.signal_update.connect(self.sloat_update_label)
        self.signal_update.emit(label, stylesheet)


class _USB_PROGRESS:
    usb: USB_PORT
    label: QtWidgets.QLabel
    flag_working = False

    def __callback_connected(self, port: USB_PORT):
        acm_path = port.get_dev_path()
        print("uSB插入", port.description)
        if os.path.exists(acm_path):
            print(acm_path)
        else:
            print("未找到acm路径")
            return
        self.flag_working = True
        label_set_stylesheet(self.label, ui.label_color_burn_bin.styleSheet())
        if transfer.TRANSFER(acm_path).burner_picoW(self.bin_file):
            label_set_stylesheet(self.label, ui.label_color_burn_bin_end.styleSheet())
        else:
            label_set_stylesheet(self.label, ui.label_color_error.styleSheet())
        self.flag_working = False

    def __callback_disconnect(self, port: USB_PORT):
        self.flag_working = True
        print("USB拔出", port.description)
        label_set_stylesheet(self.label, ui.label_color_free.styleSheet())
        self.flag_working = False

    def __init__(self, usb: USB_PORT, bin_file, label: QtWidgets.QLabel):
        self.bin_file = bin_file
        self.label = label
        self.usb = usb
        self.usb.regester_callback_connected(self.__callback_connected)
        self.usb.regester_callback_disconnect(self.__callback_disconnect)

    def run(self):
        self.usb.start_detection()

    def exit(self):
        self.usb.stop_detection()
        while self.flag_working:
            time.sleep(0.1)


class PAGE(QtWidgets.QMainWindow):
    bin_file: str

    usb1: _USB_PROGRESS
    usb2: _USB_PROGRESS
    usb3: _USB_PROGRESS

    signal_return = pyqtSignal()

    def sloat_return_click(self):
        self.usb1.exit()
        self.usb2.exit()
        self.usb3.exit()
        self.close()
        self.signal_return.emit()

    def __init__(
        self,
        bin_file_path: str,
        usb1: USB_PORT,
        usb2: USB_PORT,
        usb3: USB_PORT,
    ):
        super().__init__()
        ui.setupUi(self)
        self.bin_file = bin_file_path
        ui.textEdit_bin.setText(self.bin_file)
        ui.pushButton_return.clicked.connect(self.sloat_return_click)

        self.usb1 = _USB_PROGRESS(usb1, bin_file_path, ui.label_usb_1)
        self.usb2 = _USB_PROGRESS(usb2, bin_file_path, ui.label_usb_2)
        self.usb3 = _USB_PROGRESS(usb3, bin_file_path, ui.label_usb_3)

    def showEvent(self, event):
        super().showEvent(event)
        self.usb1.run()
        self.usb2.run()
        self.usb3.run()
