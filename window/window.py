# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window/window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(242, 322)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(False)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        MainWindow.setAcceptDrops(False)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.l_color_role = QtWidgets.QLabel(self.groupBox_3)
        self.l_color_role.setGeometry(QtCore.QRect(20, 50, 181, 171))
        self.l_color_role.setObjectName("l_color_role")
        self.l_current_color = QtWidgets.QLabel(self.groupBox_3)
        self.l_current_color.setEnabled(True)
        self.l_current_color.setGeometry(QtCore.QRect(10, 20, 201, 21))
        self.l_current_color.setAutoFillBackground(False)
        self.l_current_color.setStyleSheet("")
        self.l_current_color.setFrameShape(QtWidgets.QFrame.Box)
        self.l_current_color.setText("")
        self.l_current_color.setObjectName("l_current_color")
        self.sl_value = QtWidgets.QSlider(self.groupBox_3)
        self.sl_value.setGeometry(QtCore.QRect(10, 270, 201, 22))
        self.sl_value.setStyleSheet("QSlider::groove:horizontal {\n"
"background:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop:0 #000 , stop:1 #fff,);\n"
"height: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle::horizontal\n"
"{\n"
"    background: #333;\n"
"    width:8px;\n"
"    margin: -6px 0;\n"
"}")
        self.sl_value.setMaximum(255)
        self.sl_value.setProperty("value", 255)
        self.sl_value.setOrientation(QtCore.Qt.Horizontal)
        self.sl_value.setObjectName("sl_value")
        self.sl_saturation = QtWidgets.QSlider(self.groupBox_3)
        self.sl_saturation.setGeometry(QtCore.QRect(10, 240, 201, 22))
        self.sl_saturation.setStyleSheet("QSlider::groove:horizontal {\n"
"background:qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"    stop:0 #000 , stop:1 #fff,);\n"
"height: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::handle::horizontal\n"
"{\n"
"    background: #333;\n"
"    width:8px;\n"
"    margin: -6px 0;\n"
"}")
        self.sl_saturation.setMaximum(255)
        self.sl_saturation.setProperty("value", 255)
        self.sl_saturation.setOrientation(QtCore.Qt.Horizontal)
        self.sl_saturation.setObjectName("sl_saturation")
        self.verticalLayout.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Set Color"))
        self.l_color_role.setText(_translate("MainWindow", "TextLabel"))
