# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expChooseView.ui'
#
# Created: Sat Mar 14 01:53:22 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import os
root = os.getenv('EXPRESSO_ROOT')

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
        Form.setStyleSheet(_fromUtf8("background-color:rgb(150,210,150);"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(50, 20, 171, 241))
        self.widget.setStyleSheet(_fromUtf8("background-color:rgb(150,210,150)"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 170, 201, 71))
        self.label.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(45,60,45)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 141, 141))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(410, 20, 171, 241))
        self.widget_2.setStyleSheet(_fromUtf8("background-color:rgb(150,210,150)"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.pushButton_2 = QtGui.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 20, 141, 141))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 151, 71))
        self.label_2.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(45,60,45)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.widget_3 = QtGui.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(230, 20, 171, 241))
        self.widget_3.setStyleSheet(_fromUtf8("background-color:rgb(150,210,150)"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.pushButton_3 = QtGui.QPushButton(self.widget_3)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 20, 141, 141))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.label_3 = QtGui.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(10, 170, 151, 71))
        self.label_3.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(45,60,45)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))

	self.widget_2.hide()#Temporary Fix
	#To be corrected Later

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Train New \n"
"Model", None))
	self.setPushButtonIcons()
        self.label_2.setText(_translate("Form", "FineTune \n"
"Existing Model", None))
	self.label_3.setText(_translate("Form", "Train SVM \n"
"", None))

    def setPushButtonIcons(self):
	icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(root+"/res/training.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(141,141))

	
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(root+"/src/train/images/visuallize.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(141,141))

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(root+"/res/svmtrain.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(141,141))

    def clickSlot(self):
	icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(root+"/src/train/images/visuallize.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(141,141))

   

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

