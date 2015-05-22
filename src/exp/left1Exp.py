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
import sys
import os
root=os.getenv('EXPRESSO_ROOT')
sys.path.append(root+'/wizard')
import wizardView

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
        self.widget = wizardView.Ui_Form(Form,flowName='Experiment View')
        self.widget.setGeometry(QtCore.QRect(0, 0, 291, 351))
	self.widget.setStyleSheet('background-color:rgba(255,255,225,0);border:0px;')
	self.heading2List=[]
	self.addPages()#Add Pages
	#self.addWidgets() #Add the necessary Widgets
	self.pushButtonBack=QtGui.QPushButton(Form)
	self.pushButtonBack.setGeometry(221,0,60,30)
	self.pushButtonBack.setStyleSheet('background-color:rgba(255,255,255,175);font:15pt \"Ubuntu Condensed\";')
	
	self.pushButtonBack.setText('Return')
	self.pushButtonBack.hide()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
    def addPages(self):
	#self.addPage2()
	#self.addPage3()
	self.currentIndex=0

    def pushButtonBackSlot(self):
	self.pushButtonBack.hide()
	if(self.currentIndex==0):return
	self.currentIndex=0
	#self.stackedWidget.setCurrentIndex(self.currentIndex)	
	pass

    def pushButtonNextSlot(self):
	if(self.currentIndex==1):return
	self.currentIndex=self.currentIndex+1
	#self.stackedWidget.setCurrentIndex(self.currentIndex)
	pass

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

