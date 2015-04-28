# -*- coding: utf-8 -*-
##############
# Written by : Jaley Dholakiya
# Video Analytics Lab,IISc
#############


# Form implementation generated from reading ui file 'expView.ui'
#
# Created: Tue Apr  7 14:49:45 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import os
import sys
root=os.getenv('EXPRESSO_ROOT')
sys.path.append(root+'/src/net/config')
import netConfig_pb2
from google.protobuf import text_format
sys.path.append(os.getenv('CAFFE_ROOT')+'/python/caffe/proto')
import caffe_pb2

from qtutils import inmain_later,inthread,inmain
from netOperation import NetHandler

sys.path.append(os.getenv('CAFFE_ROOT')+'/python')
import caffe
import numpy as np
import h5py
import copy
import inspect
import netOperation
import time
from time import sleep
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
    signalCompleteTrigger=QtCore.pyqtSignal(object)
    signalStartedTrigger=QtCore.pyqtSignal(object)
    signalRefreshTrigger=QtCore.pyqtSignal(object) 

    def __init__(self,parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 591)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(150,150,90);"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 109, 256, 261))
        self.listWidget.setStyleSheet(_fromUtf8(";background-color:rgb(230,240,210);"))
        self.listWidget.setObjectName(_fromUtf8("listView"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(330, 110, 201, 31))
        self.comboBox.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);\n"
"font: 14pt \"Ubuntu Condensed\";"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(334, 170, 66, 17))
        self.label.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(230,240,210);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(420, 164, 113, 27))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 410, 261, 34))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_12.setMargin(0)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu Condensed\";color:rgb(90, 90, 60)"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_12.addWidget(self.label_11)
        self.lineEditName = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditName.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(230,240,210);color:rgb(120,120,75);"))
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.horizontalLayout_12.addWidget(self.lineEditName)
        self.pushButtonGenerate = QtGui.QPushButton(Form)
        self.pushButtonGenerate.setGeometry(QtCore.QRect(200, 460, 101, 32))
        self.pushButtonGenerate.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(225, 225, 210)"))
        self.pushButtonGenerate.setObjectName(_fromUtf8("pushButtonGenerate"))
        self.textEdit_3 = QtGui.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(330, 250, 201, 121))
        self.textEdit_3.setStyleSheet(_fromUtf8("background-color:rgb(120,120,75);color:rgb(230,240,210);\n"
"font: 14pt \"Ubuntu Condensed\";"))
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 380, 541, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(40, 510, 261, 23))
        self.progressBar.setStyleSheet(_fromUtf8("QProgressBar{\n"
"    border: 2px solid white;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color:rgb(45,60,30);\n"
"    background-color:rgb(230,240,210);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(120,120,75);\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}\n"
""))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
	self.progressBar.hide()
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(320, 10, 271, 33))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(120,120,75);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox_2 = QtGui.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 60, 256, 31))
        self.comboBox_2.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);\n"
