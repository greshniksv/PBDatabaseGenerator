from .UserForm import UserForm
from .TranslationFormUi import Ui_TranslationForm
from .MetadataForm import MetadataWidget
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from models.TranslationModel import TranslationModel
from pydantic import BaseModel, ValidationError, validator
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


class TranslationForm(QtWidgets.QMainWindow, Ui_TranslationForm):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)
        self.translation_model = None
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
        self.btnBrowseFile.clicked.connect(self.open_file_names_dialog)

    def open_file_names_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;", options=options)
        if len(files) > 0:
            self.txbFile.setText(files[0])

    def save(self):
        error_acquire = False
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

            self.translation_model = TranslationModel(
                language=self.txbLangId.text(),
                draft_by=self.txbDraftBy.text(),
                slug=self.txbSlug.text(),
                permalink=self.txbPermalink.text(),
                created_by=self.txbCreatedBy.text(),
                allowed_children=self.txbAllowedChildren.text(),
                title=self.txbTitle.text(),
                is_published=self.txbIsPublished.text(),
                file=self.txbFile.text(),
                metadata=metadata,
                content_data=content_data
            )
        except ValidationError as e:
            error_acquire = True
            QMessageBox.about(self, 'Error message', '{}'.format(e))

        except BaseException as err:
            error_acquire = True
            QMessageBox.about(self, 'Error message', 'An exception occurred: {}'.format(err))

        if error_acquire is False:
            self.close()

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
        return self.translation_model
