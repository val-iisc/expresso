# -*- coding: utf-8 -*-
##############
# Written by : Jaley Dholakiya
# Video Analytics Lab,IISc
#############


# Form implementation generated from reading ui file 'left1Default.ui'
#
# Created: Sat Mar  7 00:20:17 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
import os
root=os.getenv('EXPRESSO_ROOT')
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
        Form.resize(291, 351)
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 291, 321))
	self.stackedWidget.setStyleSheet('background-color:rgba(255,255,225,0);border:0px;')
	self.addPages()#Add Pages
	self.addWidgets() #Add the necessary Widgets

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
    def addPages(self):
	self.addPage0()
	self.addPage0()
	self.addPage1()
	#self.addPage2()
	#self.addPage3()
	self.currentIndex=0

    def addPage0(self):
	self.textEdit=QtGui.QTextEdit(self)
	self.textEdit.setStyleSheet(_fromUtf8("font: 24pt \"Ubuntu Condensed\";color:rgba(0,0,0,105);background-color:rgba(255,255,255,0)"))
 	self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Condensed\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:20pt;\">Welcome to </span><span style=\" font-family:\'Ubuntu\'; font-size:20pt; font-weight:600;\">Experiment View.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:20pt;\">Select one of the options to proceed.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:20pt;\"><br /></p></body></html>", None))

	self.stackedWidget.setGeometry(QtCore.QRect(0,0,291,321))
	self.stackedWidget.addWidget(self.textEdit)


    def addPage0Old(self):
        self.label0=QtGui.QLabel(self)
        self.pixmap0=QtGui.QPixmap(root+'/res/exp/steps/step0Exp.jpg')
        self.label0.setPixmap(self.pixmap0.scaled(291,321,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.FastTransformation))

        #self.Page0TextEdit=QtGui.QTextEdit(self)
        self.stackedWidget.addWidget(self.label0)

    def addPage1(self):
        self.label1=QtGui.QLabel(self)
        self.pixmap1=QtGui.QPixmap(root+'/res/exp/steps/step1Exp.jpg')
        self.label1.setPixmap(self.pixmap1.scaled(291,321,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.FastTransformation))
        self.stackedWidget.addWidget(self.label1)

    def addPage2(self):
        self.label2=QtGui.QLabel(self)
        self.pixmap2=QtGui.QPixmap(root+'/res/exp/steps/step2Exp.jpg')
        self.label2.setPixmap(self.pixmap2.scaled(291,321,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.FastTransformation))
        self.stackedWidget.addWidget(self.label2)

    def addPage3(self):
        self.label3=QtGui.QLabel(self)
        self.pixmap3=QtGui.QPixmap(root+'/res/exp/steps/step3Exp.jpg')
        self.label3.setPixmap(self.pixmap3.scaled(291,321,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.FastTransformation))
        self.stackedWidget.addWidget(self.label3)

    #Add the necessary Widgets
    def addWidgets(self):
	self.pushButtonBack=QtGui.QPushButton(self)
	self.pushButtonBack.setGeometry(QtCore.QRect(0,321,150,30))
	self.pushButtonBack.setText("Back")
	self.pushButtonBack.setStyleSheet("background-color:rgb(120,120,90);\
						color:rgb(225,225,210)")
	self.pushButtonNext=QtGui.QPushButton(self)
	self.pushButtonNext.setGeometry(QtCore.QRect(150,321,141,30))
	self.pushButtonNext.setText("Next")
	self.pushButtonNext.setStyleSheet("background-color:rgb(120,120,90);\
						color:rgb(225,225,210)")
	self.pushButtonBack.clicked.connect(self.pushButtonBackSlot)
	self.pushButtonNext.clicked.connect(self.pushButtonNextSlot)
	self.pushButtonBack.setVisible(True)
	self.pushButtonNext.setVisible(False)

    def pushButtonBackSlot(self):
	if(self.currentIndex==0):return
	self.currentIndex=0
	self.stackedWidget.setCurrentIndex(self.currentIndex)	
	pass

    def pushButtonNextSlot(self):
	if(self.currentIndex==1):return
	self.currentIndex=self.currentIndex+1
	self.stackedWidget.setCurrentIndex(self.currentIndex)
	pass

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

