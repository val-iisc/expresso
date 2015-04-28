# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addNameView.ui'
#
# Created: Mon Apr 27 11:43:37 2015
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

class Ui_Form(QtGui.QWidget):
    def __init__(self,parent=None,index=None):
        super(Ui_Form,self).__init__(parent)
	self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(421, 183)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 10, 361, 51))
        self.label.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButtonCancel = QtGui.QPushButton(Form)
        self.pushButtonCancel.setGeometry(QtCore.QRect(253, 140, 71, 27))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.pushButtonOk = QtGui.QPushButton(Form)
        self.pushButtonOk.setGeometry(QtCore.QRect(330, 140, 71, 27))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 70, 331, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(380, 70, 23, 25))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Enter the name by which you wish \n"
" to refer to the data\n"
"", None))
        self.pushButtonCancel.setText(_translate("Form", "Cancel", None))
        self.pushButtonOk.setText(_translate("Form", "Ok", None))
        self.toolButton.setText(_translate("Form", "...", None))
	self.toolButton.hide()
    	self.pushButtonOk.clicked.connect(self.submitSlot)
	self.pushButtonCancel.clicked.connect(self.cancelSlot)

    def submitSlot(self):
	self.close()
    def cancelSlot(self):
	self.lineEdit.clear()
	self.close()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

