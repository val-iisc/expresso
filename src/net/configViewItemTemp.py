# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configViewItem.ui'
#
# Created: Mon Apr  6 00:55:33 2015
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
        Form.resize(611, 530)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(49, 74, 93)"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(510, 93, 23, 25))
        self.toolButton.setStyleSheet(_fromUtf8("background-color:rgb(50, 165, 211)"))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 100, 471, 16))
        self.label.setStyleSheet(_fromUtf8("color:rgb(50, 165, 211);\n"
"font: 12pt \"Ubuntu Condensed\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.toolButton_2 = QtGui.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(540, 93, 23, 25))
        self.toolButton_2.setStyleSheet(_fromUtf8("background-color:rgb(50, 165, 211)"))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 261, 31))
        self.label_2.setStyleSheet(_fromUtf8(";color:rgb(50, 165, 211);\n"
"font: 24pt \"Ubuntu Condensed\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.toolButton_3 = QtGui.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(570, 93, 23, 25))
        self.toolButton_3.setStyleSheet(_fromUtf8("background-color:rgb(50, 165, 211)"))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.toolButton_4 = QtGui.QToolButton(Form)
        self.toolButton_4.setGeometry(QtCore.QRect(570, 498, 23, 25))
        self.toolButton_4.setStyleSheet(_fromUtf8("background-color:rgb(50, 165, 211)"))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(15, 150, 581, 331))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.toolButton.setText(_translate("Form", "...", None))
        self.label.setText(_translate("Form", "/usr/home/", None))
        self.toolButton_2.setText(_translate("Form", "*", None))
        self.label_2.setText(_translate("Form", "Deploy Net", None))
        self.toolButton_3.setText(_translate("Form", "+", None))
        self.toolButton_4.setText(_translate("Form", "-", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

