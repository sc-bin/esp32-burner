# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 762)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 461, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_py = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_py.setObjectName("textEdit_py")
        self.gridLayout.addWidget(self.textEdit_py, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.textEdit_bin = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit_bin.setObjectName("textEdit_bin")
        self.gridLayout.addWidget(self.textEdit_bin, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 80, 381, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_color_free = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_color_free.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.label_color_free.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_color_free.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color_free.setObjectName("label_color_free")
        self.horizontalLayout_2.addWidget(self.label_color_free)
        self.label_color_burn_bin = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_color_burn_bin.setStyleSheet("background-color:rgb(113, 255, 47)")
        self.label_color_burn_bin.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_color_burn_bin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color_burn_bin.setObjectName("label_color_burn_bin")
        self.horizontalLayout_2.addWidget(self.label_color_burn_bin)
        self.label_color_burn_bin_end = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_color_burn_bin_end.setStyleSheet("background-color:rgb(170, 108, 54)")
        self.label_color_burn_bin_end.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_color_burn_bin_end.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color_burn_bin_end.setObjectName("label_color_burn_bin_end")
        self.horizontalLayout_2.addWidget(self.label_color_burn_bin_end)
        self.label_color_send_py = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_color_send_py.setStyleSheet("background-color:rgb(85, 170, 255)")
        self.label_color_send_py.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_color_send_py.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color_send_py.setObjectName("label_color_send_py")
        self.horizontalLayout_2.addWidget(self.label_color_send_py)
        self.label_color_send_py_end = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_color_send_py_end.setStyleSheet("background-color:rgb(164, 181, 79)")
        self.label_color_send_py_end.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_color_send_py_end.setAlignment(QtCore.Qt.AlignCenter)
        self.label_color_send_py_end.setObjectName("label_color_send_py_end")
        self.horizontalLayout_2.addWidget(self.label_color_send_py_end)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(40, 140, 391, 277))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit_usb_2 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_usb_2.setObjectName("textEdit_usb_2")
        self.gridLayout_2.addWidget(self.textEdit_usb_2, 1, 1, 1, 1)
        self.label_usb_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_usb_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_usb_3.setObjectName("label_usb_3")
        self.gridLayout_2.addWidget(self.label_usb_3, 2, 0, 1, 1)
        self.label_usb_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_usb_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_usb_2.setObjectName("label_usb_2")
        self.gridLayout_2.addWidget(self.label_usb_2, 1, 0, 1, 1)
        self.label_usb_1 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_usb_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_usb_1.setObjectName("label_usb_1")
        self.gridLayout_2.addWidget(self.label_usb_1, 0, 0, 1, 1)
        self.textEdit_usb_1 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_usb_1.setObjectName("textEdit_usb_1")
        self.gridLayout_2.addWidget(self.textEdit_usb_1, 0, 1, 1, 1)
        self.textEdit_usb_3 = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_usb_3.setObjectName("textEdit_usb_3")
        self.gridLayout_2.addWidget(self.textEdit_usb_3, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", " py"))
        self.label.setText(_translate("MainWindow", "bin"))
        self.label_color_free.setText(_translate("MainWindow", "空闲"))
        self.label_color_burn_bin.setText(_translate("MainWindow", "在烧bin"))
        self.label_color_burn_bin_end.setText(_translate("MainWindow", "结束烧bin"))
        self.label_color_send_py.setText(_translate("MainWindow", "传py"))
        self.label_color_send_py_end.setText(_translate("MainWindow", "结束传py"))
        self.label_usb_3.setText(_translate("MainWindow", "usb3"))
        self.label_usb_2.setText(_translate("MainWindow", "usb2"))
        self.label_usb_1.setText(_translate("MainWindow", "usb1"))
