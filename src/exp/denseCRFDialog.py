# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'denseCRFDialog.ui'
#
# Created: Mon Jun  1 23:05:07 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
root=os.getenv('EXPRESSO_ROOT')
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
    signalCompleteTrigger=QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(491, 246)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(150,150,90)"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(230, 20, 221, 31))
        self.comboBox.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255)"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 30, 141, 17))
        self.label.setStyleSheet(_fromUtf8("color:rgb(255,255,255);\n"
"font: 18pt \"Ubuntu Condensed\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 241, 31))
        self.label_2.setStyleSheet(_fromUtf8("color:rgb(255,255,255);\n"
"font: 18pt \"Ubuntu Condensed\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(300, 130, 151, 31))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255)"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 190, 98, 27))
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(225,225,180);\n"
"font: 14pt \"Ubuntu Condensed\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 190, 98, 27))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:rgb(225,225,180);\n"
"font: 14pt \"Ubuntu Condensed\";"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 70, 241, 31))
        self.label_3.setStyleSheet(_fromUtf8("color:rgb(255,255,255);\n"
"font: 18pt \"Ubuntu Condensed\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox_2 = QtGui.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(230, 70, 221, 31))
        self.comboBox_2.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255)"))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
	self.comboBox_2.addItem("IOU(50%)")
	self.initialize()
	self.pushButton.clicked.connect(self.onSubmit)
	self.pushButton_2.clicked.connect(self.onReject)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Ground Truth", None))
        self.label_2.setText(_translate("Form", "Name of Dense Experiment", None))
        self.pushButton.setText(_translate("Form", "Ok", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))
        self.label_3.setText(_translate("Form", "Evaluation Metric", None))

    def initialize(self):
	self.comboBox.clear()
	for elem in os.listdir(root+'/data'):
	    if(elem.endswith('.hdf5')):self.comboBox.addItem(elem[:-5])
    def onSubmit(self):
	self.close()
	self.signalCompleteTrigger.emit('Complete')

    def onReject(self):
	self.close()

    def refresh(self):
	self.comboBox.clear()
	for elem in os.listdir(root+'/data'):
	    if(elem.endswith('.hdf5')):self.comboBox.addItem(elem[:-5])



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

