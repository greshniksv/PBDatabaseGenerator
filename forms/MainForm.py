from .TranslationForm import TranslationForm
from .UserForm import UserForm
from .MainFormUi import Ui_MainForm
from PyQt5 import QtWidgets, QtCore
from Services.SqlService import SqlService
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QMessageBox, QFileDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Services.WorkerService import WorkerService
from models.TranslationModel import TranslationModel
import json


class MainForm(QtWidgets.QMainWindow, Ui_MainForm):
    def __init__(self):
        super().__init__()
        self.user_model = None
        self.translation_model = None
        self.user_form = UserForm(parent=self)
        self.trans_form = TranslationForm(parent=self)
        self.setupUi(self)
        self.thread_pool = QThreadPool()

        # control assignation
        self.btnConfigureTranslation.clicked.connect(self.open_translation)
        self.btnConfigureUser.clicked.connect(self.open_user)
        self.btnExecute.clicked.connect(self.execute)
        self.btnSaveTemplate.clicked.connect(self.save_template)
        self.btnLoadTemplate.clicked.connect(self.load_template)
        self.btnVerifyConnection.clicked.connect(self.test_connection)
        drivers = SqlService.drivers()
        for i in range(len(drivers)):
            self.cbDataSources.addItem(drivers[i])

    def test_connection(self):
        def result(r):
            self.lblVerifyConnection.setStyleSheet("color : grey;")
            self.lblVerifyConnection.setText("success")
            print(r)

        def error(r):
            self.lblVerifyConnection.setStyleSheet("color : red;")
            self.lblVerifyConnection.setText("error")

        def verify_connection():
            self.lblVerifyConnection.setStyleSheet("color : green;")
            self.lblVerifyConnection.setText("executing...")
            service = SqlService(
                driver=self.cbDataSources.currentText(),
                server=self.txbServer.text(),
                database=self.txbDatabase.text(),
                user=self.txbUser.text(),
                password=self.txbPassword.text(),
                trust=self.cbTrustedConnection.isChecked()
            )
            return service.test_connection()

        worker = WorkerService(verify_connection)
        worker.signals.result.connect(result)
        # worker.signals.finished.connect(self.thread_complete)
        worker.signals.error.connect(error)
        # worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.thread_pool.start(worker)

    def save_template(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getOpenFileNames()", "",
                                                "Json Files (*.json)", options=options)
        # TODO:Save template
        if len(file) > 0:
            if not file.endswith(".json"):
                file += ".json"
            with open(file, 'w') as f:
                json_data = json.dumps(self.translation_model.__dict__)
                f.write(json_data)
        else:
            QMessageBox.about(self, 'Error message', 'Files was not selected')

    def load_template(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "Json Files (*.json)", options=options)
        # TODO:Load template
        if len(files) > 0:
            with open(files[0], 'r') as f:
                json_data = f.read()
                self.translation_model = TranslationModel(**json.loads(json_data))
        else:
            QMessageBox.about(self, 'Error message', 'Files was not selected')

    def execute(self):
        model = self.translation_model

    def set_translation(self, model):
        self.translation_model = model
        self.lblTranslation.setStyleSheet("color : green;")
        self.lblTranslation.setText("OK")

    def set_user(self, model):
        self.user_model = model
        self.lblUser.setStyleSheet("color : green;")
        self.lblUser.setText("OK")

    def open_translation(self):
        self.trans_form.setParent(self)
        self.trans_form.setWindowFlag(QtCore.Qt.Window)
        self.trans_form.show()

    def open_user(self):
        self.user_form.setParent(self)
        self.user_form.setWindowFlag(QtCore.Qt.Window)
        self.user_form.show()
