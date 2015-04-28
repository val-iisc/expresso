# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expView.ui'
#
# Created: Tue Apr  7 14:49:45 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import os
import sys
root=os.getenv('HOME')+'/ACM'
sys.path.append(root+'/src/net/config')
import netConfig_pb2
from google.protobuf import text_format
sys.path.append(os.getenv('HOME')+'/caffe/python/caffe/proto')
import caffe_pb2

sys.path.append(os.getenv('HOME')+'/caffe/python')
import caffe
import numpy as np
import h5py
import copy
import inspect
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
    signalCompleteTrigger=QtCore.pyqtSignal()

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
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(430, 460, 71, 21))
        self.label_5.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(230,240,210);background-color:rgb(120,120,75);"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.widget_4 = QtGui.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(330, 480, 221, 101))
        self.widget_4.setStyleSheet(_fromUtf8("background-color:rgb(120,120,75);"))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.textEdit = QtGui.QTextEdit(self.widget_4)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 201, 81))
        self.textEdit.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.widget_5 = QtGui.QWidget(self.widget_4)
        self.widget_5.setGeometry(QtCore.QRect(160, 100, 191, 101))
        self.widget_5.setStyleSheet(_fromUtf8("background-color:rgb(120, 180, 120)"))
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.textEdit_2 = QtGui.QTextEdit(self.widget_5)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 10, 171, 81))
        self.textEdit_2.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(340, 430, 71, 17))
        self.label_4.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
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
        self.widget_3 = QtGui.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(400, 430, 18, 18))
        self.widget_3.setStyleSheet(_fromUtf8("background-color:rgb(255, 0, 0)"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
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
        self.label_5.setText(_translate("Form", "  Details", None))
        self.label_4.setText(_translate("Form", "Status", None))
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
	    

    def onDataSelectionChangedSlot(self,index=0):
	datapath=root+'/data/'+self.comboBox.currentText().__str__()+'.hdf5'
	with h5py.File(datapath,'r') as f:
	    if 'data' not in f.keys():
		self.textEdit_3.setText('Invalid Blob')
		return
	    s=f['data'].shape
	    self.textEdit_3.setText('Dimensions are \n '+str(s[0])+' x '+str(s[1])+' x '+str(s[2])+' x '+str(s[3]))	


    def onNetSelectionChangedSlot(self,index=0):
	#Update the listWidget on change of the comboBox
	self.currentNet=netConfig_pb2.NetParam()
	for elem in self.netHandler.net:
		if elem.name==self.comboBox_2.currentText().__str__():
		    self.currentNet.CopyFrom(elem)
	####### NET CREATION ### CAFFE WRAPPER ###
	print self.currentNet
	channel_swap=(2,1,0) if self.currentNet.channel_swap else None
        self.net=caffe.Classifier(str(self.currentNet.protopath),str(self.currentNet.modelpath),mean=np.load(str(self.currentNet.meanpath)),gpu=False,raw_scale=int(self.currentNet.raw_scale),channel_swap=channel_swap)
	####### WRAPPING COMPLETE !!! ###########

	self.listWidget.clear()
        for elem in self.net.blobs.keys():
            item = QtGui.QListWidgetItem(elem)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)


    def updateNet(self):
        channel_swap=(2,1,0) if self.currentNet.channel_swap else None
	self.net=caffe.Classifier(str(self.currentNet.protopath),str(self.currentNet.modelpath),mean=np.load(str(self.currentNet.meanpath)),gpu=False,raw_scale=int(self.currentNet.raw_scale),channel_swap=channel_swap)

		
	pass


    def operate(self):
      # Load Data
        name=root+'/data/'+self.comboBox.currentText().__str__() +'.hdf5'
        print name
        self.opData=h5py.File(name,'r')
        self.batchSize=self.lineEdit.text().__str__()
	self.batchSize=int(self.batchSize) if self.batchSize!='' else 50

        print 'data shape : ',self.opData['data'].shape
        print 'batch size : ',self.batchSize
        self.batchSize=10;
        out=[]
        #data=self.net.preprocess('data',np.array(self.opData['data']))
        #print data.shape
        self.data={}

        if self.currentNet.channel_swap==True:self.data['data']=np.array(self.opData['data'])[:,[2,1,0],:,:]
        else:
            self.data['data']=np.array(self.opData['data'])

        for i in range(self.data['data'].shape[0]//self.batchSize):
            out[i*self.batchSize:(i+1)*self.batchSize]=self.net.forward_all(**{'data':self.data['data'][i*self.batchSize:(i+1)*self.batchSize]}).values()[0]
        print len(out)
        out[len(out):self.data['data'].shape[0]]=self.net.forward_all(**{'data':self.data['data'][len(out):self.data['data'].shape[0]]}).values()[0]

        print np.array(out).shape
        print np.amax(np.array(out))
        return out


    #Fills the restricted net into tempHandler
    def fillNet(self,layername):
        tick=False;
	index=0;
	paramDict=self.net.params.keys()
       	for idx,name in enumerate(paramDict):
	    if(tick==True):
		#del self.net.params[name]
		self.net.params.pop(name)

            if(layername==name):tick=True	   

	#self.net['outputs']=[layername]
	#xxxxxxxxxxxxxxxxxxxxxx	
	for elem in inspect.getmembers(self.net):
	    print elem
	#xxxxxxxxxxxxxxxxxxxxxx



    def findTicked(self):
        self.fileHandle=h5py.File(root+'/exp/data/'+self.lineEditName.text().__str__()+'.hdf5','w')

        for i in range(self.listWidget.count()):
            if self.listWidget.item(i).checkState()!=0:
                print self.listWidget.item(i).text()
                self.updateNet()
                self.fillNet(self.listWidget.item(i).text().__str__())
                #Change Net everytime
                data=self.operate()
                #Creating and storing in HDF5 file
                # Data=data, key=self.listWidget.item(i).text()
                # Name is self.lineEditName.text()
                comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
                self.fileHandle.create_dataset(self.listWidget.item(i).text().__str__(),data=data,**comp_kwargs)
        self.fileHandle.close()
        self.signalCompleteTrigger.emit()



    def onSubmitClickedSlot(self):
	#Finally Generating the results and storing it appropreately
 	pass
	self.findTicked()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

