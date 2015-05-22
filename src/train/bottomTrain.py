# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bottomDefault.ui'
#
# Created: Sat Mar  7 00:19:53 2015
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
sys.path.append(root+'/src/train')
sys.path.append(root+'/src/net')
import netButtonView


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
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 611, 61))
        self.widget.setObjectName(_fromUtf8("widget"))
	self.currentIndex=0;
	self.addWidgets()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

    #Add the necessary Widgets
    def addWidgets(self):
        self.pushButtonBack=QtGui.QPushButton(self)
        self.pushButtonBack.setGeometry(QtCore.QRect(300,10,150,30))
        self.pushButtonBack.setText("Back")
        self.pushButtonBack.setStyleSheet("background-color:rgb(120,120,90);\
                                                color:rgb(225,225,210)")
	self.pushButtonBack.hide()
        self.pushButtonNext=QtGui.QPushButton(self)
        self.pushButtonNext.setGeometry(QtCore.QRect(450,10,141,30))
        self.pushButtonNext.setText("Next")
        self.pushButtonNext.setStyleSheet("background-color:rgb(120,120,90);\
                                                color:rgb(225,225,210)")
	self.pushButtonNext.hide()
        self.pushButtonBack.clicked.connect(self.pushButtonBackSlot)
        self.pushButtonNext.clicked.connect(self.pushButtonNextSlot)
	




    def pushButtonBackSlot(self):
        print 'back clicked'
        if self.currentIndex==5:
            self.currentIndex=0;
            self.pushButtonNext.hide()
            self.pushButtonBack.hide()
            return;
        if self.currentIndex==0:return
        if self.currentIndex==1:
            self.pushButtonNext.hide()
            self.pushButtonBack.hide()
        self.currentIndex=self.currentIndex-1



    def pushButtonNextSlot(self):
        if(self.currentIndex==0):
            self.pushButtonNext.show()
            self.pushButtonBack.show()

	if(self.currentIndex==2):
	    self.pushButtonNext.setText('Finish')
	else:
	    self.pushButtonNext.setText('Next')

        if(self.currentIndex==3):
            self.currentIndex=0;
	    self.pushButtonBack.hide()
	    self.pushButtonNext.hide()
	    return
        if(self.currentIndex==4):return
        self.currentIndex=self.currentIndex+1
        pass


    def switchToPageSVM(self):
        print 'SVM Page in central'
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

