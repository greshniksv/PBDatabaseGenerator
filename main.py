import sys
from PyQt5 import QtWidgets
import forms.TranslationForm
from PyQt5.QtGui import QStandardItemModel, QStandardItem


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class ExampleApp(QtWidgets.QMainWindow, forms.TranslationForm.Ui_TranslationForm):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.model = QStandardItemModel()
        self.tvMetadata.setModel(self.model)
        self.model.setHorizontalHeaderLabels(["Name", "Value", "Type"])
        self.tvMetadata.setColumnWidth(0, 200)
        self.tvMetadata.setColumnWidth(1, 300)
        self.tvMetadata.setColumnWidth(2, 300)
        self.btnAddMetodata.clicked.connect(self.add_metadata)

    def add_metadata(self):
        self.model.appendRow([QStandardItem("11sdfdsfsdfsdfsdfsdf"), QStandardItem("22sdfdsdsfdsfsdfsfdsdfsdf")])


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
