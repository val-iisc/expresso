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
sys.path.append(root+'/src/data')

import netButtonView
import dataGuideView

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
	self.stackedWidget.setStyleSheet('background-color:rgb(150,150,90);border:0;')
	Form.setStyleSheet('background-color:rgb(150,150,90)')

	self.pushButtonBack=QtGui.QPushButton(Form)
        self.pushButtonBack.setGeometry(510,0,75,30)
        self.pushButtonBack.setStyleSheet('background-color:rgba(255,255,255,175);font:15pt \"Ubuntu Condensed\";')
        
        self.pushButtonBack.setText('Back')
	self.pushButtonBack.hide()

	
	self.addPages()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

    def addPages(self):
        self.addPage0()
        self.addPage1()
        self.addPage2()
        self.addPage3()
	self.currentIndex=0

    def addPage0(self):
	self.containerWidget=QtGui.QScrollArea(self)
        self.containerWidget.setStyleSheet('background-color:rgb(150,150,90)')
	self.stackedWidget.addWidget(self.containerWidget)

    def addPage1(self):
        self.page1Container=QtGui.QWidget(self)
        self.page1Container.setGeometry(0,0,611,61)
        self.page1Container.setStyleSheet("background-color:rgb(210,225,210);")
        self.page1Widget=netButtonView.Ui_Form(self.page1Container)
        self.page1Widget.setGeometry(0,0,611,61)
        #self.page1Container.setWidget(self.page1Widget)
        self.stackedWidget.addWidget(self.page1Container)

    def addPage2(self):
        self.page2Container=QtGui.QWidget(self)
        self.page2Container.setGeometry(0,0,611,61)
        self.page2Container.setStyleSheet("background-color:rgb(210,225,210);")
        self.page2Widget=dataGuideView.Ui_Form(self.page2Container)
        self.page2Widget.setGeometry(0,0,611,61)
        #self.page1Container.setWidget(self.page1Widget)
        self.stackedWidget.addWidget(self.page2Container)

    def addPage3(self):
	self.containerWidget=QtGui.QScrollArea(self)
	self.stackedWidget.addWidget(self.containerWidget)


    def pushButtonNextSlot(self):
        if self.currentIndex==3:return
        print 'Next Clicked: '+str(self.currentIndex)
        self.currentIndex=self.currentIndex+1
        self.stackedWidget.setCurrentIndex(self.currentIndex)

    def pushButtonBackSlot(self):
        if(self.currentIndex==0):return
        self.currentIndex=0;
        #self.stackedWidget.setCurrentIndex(self.currentIndex)  
        pass

    """
    def pushButtonBackSlot(self):
        print 'back clicked'
        if self.currentIndex==0:return
        self.currentIndex=self.currentIndex-1
        self.stackedWidget.setCurrentIndex(self.currentIndex)

    """


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

