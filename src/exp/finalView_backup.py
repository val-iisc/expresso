# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalView.ui'
#
# Created: Fri Mar 13 20:41:49 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#Imports begin
import sys
import os
root=os.getenv('HOME')+'/ACM'
#sys.path.append(root)
import sys
sys.path.append(os.getenv('HOME')+'/caffe/python/caffe/proto')
sys.path.append(os.getenv('HOME')+'/caffe/python')

from google.protobuf import text_format
import caffe_pb2
import os
import caffe
import numpy as np
sys.path.append(root+'/src/net/config')
import h5py
import netConfig_pb2




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
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.root=root
	self.index=0
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 591)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(120, 180, 120)"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 30, 311, 421))
        self.widget.setStyleSheet(_fromUtf8("background-color:rgb(150,195,150)"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 10, 271, 33))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(45, 60, 45)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidgetNetList = QtGui.QListWidget(self.widget)
        self.listWidgetNetList.setGeometry(QtCore.QRect(20, 50, 271, 351))
        self.listWidgetNetList.setStyleSheet(_fromUtf8("font: 12pt \"Ubuntu Condensed\";background-color:rgb(210, 230, 210);color:rgb(45,60,45)"))
        self.listWidgetNetList.setObjectName(_fromUtf8("listWidgetNetList"))
        self.widget_6 = QtGui.QWidget(Form)
        self.widget_6.setGeometry(QtCore.QRect(20, 490, 551, 71))
        self.widget_6.setStyleSheet(_fromUtf8("background-color:rgb(180,195,150)"))
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.pushButtonGenerate = QtGui.QPushButton(self.widget_6)
        self.pushButtonGenerate.setGeometry(QtCore.QRect(450, 30, 75, 32))
        self.pushButtonGenerate.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(225, 225, 210)"))
        self.pushButtonGenerate.setObjectName(_fromUtf8("pushButtonGenerate"))
        self.layoutWidget = QtGui.QWidget(self.widget_6)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 211, 34))
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
        self.lineEditName.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(150,150,90);color:rgb(225,225,180)"))
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.horizontalLayout_12.addWidget(self.lineEditName)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(340, 30, 241, 421))
        self.widget_2.setStyleSheet(_fromUtf8(";background-color:rgb(210, 225, 210)"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_4 = QtGui.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(10, 270, 71, 17))
        self.label_4.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.progressBar = QtGui.QProgressBar(self.widget_2)
        self.progressBar.setGeometry(QtCore.QRect(10, 130, 191, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.widget_3 = QtGui.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(60, 270, 18, 18))
        self.widget_3.setStyleSheet(_fromUtf8("background-color:rgb(255, 0, 0)"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.label_5 = QtGui.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(115, 290, 71, 21))
        self.label_5.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210);background-color:rgb(120, 180, 120)"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.widget_4 = QtGui.QWidget(self.widget_2)
        self.widget_4.setGeometry(QtCore.QRect(10, 310, 221, 101))
        self.widget_4.setStyleSheet(_fromUtf8("background-color:rgb(120, 180, 120)"))
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
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 271, 33))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(45, 60, 45)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.layoutWidget_9 = QtGui.QWidget(self.widget_2)
        self.layoutWidget_9.setGeometry(QtCore.QRect(10, 80, 191, 34))
        self.layoutWidget_9.setObjectName(_fromUtf8("layoutWidget_9"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_10.setMargin(0)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_17 = QtGui.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(45, 60, 45)"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_10.addWidget(self.label_17)
        self.comboBoxSelectModel = QtGui.QComboBox(self.layoutWidget_9)
        self.comboBoxSelectModel.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(90, 120, 90);color:rgb(210,225,210);"))
        self.comboBoxSelectModel.setObjectName(_fromUtf8("comboBoxSelectModel"))
        self.horizontalLayout_10.addWidget(self.comboBoxSelectModel)
        self.label_18 = QtGui.QLabel(self.widget_2)
        self.label_18.setGeometry(QtCore.QRect(10, 40, 92, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(45, 60, 45)"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.lineEditTestIteration = QtGui.QLineEdit(self.widget_2)
        self.lineEditTestIteration.setGeometry(QtCore.QRect(110, 40, 95, 32))
        self.lineEditTestIteration.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(90, 120, 90);color:rgb(210,225,210)"))
        self.lineEditTestIteration.setObjectName(_fromUtf8("lineEditTestIteration"))
        self.widget_7 = QtGui.QWidget(self.widget_2)
        self.widget_7.setGeometry(QtCore.QRect(10, 170, 221, 71))
        self.widget_7.setStyleSheet(_fromUtf8("background-color:rgb(120, 180, 120)"))
        self.widget_7.setObjectName(_fromUtf8("widget_7"))
        self.widget_8 = QtGui.QWidget(self.widget_7)
        self.widget_8.setGeometry(QtCore.QRect(160, 100, 191, 101))
        self.widget_8.setStyleSheet(_fromUtf8("background-color:rgb(120, 180, 120)"))
        self.widget_8.setObjectName(_fromUtf8("widget_8"))
        self.textEdit_4 = QtGui.QTextEdit(self.widget_8)
        self.textEdit_4.setGeometry(QtCore.QRect(10, 10, 171, 81))
        self.textEdit_4.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.widget_9 = QtGui.QWidget(self.widget_7)
        self.widget_9.setGeometry(QtCore.QRect(10, 10, 201, 51))
        self.widget_9.setStyleSheet(_fromUtf8("background-color:rgb(150, 195, 150)"))
        self.widget_9.setObjectName(_fromUtf8("widget_9"))
        self.widget_10 = QtGui.QWidget(self.widget_9)
        self.widget_10.setGeometry(QtCore.QRect(160, 100, 191, 101))
        self.widget_10.setStyleSheet(_fromUtf8("background-color:rgb(120, 180, 120)"))
        self.widget_10.setObjectName(_fromUtf8("widget_10"))
        self.textEdit_5 = QtGui.QTextEdit(self.widget_10)
        self.textEdit_5.setGeometry(QtCore.QRect(10, 10, 171, 81))
        self.textEdit_5.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.label_19 = QtGui.QLabel(self.widget_9)
        self.label_19.setGeometry(QtCore.QRect(10, 0, 201, 32))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(_fromUtf8("font: 12pt \"Ubuntu Condensed\";color:rgb(255, 225, 255)"))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.labelTimeRemaining = QtGui.QLabel(self.widget_9)
        self.labelTimeRemaining.setGeometry(QtCore.QRect(10, 30, 92, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelTimeRemaining.setFont(font)
        self.labelTimeRemaining.setStyleSheet(_fromUtf8("font: 12pt \"Ubuntu Condensed\";color:rgb(45,60 , 45)"))
        self.labelTimeRemaining.setObjectName(_fromUtf8("labelTimeRemaining"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Select Layers for Output", None))
        self.pushButtonGenerate.setText(_translate("Form", "Generate", None))
        self.label_11.setText(_translate("Form", "Name          ", None))
        self.lineEditName.setText(_translate("Form", "Untitled", None))
        self.label_4.setText(_translate("Form", "Status", None))
        self.label_5.setText(_translate("Form", "  Details", None))
        self.label_2.setText(_translate("Form", "Run Experiment", None))
        self.label_17.setText(_translate("Form", "Data", None))
        self.label_18.setText(_translate("Form", "BatchSize", None))
        self.lineEditTestIteration.setText(_translate("Form", "50", None))
        self.label_19.setText(_translate("Form", "Estimated Time Remaining", None))
        self.labelTimeRemaining.setText(_translate("Form", "10 minutes", None))
	self.listWidgetNetList.addItem('ItemAdded')
	self.fillList()
	self.pushButtonGenerate.clicked.connect(self.operate)

    def fillList(self):

	self.listWidgetNetList.addItem('Fault while loading')
        self.data=open(root+'/net/netData.prototxt').read()
        self.netHandler=netConfig_pb2.Param();
        self.protoHandler=caffe_pb2.NetParameter()
        text_format.Merge(self.data,self.netHandler)
        text_format.Merge(open(self.netHandler.net[self.index].protopath).read(),self.protoHandler)
	#Loading Net
	
	channel_swap=(2,1,0) if self.netHandler.net[self.index].channel_swap else None
        self.net=caffe.Classifier(str(self.netHandler.net[self.index].protopath),str(self.netHandler.net[self.index].modelpath),mean=np.load(str(self.netHandler.net[self.index].meanpath)),gpu=False,raw_scale=int(self.netHandler.net[self.index].raw_scale),channel_swap=channel_swap)
		

        self.listWidgetNetList.clear()
	#Loading Net Ends
        for elem in self.net.blobs.keys():
            item = QtGui.QListWidgetItem(elem)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidgetNetList.addItem(item)


	for fileName in os.listdir(root+'/data'):
	    if fileName.endswith('.hdf5'):self.comboBoxSelectModel.addItem(fileName[0:len(fileName)-5])

    def operate(self):
	# Load Data
	name=root+'/data/'+'Reddy4.hdf5'
	print name
	self.opData=h5py.File(name,'r')
	self.batchSize=int(self.lineEditTestIteration.text().__str__())
	print 'data shape : ',self.opData['data'].shape
	print 'batch size : ',self.batchSize
	self.batchSize=10;
	out=[]
	#data=self.net.preprocess('data',np.array(self.opData['data']))
	#print data.shape
	self.data={}
	
	if self.netHandler.net[self.index].channel_swap==True:self.data['data']=np.array(self.opData['data'])[:,[2,1,0],:,:]
	else:
	    self.data['data']=np.array(self.opData['data'])

	for i in range(self.data['data'].shape[0]//self.batchSize):
	    out[i*self.batchSize:(i+1)*self.batchSize]=self.net.forward_all(**{'data':self.data['data'][i*self.batchSize:(i+1)*self.batchSize]})['prob']
	print len(out)
	out[len(out):self.data['data'].shape[0]]=self.net.forward_all(**{'data':self.data['data'][len(out):self.data['data'].shape[0]]})['prob']
	

	print np.array(out).shape	
	print np.amax(np.array(out))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

