# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importView.ui'
#
# Created: Thu Mar 12 01:15:28 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from time import sleep

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
        self.progressBar = QtGui.QProgressBar(self.widget_2)
        self.progressBar.setGeometry(QtCore.QRect(10, 20, 191, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
	self.progressBar.setStyleSheet(_fromUtf8("QProgressBar{\n"
"    border: 2px solid rgb(115,115,115);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color:rgb(115,115,115);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(116, 175, 211);\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}\n"
""))
        self.widget = QtGui.QWidget(self.widget_2)
        self.widget.setGeometry(QtCore.QRect(60, 90, 18, 18))
        self.widget.setStyleSheet(_fromUtf8("background-color:rgb(255, 0, 0);"\
"    border: 2px solid rgb(255,255,255);\n"
"    border-radius: 10px;\n"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_5 = QtGui.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(115, 100, 71, 21))
        self.label_5.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(200, 200, 200);background-color:rgb(115, 115, 115)"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.widget_3 = QtGui.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(10, 120, 191, 101))
        self.widget_3.setStyleSheet(_fromUtf8("background-color:rgb(115, 115, 115)"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.textEdit = QtGui.QTextEdit(self.widget_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 171, 81))
        self.textEdit.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButtonOk = QtGui.QPushButton(Form)
        self.pushButtonOk.setGeometry(QtCore.QRect(240, 120, 101, 27))
        self.pushButtonOk.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(200, 200, 200)"))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButton"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(192, 10, 161, 28))
        self.comboBox.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(200, 200, 200)"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.textEdit1 = QtGui.QTextEdit(Form)
        self.textEdit1.setGeometry(QtCore.QRect(60, 160, 281, 78))
        self.textEdit1.setStyleSheet(_fromUtf8("background-color:rgb(200,200,200)"))
        self.textEdit1.setObjectName(_fromUtf8("textEdit1"))
	self.textEdit1.setReadOnly(True)
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
	"""
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 255)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(120, 180, 120)"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 101, 91))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.lineEditFolderData = QtGui.QLabel(self.layoutWidget)
        self.lineEditFolderData.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.lineEditFolderData.setObjectName(_fromUtf8("lineEditFolderData"))
        self.verticalLayout_2.addWidget(self.lineEditFolderData)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.layoutWidget_2 = QtGui.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 130, 341, 34))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonData = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButtonData.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.pushButtonData.setObjectName(_fromUtf8("pushButtonData"))
        self.horizontalLayout.addWidget(self.pushButtonData)
        self.layoutWidget_3 = QtGui.QWidget(Form)
        self.layoutWidget_3.setGeometry(QtCore.QRect(140, 20, 224, 106))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEditData = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEditData.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.lineEditData.setObjectName(_fromUtf8("lineEditData"))
        self.verticalLayout.addWidget(self.lineEditData)
        self.lineEditData = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEditData.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.lineEditData.setObjectName(_fromUtf8("lineEditData"))
        self.verticalLayout.addWidget(self.lineEditData)
        self.comboBox = QtGui.QComboBox(self.layoutWidget_3)
        self.comboBox.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210);color:rgb(45,60,45);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout.addWidget(self.comboBox)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(380, 10, 211, 231))
        self.widget_2.setStyleSheet(_fromUtf8(";background-color:rgb(210, 225, 210)"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_4 = QtGui.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 71, 17))
        self.label_4.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.progressBar = QtGui.QProgressBar(self.widget_2)
        self.progressBar.setGeometry(QtCore.QRect(10, 20, 191, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.widget = QtGui.QWidget(self.widget_2)
        self.widget.setGeometry(QtCore.QRect(60, 90, 18, 18))
        self.widget.setStyleSheet(_fromUtf8("background-color:rgb(255,0, 0)"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_5 = QtGui.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(115, 100, 71, 21))
        self.label_5.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210);background-color:rgb(120, 180, 120)"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.widget_3 = QtGui.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(10, 120, 191, 101))
        self.widget_3.setStyleSheet(_fromUtf8("background-color:rgb(120, 180, 120)"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.textEdit = QtGui.QTextEdit(self.widget_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 171, 81))
        self.textEdit.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButtonOk = QtGui.QPushButton(Form)
        self.pushButtonOk.setGeometry(QtCore.QRect(260, 180, 98, 27))
        self.pushButtonOk.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButton"))

	
        #Added by Jaley start
        self.checkbox = QtGui.QCheckBox(Form);
        self.checkbox.setGeometry(QtCore.QRect(21, 186, 100, 15))
        self.checkbox.setObjectName(_fromUtf8("checkbox"))
        self.checkbox.setText('Has Label')
        #Added by Jaley Ends
	"""

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        #self.pushButtonData.setText(_translate("Form", "Options", None))
       	self.label_4.setText(_translate("Form", "Status", None))
        self.label_5.setText(_translate("Form", "  Details", None))
        self.pushButtonOk.setText(_translate("Form", "Import", None))
	self.textEdit1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can import data in<span style=\" font-weight:600;\"> format</span> specified in combobox.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Data will  be stored internally, as specified in <span style=\" font-weight:600;\">name</span> text field.</p></body></html>", None))
	self.textEdit1.setVisible(False)
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

	#Event filters end

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
	    self.pushButtonOkClicked()
	    

        return QtGui.QWidget.eventFilter(self, source, event)

    def onToolButtonClicked(self):
	print 'Tool Button Clicked'
 	if self.isFolder==False:
            self.lineEditFolderData.setText(self.dialogHandle.getOpenFileName(self,self.tr("Open File"),str(self.prevPath)))

	if self.isFolder==True:
            self.lineEditFolderData.setText(self.dialogHandle.getExistingDirectory(self,self.tr("Open File"),str(self.prevPath)))    
            self.widget.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 0)"))	
	#After Selection Starts
	
	self.addNewWidget.show()
	
	#After Selection Ends
	


    def pushButtonOkClicked(self):
        if self.lineEditData.text()=='' or self.lineEditFolderData.text()=='':
            QtGui.QMessageBox.about(self,'Incomplete Conversion','Data Left Out\nCheck Form again')
        #For TEXT option
        if(self.comboBox.currentIndex()==0 and str(self.lineEditData.text())!='' and self.lineEditFolderData.text()!=''):

            if(os.path.exists(self.lineEditFolderData.text())==0):
                QtGui.QMessageBox.about(self,'File Not Found',self.lineEditFolderData.text() +'\n Does not Exist')
                return
	    triggerList=self.createTriggerList()
	    inthread(self.runParallel,DataHandler.text2HDF5,str(self.lineEditData.text()), self.lineEditFolderData.text(),self.root+'/data',True,triggerList)#Parallel ThreadExecution

            return
        #Jaley End

        if(self.comboBox.currentIndex()==2 and str(self.lineEditData.text())!='' and self.lineEditFolderData.text()!=''):
            if(os.path.exists(self.lineEditFolderData.text())==0):
                QtGui.QMessageBox.about(self,'File Not Found',self.lineEditFolderData.text()+'\n Does not Exist')
                return
	    
	    triggerList=self.createTriggerList()
	    inthread(self.runParallel,DataHandler.mat2HDF5,str(self.lineEditData.text()), self.lineEditFolderData.text(),self.root+'/data',True,triggerList)#Parallel ThreadExecution
	    #os.kill(p.pid(),SIGTERM)
            return

        if(self.comboBox.currentIndex()==1 and str(self.lineEditData.text())!='' and self.lineEditFolderData.text()!=''):
            if(os.path.exists(self.lineEditFolderData.text())==0):

                QtGui.QMessageBox.about(self,'Folder Not Found',self.lineEditFolderData.text()+'/test_leveldb\n Does not Exist')
                return

	    triggerList=self.createTriggerList()
	    inthread(self.runParallel,DataHandler.leveldb2HDF5,str(self.lineEditData.text()), self.lineEditFolderData.text(),self.root+'/data',True,triggerList)#Parallel ThreadExecution



        if(str(self.comboBox.currentText())=='Folder' and str(self.lineEditData.text())!='' and self.lineEditFolderData.text()!=''):
            if(os.path.exists(self.lineEditFolderData.text())==0):
                QtGui.QMessageBox.about(self,'Folder Not Found',self.lineEditFolderData.text()+'\n Does not Exist')
                return

	    triggerList=self.createTriggerList()
	    inthread(self.runParallel,DataHandler.folder2HDF5,str(self.lineEditData.text()), self.lineEditFolderData.text().__str__(),self.root+'/data',True,triggerList)#Parallel ThreadExecution	    

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

    def runParallel(self,target,saveName,importLoc,saveLoc,hasLabel,triggerList):
		
        p=Process(target=target,args=(saveName,importLoc,saveLoc,hasLabel))
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
	    triggerList[5]=(triggerList[5]+3)%100
	    self.startTrigger(triggerList)
	    #triggerList[4]=self.getAccuracyAndPrecision(p)

	    print 'is alive'
	    sleep(0.5)
    """
    def getAccuracyAndPrecision(self,p):
	import socket
	hostname=str(socket.gethostname())
	import getpass
	username=str(getpass.getuser())
	foldername='/tmp'
 	locationprefix=foldername+'/'+hostname+'.'+username+'.log.INFO.'
	processid=str(p.pid)

	filename=''
	print '#############'
	print 'PID', processid
	print 'prefix',locationprefix
	print '#############'

	for files in os.listdir(foldername):
	    if files.startwith(locationprefix) and files.endwith(processid):
		print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
	        print files
		print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
		filename=files
		break;
	
	if(filename!=''):
	    lines=open(foldername+'/'+filename,'r').readlines()
	    print lines[-3:-1]
	    return ' '.join(lines[-3:-1])
	return ''
        """

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

