from .UserFormUi import Ui_UserForm
from .MetadataForm import MetadataWidget
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from models.TranslationModel import TranslationModel
from pydantic import BaseModel, ValidationError, validator
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from models.UserModel import UserModel


class UserForm(QtWidgets.QMainWindow, Ui_UserForm):
    def __init__(self, parent):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.parent_form = parent
        self.setupUi(self)
        self.user_model = None
        self.model = QStandardItemModel()
        self.tvMetadata.setModel(self.model)
        self.model.setHorizontalHeaderLabels(["Name", "Value", "Type", "Row Type"])
        self.tvMetadata.setColumnWidth(0, 200)
        self.tvMetadata.setColumnWidth(1, 290)
        self.tvMetadata.setColumnWidth(2, 290)
        self.tvMetadata.setColumnWidth(3, 100)  # this column should be read-only
        self.btnAddMetodata.clicked.connect(self.add_metadata)
        self.btnRemoveMetodata.clicked.connect(self.remove_metadata)
        self.btnSave.clicked.connect(self.save)
        self.setFixedSize(self.width(), self.height() - 20)

    def apply_model(self):
        model = self.user_model
        self.txbUsername.setText(model.username)
        self.txbComment.setText(model.comment)
        self.txbProviderUserKey.setText(model.provider_user_key)
        self.txbEmail.setText(model.email)
        self.txbIsAdmin.setText(model.is_admin)
        self.txbPassword.setText(model.password)
        self.txbName.setText(model.name)
        self.txbApplicationName.setText(model.application_name)
        self.txbUserState.setText(model.user_state)
        self.txbProviderName.setText(model.provider_name)

        # Clear
        while self.model.rowCount() > 0:
            self.model.removeRow(0)

        for item in model.metadata:
            self.model.appendRow(
                [
                    QStandardItem(item['name']),
                    QStandardItem(item['value']),
                    QStandardItem(item['type']),
                    QStandardItem('MetaData')
                ])

        for item in model.content_data:
            self.model.appendRow(
                [
                    QStandardItem(item['name']),
                    QStandardItem(item['value']),
                    QStandardItem(item['type']),
                    QStandardItem('ContentData')
                ])

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

    def save(self):
        try:
            metadata = []
            content_data = []
            row_count = self.model.rowCount()
            for row in range(row_count):
                name = self.model.data(self.model.index(row, 0))
                value = self.model.data(self.model.index(row, 1))
                value_type = self.model.data(self.model.index(row, 2))
                row_type = self.model.data(self.model.index(row, 3))
                if row_type == "ContentData":
                    content_data.append({'name': name, 'value': value, 'type': value_type})
                if row_type == "MetaData":
                    metadata.append({'name': name, 'value': value, 'type': value_type})

            self.user_model = UserModel(
                username=self.txbUsername.text(),
                comment=self.txbComment.text(),
                provider_user_key=self.txbProviderUserKey.text(),
                email=self.txbEmail.text(),
                is_admin=self.txbIsAdmin.text(),
                password=self.txbPassword.text(),
                name=self.txbName.text(),
                application_name=self.txbApplicationName.text(),
                user_state=self.txbUserState.text(),
                provider_name=self.txbProviderName.text(),
                metadata=metadata,
                content_data=content_data
            )
            self.parent_form.set_user(self.user_model)

        except ValidationError as e:
            QMessageBox.about(self, 'Error message', '{}'.format(e))

        except BaseException as err:
            QMessageBox.about(self, 'Error message', 'An exception occurred: {}'.format(err))

        self.close()
