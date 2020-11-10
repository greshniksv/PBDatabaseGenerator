from .TranslationFormUi import Ui_TranslationForm
from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
from pydantic import ValidationError

from models.TranslationModel import TranslationModel
from .MetadataForm import MetadataWidget
from .TranslationFormUi import Ui_TranslationForm


class TranslationForm(QtWidgets.QMainWindow, Ui_TranslationForm):
    def __init__(self, parent):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.parent_form = parent
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
        self.setFixedSize(self.width(), self.height()-20)

    def apply_model(self):
        model = self.translation_model
        self.txbLangId.setText(model.language)
        self.txbDraftBy.setText(model.draft_by)
        self.txbSlug.setText(model.slug)
        self.txbPermalink.setText(model.permalink)
        self.txbCreatedBy.setText(model.created_by)
        self.txbAllowedChildren.setText(model.allowed_children)
        self.txbTitle.setText(model.title)
        self.txbIsPublished.setText(model.is_published)
        self.txbFile.setText(model.file)

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

    def open_file_names_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;", options=options)
        if len(files) > 0:
            self.txbFile.setText(files[0])

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
            self.parent_form.set_translation(self.translation_model)

        except ValidationError as e:
            error_acquire = True
            QMessageBox.about(self, 'Error message', '{}'.format(e))

        except BaseException as err:
            error_acquire = True
            QMessageBox.about(self, 'Error message', 'An exception occurred: {}'.format(err))

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
                # fxgfdgfdg
                self.model.appendRow(
                    [
                        QStandardItem(data['name']),
                        QStandardItem(data['value']),
                        QStandardItem(data['type']),
                        QStandardItem(data['row_type'])
                    ])
        except BaseException as err:
            QMessageBox.about(self, 'PyQt5 message', 'An exception occurred: {}'.format(err))
