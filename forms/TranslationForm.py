from .UserForm import UserForm
from .TranslationFormUi import Ui_TranslationForm
from .MetadataForm import MetadataWidget
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from models.translation import TranslationModel
from models.constants.translation_prop import *


class TranslationForm(QtWidgets.QMainWindow, Ui_TranslationForm):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        self.model = QStandardItemModel()
        self.tvMetadata.setModel(self.model)
        self.model.setHorizontalHeaderLabels(["Name", "Value", "Type", "Row Type"])
        self.tvMetadata.setColumnWidth(0, 200)
        self.tvMetadata.setColumnWidth(1, 290)
        self.tvMetadata.setColumnWidth(2, 290)
        self.tvMetadata.setColumnWidth(3, 100)
        self.btnAddMetodata.clicked.connect(self.add_metadata)
        self.btnRemoveMetodata.clicked.connect(self.remove_metadata)
        self.btnSave.clicked.connect(self.save)

    def save(self):
        try:
            user = UserForm()
            user.setParent(self)
            user.setWindowFlag(QtCore.Qt.Window)
            user.show()
        except BaseException as err:
            QMessageBox.about(self, 'PyQt5 message', 'An exception occurred: {}'.format(err))

    def remove_metadata(self):
        indexes = self.tvMetadata.selectedIndexes()
        for index in indexes:
            self.model.removeRow(index.row())

    def add_metadata(self):
        try:
            dialog = MetadataWidget()
            result = dialog.exec_()
            if result == 1:
                data = dialog.return_data()
                # TODO: Make 'row_type' read only
                self.model.appendRow(
                    [
                        QStandardItem(data['name']),
                        QStandardItem(data['value']),
                        QStandardItem(data['type']),
                        QStandardItem(data['row_type'])
                    ])
        except BaseException as err:
            QMessageBox.about(self, 'PyQt5 message', 'An exception occurred: {}'.format(err))

    def get_translation_model(self):
        return TranslationModel({
            LANGUAGE: self.txbLangId.text(),
            CREATED_BY: self.txbCreatedBy.text(),
            DRAFT_BY: self.txbDraftBy.text(),
            'allowed_children': self.txbAllowedChildren.text(),

        })