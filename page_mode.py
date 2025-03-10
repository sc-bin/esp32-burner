import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import time
from usb_port import USB_PORT
import ui_mode
import color
from widget_set import *

ui = ui_mode.Ui_MainWindow()


class bar_ops(PyQt5.QtCore.QObject):
    progressBar: QtWidgets.QProgressBar
    signal_set_value = pyqtSignal(int)

    def slot_set_value(self, value: int):
        self.progressBar.setValue(value)

    def set_value(self, value: int):
        self.signal_set_value.emit(value)

    def __init__(self, progressBar: QtWidgets.QProgressBar):
        super().__init__()
        self.progressBar = progressBar
        self.signal_set_value.connect(self.slot_set_value)


class USB_PROGRESS:
    usb: USB_PORT
    label: QtWidgets.QLabel
    textEdit: QtWidgets.QTextEdit
    flag_working = False
    callback = None
    last_disconnect_time = None  # 新增属性，记录上次USB拔出的时间

    def textEdit_append(self, string: str):
        run_at_sloat(lambda: self.textEdit.append(string))
    def label_setText(self, string: str):
        run_at_sloat(lambda: self.label.setText(string))

    def print(self, text: str):
        log_str = f'{time.strftime("%H:%M:%S", time.localtime())}: {text}'
        self.textEdit_append(log_str)
        print(f"{self.usb.description} : " + log_str)

    def __callback_connected(self, port: USB_PORT):
        current_time = time.time()
        if self.last_disconnect_time and (current_time - self.last_disconnect_time) < 3:
            self.print("本次拔出不超过3秒,不处理")
            self.label_setText("usb防抖保护")
            return  
        self.print("插入")
        self.label_setText(port.description + "插入")
        self.flag_working = True
        if self.callback != None:
            self.callback(port, self)
        self.flag_working = False

    def __callback_disconnect(self, port: USB_PORT):
        self.flag_working = True
        self.print("拔出")
        self.label_setText(port.description + "拔出")
        label_set_stylesheet(self.label, color.label_background.free)
        self.progress.set_value(0)
        self.last_disconnect_time = time.time()  # 记录USB拔出的时间
        self.flag_working = False

    def __init__(
        self,
        usb: USB_PORT,
        label: QtWidgets.QLabel,
        textEdit: QtWidgets.QTextEdit,
        progressBar: QtWidgets.QProgressBar,
    ):
        self.label = label
        self.progress = bar_ops(progressBar)
        self.textEdit = textEdit
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
        self.usb1 = USB_PROGRESS(
            usb1, ui.label_usb_1, ui.textEdit_usb_1, ui.progressBar_usb_1
        )
        self.usb2 = USB_PROGRESS(
            usb2, ui.label_usb_2, ui.textEdit_usb_2, ui.progressBar_usb_2
        )
        self.usb3 = USB_PROGRESS(
            usb3, ui.label_usb_3, ui.textEdit_usb_3, ui.progressBar_usb_3
        )

    def showEvent(self, event):
        super().showEvent(event)
        self.usb1.run()
        self.usb2.run()
        self.usb3.run()
