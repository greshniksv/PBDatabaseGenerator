# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './TranslationForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TranslationForm(object):
    def setupUi(self, TranslationForm):
        TranslationForm.setObjectName("TranslationForm")
        TranslationForm.resize(985, 715)
        TranslationForm.setMinimumSize(QtCore.QSize(985, 700))
        TranslationForm.setMaximumSize(QtCore.QSize(985, 715))
        self.centralwidget = QtWidgets.QWidget(TranslationForm)
        self.centralwidget.setObjectName("centralwidget")
        self.tvMetadata = QtWidgets.QTableView(self.centralwidget)
        self.tvMetadata.setGeometry(QtCore.QRect(10, 270, 921, 341))
        self.tvMetadata.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tvMetadata.setObjectName("tvMetadata")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 250, 251, 16))
        self.label.setObjectName("label")
        self.btnAddMetodata = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddMetodata.setGeometry(QtCore.QRect(940, 270, 31, 23))
        self.btnAddMetodata.setObjectName("btnAddMetodata")
        self.btnRemoveMetodata = QtWidgets.QPushButton(self.centralwidget)
        self.btnRemoveMetodata.setGeometry(QtCore.QRect(940, 300, 31, 23))
        self.btnRemoveMetodata.setObjectName("btnRemoveMetodata")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 501, 231))
        self.groupBox.setObjectName("groupBox")
        self.txbLangId = QtWidgets.QLineEdit(self.groupBox)
        self.txbLangId.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.txbLangId.setObjectName("txbLangId")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 47, 13))
        self.label_3.setObjectName("label_3")
        self.txbDraftBy = QtWidgets.QLineEdit(self.groupBox)
        self.txbDraftBy.setGeometry(QtCore.QRect(10, 90, 113, 20))
        self.txbDraftBy.setObjectName("txbDraftBy")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(250, 170, 47, 13))
        self.label_4.setObjectName("label_4")
        self.txbSlug = QtWidgets.QLineEdit(self.groupBox)
        self.txbSlug.setGeometry(QtCore.QRect(250, 190, 231, 20))
        self.txbSlug.setObjectName("txbSlug")
        self.txbPermalink = QtWidgets.QLineEdit(self.groupBox)
        self.txbPermalink.setGeometry(QtCore.QRect(10, 190, 231, 20))
        self.txbPermalink.setObjectName("txbPermalink")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(150, 20, 91, 16))
        self.label_6.setObjectName("label_6")
        self.txbCreatedBy = QtWidgets.QLineEdit(self.groupBox)
        self.txbCreatedBy.setGeometry(QtCore.QRect(150, 40, 113, 20))
        self.txbCreatedBy.setObjectName("txbCreatedBy")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(150, 70, 101, 16))
        self.label_7.setObjectName("label_7")
        self.txbAllowedChildren = QtWidgets.QLineEdit(self.groupBox)
        self.txbAllowedChildren.setGeometry(QtCore.QRect(150, 90, 113, 20))
        self.txbAllowedChildren.setObjectName("txbAllowedChildren")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 120, 101, 16))
        self.label_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_8.setObjectName("label_8")
        self.txbTitle = QtWidgets.QLineEdit(self.groupBox)
        self.txbTitle.setGeometry(QtCore.QRect(10, 140, 231, 20))
        self.txbTitle.setObjectName("txbTitle")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(290, 70, 101, 16))
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setObjectName("label_9")
        self.txbIsPublished = QtWidgets.QLineEdit(self.groupBox)
        self.txbIsPublished.setGeometry(QtCore.QRect(290, 90, 113, 20))
        self.txbIsPublished.setObjectName("txbIsPublished")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(250, 120, 101, 16))
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setObjectName("label_10")
        self.txbFile = QtWidgets.QLineEdit(self.groupBox)
        self.txbFile.setGeometry(QtCore.QRect(250, 140, 201, 20))
        self.txbFile.setObjectName("txbFile")
        self.btnBrowseFile = QtWidgets.QToolButton(self.groupBox)
        self.btnBrowseFile.setGeometry(QtCore.QRect(460, 140, 25, 19))
        self.btnBrowseFile.setObjectName("btnBrowseFile")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(520, 10, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(760, 650, 171, 23))
        self.btnSave.setObjectName("btnSave")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 620, 991, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        TranslationForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TranslationForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 21))
        self.menubar.setObjectName("menubar")
        TranslationForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TranslationForm)
        self.statusbar.setObjectName("statusbar")
        TranslationForm.setStatusBar(self.statusbar)

        self.retranslateUi(TranslationForm)
        QtCore.QMetaObject.connectSlotsByName(TranslationForm)

    def retranslateUi(self, TranslationForm):
        _translate = QtCore.QCoreApplication.translate
        TranslationForm.setWindowTitle(_translate("TranslationForm", "TranslationForm"))
        self.label.setText(_translate("TranslationForm", "Contentdata/Metadata*"))
        self.btnAddMetodata.setText(_translate("TranslationForm", "+"))
        self.btnRemoveMetodata.setText(_translate("TranslationForm", "-"))
        self.groupBox.setTitle(_translate("TranslationForm", "Permalink"))
        self.label_2.setText(_translate("TranslationForm", "Language ID"))
        self.label_3.setText(_translate("TranslationForm", "Draft By"))
        self.label_4.setText(_translate("TranslationForm", "Slug*"))
        self.label_5.setText(_translate("TranslationForm", "Permalink*"))
        self.label_6.setText(_translate("TranslationForm", "Created By"))
        self.label_7.setText(_translate("TranslationForm", "AllowedChildren"))
        self.label_8.setText(_translate("TranslationForm", "Title*"))
        self.label_9.setText(_translate("TranslationForm", "IsPublished"))
        self.label_10.setText(_translate("TranslationForm", "File"))
        self.btnBrowseFile.setText(_translate("TranslationForm", "..."))
        self.label_11.setText(_translate("TranslationForm", "*Tag replacement: \n"
"{r:0-999} - Random chars (number this is a length)\n"
"{c} - Content number\n"
"{i} - Itegation number"))
        self.btnSave.setText(_translate("TranslationForm", "Save"))
