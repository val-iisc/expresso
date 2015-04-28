# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataView.ui'
#
# Created: Sun Apr  5 01:26:41 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 336)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(115, 115, 115)"))
        self.tableView = QtGui.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(10, 50, 331, 261))
        self.tableView.setStyleSheet(_fromUtf8("background-color:rgb(200, 200, 200)"))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(360, 20, 231, 231))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 31, 31))
        self.label_2.setStyleSheet(_fromUtf8("color:rgb(115,115,115); \n"
"background-color:rgb(255,255,255,66%);\n"
"font: 18pt \"Ubuntu Condensed\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalSlider = QtGui.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(440, 260, 151, 29))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 201, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu Condensed\";color:rgb(200, 200, 200)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(360, 260, 60, 27))
        self.spinBox.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255)"))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", "  0", None))
        self.label.setText(_translate("Form", "View/Select  Data", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

