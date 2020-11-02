import sys
from .TranslationForm import TranslationForm
from .UserForm import UserForm
from .MainFormUi import Ui_MainForm
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog


class MainForm(QtWidgets.QMainWindow, Ui_MainForm):
    def __init__(self):
        super().__init__()
        self.user_form = UserForm()
        self.trans_form = TranslationForm()
        self.setupUi(self)
        self.btnConfigureTranslation.clicked.connect(self.open_translation)
        self.btnConfigureUser.clicked.connect(self.open_user)
        self.btnExecute.clicked.connect(self.execute)
        self.btnSaveConfiguration.clicked.connect()

    def save_template(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "Json Files (*.json)", options=options)
        # TODO:Save template

    def load_template(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "Json Files (*.json)", options=options)
        # TODO:Load template
        # if len(files) > 0:

    def execute(self):
        model = self.trans_form.get_translation_model()

    def open_translation(self):
        self.trans_form.setParent(self)
        self.trans_form.setWindowFlag(QtCore.Qt.Window)
        self.trans_form.show()

    def open_user(self):
        self.user_form.setParent(self)
        self.user_form.setWindowFlag(QtCore.Qt.Window)
        self.user_form.show()
