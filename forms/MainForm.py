import sys
from .TranslationForm import TranslationForm
from .UserForm import UserForm
from .MainFormUi import Ui_MainForm
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class MainForm(QtWidgets.QMainWindow, Ui_MainForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnConfigureTranslation.clicked.connect(self.open_translation)
        self.btnConfigureUser.clicked.connect(self.open_user)

    def open_translation(self):
        form = TranslationForm()
        form.setParent(self)
        form.setWindowFlag(QtCore.Qt.Window)
        form.show()

    def open_user(self):
        form = UserForm()
        form.setParent(self)
        form.setWindowFlag(QtCore.Qt.Window)
        form.show()
