# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_choose.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_mode_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mode_1.setGeometry(QtCore.QRect(20, 10, 200, 250))
        self.pushButton_mode_1.setObjectName("pushButton_mode_1")
        self.pushButton_mode_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_mode_2.setGeometry(QtCore.QRect(250, 10, 200, 250))
        self.pushButton_mode_2.setObjectName("pushButton_mode_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
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
        self.pushButton_mode_1.setText(_translate("MainWindow", "A.烧录固件"))
        self.pushButton_mode_2.setText(_translate("MainWindow", "B.传py文件并运行"))
