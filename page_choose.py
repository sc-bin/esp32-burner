import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import ui_choose


class PAGE(QtWidgets.QMainWindow):
    ui = ui_choose.Ui_MainWindow()
    signal_choose = pyqtSignal(int)

    def callback(self, num: int):
        print("选择模式 ", num)
        self.signal_choose.emit(num)
        self.close()

    def __init__(self):
        super().__init__()
        self.ui.setupUi(self)
        self.ui.pushButton_mode_1.clicked.connect(lambda: self.callback(1))
        self.ui.pushButton_mode_2.clicked.connect(lambda: self.callback(2))
        self.ui.pushButton_mode_3.clicked.connect(lambda: self.callback(3))
