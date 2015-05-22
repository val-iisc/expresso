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
sys.path.append(root+'/wizard')
import wizardView

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

        self.widget =wizardView.Ui_Form(Form,flowName='Train View')
        self.widget.setGeometry(QtCore.QRect(0, 0, 291, 351))
        self.widget.setStyleSheet('background-color:rgba(255,255,225,0);border:0px;')
 
        self.widget.setGeometry(QtCore.QRect(0, 0, 291, 351))
	self.addWidgets() #Add the necessary Widgets
	self.pushButtonNext.hide()
	self.pushButtonBack.hide()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))


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

