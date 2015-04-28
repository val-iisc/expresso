# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Mon Apr 27 22:03:28 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import os


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
    def __init__(self,parent=None):
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(414, 275)
	Form.setStyleSheet("background-color:rgb(255,255,255)")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 60, 151, 31))
        self.label.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\""))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 96, 331, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(360, 94, 31, 31))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 151, 31))
        self.label_2.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 202, 331, 31))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.toolButton_2 = QtGui.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(360, 200, 31, 31))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(140, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Caffe Path", None))
        self.toolButton.setText(_translate("Form", "...", None))
        self.label_2.setText(_translate("Form", "Expresso  Path", None))
        self.toolButton_2.setText(_translate("Form", "...", None))
        self.label_3.setText(_translate("Form", "Settings", None))
	self.toolButton.setStyleSheet("background-color:rgb(210,210,210)")
	self.toolButton_2.setStyleSheet("background-color:rgb(210,210,210)")
	self.toolButton.clicked.connect(self.setCaffePath)
	self.lineEdit.setText(os.getenv('CAFFE_ROOT'))
	self.lineEdit_2.setText(os.getenv('EXPRESSO_ROOT'))


    def setCaffePath(self):
	#os.getenviron['EXPRESSO_ROOT']=self.
	pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

