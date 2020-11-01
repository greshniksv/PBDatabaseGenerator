# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(811, 336)
        self.centralwidget = QtWidgets.QWidget(MainForm)
        self.centralwidget.setObjectName("centralwidget")
        self.btnCreateSql = QtWidgets.QPushButton(self.centralwidget)
        self.btnCreateSql.setGeometry(QtCore.QRect(590, 250, 91, 23))
        self.btnCreateSql.setObjectName("btnCreateSql")
        self.btnExecute = QtWidgets.QPushButton(self.centralwidget)
        self.btnExecute.setGeometry(QtCore.QRect(694, 250, 101, 23))
        self.btnExecute.setObjectName("btnExecute")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 250, 571, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 230, 781, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(370, 10, 431, 151))
        self.groupBox.setObjectName("groupBox")
        self.txbServer = QtWidgets.QLineEdit(self.groupBox)
        self.txbServer.setGeometry(QtCore.QRect(10, 40, 181, 20))
        self.txbServer.setObjectName("txbServer")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_2.setObjectName("label_2")
        self.txbDatabase = QtWidgets.QLineEdit(self.groupBox)
        self.txbDatabase.setGeometry(QtCore.QRect(10, 90, 181, 20))
        self.txbDatabase.setObjectName("txbDatabase")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(220, 20, 71, 16))
        self.label_3.setObjectName("label_3")
        self.txbUser = QtWidgets.QLineEdit(self.groupBox)
        self.txbUser.setGeometry(QtCore.QRect(220, 40, 181, 20))
        self.txbUser.setObjectName("txbUser")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(220, 70, 71, 16))
        self.label_4.setObjectName("label_4")
        self.txbPassword = QtWidgets.QLineEdit(self.groupBox)
        self.txbPassword.setGeometry(QtCore.QRect(220, 90, 181, 20))
        self.txbPassword.setObjectName("txbPassword")
        self.cbTrustedConnection = QtWidgets.QCheckBox(self.groupBox)
        self.cbTrustedConnection.setGeometry(QtCore.QRect(220, 120, 181, 21))
        self.cbTrustedConnection.setObjectName("cbTrustedConnection")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 351, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(190, 30, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lblTranslation = QtWidgets.QLabel(self.groupBox_2)
        self.lblTranslation.setGeometry(QtCore.QRect(290, 30, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.lblTranslation.setFont(font)
        self.lblTranslation.setStyleSheet("background-color : transparent; color : geen;")
        self.lblTranslation.setObjectName("lblTranslation")
        self.lblUser = QtWidgets.QLabel(self.groupBox_2)
        self.lblUser.setGeometry(QtCore.QRect(290, 70, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.lblUser.setFont(font)
        self.lblUser.setStyleSheet("background-color : transparent; color : geen;")
        self.lblUser.setObjectName("lblUser")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(190, 70, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.btnConfigureTranslation = QtWidgets.QPushButton(self.groupBox_2)
        self.btnConfigureTranslation.setGeometry(QtCore.QRect(10, 30, 161, 23))
        self.btnConfigureTranslation.setObjectName("btnConfigureTranslation")
        self.btnConfigureUser = QtWidgets.QPushButton(self.groupBox_2)
        self.btnConfigureUser.setGeometry(QtCore.QRect(10, 70, 161, 23))
        self.btnConfigureUser.setObjectName("btnConfigureUser")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 150, 331, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 141, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 20, 141, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 21))
        self.menubar.setObjectName("menubar")
        MainForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "PB Database Generator"))
        self.btnCreateSql.setText(_translate("MainForm", "Generate SQL"))
        self.btnExecute.setText(_translate("MainForm", "Execute in DB"))
        self.groupBox.setTitle(_translate("MainForm", "Database connection settings"))
        self.label.setText(_translate("MainForm", "Server"))
        self.label_2.setText(_translate("MainForm", "Database"))
        self.label_3.setText(_translate("MainForm", "User"))
        self.label_4.setText(_translate("MainForm", "Password"))
        self.cbTrustedConnection.setText(_translate("MainForm", "Trusted Connection"))
        self.groupBox_2.setTitle(_translate("MainForm", "Generator settings"))
        self.label_5.setText(_translate("MainForm", "Translation set:"))
        self.lblTranslation.setText(_translate("MainForm", "<html><head/><body><p><span style=\" font-weight:600; color:#03bd00;\">OK</span></p></body></html>"))
        self.lblUser.setText(_translate("MainForm", "<html><head/><body><p><span style=\" font-weight:600; color:#03bd00;\">OK</span></p></body></html>"))
        self.label_6.setText(_translate("MainForm", "User set:"))
        self.btnConfigureTranslation.setText(_translate("MainForm", "Configure Translation"))
        self.btnConfigureUser.setText(_translate("MainForm", "Configure User"))
        self.groupBox_3.setTitle(_translate("MainForm", "Configuration"))
        self.pushButton.setText(_translate("MainForm", "Save"))
        self.pushButton_3.setText(_translate("MainForm", "Load"))
