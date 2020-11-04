import sys
from PyQt5 import QtWidgets
from forms.MainForm import MainForm


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainForm()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
