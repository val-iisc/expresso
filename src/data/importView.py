# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importView.ui'
#
# Created: Thu Mar 12 01:15:28 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from time import sleep
import numpy as np

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
#Imports begin
import sys
import os
root=os.getenv('EXPRESSO_ROOT')
#sys.path.append(root)
import DataHandler
import addNameView
from qtutils import inmain_later,inthread,inmain
from multiprocessing import Process
from signal import SIGTERM
import time
import importMultipleFoldersView
sys.path.append(root+'/src/augmentation')
import augmentationView
import subprocess

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

    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.root=root
        self.setupUi(self)
        ## Jaley Start

        ## Jaley end

    def setupUi(self, Form):
	#----Starts here-----
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 255)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(115, 115, 115)"))
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(380, 10, 211, 231))
        self.widget_2.setStyleSheet(_fromUtf8(";background-color:rgb(200, 200, 200)"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_4 = QtGui.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 71, 17))
        self.label_4.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButtonOk = QtGui.QPushButton(Form)
        self.pushButtonOk.setGeometry(QtCore.QRect(240, 120, 101, 27))
        self.pushButtonOk.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(200, 200, 200)"))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButton"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(192, 10, 161, 28))
        self.comboBox.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(200, 200, 200);selection-color:rgb(0,0,0);selection-background-color:rgba(255,255,255,100);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.lineEditData = QtGui.QLineEdit(Form)
        self.lineEditData.setGeometry(QtCore.QRect(130, 34, 211, 32))
        self.lineEditData.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(200, 200, 200)"))
        self.lineEditData.setObjectName(_fromUtf8("lineEditData"))
	self.lineEditData.hide()
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 15, 162, 22))
        self.label_3.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(200, 200, 200)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 54, 75, 22))
        self.label.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(200, 200, 200)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.widget1 = QtGui.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(327, 50, 28, 28))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEditFolderData = QtGui.QLabel(self.widget1)
        self.lineEditFolderData.setObjectName(_fromUtf8("lineEditFolderData"))
        self.lineEditFolderData.setStyleSheet(_fromUtf8("font: 11pt \"Ubuntu Condensed\";color:rgb(200, 200, 200)"))
        self.horizontalLayout.addWidget(self.lineEditFolderData)

        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setStyleSheet(_fromUtf8("background-color:rgb(200,200,200)"))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)

	self.toolButton.clicked.connect(self.onToolButtonClicked)


	#----Ends here ------
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        #self.pushButtonData.setText(_translate("Form", "Options", None))
        self.pushButtonOk.setText(_translate("Form", "Import", None))
        self.label_3.setText(_translate("Form", "Select the type of Data", None))
        self.label.setText(_translate("Form", "Load Data", None))
        self.lineEditFolderData.setText(_translate("Form",root, None))
	self.lineEditFolderData.hide()
        self.toolButton.setText(_translate("Form", "...", None))
	self.pushButtonOk.hide()


        self.pushButtonOk.clicked.connect(self.pushButtonOkClicked)
        self.comboBox.currentIndexChanged.connect(self.onIndexChange)
	self.comboBox.addItem("Text")
        self.comboBox.addItem("LevelDB")
        self.comboBox.addItem("Mat")
        self.comboBox.addItem("HDF5")
	self.comboBox.addItem("Folder")
        #self.comboBox.addItem("PKL")
        #self.comboBox.addItem("NPY")
	self.prevPath=self.root+"/data"
	self.isFolder=False
	self.signalCompleteTrigger.connect(self.testing)
	self.widget_2.setVisible(False)
	#Event filters for file dialog starts
	self.dialogHandle=QtGui.QFileDialog()
	self.addNewWidget=addNameView.Ui_Form()
	self.addNewWidget.setGeometry(QtCore.QRect(0,0,421,183))
        self.addNewWidget.installEventFilter(self)
	#self.addNewWidget.checkBoxAugmentation.hide() #March 16
	#Aumentation Widget Optional
	
	self.addAugmentationWidget=augmentationView.Ui_Form()
	self.addAugmentationWidget.setGeometry(100,100,291,255)
	self.addAugmentationWidget.signalRefreshTrigger.connect(self.signalRefreshTrigger.emit)

	#Event filters end
	#------Other Modalities
	self.addMagicFolderButton(Form)
	self.pushButtonMagicFolder.clicked.connect(self.magicFolderSlot)
	#------Other Modalities End

    def testing(self):
	print 'Hello'
    def onIndexChange(self,i):
        print i
	if(str(self.comboBox.currentText())=="Folder" or str(self.comboBox.currentText())=="LevelDB"):
	    self.isFolder=True
	else:
	    self.isFolder=False

    def eventFilter(self, source, event):
        import sys
	if event.type()==QtCore.QEvent.Close:
	    self.prevPath=str(self.lineEditFolderData.text())
	    if(self.addNewWidget.lineEdit.text().__str__()==""):return
	    if(self.lineEditFolderData.text().__str__()==""):return

	    self.lineEditData.setText(self.addNewWidget.lineEdit.text().__str__())
	    print self.addNewWidget.lineEdit.text().__str__() 
	    self.dimx=self.addNewWidget.spinBoxDimX.value()
	    self.dimy=self.addNewWidget.spinBoxDimY.value()
	    self.dimz=self.addNewWidget.spinBoxDimZ.value()
	    print self.addNewWidget.checkBoxAugmentation.isChecked() 
	    if(self.addNewWidget.checkBoxAugmentation.isChecked()):
		#Create LineList
		if(self.comboBox.currentText()=='Text'):
		    with open(self.lineEditFolderData.text().__str__()) as f:
			allLines=f.readlines()
			self.lineList=allLines[1:]
			staticArg=allLines[0]
			self.addAugmentationWidget.augmentationHandler.hasLabel=True;
			self.addAugmentationWidget.setParams(lineList=self.lineList,fileName=self.lineEditData.text().__str__(),dim=(self.dimz,self.dimx,self.dimy),staticArg=staticArg)
				
		if(self.comboBox.currentText()=="Folder"):
		    staticArg=self.lineEditFolderData.text().__str__()
		    if(staticArg==""):return
		    proc=subprocess.Popen('ls '+staticArg,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    		    out,err=proc.communicate()
		    strary=out.split('\n')
		    strary.remove('')
		    self.lineList=strary
		    self.addAugmentationWidget.augmentationHandler.hasLabel=False;
		    self.addAugmentationWidget.setParams(lineList=self.lineList,fileName=self.lineEditData.text().__str__(),dim=(self.dimz,self.dimx,self.dimy),staticArg=staticArg)
			

 

		#Create LineList Ends
		self.addAugmentationWidget.show()

		return
	    self.pushButtonOkClicked()
	    

        return QtGui.QWidget.eventFilter(self, source, event)

    def onToolButtonClicked(self):
	print 'Tool Button Clicked'
 	if self.isFolder==False:
            self.lineEditFolderData.setText(self.dialogHandle.getOpenFileName(self,self.tr("Open File"),str(self.prevPath)))

	if self.isFolder==True:
            self.lineEditFolderData.setText(self.dialogHandle.getExistingDirectory(self,self.tr("Open File"),str(self.prevPath)))    
            #self.widget.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 0)"))	
	#After Selection Starts
	if self.lineEditFolderData.text().__str__()=='':return
	self.addNewWidget.hideDim()
	if(self.comboBox.currentText()=='Folder' or self.comboBox.currentText()=='Text'):self.addNewWidget.showDim()
	self.addNewWidget.show()
	
	#After Selection Ends
	


    def pushButtonOkClicked(self):
        if self.lineEditData.text()=='' or self.lineEditFolderData.text()=='':
            QtGui.QMessageBox.about(self,'Incomplete Conversion','Data Left Out\nCheck Form again')
        #For TEXT option
        if(self.comboBox.currentText().__str__()=='Text' and str(self.lineEditData.text())!='' and self.lineEditFolderData.text()!=''):

            if(os.path.exists(self.lineEditFolderData.text())==0):
                QtGui.QMessageBox.about(self,'File Not Found',self.lineEditFolderData.text() +'\n Does not Exist')
                return
	    triggerList=self.createTriggerList()
	    inthread(self.runParallel,DataHandler.text2HDF5,str(self.lineEditData.text()), self.lineEditFolderData.text(),self.root+'/data',False,self.dimx,self.dimy,self.dimz,triggerList)#Parallel ThreadExecution

            return
        #Jaley End

        if(self.comboBox.currentText().__str__()=='Mat' and str(self.lineEditData.text())!='' and self.lineEditFolderData.text()!=''):
            if(os.path.exists(self.lineEditFolderData.text())==0):
                QtGui.QMessageBox.about(self,'File Not Found',self.lineEditFolderData.text()+'\n Does not Exist')
                return
	    
	    triggerList=self.createTriggerList()
	    inthread(self.runParallel,DataHandler.mat2HDF5,str(self.lineEditData.text()), str(self.lineEditFolderData.text()),self.root+'/data',True,None,None,None,triggerList)#Parallel ThreadExecution
	    #os.kill(p.pid(),SIGTERM)
            return

        if(self.comboBox.currentText().__str__()=='LevelDB' and str(self.lineEditData.text())!='' and self.lineEditFolderData.text()!=''):
            if(os.path.exists(self.lineEditFolderData.text())==0):

                QtGui.QMessageBox.about(self,'Folder Not Found',self.lineEditFolderData.text()+'/test_leveldb\n Does not Exist')
                return

	    triggerList=self.createTriggerList()
	    inthread(self.runParallel,DataHandler.leveldb2HDF5,str(self.lineEditData.text()), str(self.lineEditFolderData.text()),self.root+'/data',True,self.dimx,self.dimy,self.dimz,triggerList)#Parallel ThreadExecution



        if(str(self.comboBox.currentText())=='Folder' and str(self.lineEditData.text())!='' and self.lineEditFolderData.text()!=''):
            if(os.path.exists(self.lineEditFolderData.text())==0):
                QtGui.QMessageBox.about(self,'Folder Not Found',self.lineEditFolderData.text()+'\n Does not Exist')
                return

	    triggerList=self.createTriggerList()
	    inthread(self.runParallel,DataHandler.folder2HDF5,str(self.lineEditData.text()), self.lineEditFolderData.text().__str__(),self.root+'/data',True,self.dimx,self.dimy,self.dimz,triggerList)#Parallel ThreadExecution	    

	
        if(self.comboBox.currentText().__str__()=='HDF5' and str(self.lineEditData.text())!='' and self.lineEditFolderData.text()!=''):

            if(os.path.exists(self.lineEditFolderData.text())==0):
                QtGui.QMessageBox.about(self,'File Not Found',self.lineEditFolderData.text() +'\n Does not Exist')
                return
	    triggerList=self.createTriggerList()
	    inthread(self.runParallel,DataHandler.HDF52HDF5,str(self.lineEditData.text()), self.lineEditFolderData.text(),self.root+'/data',False,None,None,None,triggerList)#Parallel ThreadExecution

            return


	    return

			

 
    def runprogress(self):
	print self.progressBar.value()
	print str(self.progressBar.text())
	while(self.progressBar.value()<99):self.mydelay()
	self.progressBar.setValue(100)
        self.widget.setStyleSheet(_fromUtf8("background-color:rgb(0, 255, 0)"))
	mb=QtGui.QMessageBox.about(None,"Import Completed","Data has Sucessfully been Imported")
	#mb.setText('Process Completed')

    def mydelay(self):
	sleep(0.1)
	self.progressBar.setValue(self.progressBar.value()+5)

    def createTriggerList(self):
	triggerList=[]
	triggerList.append('Data View')
	triggerList.append('Importing Data')
	triggerList.append(self.lineEditData.text().__str__()+'_'+str(time.time()))
	triggerList.append(0)
	triggerList.append('Importing of Data has started for data '+self.lineEditData.text().__str__()+' from location '+self.lineEditFolderData.text().__str__())
	triggerList.append(0)
	return triggerList
    def startTrigger(self,triggerList):
	print triggerList
	self.signalStartedTrigger.emit(triggerList)
	return triggerList

    def endTrigger(self,triggerList):	
	triggerList[3]=1
	triggerList[4].replace('started','completed')
	triggerList[5]=100
	self.signalCompleteTrigger.emit(triggerList)
	self.signalRefreshTrigger.emit(triggerList[4])

    def runParallel(self,target,saveName,importLoc,saveLoc,hasLabel,dimx,dimy,dimz,triggerList):
		
        p=Process(target=target,args=(saveName,importLoc,saveLoc,hasLabel,dimx,dimy,dimz))
	inthread(self.sidethread,p,triggerList)	
	p.start()
	p.join()
	sleep(0.5)
	self.endTrigger(triggerList) #====>End
	return

    def sidethread(self,p,triggerList):
	triggerList=self.startTrigger(triggerList) #====>End
	while(p.is_alive()):
	    sleep(0.5)
	    triggerList[3]=2;
	    triggerList[5]=(triggerList[5]+1) if (triggerList[5]+1)<99 else 99  
	    self.startTrigger(triggerList)
	    #triggerList[4]=self.getAccuracyAndPrecision(p)

	    print 'is alive'
	    sleep(0.5)

#----------------Rest ----------------------------
    #Magic Tool
    def addMagicFolderButton(self,Form):
	self.pushButtonMagicFolder=QtGui.QPushButton(Form)
	self.pushButtonMagicFolder.setGeometry(QtCore.QRect(50,50,50,50))
	self.pushButtonMagicFolder.setText('Magic')
	self.addMagicFolderWidget=importMultipleFoldersView.Ui_Form()
	self.addMagicFolderWidget.setGeometry(QtCore.QRect(100,100,507,300))
	self.pushButtonMagicFolder.hide()

	pass
    def magicFolderSlot(self):
	self.addMagicFolderWidget.show()
	pass

    def runMagicFolderParallel(self):
	pass

    #User Defined Croping Function for Text,Magic Folder,Folder Flow


	


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

