# -*- coding: utf-8 -*-
##############
# Written by : Jaley Dholakiya
# Video Analytics Lab,IISc
#############

# Form implementation generated from reading ui file 'expTesting.ui'
#
# Created: Wed Apr  8 14:32:01 2015
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
from netOperation import SoftMaxAccuracy


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
    signalAccuracyTrigger=QtCore.pyqtSignal(object)

    def __init__(self,parent=None):
        super(Ui_Form,self).__init__(parent)
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
        self.comboBox.setGeometry(QtCore.QRect(330, 87, 201, 31))
        self.comboBox.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);selection-color:rgb(0,0,0);selection-background-color:rgba(255,255,255,100);\n"
"font: 14pt \"Ubuntu Condensed\";"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(334, 223, 66, 17))
        self.label.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(230,240,210);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(420, 217, 113, 27))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 420, 261, 34))
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
        self.pushButtonGenerate.setGeometry(QtCore.QRect(430, 360, 101, 32))
        self.pushButtonGenerate.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(225, 225, 210)"))
        self.pushButtonGenerate.setObjectName(_fromUtf8("pushButtonGenerate"))
        self.textEdit_3 = QtGui.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(330, 257, 201, 91))
        self.textEdit_3.setStyleSheet(_fromUtf8("background-color:rgb(120,120,75);color:rgb(230,240,210);\n"
"font: 14pt \"Ubuntu Condensed\";"))
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(20, 392, 541, 21))
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
        self.comboBox_2.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);selection-color:rgb(0,0,0);selection-background-color:rgba(255,255,255,100);\n"
"font: 14pt \"Ubuntu Condensed\";"))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(330, 47, 271, 33))
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
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(330, 137, 271, 33))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";color:rgb(230,240,210);"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox_3 = QtGui.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(330, 170, 201, 31))
        self.comboBox_3.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);selection-color:rgb(0,0,0);selection-background-color:rgba(255,255,255,100);\n"
"font: 14pt \"Ubuntu Condensed\";"))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.layoutWidget_2 = QtGui.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 460, 261, 34))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_13.setMargin(0)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_12 = QtGui.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu Condensed\";color:rgb(90, 90, 60)"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_13.addWidget(self.label_12)
        self.lineEditName_2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditName_2.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(230,240,210);color:rgb(120,120,75);"))
        self.lineEditName_2.setObjectName(_fromUtf8("lineEditName_2"))
        self.horizontalLayout_13.addWidget(self.lineEditName_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "BatchSize", None))
        self.label_11.setText(_translate("Form", "Accuracy       ", None))
        self.lineEditName.setText(_translate("Form", "", None))
	self.lineEditName.setReadOnly(True)
        self.pushButtonGenerate.setText(_translate("Form", "Evaluate", None))
        self.textEdit_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Condensed\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Testing Blob Dimentions</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">50000 x 3 x 32 x 32 </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; text-decoration: underline;\"><br /></p></body></html>", None))
        self.label_2.setText(_translate("Form", "Testing", None))
        self.label_3.setText(_translate("Form", "Loss Type", None))
        self.label_6.setText(_translate("Form", "Feature Set", None))
        self.label_7.setText(_translate("Form", "Testing Blob Selection", None))
        self.label_12.setText(_translate("Form", "Loss                ", None))
        self.lineEditName_2.setText(_translate("Form", "", None))
	self.fillData()
        self.onNetSelectionChangedSlot()
        self.comboBox_2.currentIndexChanged.connect(self.onNetSelectionChangedSlot)
        self.onDataSelectionChangedSlot()
	self.comboBox_3.currentIndexChanged.connect(self.onDataSelectionChangedSlot)
	self.pushButtonGenerate.clicked.connect(self.onSubmitClickedSlot)
	self.comboBox_3.hide()
	self.textEdit_3.hide()
	self.label_7.hide()
	self.label.hide()
	self.lineEdit.hide()
	self.lineEditName_2.hide()
	self.label_12.hide()
	self.signalAccuracyTrigger.connect(self.setAccuracy)

    def fillData(self):
	self.comboBox_2.clear()
	self.comboBox.clear()
	self.comboBox_3.clear()

        #Fill the data in all the comboBoxes
        #Step 1 : Fill the Deploy List
	self.comboBox_2.addItems([elem[0:-5] for elem in os.listdir(root+'/exp/data') if elem.endswith('.hdf5')])

        #Filling the Data List Here
        self.comboBox_3.addItems([files[0:-5] for files in os.listdir(root+'/data') if files.endswith('.hdf5')])
	#Selecting the different type of Loss Functions
	self.comboBox.addItems(['SOFTMAX'])





    def onDataSelectionChangedSlot(self,index=0):
	if(self.comboBox_3.currentText().__str__()==""):return
        datapath=root+'/data/'+self.comboBox_3.currentText().__str__()+'.hdf5'
        with h5py.File(datapath,'r') as f:
            if 'data' not in f.keys():
                self.textEdit_3.setText('Invalid Blob')
                return
            s=f['data'].shape
            self.textEdit_3.setText('Dimensions are \n '+str(s[0])+' x '+str(s[1])+' x '+str(s[2])+' x '+str(s[3]))


    def onNetSelectionChangedSlot(self,index=0):
        #Update the listWidget on change of the comboBox
	print 'Updating Checkable List Widget'
	print self.comboBox_2.currentText().__str__()
	self.listWidget.clear()
	if self.comboBox_2.currentText().__str__()=="":return
	with h5py.File(root+'/exp/data/'+self.comboBox_2.currentText().__str__()+'.hdf5','r') as f:
	    print f.keys()
            for elem in f.keys():
            	item = QtGui.QListWidgetItem(elem)
            	item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
           	item.setCheckState(QtCore.Qt.Unchecked)
            	if elem!='label':self.listWidget.addItem(item)

    def onSubmitClickedSlot(self):
        #Finally Generating the results and storing it appropreately
        tickedList=[self.listWidget.item(i).text().__str__() for i in range(self.listWidget.count()) if self.listWidget.item(i).checkState()!=0]
        print tickedList

        dataName=self.comboBox_3.currentText().__str__()
        netName=self.comboBox_2.currentText().__str__()
	inthread(self.runParallel,netName,tickedList,dataName)


    def runParallel(self,netName,netList,dataName):
	handle=SoftMaxAccuracy(netName+'.hdf5',netList,dataName)
	accuracy=handle.getAccuracy()
	print accuracy
	self.signalRefreshTrigger.emit("Accuracy for experiment is "+str(accuracy))
	self.signalAccuracyTrigger.emit(str(accuracy))
	#Temporary Display

    def setAccuracy(self,name):
	self.lineEditName.setText(name)


    def refreshTrigger(self):
	self.fillData()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

