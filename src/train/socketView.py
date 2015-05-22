# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'socketView.ui'
#
# Created: Fri Mar 13 20:30:48 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#Imports begin
import sys
import os
import trainValidDataView 
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
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.root=root
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 591)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(120, 180, 120)"))
        self.pushButtonFinish = QtGui.QPushButton(Form)
        self.pushButtonFinish.setGeometry(QtCore.QRect(450, 516, 141, 31))
        self.pushButtonFinish.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(210, 225, 210);background-color:rgb(105,150,105)"))
        self.pushButtonFinish.setObjectName(_fromUtf8("pushButtonFinish"))
        self.widget_6 = QtGui.QWidget(Form)
        self.widget_6.setGeometry(QtCore.QRect(40, 390, 551, 101))
        self.widget_6.setStyleSheet(_fromUtf8("background-color:rgb(210,225,210)"))
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.layoutWidget_2 = QtGui.QWidget(self.widget_6)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 10, 291, 34))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_12.setMargin(0)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_11 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu Condensed\";color:rgb(90, 90, 60)"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_12.addWidget(self.label_11)
        self.lineEditModelName = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditModelName.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(120,180,120);color:rgb(210,225,210)"))
        self.lineEditModelName.setObjectName(_fromUtf8("lineEditModelName"))
        self.horizontalLayout_12.addWidget(self.lineEditModelName)
        self.layoutWidget_3 = QtGui.QWidget(self.widget_6)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 60, 291, 34))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_13.setMargin(0)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_12 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu Condensed\";color:rgb(90, 90, 60)"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_13.addWidget(self.label_12)
        self.lineEditConfigName = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEditConfigName.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(120,180,120);color:rgb(210,225,210)"))
        self.lineEditConfigName.setObjectName(_fromUtf8("lineEditConfigName"))
        self.horizontalLayout_13.addWidget(self.lineEditConfigName)
        self.label_2 = QtGui.QLabel(self.widget_6)
        self.label_2.setGeometry(QtCore.QRect(320, 20, 221, 17))
        self.label_2.setStyleSheet(_fromUtf8("font: oblique 14pt \"Ubuntu Condensed\";color:rgb(120, 180, 120)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.widget_6)
        self.label_3.setGeometry(QtCore.QRect(320, 70, 221, 17))
        self.label_3.setStyleSheet(_fromUtf8("font: oblique 14pt \"Ubuntu Condensed\";color:rgb(120, 180, 120)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 520, 411, 21))
        self.label_4.setStyleSheet(_fromUtf8("font: oblique 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 10, 341, 31))
        self.label_5.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
	#Added Seperately
        self.widgetContainer = QtGui.QWidget(Form)
        self.widgetContainer.setGeometry(QtCore.QRect(40, 59, 551, 311))
        self.widgetContainer.setObjectName(_fromUtf8("widget"))
        self.widget = trainValidDataView.Ui_Form(self.widgetContainer)
	self.widget.setGeometry(QtCore.QRect(0, 0, 511, 340))
        self.widget.setObjectName(_fromUtf8("scrollAreaWidgetContents"))


        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButtonFinish.setText(_translate("Form", "Finish", None))
	self.pushButtonFinish.hide()
        self.label_11.setText(_translate("Form", "Model Name         ", None))
	self.label_11.setVisible(False)
        self.lineEditModelName.setText(_translate("Form", "Untitled", None))
	self.lineEditModelName.setVisible(False)
        self.label_12.setText(_translate("Form", "Name of Trained Model         ", None))
        self.lineEditConfigName.setText(_translate("Form", "Untitled", None))
        self.label_2.setText(_translate("Form", "Name by which model is saved", None))
	self.label_2.setVisible(False)
        self.label_3.setText(_translate("Form", "Name by which config is saved", None))
        self.label_4.setText(_translate("Form", "Note: Once you go to next step, you start \"actual\" Training", None))
        self.label_5.setText(_translate("Form", "Associate Data with Train Blobs", None))




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