"font: 14pt \"Ubuntu Condensed\";"))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(330, 70, 271, 33))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";color:rgb(230,240,210);"))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 271, 33))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";color:rgb(230,240,210);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "BatchSize", None))
        self.label_11.setText(_translate("Form", "Name          ", None))
        self.lineEditName.setText(_translate("Form", "Untitled", None))
        self.pushButtonGenerate.setText(_translate("Form", "Generate", None))
        self.textEdit_3.setText("Dimensions are \n ")
        self.label_2.setText(_translate("Form", "Feature Extraction", None))
        self.label_3.setText(_translate("Form", "Data Selection", None))
        self.label_6.setText(_translate("Form", "Deploy Net Selection", None))
	self.lineEdit.setText('50')
	self.fillData()
	self.onNetSelectionChangedSlot()
	self.comboBox_2.currentIndexChanged.connect(self.onNetSelectionChangedSlot)

	self.onDataSelectionChangedSlot()
	self.comboBox.currentIndexChanged.connect(self.onDataSelectionChangedSlot)
	self.pushButtonGenerate.clicked.connect(self.onSubmitClickedSlot)
	

    def fillData(self):
	self.comboBox.clear()
	self.comboBox_2.clear()
	#Fill the data in all the comboBoxes
	#Step 1 : Fill the Deploy List 
	self.netHandler=netConfig_pb2.Param()
	text_format.Merge(open(root+'/net/netData.prototxt').read(),self.netHandler)
	for elem in self.netHandler.net:
	    if(elem.HasField('modelpath') and elem.modelpath.endswith('.caffemodel')):
		print elem.protopath
		self.comboBox_2.addItem(elem.name)

	#Filling the Data List Here
	self.comboBox.addItems([files[0:-5] for files in os.listdir(root+'/data') if files.endswith('.hdf5')])
	    

    def onDataSelectionChangedSlot(self,index=None):
	if(self.comboBox.currentText().__str__()==""):return
	datapath=root+'/data/'+self.comboBox.currentText().__str__()+'.hdf5'
	with h5py.File(datapath,'r') as f:
	    if 'data' not in f.keys():
		self.textEdit_3.setText('Invalid Blob')
		return
	    s=f['data'].shape
	    self.textEdit_3.setText('Dimensions are \n '+str(s[0])+' x '+str(s[1])+' x '+str(s[2])+' x '+str(s[3]))	


    def onNetSelectionChangedSlot(self,index=0):
	self.currentNet=netConfig_pb2.NetParam()
	for elem in self.netHandler.net:
		if elem.name==self.comboBox_2.currentText().__str__():
		    self.currentNet.CopyFrom(elem)
	#if str(self.currentNet)=="":self.currentNet.
	self.listWidget.clear()
	handle=caffe_pb2.NetParameter()
	if(self.currentNet.__str__()==""):return	
	text_format.Merge(open(self.currentNet.protopath).read(),handle)
        for elem in handle.layers:
            item = QtGui.QListWidgetItem(elem.name)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)



    def onSubmitClickedSlot(self):
	#Finally Generating the results and storing it appropreately
	tickedList=[self.listWidget.item(i).text().__str__() for i in range(self.listWidget.count()) if self.listWidget.item(i).checkState()!=0]
	print tickedList

        batchSize=self.lineEdit.text().__str__()
	dataName=self.comboBox.currentText().__str__()
	saveName=self.lineEditName.text().__str__()
	netName=self.comboBox_2.currentText().__str__()
	triggerList=self.createTriggerList()	
	inthread(self.runParallel,netName,tickedList,batchSize,dataName,saveName,triggerList)



    def runParallel(self,netName,netList,batchSize,dataName,saveName,triggerList):
	print triggerList
        self.startTrigger(triggerList) #====>End
 	handle=NetHandler(netName,netList,batchSize,dataName,saveName)
	handle.start()	
        self.signalRefreshTrigger.emit("Experiment Created with name"+saveName)
        triggerList=self.endTrigger(triggerList) #====>End


    def createTriggerList(self):
        triggerList=[]
        triggerList.append('Exp View')
        triggerList.append('Creating Experiment')
        triggerList.append(self.lineEditName.text().__str__()+'_'+str(time.time()))
        triggerList.append(0)
        triggerList.append('Creating Experiment with name '+self.lineEditName.text().__str__())

        triggerList.append(0)
	return triggerList

    def startTrigger(self,triggerList):
        print triggerList
        self.signalStartedTrigger.emit(triggerList)
        return triggerList

    def endTrigger(self,triggerList):
	if triggerList==None:
            self.signalRefreshTrigger.emit("Exp Created")
	    return
        triggerList[3]=1
        triggerList[4].replace('Creating','Created')
        triggerList[5]=100
        self.signalCompleteTrigger.emit(triggerList)




	#self.findTicked()
    def refreshTrigger(self):
	print 'refreshing ExpView'
	self.fillData()



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

