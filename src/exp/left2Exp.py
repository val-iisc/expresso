# -*- coding: utf-8 -*-
##############
# Written by : Jaley Dholakiya
# Video Analytics Lab,IISc
#############


# Form implementation generated from reading ui file 'left2Default.ui'
#
# Created: Sat Mar  7 00:20:23 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sys
import os
root=os.getenv('EXPRESSO_ROOT')
sys.path.append(root+'/src/train')
sys.path.append(root+'/src/net')
sys.path.append(root+'/src/exp')

import configNetListView
import expListView
import pipelineView
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
        Form.resize(291, 301)
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 291, 301))
        self.stackedWidget.setObjectName(_fromUtf8("widget"))
	self.stackedWidget.setStyleSheet('border:0px;')
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
	self.addPages()
        Form.setWindowTitle(_translate("Form", "Form", None))

    def addPages(self):
        #self.addPage0()
        self.addPage1()
	self.addPage1copy()
        self.addPage3()
        self.addPage0()
        self.currentIndex=0

    def addPage0(self):
        self.containerWidget=QtGui.QScrollArea(self)
        self.containerWidget.setStyleSheet('background-color:rgb(150,150,90);')
        self.stackedWidget.addWidget(self.containerWidget)


    def addPage1copy(self):
        self.stackedWidget.addWidget(self.page1Container)
	
    def addPage1(self):
        self.page1Container=QtGui.QWidget(self)
        self.page1Container.setGeometry(0,0,291,301)
        self.page1Container.setStyleSheet('background-color:rgb(150,150,90);')
        self.page1Widget=expListView.Ui_Form(self.page1Container)
        self.page1Widget.setGeometry(0,0,291,301)
        #self.page1Container.setWidget(self.page1Widget)
        self.stackedWidget.addWidget(self.page1Container)

    def addPage2(self):
        self.containerWidget=QtGui.QScrollArea(self)
        self.stackedWidget.addWidget(self.containerWidget)

    def addPage3(self):
        self.page3Container=QtGui.QWidget(self)
        self.page3Container.setGeometry(0,0,291,301)
        self.page3Container.setStyleSheet('background-color:rgb(150,150,90);')
        #self.page3Widget=pipelineView.Ui_Form(self.page3Container) ### Uncomment It Later
        #self.page3Widget.setGeometry(0,0,291,301)
        #self.page1Container.setWidget(self.page1Widget)
        self.stackedWidget.addWidget(self.page3Container)

    def pushButtonNextSlot(self):
        if self.currentIndex==3:return
        print 'Next Clicked: '+str(self.currentIndex)
        self.currentIndex=self.currentIndex+1
        self.stackedWidget.setCurrentIndex(self.currentIndex)
    
    def pushButtonBackSlot(self):
        print 'back clicked'
        if self.currentIndex==0:return
        self.currentIndex=0
        self.stackedWidget.setCurrentIndex(self.currentIndex)

    def switchToPage1(self):
	self.currentIndex=1
	self.stackedWidget.setCurrentIndex(self.currentIndex)
    def switchToPage2(self):
	self.currentIndex=2
	self.stackedWidget.setCurrentIndex(self.currentIndex)

    def switchToPage3(self):
	self.currentIndex=3
	self.stackedWidget.setCurrentIndex(self.currentIndex)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

