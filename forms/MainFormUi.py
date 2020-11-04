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
        MainForm.resize(811, 324)
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
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 230, 781, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(370, 10, 431, 181))
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
        self.cbTrustedConnection.setGeometry(QtCore.QRect(220, 140, 181, 21))
        self.cbTrustedConnection.setObjectName("cbTrustedConnection")
        self.cbDataSources = QtWidgets.QComboBox(self.groupBox)
        self.cbDataSources.setGeometry(QtCore.QRect(10, 140, 181, 22))
        self.cbDataSources.setObjectName("cbDataSources")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 120, 71, 16))
        self.label_8.setObjectName("label_8")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 351, 211))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(190, 30, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lblTranslation = QtWidgets.QLabel(self.groupBox_2)
        self.lblTranslation.setGeometry(QtCore.QRect(270, 30, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.lblTranslation.setFont(font)
        self.lblTranslation.setStyleSheet("color : rgb(129, 129, 129);")
        self.lblTranslation.setObjectName("lblTranslation")
        self.lblUser = QtWidgets.QLabel(self.groupBox_2)
        self.lblUser.setGeometry(QtCore.QRect(270, 70, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.lblUser.setFont(font)
        self.lblUser.setStyleSheet("color : rgb(129, 129, 129);")
        self.lblUser.setObjectName("lblUser")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(200, 70, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.btnConfigureTranslation = QtWidgets.QPushButton(self.groupBox_2)
        self.btnConfigureTranslation.setGeometry(QtCore.QRect(10, 30, 161, 23))
        self.btnConfigureTranslation.setObjectName("btnConfigureTranslation")
        self.btnConfigureUser = QtWidgets.QPushButton(self.groupBox_2)
        self.btnConfigureUser.setGeometry(QtCore.QRect(10, 70, 161, 23))
        self.btnConfigureUser.setObjectName("btnConfigureUser")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 140, 331, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.btnSaveTemplate = QtWidgets.QPushButton(self.groupBox_3)
        self.btnSaveTemplate.setGeometry(QtCore.QRect(10, 30, 141, 23))
        self.btnSaveTemplate.setObjectName("btnSaveTemplate")
        self.btnLoadTemplate = QtWidgets.QPushButton(self.groupBox_3)
        self.btnLoadTemplate.setGeometry(QtCore.QRect(180, 30, 141, 23))
        self.btnLoadTemplate.setObjectName("btnLoadTemplate")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 200, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lblVerifyConnection = QtWidgets.QLabel(self.centralwidget)
        self.lblVerifyConnection.setGeometry(QtCore.QRect(520, 200, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        self.lblVerifyConnection.setFont(font)
        self.lblVerifyConnection.setStyleSheet("color : rgb(129, 129, 129);")
        self.lblVerifyConnection.setObjectName("lblVerifyConnection")
        self.btnVerifyConnection = QtWidgets.QPushButton(self.centralwidget)
        self.btnVerifyConnection.setGeometry(QtCore.QRect(670, 200, 121, 23))
        self.btnVerifyConnection.setObjectName("btnVerifyConnection")
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
        self.label_8.setText(_translate("MainForm", "Data Source"))
        self.groupBox_2.setTitle(_translate("MainForm", "Generator settings"))
        self.label_5.setText(_translate("MainForm", "Translation:"))
        self.lblTranslation.setText(_translate("MainForm", "not set"))
        self.lblUser.setText(_translate("MainForm", "not set"))
        self.label_6.setText(_translate("MainForm", "User:"))
        self.btnConfigureTranslation.setText(_translate("MainForm", "Configure Translation"))
        self.btnConfigureUser.setText(_translate("MainForm", "Configure User"))
        self.groupBox_3.setTitle(_translate("MainForm", "Template"))
        self.btnSaveTemplate.setText(_translate("MainForm", "Save"))
        self.btnLoadTemplate.setText(_translate("MainForm", "Load"))
        self.label_7.setText(_translate("MainForm", "Connection to database:"))
        self.lblVerifyConnection.setText(_translate("MainForm", "not tested"))
        self.btnVerifyConnection.setText(_translate("MainForm", "Verify connection"))
