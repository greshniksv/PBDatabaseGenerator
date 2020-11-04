from .TranslationForm import TranslationForm
from .UserForm import UserForm
from .MainFormUi import Ui_MainForm
from PyQt5 import QtWidgets, QtCore
from Services.SqlService import SqlService
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QMessageBox, QFileDialog
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Services.WorkerService import WorkerService


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
        self.btnVerifyConnection.clicked.connect(self.test)
        drivers = SqlService.drivers()
        for i in range(len(drivers)):
            self.cbDataSources.addItem(drivers[i])

    def thread_complete(self):
        self.lblVerifyConnection.setStyleSheet("color : grey;")
        self.lblVerifyConnection.setText("Compl")

    def result(self, r):
        self.lblVerifyConnection.setStyleSheet("color : grey;")
        self.lblVerifyConnection.setText("result")

    def result22(self, r):
        self.lblVerifyConnection.setStyleSheet("color : grey;")
        self.lblVerifyConnection.setText("error")

    def test(self):
        # Pass the function to execute
        worker = WorkerService(self.verify_connection)
        worker.signals.result.connect(self.result)
        #worker.signals.finished.connect(self.thread_complete)
        worker.signals.error.connect(self.result22)
        #worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.thread_pool.start(worker)

    def verify_connection(self):
        self.lblVerifyConnection.setStyleSheet("color : grey;")
        self.lblVerifyConnection.setText("not tested")

        service = SqlService(
            driver=self.cbDataSources.currentText(),
            server=self.txbServer.text(),
            database=self.txbDatabase.text(),
            user=self.txbUser.text(),
            password=self.txbPassword.text(),
            trust=self.cbTrustedConnection.isChecked()
        )

        # try:
        result = service.test_connection()
        if result is True:
            self.lblVerifyConnection.setStyleSheet("color : green;")
            self.lblVerifyConnection.setText("Success")
        # except BaseException as e:
        #     self.lblVerifyConnection.setStyleSheet("color : red;")
        #     self.lblVerifyConnection.setText("Error")
        #     QMessageBox.about(self, 'Error message', '{}'.format(e))

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
