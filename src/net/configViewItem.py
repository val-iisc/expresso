# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configViewItem.ui'
#
# Created: Sun Apr  5 23:19:39 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import sys
root=os.getenv('EXPRESSO_ROOT')
sys.path.append(root+'/src/custom')
import netWidget

sys.path.append(os.getenv('CAFFE_ROOT')+'/python/caffe/proto')
import caffe_pb2
sys.path.append(root+'/src/net/config')
import netConfig_pb2
from google.protobuf import text_format

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
    def __init__(self,parent=None,trainMode=False,index=None):
        super(Ui_Form, self).__init__(parent)
	self.trainMode=trainMode
	self.index=index
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 530)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(49, 74, 93)"))
	self.labelLoad=QtGui.QLabel(Form)
	self.labelLoad.setGeometry(QtCore.QRect(10,93,300,25));
        self.labelLoad.setStyleSheet(_fromUtf8("background-color:rgb(49, 73, 93);color:rgb(255,255,255)"))

        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(302, 93, 25, 25))
        self.toolButton.setStyleSheet(_fromUtf8("color:rgb(49, 73, 93);background-color:rgb(255,255,0)"))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 100, 471, 16))
        self.label.setStyleSheet(_fromUtf8("color:rgb(50, 165, 211);\n"
"font: 12pt \"Ubuntu Condensed\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.toolButton_2 = QtGui.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(475, 93, 123, 25))
        self.toolButton_2.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 0)"))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 261, 31))
        self.label_2.setStyleSheet(_fromUtf8(";color:rgb(50, 165, 211);\n"
"font: 24pt \"Ubuntu Condensed\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.toolButton_3 = QtGui.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(570, 93, 23, 25))
        self.toolButton_3.setStyleSheet(_fromUtf8("background-color:rgb(50, 165, 211)"))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.toolButton_4 = QtGui.QToolButton(Form)
        self.toolButton_4.setGeometry(QtCore.QRect(570, 485, 23, 25))
        self.toolButton_4.setStyleSheet(_fromUtf8("background-color:rgb(50, 165, 211)"))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))

        self.toolButton_5 = QtGui.QToolButton(Form)
        self.toolButton_5.setGeometry(QtCore.QRect(405, 485, 192, 25))
        self.toolButton_5.setStyleSheet(_fromUtf8("background-color:rgb(250, 245, 11)"))
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))

        self.widget = QtGui.QScrollArea(Form)
        self.widget.setGeometry(QtCore.QRect(15, 150, 581, 331))
        self.widget.setObjectName(_fromUtf8("widget"))
	self.widget.setStyleSheet(_fromUtf8("background-color:rgb(225, 225, 225)"))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.labelLoad.setText(_translate("Form", "Load / modify existing net configuration", None))
        self.toolButton.setText(_translate("Form", "...", None))
        self.label.setText(_translate("Form", "/usr/home/", None))
        self.toolButton_2.setText(_translate("Form", "Create new net", None))
	self.toolButton_2.clicked.connect(self.onNewNetClickedSlot)
        self.label_2.setText(_translate("Form", "Deploy Net", None))
        self.toolButton_3.setText(_translate("Form", "+", None))
	self.toolButton_3.clicked.connect(self.expandSlot)
        self.toolButton_4.setText(_translate("Form", "-", None))
	self.toolButton_4.clicked.connect(self.shrinkSlot)
	ctext="Train" if self.trainMode==True else "Deploy"
	self.toolButton_5.setText(_translate("Form","Copy from "+ctext+" Net",None))
	self.widget.setVisible(False)
	self.toolButton_4.setVisible(False)
	self.toolButton_5.setVisible(False)
	self.toolButton.clicked.connect(self.onThreeDotsClickedSlot)

	if(self.index==None):
	    if(self.trainMode==True):
		self.subWidget=netWidget.MyForm(root+'/src/custom/defaultTrain.prototxt',parent=self.widget,trainMode=self.trainMode)
		self.label.setText(root+'/src/custom/defaultTrain.prototxt')
	    else:
		self.subWidget=netWidget.MyForm(root+'/src/custom/defaultDeploy.prototxt',parent=self.widget,trainMode=self.trainMode)
		self.label.setText(root+'/src/custom/defaultDeploy.prototxt')
	    self.subWidget.setGeometry(0,0,591,400)
	
	else: 
	    self.subWidget=netWidget.MyForm(root+'/src/custom/defaultDeploy.prototxt',parent=self.widget,trainMode=self.trainMode)
	    self.label.setText(root+'/src/custom/defaultTrain.prototxt')
	    #self.subWidget=netWidget.MyForm(self.netHandle.net[self.index].protopath,parent=self.widget,trainMode=self.trainMode)
	    self.subWidget.setGeometry(0,0,591,400)

	self.subWidget.treeWidget.setGeometry(QtCore.QRect(0,0,581,330))
	
	#For Hiding Work starts
	self.expandSlot()
	self.toolButton_4.hide()	
	self.label.hide()
	#Hiding work ends

    def changeNet(self):
	    self.netHandler=netConfig_pb2.Param()
	    text_format.Merge(open(root+'/net/netData.prototxt').read(),self.netHandler)
	    print self.netHandler

	    if(self.trainMode==True):
	        if self.index!=None and self.netHandler.net[self.index].HasField('trainpath') and os.path.exists(self.netHandler.net[self.index].trainpath):
	    	    self.subWidget.loadFromListSlot(self.index)
		    self.label.setText(self.netHandler.net[self.index].trainpath)		    
	        else:
		    #self.subWidget=netWidget.MyForm(root+'/src/custom/defaultTrain.prototxt',parent=self.widget,trainMode=self.trainMode)
		    self.subWidget.loadFromListSlot(self.index)
	    	    self.label.setText(root+'/src/custom/defaultTrain.prototxt')
		return
   
	    if(self.trainMode==False):
	        if self.index!=None and self.netHandler.net[self.index].HasField('protopath') and os.path.exists(self.netHandler.net[self.index].protopath):
	    	    self.subWidget.loadFromListSlot(self.index)
		    self.label.setText(self.netHandler.net[self.index].protopath)		    
	        else:
		    #self.subWidget=netWidget.MyForm(root+'/src/custom/defaultDeploy.prototxt',parent=self.widget,trainMode=self.trainMode)
		    self.subWidget.loadFromListSlot(self.index)
	   	    self.label.setText(root+'/src/custom/defaultDeploy.prototxt')
	        return	

    def expandSlot(self):
	self.toolButton_3.setVisible(False)
	self.toolButton_4.setVisible(True)
	self.toolButton_5.setVisible(True)
	self.widget.setVisible(True)
	

    def shrinkSlot(self):
	self.toolButton_3.setVisible(True)
	self.toolButton_4.setVisible(False)
	self.toolButton_5.setVisible(False)
	self.widget.setVisible(False)


    def onThreeDotsClickedSlot(self):
	prevtext=self.label.text().__str__()
	self.label.setText(QtGui.QFileDialog.getOpenFileName(self,self.tr("Open File"),prevtext))
	self.subWidget.textEdit.setText(open(self.label.text().__str__()).read())
	self.subWidget.loadTreeWidget()
	selfexpandSlot()
		
    def onNewNetClickedSlot(self):#Load/Modify Existing Configuration
        self.index=None;
        self.changeNet()



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

