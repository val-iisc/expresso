# -*- coding: utf-8 -*-

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
import sys
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
	self.addPages()#Add Pages
	self.addWidgets() #Add the necessary Widgets
	self.pushButtonNext.hide()
	self.pushButtonBack.hide()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
    def addPages(self):
	self.addPage0()
	self.addPage1()
	self.addPage2()
	self.addPage3()
	self.addPage4()
	self.addPage5()
	self.currentIndex=0
    def addPage0(self):
	self.label0=QtGui.QLabel(self)
        self.pixmap0=QtGui.QPixmap(root+'/res/train/steps/step0Train.jpg')
        self.label0.setPixmap(self.pixmap0.scaled(291,321,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.FastTransformation))

	#self.Page0TextEdit=QtGui.QTextEdit(self)
	self.stackedWidget.addWidget(self.label0)

    def addPage1(self):
	self.label1=QtGui.QLabel(self)
        self.pixmap1=QtGui.QPixmap(root+'/res/train/steps/step1Train.jpg')
        self.label1.setPixmap(self.pixmap1.scaled(291,321,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.FastTransformation))

	#self.Page0TextEdit=QtGui.QTextEdit(self)
	self.stackedWidget.addWidget(self.label1)

    def addPage2(self):
	self.label2=QtGui.QLabel(self)
        self.pixmap2=QtGui.QPixmap(root+'/res/train/steps/step2Train.jpg')
        self.label2.setPixmap(self.pixmap2.scaled(291,321,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.FastTransformation))

	#self.Page0TextEdit=QtGui.QTextEdit(self)
	self.stackedWidget.addWidget(self.label2)


    def addPage3(self):
	self.label3=QtGui.QLabel(self)
        self.pixmap3=QtGui.QPixmap(root+'/res/train/steps/step3Train.jpg')
        self.label3.setPixmap(self.pixmap3.scaled(291,321,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.FastTransformation))

	#self.Page0TextEdit=QtGui.QTextEdit(self)
	self.stackedWidget.addWidget(self.label3)


    def addPage4(self):
	self.label4=QtGui.QLabel(self)
        self.pixmap4=QtGui.QPixmap(root+'/res/train/steps/step4Train.jpg')
        self.label4.setPixmap(self.pixmap4.scaled(291,321,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.FastTransformation))

	#self.Page0TextEdit=QtGui.QTextEdit(self)
	self.stackedWidget.addWidget(self.label4)

    def addPage5(self):
        self.containerWidget=QtGui.QScrollArea(self)
        self.stackedWidget.addWidget(self.containerWidget)




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


    def pushButtonBackSlot(self):
        print 'back clicked'
        if self.currentIndex==5:
            self.currentIndex=0;
	    self.pushButtonNext.hide()
	    self.pushButtonBack.hide()
            self.stackedWidget.setCurrentIndex(self.currentIndex)
            return;
        if self.currentIndex==0:return
       	if self.currentIndex==1:
	    self.pushButtonNext.hide()
	    self.pushButtonBack.hide()
	self.currentIndex=self.currentIndex-1
        self.stackedWidget.setCurrentIndex(self.currentIndex)



    def pushButtonNextSlot(self):
	if(self.currentIndex==0):
	    self.pushButtonNext.show()
	    self.pushButtonBack.show()

	if(self.currentIndex==3):
	    self.currentIndex=-1
	if(self.currentIndex==4):return
	self.currentIndex=self.currentIndex+1
	self.stackedWidget.setCurrentIndex(self.currentIndex)
	pass


    def switchToPageSVM(self):
        print 'SVM Page in central'
        self.stackedWidget.setCurrentIndex(5)
        self.currentIndex=5
	self.pushButtonBack.show()



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

