# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configViewNew.ui'
#
# Created: Sun Apr  5 23:19:11 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import configViewItem
from PyQt4 import QtCore, QtGui

import os
import sys
root=os.getenv('EXPRESSO_ROOT')
sys.path.append(root+'/src/custom')
import netWidget
import configViewItem
import otherParametersView
sys.path.append(os.getenv('CAFFE_ROOT')+'/python/caffe/proto')
import caffe_pb2
sys.path.append(root+'/src/net/config')
import netConfig_pb2
from google.protobuf import text_format
import shutil

sys.path.append(root+'/src/custom')
import solverView


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
    signalRefreshTrigger=QtCore.pyqtSignal(object)

    def __init__(self,parent=None,index=None):	
        self.index=index
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form,index=None):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 591)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(50, 165, 211)"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 1, 611, 551))
        self.tabWidget.setStyleSheet(_fromUtf8("background-color:rgb(49, 74, 93);\n"
"font: 14pt \"Ubuntu Condensed\";"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        #self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
	#Commented Temporarily ***
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))

        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(210, 560, 162, 27))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255);\n"
"font: 14pt \"Ubuntu Condensed\";"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 567, 186, 17))
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
	self.label.setStyleSheet("color:rgb(255,255,255);background-color:rgb(49,74,93);font: 15pt \"Ubuntu Condensed\";")
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(490, 558, 98, 27))
        self.pushButton.setStyleSheet(_fromUtf8("color:rgb(255, 255, 255);\n"
"color:rgb(255,255,255)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Train Net", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Deploy Net", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Solver Configuration(Optional)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Other", None))
        self.label.setText(_translate("Form", "Save net configuration as", None))
        self.pushButton.setText(_translate("Form", "Save", None))
	self.netHandle=netConfig_pb2.Param()
        text_format.Merge(open(root+'/net/netData.prototxt').read(),self.netHandle)
	self.lineEdit.setText("Untitled")
	self.addTabs()
	self.onIndexChanged(self.index)
	self.pushButton.clicked.connect(self.onSubmitClicked)

	self.page0Widget.toolButton_5.clicked.connect(self.copyFromDeploySlot)
	self.page1Widget.toolButton_5.clicked.connect(self.copyFromTrainSlot)

    def addTabs(self):
        self.page0Widget=configViewItem.Ui_Form(parent=self.tab,trainMode=True,index=self.index)
        self.page0Widget.setGeometry(0,0,611,591)
	self.page0Widget.label_2.setText('Train Net')
        self.page1Widget=configViewItem.Ui_Form(parent=self.tab_2,trainMode=False,index=self.index)
        self.page1Widget.setGeometry(0,0,611,591)
        self.page2Widget=solverView.Ui_Form(parent=self.tab_3)
        self.page2Widget.setGeometry(0,0,611,491)

	self.page2Widget.widget.setStyleSheet('background-color:rgb(49, 74, 93)')
	self.page2Widget.widget_2.setStyleSheet('background-color:rgb(49, 74, 93)')
	self.page2Widget.widget_3.setStyleSheet('background-color:rgb(50, 165, 211)')
	self.page2Widget.widget_4.setStyleSheet('background-color:rgb(50, 165, 211)')

        self.page3Widget=otherParametersView.Ui_Form(parent=self.tab_4)
        self.page3Widget.setGeometry(0,0,611,491)


    def onIndexChanged(self,index):
	#Page 0 Changes
	self.page0Widget.index=index
	if(index!=None):
	    self.page0Widget.widget.show()
	else:
	    self.page0Widget.widget.hide()
	self.page0Widget.changeNet()
	#PAGE 1 Changes
	self.page1Widget.index=index
	if(index!=None):
	    self.page1Widget.widget.show()
	else:
	    self.page1Widget.widget.hide()

	self.page1Widget.changeNet()
	#Page 1 Changes End
	if(index!=None):
	    self.lineEdit.setText(self.netHandle.net[index].name)
	else:
	    self.lineEdit.setText('Untitled')
	self.page3Widget.index=index
	self.page3Widget.setFields()

    def onNewConfigClickedSlot(self):
	self.page0Widget.widget.hide()
	self.page0Widget.index=None;
	self.page0Widget.changeNet()
	self.page1Widget.widget.hide()
	self.page1Widget.index=None;
	self.page1Widget.changeNet()
	self.lineEdit.setText('Untitled')
	self.page3Widget.index=None
	self.page3Widget.setFields()

    def onSubmitClicked(self):
        self.netHandle=netConfig_pb2.Param();
        self.data=open(root+'/net/netData.prototxt').read()
        text_format.Merge(self.data,self.netHandle)   

	print 'Net is now saving its configuration'
	ch=None
	for item in self.netHandle.net:
	    if(item.name==self.lineEdit.text().__str__().upper()):ch=item
	#ch=self.netHandle.net[index] #Current Handle of the net
	#Step 1 : Create Folder with all the configurations and save it
	savefolder=root+'/net/data/'+self.lineEdit.text().__str__().lower()
	
	if os.path.exists(savefolder):
	    reply = QtGui.QMessageBox.question(self, 'Message',\
            "Are you sure to override existing?", QtGui.QMessageBox.Yes | \
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
	    found=False
	    for idx,elem in enumerate(self.netHandle.net):
		if elem.name==self.lineEdit.text().__str__().upper():
		    ch=self.netHandle.net[idx]
		    found=True
	    if(found==False):
	        ch=self.netHandle.net.add()
	        ch.name=self.lineEdit.text().__str__().upper()
	    if(reply==QtGui.QMessageBox.No): return;
	else:
	    os.mkdir(savefolder)
	    ch=self.netHandle.net.add()
	    ch.name=self.lineEdit.text().__str__().upper()

	#Step 1.1 : Saving Train Net
	extension=self.lineEdit.text().__str__().lower()+'_train.prototxt'
	if os.path.exists(savefolder+'/'+extension):
	    reply = QtGui.QMessageBox.question(self, 'Message',\
            "Are you sure to override existing Train File?", QtGui.QMessageBox.Yes | \
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
	    if(reply==QtGui.QMessageBox.Yes): 
		open(savefolder+'/'+extension,'w').write(self.page0Widget.subWidget.textEdit.toPlainText().__str__())
		ch.trainpath=savefolder+'/'+extension
	else:
	    open(savefolder+'/'+extension,'w').write(self.page0Widget.subWidget.textEdit.toPlainText().__str__())
	    ch.trainpath=savefolder+'/'+extension
	    ch.tdim0=self.page0Widget.subWidget.dim[0]
	    ch.tdim1=self.page0Widget.subWidget.dim[1]
	    ch.tdim2=self.page0Widget.subWidget.dim[2]
	    ch.tdim3=self.page0Widget.subWidget.dim[3]

		
	   	
	#Step 1.2 : Saving Deploy Net
	extension=self.lineEdit.text().__str__().lower()+'_deploy.prototxt'
	if os.path.exists(savefolder+'/'+extension):
	    reply = QtGui.QMessageBox.question(self, 'Message',\
            "Are you sure to override existing Deploy File?", QtGui.QMessageBox.Yes | \
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
	    if(reply==QtGui.QMessageBox.Yes): 
		open(savefolder+'/'+extension,'w').write(self.page1Widget.subWidget.textEdit.toPlainText().__str__())
		ch.protopath=savefolder+'/'+extension

	else:
	    open(savefolder+'/'+extension,'w').write(self.page1Widget.subWidget.textEdit.toPlainText().__str__())
	    ch.protopath=savefolder+'/'+extension

	#Step 1.3 Saving Model File
	extension=self.lineEdit.text().__str__().lower()+'_model.caffemodel'
	modelpath=self.page3Widget.lineEditModelPath.text().__str__()
	if(modelpath!='' and modelpath.endswith('.caffemodel')):
		#Copy Model Path
	    if os.path.exists(savefolder+'/'+extension):
	        reply = QtGui.QMessageBox.question(self, 'Message',\
                "Are you sure to override existing Model File?", QtGui.QMessageBox.Yes | \
                QtGui.QMessageBox.No, QtGui.QMessageBox.No)
	        if(reply==QtGui.QMessageBox.Yes and modelpath!=savefolder+'/'+extension): 
		    shutil.copy(modelpath,savefolder+'/'+extension)	
		    ch.modelpath=savefolder+'/'+extension

	    else:
	        if(modelpath!=savefolder+'/'+extension):shutil.copy(modelpath,savefolder+'/'+extension)	
		ch.modelpath=savefolder+'/'+extension
			
	
	else:
	    QtGui.QMessageBox.critical(self, 'Warning',\
            "Model File is MUST for both training and Deploy.Please include Path")

	#Other Parameters Assignment and copying
	#Other 1
	ch.has_mean=self.page3Widget.checkBoxHasMean.isChecked() and self.page3Widget.lineEditMeanPath.text().__str__()!=''

	if(self.page3Widget.lineEditMeanPath.text().__str__()!=''): ch.meanpath=self.page3Widget.lineEditMeanPath.text().__str__()
	
	if(self.page3Widget.lineEditRawScale.text().__str__()!=''):ch.raw_scale=int(self.page3Widget.lineEditRawScale.text().__str__())
	ch.gpu=self.page3Widget.checkBoxUseGPU.isChecked()
	ch.gpu_index=int(self.page3Widget.lineEditGPUIndex.text().__str__())
	ch.channel_swap=self.page3Widget.checkBoxChannelSwap.isChecked()
	print ch

	#Solver Parameters for saving . . . 
	extension=self.lineEdit.text().__str__().lower()+'_solver.prototxt'
	with open(savefolder+'/'+extension,'w') as f:
	    print self.page2Widget.protoHandler
	    self.page2Widget.updateHandle()
            self.page2Widget.protoHandler.net=(savefolder+'/'+self.lineEdit.text().__str__().lower()+'_train.prototxt')
	    self.page2Widget.protoHandler.snapshot_prefix=savefolder
	    self.page2Widget.protoHandler.solver_mode=self.page3Widget.checkBoxUseGPU.isChecked()
	    
            f.write(self.page2Widget.protoHandler.__str__())
	    ch.solverpath=savefolder+'/'+extension


	    

	#self.lineEdit.text().__str__().lower()+
	#Other Ends
	open(root+'/net/netData.prototxt','w').write(self.netHandle.__str__())
	self.signalCompleteTrigger.emit(self.lineEdit.text().__str__().upper())
	self.signalRefreshTrigger.emit("Net("+self.lineEdit.text().__str__().upper()+") is bieng saved")




	
		
	
	#Step 2 : Update Paths in the netData
	#Step 3 : Refresh The display

    def copyFromDeploySlot(self):
	del self.page0Widget.subWidget.protohandler.layers[2];
	trainLen=len(self.page0Widget.subWidget.protohandler.layers)
	for idx in range(trainLen-2):
	    del self.page0Widget.subWidget.protohandler.layers[2]
	self.page0Widget.subWidget.protohandler.MergeFrom(self.page1Widget.subWidget.protohandler)

	
	#for layer in self.page0Widget.subWidget.protohandler.layers:
	    #del layer
		#if layer.type!=	None or layer.type not in [32,5,9,29,24,12]:del layer

	self.page0Widget.subWidget.textEdit.setText(self.page0Widget.subWidget.protohandler.__str__())
	self.page0Widget.subWidget.loadTreeWidget()


    def copyFromTrainSlot(self):
	deployLen=len(self.page1Widget.subWidget.protohandler.layers)
	for idx in range(deployLen):
	    del self.page1Widget.subWidget.protohandler.layers[0]
	self.page1Widget.subWidget.protohandler.MergeFrom(self.page0Widget.subWidget.protohandler)
	del self.page1Widget.subWidget.protohandler.layers[-1]
	del self.page1Widget.subWidget.protohandler.layers[-1]
	del self.page1Widget.subWidget.protohandler.layers[0]
	del self.page1Widget.subWidget.protohandler.layers[0]

	self.page1Widget.subWidget.textEdit.setText(self.page1Widget.subWidget.protohandler.__str__())
	self.page1Widget.subWidget.loadTreeWidget()

    def refreshTrigger(self,extra=None):
	self.netHandle=netConfig_pb2.Param()
        text_format.Merge(open(root+'/net/netData.prototxt').read(),self.netHandle)


	

	

if __name__== "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

