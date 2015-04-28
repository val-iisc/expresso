# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bottomDefault.ui'
#
# Created: Sat Mar  7 00:19:53 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sys
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
    def __init__(self,parent=None):
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 61)
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 611, 61))
        self.stackedWidget.setObjectName(_fromUtf8("widget"))
	#Left Button
	self.addPages()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

    def addPages(self):
        self.addPage0()
        self.addPage1()

    def addPage0(self):
        self.label0=QtGui.QLabel(self)
	print root+'/res/data/help/helpBarData0.jpg'
        self.pixmap0=QtGui.QPixmap(root+'/res/data/help/helpBarData0.jpg')
        self.label0.setPixmap(self.pixmap0.scaled(661,61,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.FastTransformation))
        self.stackedWidget.addWidget(self.label0)


    def addPage1(self):
        self.label1=QtGui.QLabel(self)
        self.pixmap1=QtGui.QPixmap(root+'/res/data/help/helpBarData1.jpg')
        self.label1.setPixmap(self.pixmap1.scaled(661,61,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.FastTransformation))
        self.stackedWidget.addWidget(self.label1)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

