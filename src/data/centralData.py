# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'centralDefault.ui'
#
# Created: Sat Mar  7 00:20:05 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
root=os.getenv('EXPRESSO_ROOT')
#sys.path.append(root+'/src/data')
import dataView
import importView

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
        Form.resize(611, 591)
        self.widget = QtGui.QWidget(Form)
	#self.widgetLayout=QtGui.QVBoxLayout()
	#self.widget.setLayout(self.widgetLayout)
	self.importViewContainer=QtGui.QWidget(self.widget)
	self.importViewContainer.setStyleSheet("background-color:rgb(115, 115, 115)")
	self.importViewContainer.setGeometry(QtCore.QRect(0,0,611,255))
	#self.widgetLayout.addWidget(self.importViewContainer)
	self.importViewWidget=importView.Ui_Form(self.importViewContainer)
	self.dataViewContainer=QtGui.QWidget(self.widget)
	self.dataViewContainer.setStyleSheet("background-color:rgb(115, 115, 115)")
	self.dataViewContainer.setGeometry(QtCore.QRect(0,255,611,336))
	self.dataViewWidget=dataView.Ui_Form(self.dataViewContainer)
	#self.widgetLayout.addWidget(self.dataViewContainer)



        self.widget.setGeometry(QtCore.QRect(0, 0, 611, 591))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

