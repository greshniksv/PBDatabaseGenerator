import sys
from .UserFormUi import Ui_UserForm
from PyQt5 import QtWidgets


class UserForm(QtWidgets.QMainWindow, Ui_UserForm):
    def __init__(self, parent):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
