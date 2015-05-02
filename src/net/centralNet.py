# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'centralDefault.ui'
#
# Created: Sat Mar  7 00:20:05 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sys
import os
root=os.getenv('EXPRESSO_ROOT')
sys.path.append(root+'/src/net')
import configViewNew



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
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 611, 591))
        self.stackedWidget.setObjectName(_fromUtf8("widget"))


	self.addPages()
	

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

    def addPages(self):
        self.addPage0()

    def addPage0(self):
        self.page0Container=QtGui.QWidget(self)
        self.page0Container.setGeometry(0,0,611,591)
        self.page0Container.setStyleSheet("background-color:rgb(49,74,93);")
        self.page0Widget=configViewNew.Ui_Form(self.page0Container)
        self.page0Widget.setGeometry(0,0,611,591)
        self.stackedWidget.addWidget(self.page0Container)




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

