# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trainSVMView.ui'
#
# Created: Wed Apr 15 00:53:25 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import sys
root=os.getenv('HOME')+'/ACM'
import h5py
import time
from time import sleep
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
# SVM LIBRARY STARTS
sys.path.append(root+'/tools/liblinear-1.96/python')
sys.path.append(root+'/tools/libsvm-3.20/python')

import liblinearutil
import svmutil
import numpy as np
# SVM LIBRARY ENDS
from qtutils import inthread
from multiprocessing import Process
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
    def __init__(self,parent=None):
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 591)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(120,180,120)"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 40, 161, 31))
        self.comboBox.setStyleSheet(_fromUtf8("background-color:rgb(210,240,210)"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 100, 551, 151))
        self.stackedWidget.setStyleSheet(_fromUtf8("background-color:rgb(175,225,175)"))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.label = QtGui.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 41))
        self.label.setStyleSheet(_fromUtf8("font: 22pt \"Ubuntu Condensed\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.widget = QtGui.QWidget(self.page)
        self.widget.setGeometry(QtCore.QRect(20, 70, 111, 41))
        self.widget.setStyleSheet(_fromUtf8("background-color:rgb(210,240,210)"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 14, 66, 17))
        self.label_2.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 8, 51, 27))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255)"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.label_3 = QtGui.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 141, 41))
        self.label_3.setStyleSheet(_fromUtf8("font: 22pt \"Ubuntu Condensed\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.widget_2 = QtGui.QWidget(self.page_2)
        self.widget_2.setGeometry(QtCore.QRect(20, 70, 111, 41))
        self.widget_2.setStyleSheet(_fromUtf8("background-color:rgb(210,240,210)"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_4 = QtGui.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(10, 14, 66, 17))
        self.label_4.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_2 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 8, 51, 27))
        self.lineEdit_2.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255)"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.widget_3 = QtGui.QWidget(self.page_2)
        self.widget_3.setGeometry(QtCore.QRect(280, 70, 211, 41))
        self.widget_3.setStyleSheet(_fromUtf8("background-color:rgb(210,240,210)"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.label_6 = QtGui.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(10, 14, 81, 17))
        self.label_6.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_4 = QtGui.QLineEdit(self.widget_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 8, 51, 27))
        self.lineEdit_4.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255)"))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.stackedWidget.addWidget(self.page_2)
        self.labelTraining = QtGui.QLabel(Form)
        self.labelTraining.setGeometry(QtCore.QRect(49, 339, 241, 17))
        self.labelTraining.setStyleSheet(_fromUtf8("font:italic 15pt  \"Ubuntu Condensed\";color:rgb(45,60,45)"))
        self.labelTraining.setObjectName(_fromUtf8("labelTraining"))
        self.comboBoxTraining = QtGui.QComboBox(Form)
        self.comboBoxTraining.setGeometry(QtCore.QRect(300, 291, 198, 31))
        self.comboBoxTraining.setStyleSheet(_fromUtf8("font: 18 pt \"Ubuntu Condensed\";color:rgb(45,60,45);background-color:rgb(210,225,210)"))
        self.comboBoxTraining.setObjectName(_fromUtf8("comboBoxTraining"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 290, 215, 33))
        self.label_7.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(210,225,210)"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.widget_4 = QtGui.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(20, 460, 551, 80))
        self.widget_4.setStyleSheet(_fromUtf8("background-color:rgb(175,225,175)"))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.widget_5 = QtGui.QWidget(self.widget_4)
        self.widget_5.setGeometry(QtCore.QRect(20, 20, 381, 41))
        self.widget_5.setStyleSheet(_fromUtf8("background-color:rgb(210,240,210)"))
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.label_8 = QtGui.QLabel(self.widget_5)
        self.label_8.setGeometry(QtCore.QRect(10, 14, 121, 17))
        self.label_8.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_5 = QtGui.QLineEdit(self.widget_5)
        self.lineEdit_5.setGeometry(QtCore.QRect(140, 8, 231, 27))
        self.lineEdit_5.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255)"))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.pushButton = QtGui.QPushButton(self.widget_4)
        self.pushButton.setGeometry(QtCore.QRect(420, 20, 98, 41))
        self.pushButton.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";background-color:rgb(120,180,120)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(260, 20, 281, 61))
        self.label_9.setStyleSheet(_fromUtf8("font: 30pt \"Ubuntu Condensed\";color:rgb(255,255,255)"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
	self.comboBox.addItems(['LIBLINEAR','LIBSVM'])
	
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Lib-linear", None))
        self.label_2.setText(_translate("Form", "C", None))
        self.label_3.setText(_translate("Form", "Lib-SVM", None))
        self.label_4.setText(_translate("Form", "C", None))
        self.label_6.setText(_translate("Form", "Gamma", None))
        self.labelTraining.setText(_translate("Form", "Dimentions are b x c x h x w", None))
        self.label_7.setText(_translate("Form", "Training Blob              ", None))
        self.label_8.setText(_translate("Form", "Model Name", None))
        self.pushButton.setText(_translate("Form", "Generate", None))
        self.label_9.setText(_translate("Form", "SVM Training", None))
	self.comboBox.currentIndexChanged.connect(self.onCurrentIndexChangedSlot)
	self.comboBoxTraining.currentIndexChanged.connect(self.trainingSlot)
	#self.trainingSlot(0)
	self.initiallize()
	self.pushButton.clicked.connect(self.onSubmitClickedSlot)

    def onCurrentIndexChangedSlot(self,index):
	self.stackedWidget.setCurrentIndex(index)

    def initiallize(self):
	self.comboBoxTraining.clear()
        for elem in os.listdir(root+'/data'):
            if(elem.endswith('.hdf5')):
                f=h5py.File(root+'/data/'+elem,'r')
                if 'label' in f.keys():self.comboBoxTraining.addItem(elem[0:-5])
                f.close()

    def trainingSlot(self,index):
	if(str(self.comboBoxTraining.currentText())==""):return
        f=h5py.File(root+'/data/'+str(self.comboBoxTraining.currentText())+'.hdf5','r')
        s=f['data'].shape
        self.labelTraining.setText("Dimentions are "+str(s[0])+' x '+str(s[1])+' x '+str(s[2])+' x '+str(s[3]))
        f.close()

    def onSubmitClickedSlot(self):
	choice=self.comboBox.currentIndex()
	name=str(self.lineEdit_5.text())
	dataName=str(self.comboBoxTraining.currentText());
	print name
	print 'Submit Clicked'
	paramstring=''
	cl=str(self.lineEdit.text())#C for liblinear
	cs=str(self.lineEdit_2.text()) # C for libSVM
	g=str(self.lineEdit_4.text()) # G for libSVM

	if(choice==0):
	    #Append Currently for LibLinear
	    if(cl==''):cl='4'
	    paramstring=paramstring+'-c '+cl
	    pass	
	elif(choice==1):
	    if(cs==''):cs='4'
	    if(g==''):g='0.5'
	    paramstring=paramstring+'-c '+cs
	    paramstring=paramstring+' -g '+g
	    #Append Currently for LibSVM
	    pass
        triggerList=self.createTriggerList(name)			
	inthread(self.runparallel,name,dataName,choice,paramstring,triggerList)

    def runparallel(self,name,dataName,choice,paramstring,triggerList):
        f=h5py.File(root+'/data/'+dataName+'.hdf5','r')
	#Conversion to SVM Format ### DATA OPS ###
        triggerList=self.startTrigger(triggerList) #====>End
	sleep(0.1)

	length=f['data'].shape[0]
	#length=50 ######!!!!!! REMOVE This line Later on!!!
	#for idx in range(f['data'].shape[0]):
	#Chunked appending to data
	batchSize=10
	os.mkdir(root+'/net/SVM/'+name)
	open(root+'/net/SVM/'+name+'/'+name,'w').write('')

	for batchIdx in range(0,length,batchSize):
	    trainx=[]
	    trainy=[]
	    for idx in range(batchSize):
		if(batchIdx+idx)>=length: #Write Remaining
		    self.appendData(name,trainx,trainy)
		    break;
		#If ends
	        row=np.array(f['data'][idx],dtype=np.float32).flatten().tolist()
	        row=dict(zip(range(1,len(row)+1),row))
	        trainx.append(row)
	        row=np.array(f['label'][idx],dtype=np.float32).flatten().tolist()[0]
	    #row=dict(zip(range(len(row)),row))
	        trainy.append(row)
	    self.appendData(name,trainx,trainy)

	#print 'train',trainx[:1]
	#print 'label',trainy[:1]
	

	if(choice==1): 	    	
	    #model=svmutil.svm_train(trainy,trainx,'-c 4')
	    with open(root+'/net/SVM/'+name+'/'+name+'.sh','w') as f:
		trainpath=root+'/net/SVM/'+name+'/'+name
		execpath=root+'/tools/libsvm-3.20'
	

		f.write(execpath+'/svm-scale -s scaling_parameters '+trainpath+' > '+trainpath+'_scaled\n')
		f.write(execpath+'/svm-train '+paramstring+' '+trainpath+'_scaled '+trainpath+'.model >'+trainpath+'_out\n')
		f.close()
	    #svmutil.svm_save_model(root+'/net/SVM/models/'+name+'_svm.model',model)
	elif(choice==0):
	    with open(root+'/net/SVM/'+name+'/'+name+'.sh','w') as f:
		trainpath=root+'/net/SVM/'+name+'/'+name
		execpath=root+'/tools/liblinear-1.96'
		execpathold=root+'/tools/libsvm-3.20'
	
		f.write(execpathold+'/svm-scale -s scaling_parameters '+trainpath+' > '+trainpath+'_scaled\n')
		f.write(execpath+'/train '+paramstring+' '+trainpath+'_scaled '+trainpath+'.model >'+trainpath+'_out\n')
		f.close()

	# Executing the Scripts and Displaying the results
	##########################################
	folderpath=root+'/net/SVM/'+name
	p=Process(target=self.callback,args=(name,folderpath))
	p.start()
	p.join()
	sleep(0.5)
	print open(folderpath+'/'+name+'_out').read() 

	triggerList[4]=open(folderpath+'/'+name+'_out').read()
        self.endTrigger(triggerList) #====>End
	##########################################
	    #Ends
	    #model=liblinearutil.train(trainy,trainx,'-c 4')
	    #liblinearutil.save_model(root+'/net/SVM/models/'+name+'_linear.model',model)
	
    def appendData(self,filename,trainx,trainy):
	#Appends to a file
	#print trainx,'TRAINX'
	#print trainy,'TRAINY' 
	writebuf='';
	for i in range(len(trainy)):
	    writebuf=writebuf+str(trainy[i])+' '+str(trainx[i]).replace(',','').replace(': ',':').replace('{','').replace('}','\n')

	open(root+'/net/SVM/'+filename+'/'+filename,'a').write(writebuf)
	
	pass

    def createTriggerList(self,name):
        triggerList=[]
        triggerList.append('Train View')
        triggerList.append('Training SVM Data')
        triggerList.append(name+'_'+str(time.time()))
        triggerList.append(0)
        triggerList.append('Training of Data has started with name '+name)
        triggerList.append(0)
        return triggerList

    def endTrigger(self,triggerList):
        triggerList[3]=1
        triggerList[4].replace('started','completed')
        triggerList[5]=100
        self.signalCompleteTrigger.emit(triggerList)


    def startTrigger(self,triggerList):
        print triggerList
        self.signalStartedTrigger.emit(triggerList)
        print '############## Start Emitted  ###########'
        return triggerList

    def callback(self,name,folderpath):
	#Call the subprocess accordingly
	print 'Work in progress'
        subprocess.call(['sh',folderpath+'/'+name+'.sh'])


    def refreshTrigger(self):
	self.initiallize()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

