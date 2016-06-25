# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'augmentationView.ui'
#
# Created: Wed May  6 14:40:42 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import sys
root=os.getenv('EXPRESSO_ROOT')
sys.path.append(root+'/src/augmentation')
import AugmentationHandler


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
    signalRefreshTrigger=QtCore.pyqtSignal(object)
    def __init__(self,parent=None,lineList=[],fileName=None,dim=(3,227,227)):
        super(Ui_Form,self).__init__(parent)
	self.lineList=lineList
	self.fileName=fileName
	self.dim=dim
        self.setupUi(self)


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(291, 255)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(111,111,111);"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 121, 131))
        self.listWidget.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";background-color:rgb(240,240,240);color:rgb(45,45,45)"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 221, 31))
        self.label.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget_2 = QtGui.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(160, 30, 121, 131))
        self.listWidget_2.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";background-color:rgb(240,240,240);color:rgb(45,45,45)"))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(134, 50, 23, 25))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(134, 80, 23, 25))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton_3 = QtGui.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(134, 110, 23, 25))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(90, 180, 41, 27))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255)"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 180, 41, 27))
        self.lineEdit_2.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255)"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 220, 81, 27))
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(175,175,175)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 220, 81, 27))
        self.pushButton_2.setStyleSheet(_fromUtf8("background-color:rgb(175,175,175)"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
	self.pushButton.clicked.connect(self.submit);	
	self.pushButton_2.clicked.connect(self.reject)

        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 226, 66, 17))
        self.label_2.setStyleSheet(_fromUtf8("color:rgb(240,240,240);\n"
"font: 14pt \"Ubuntu Condensed\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(11, 180, 73, 23))
        self.label_4.setStyleSheet(_fromUtf8("font: 12pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(160, 180, 73, 23))
        self.label_5.setStyleSheet(_fromUtf8("font: 12pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
	self.augmentationHandler=AugmentationHandler.AugmentationHandler()
	self.listWidget.clicked.connect(self.onLeftListClicked)
	self.listWidget_2.clicked.connect(self.onRightListClicked)
	self.argList=[]	
	self.initiallize()	


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Data Augmentation", None))
        self.toolButton.setText(_translate("Form", ">", None))
        self.toolButton_2.setText(_translate("Form", "x", None))
        self.toolButton_3.setText(_translate("Form", "r", None))
        self.pushButton.setText(_translate("Form", "Ok", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))
        self.label_2.setText(_translate("Form", "#len : ", None))
        self.label_4.setText(_translate("Form", "arg1", None))
        self.label_5.setText(_translate("Form", "arg2", None))
	self.toolButton.clicked.connect(self.onMoveToRightClicked)
	self.toolButton_2.clicked.connect(self.removeItemFromRight)


    def submit(self):
	if(self.fileName==None or self.fileName==''):
	    self.close()
	    return
	#Operate on set of lines
	self.augmentationHandler.operate(self.lineList,self.fileName,self.argList,self.dim)
	self.signalRefreshTrigger.emit(self.fileName+' is imported')

	self.close()

    def reject(self):
	print 'reject'
	self.close();

    def initiallize(self):
	self.listWidget.clear()
	self.listWidget.addItems(self.augmentationHandler.getKeys())

    def onMoveToRightClicked(self):
	name=self.listWidget.currentItem().text().__str__()
	arg1=self.lineEdit.text().__str__()
	arg2=self.lineEdit_2.text().__str__()
	staticArg=self.staticArg
	self.argList.append([name,arg1,arg2,staticArg])
	self.refreshRightList()

    def refreshRightList(self):
	self.listWidget_2.clear();
	for elem in self.argList:
	    self.listWidget_2.addItem(elem[0])



    def removeItemFromRight(self):
	name=self.listWidget_2.currentItem().text().__str__()

	for idx,elem in enumerate(self.argList):
	    if(elem[0]==name):
		del self.argList[idx]
	self.refreshRightList()

    def onLeftListClicked(self,index=None):
	self.lineEdit.clear()
	self.lineEdit_2.clear()
	self.setArguments(self.listWidget.currentItem().text().__str__())

	pass
    def onRightListClicked(self,index=None):
	idx=self.listWidget_2.currentRow()
	self.lineEdit.setText(self.argList[idx][1])
	self.lineEdit_2.setText(self.argList[idx][2])
	self.setArguments(self.listWidget_2.currentItem().text().__str__())

    def setParams(self,lineList=[],fileName=None,dim=(3,227,227),staticArg=root):
	self.lineList=lineList
	self.fileName=fileName
	self.dim=dim
	self.staticArg=staticArg
	self.argList=[]
	self.listWidget_2.clear()	
    def setArguments(self,name=None):
	if(name==None or name==''):return

	if(self.augmentationHandler.getArg1Name(name)==None):
	    self.label_4.hide()	
	    self.lineEdit.hide()
	else:
	    self.label_4.show()	
	    self.lineEdit.show()
	    self.label_4.setText(self.augmentationHandler.getArg1Name(name))

	if(self.augmentationHandler.getArg2Name(name)==None):
	    self.label_5.hide()
	    self.lineEdit_2.hide()
	else:
	    self.label_5.show()
	    self.lineEdit_2.show()
	    self.label_5.setText(self.augmentationHandler.getArg2Name(name))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

