import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os

import ui_main as _ui_main
import usb_port
import transfer


FIRMWARE_PATH = os.path.dirname(__file__) + "/烧录文件存放文件夹"
PY_PATH = os.path.dirname(__file__) + "/烧录文件存放文件夹"
# 查找FIRMWARE_PATH路径下第一个.bin文件
bin_file = None
for file in os.listdir(FIRMWARE_PATH):
    if file.endswith(".bin"):
        bin_file = os.path.join(FIRMWARE_PATH, file)
        break
if bin_file is None:
    print("未找到.bin文件")
    exit(1)
else:
    print("bin文件 : ", os.path.basename(bin_file))

py_file = None
for file in os.listdir(FIRMWARE_PATH):
    if file.endswith(".py"):
        py_file = os.path.join(FIRMWARE_PATH, file)
        break
if py_file is None:
    print("未找到py文件")
    exit(1)
else:
    print("py文件 : ", os.path.basename(py_file))




class label_color(QtWidgets.QLabel):
    label: QtWidgets.QLabel
    stylesheet: str
    signal_update_label = pyqtSignal(str)

    def sloat_update_label(self, sytlesheet: str):
        self.label.setStyleSheet(sytlesheet)

    def do(self):
        self.signal_update_label.emit(self.stylesheet)

    def __init__(self, label: QtWidgets.QLabel, stylesheet: str):
        super().__init__()
        self.label = label
        self.stylesheet = stylesheet
        print(self.stylesheet)
        self.signal_update_label.connect(self.sloat_update_label)


ui_main = _ui_main.Ui_MainWindow()

window_choose = QtWidgets.QMainWindow()  # 构建窗口对象


window = QtWidgets.QMainWindow()  # 构建窗口对象

ui_main.setupUi(window)
ui_main.textEdit_bin.setText(bin_file)
ui_main.textEdit_py.setText(py_file)


class RUNNER(QtWidgets.QLabel):
    usb: usb_port.USB_PORT
    label: QtWidgets.QLabel
    signal_update_label = pyqtSignal(str)

    def sloat_update_label(self, sytlesheet: str):
        self.label.setStyleSheet(sytlesheet)

    def __callback_connected(self, port: usb_port.USB_PORT):
        acm_path = port.get_dev_path()
        print("uSB插入", port.description)
        if os.path.exists(acm_path):
            print(acm_path)
        else:
            print("未找到acm路径")
            return
        if transfer.TRANSFER(acm_path).is_in_burn_mode():
            self.signal_update_label.emit(ui_main.label_color_burn_bin.styleSheet())
            transfer.TRANSFER(acm_path).burner_picoW(bin_file)
            self.signal_update_label.emit(ui_main.label_color_burn_bin_end.styleSheet())
        else:
            self.signal_update_label.emit(ui_main.label_color_send_py.styleSheet())
            transfer.TRANSFER(acm_path).send_file(py_file)
            self.signal_update_label.emit(ui_main.label_color_send_py_end.styleSheet())

    def __callback_disconnect(self, port: usb_port.USB_PORT):
        print("USB拔出", port.description)
        self.signal_update_label.emit(ui_main.label_color_free.styleSheet())

    def __init__(self, port_number: int, description: str, progress: QtWidgets.QLabel):
        super().__init__()
        self.usb = usb_port.USB_PORT(port_number, description)
        self.usb.regester_callback_connected(self.__callback_connected)
        self.usb.regester_callback_disconnect(self.__callback_disconnect)
        self.usb.start_detection()
        self.label = progress
        self.signal_update_label.connect(self.sloat_update_label)

usb1 = RUNNER(8, "左单", ui_main.label_usb_1)
usb1 = RUNNER(6, "中上", ui_main.label_usb_2)
usb1 = RUNNER(5, "中下", ui_main.label_usb_3)

window.show()  # 按绘制时的尺寸显示
# window.showFullScreen() #全屏显示
