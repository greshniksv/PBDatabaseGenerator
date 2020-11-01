from PyQt5 import QtWidgets
from .MetadataFormUi import Ui_Data


class MetadataWidget(QtWidgets.QDialog, Ui_Data):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def return_data(self):
        return {
            'name': self.txbName.text(),
            'value': self.txbValue.text(),
            'type': self.txbType.text(),
            'row_type': self.cbRowType.currentText()
        }
