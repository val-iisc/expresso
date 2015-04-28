# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notificationListItem.ui'
#
# Created: Mon Apr 13 03:11:26 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import notificationCommonView
import sys
import os
root=os.getenv('EXPRESSO_ROOT')
sys.path.append(root+'/src/notification')

#import notificationImportingData #Importing Data
import notificationDefault
import notificationTrainingData

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
    signalToggledTrigger=QtCore.pyqtSignal(object)
    def __init__(self,parent=None,l=None):
        super(Ui_Form, self).__init__(parent)
	self.l=l
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(414, 108)
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 414, 104))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
	self.commonPage=notificationCommonView.Ui_Form(self.page,self.l)
	if(self.l==None): return
	if(len(self.l)<5):return
	self.commonPage.toolButton.hide()##Remove Later!!!!!
	self.commonPage.label_2.hide()

	#Data View
	if(self.l[0]=="Data View"):
	    if(self.l[3]!=1):
		Form.setStyleSheet("background-color:rgb(80,80,80)")
	    else:
		Form.setStyleSheet("background-color:rgb(115,115,115)")
	#Net View
	if(self.l[0]=="Net View"):
	    if(self.l[3]!=1):
		Form.setStyleSheet("background-color:rgb(80,80,80)")
	    else:
		Form.setStyleSheet("background-color:rgb(115,115,115)")

	if(self.l[0]=="Exp View"):
	    if(self.l[3]!=1):
		Form.setStyleSheet("background-color:rgb(60,81,60)")
	    else:
		Form.setStyleSheet("background-color:rgb(120,180,120)")

	if(self.l[0]=="Train View"):
	    if(self.l[3]!=1):
		Form.setStyleSheet("background-color:rgb(60,81,60)")
	    else:
		Form.setStyleSheet("background-color:rgb(120,180,120)")

	if(self.l[3]==0):
	    self.commonPage.progressBar.setValue(0)
	if(self.l[3]==2):
	    self.commonPage.progressBar.setValue(self.l[5])
	if(self.l[3]==1):
	    self.commonPage.label_3.setText('Completed')
	    self.commonPage.progressBar.setValue(100)

	
	###### SEGREGATION BASED ON NOTIFICATION NAME ######
	if(self.l[1]=="Importing Data"):
	    self.auxillaryPage=notificationDefault.Ui_Form(self.page_2)
	elif(self.l[1]=="Training Data"):
	    self.commonPage.toolButton.show()
	    self.auxillaryPage=notificationTrainingData.Ui_Form(self.page_2,self.l)

	else:
	    self.auxillaryPage=notificationDefault.Ui_Form(self.page_2)

	if(self.l[-1]==True):self.stackedWidget.setCurrentIndex(1)

	self.commonPage.toolButton.clicked.connect(self.toggleViewSlot)
	self.auxillaryPage.toolButton.clicked.connect(self.toggleViewSlot)
    def toggleViewSlot(self):
	self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex()^1)
	currIdx=self.stackedWidget.currentIndex()
	uniqueId=self.l[2]
	print self.l,'%%%%%%%%'
	print currIdx, '%%%%%%'
	self.signalToggledTrigger.emit([uniqueId,currIdx])

#	self.signalToggledTrigger.emit([self.l[2] self.stackedWidget.currentIndex()])

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

