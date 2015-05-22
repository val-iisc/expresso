# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testSVMView.ui'
#
# Created: Thu Apr 16 01:21:09 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import os
import sys
root=os.getenv('EXPRESSO_ROOT')
import h5py
from qtutils import inthread
import time
from time import sleep
import numpy as np
# SVM LIBRARY STARTS
sys.path.append(root+'/tools/liblinear-1.96/python')
sys.path.append(root+'/tools/libsvm-3.20/python')

#import svmutil
from multiprocessing import Process
import subprocess

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
    signalUpdateTrigger=QtCore.pyqtSignal(object)
    signalCompleteTrigger=QtCore.pyqtSignal(object)
    signalStartedTrigger=QtCore.pyqtSignal(object)
    def __init__(self,parent=None):
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 591)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(150,150,90)"))
        self.labelTraining = QtGui.QLabel(Form)
        self.labelTraining.setGeometry(QtCore.QRect(49, 159, 241, 17))
        self.labelTraining.setStyleSheet(_fromUtf8("font:italic 15pt  \"Ubuntu Condensed\";color:rgb(60,60,45);selection-color:rgb(0,0,0);selection-background-color:rgba(255,255,255,100);"))
        self.labelTraining.setObjectName(_fromUtf8("labelTraining"))
        self.comboBoxTesting = QtGui.QComboBox(Form)
        self.comboBoxTesting.setGeometry(QtCore.QRect(300, 111, 198, 31))
        self.comboBoxTesting.setStyleSheet(_fromUtf8("font: 18 pt \"Ubuntu Condensed\";color:rgb(60,60,45);background-color:rgba(255,255,255,175);selection-color:rgb(0,0,0);selection-background-color:rgba(255,255,255,100);"))
        self.comboBoxTesting.setObjectName(_fromUtf8("comboBoxTesting"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(50, 110, 215, 33))
        self.label_7.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(255,255,225)"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.widget_4 = QtGui.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(20, 210, 551, 80))
        self.widget_4.setStyleSheet(_fromUtf8("background-color:rgba(255,255,255,100);"))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.widget_5 = QtGui.QWidget(self.widget_4)
        self.widget_5.setGeometry(QtCore.QRect(20, 20, 381, 41))
        self.widget_5.setStyleSheet(_fromUtf8("background-color:rgba(255,255,255,100)"))
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.label_8 = QtGui.QLabel(self.widget_5)
        self.label_8.setGeometry(QtCore.QRect(10, 14, 121, 17))
        self.label_8.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.comboBox = QtGui.QComboBox(self.widget_5)
        self.comboBox.setGeometry(QtCore.QRect(150, 5, 221, 31))
        self.comboBox.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255);selection-color:rgb(0,0,0);selection-background-color:rgba(255,255,255,100);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.pushButton = QtGui.QPushButton(self.widget_4)
        self.pushButton.setGeometry(QtCore.QRect(420, 20, 98, 41))
        self.pushButton.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";background-color:rgb(150,150,90)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(260, 20, 281, 61))
        self.label_9.setStyleSheet(_fromUtf8("font: 30pt \"Ubuntu Condensed\";color:rgb(255,255,255)"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 320, 551, 78))
        self.textEdit.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.labelTraining.setText(_translate("Form", "Dimentions are b x c x h x w", None))
	self.labelTraining.hide()
        self.label_7.setText(_translate("Form", "Testing Blob              ", None))
        self.label_8.setText(_translate("Form", "Model Name", None))
        self.pushButton.setText(_translate("Form", "Evaluate", None))
        self.label_9.setText(_translate("Form", "SVM Testing", None))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu Condensed\'; font-size:15pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:14pt;\">Model Dimensions :10,000 x200</span></p></body></html>", None))
	self.textEdit.hide()
	self.initiallize()
	#Added on 15th May
	self.labelName=QtGui.QLabel(Form)
        self.labelName.setGeometry(QtCore.QRect(40, 420, 90, 34))
        self.labelName.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";color:rgb(230,240,210);"))
	self.labelName.setText('Accuracy')
        self.lineEditName = QtGui.QLineEdit(Form)
        self.lineEditName.setGeometry(QtCore.QRect(135, 420, 180, 34))
        self.lineEditName.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(230,240,210);color:rgb(120,120,75);"))
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
	self.lineEditName.setReadOnly(True)
	self.signalUpdateTrigger.connect(self.lineEditName.setText)
	#End of 15th May
	self.pushButton.clicked.connect(self.onSubmitClickedSlot)

    def initiallize(self):
	self.comboBox.clear()
	self.comboBoxTesting.clear()
	print 'Filling the comboBox for Models'
	for elem in os.listdir(root+'/net/SVM'):
	    if os.path.isdir(root+'/net/SVM/'+elem) and os.path.exists(root+'/net/SVM/'+elem+'/'+elem):
		print elem
		self.comboBox.addItem(elem)
	# Filling the data inside the ComboBox 
        for elem in os.listdir(root+'/data'):
            if(elem.endswith('.hdf5')):
                with h5py.File(root+'/data/'+elem,'r') as f:
                    if 'label' in f.keys():self.comboBoxTesting.addItem(elem[0:-5])
              

    def onSubmitClickedSlot(self):
	modelName=self.comboBox.currentText().__str__()
	dataName=self.comboBoxTesting.currentText().__str__()
	option=False#False implies Liblinear else LibSVM
	if('liblinear' not in open(root+'/net/SVM/'+modelName+'/'+modelName+'.sh').read()):option=True
	triggerList=self.createTriggerList(modelName)
	inthread(self.runparallel,modelName,dataName,option,triggerList)


    def runparallel(self,modelName,dataName,option,triggerList):
	print 'run parallel'
	f=h5py.File(root+'/data/'+dataName+'.hdf5','r')
        #Conversion to SVM Format ### DATA OPS ###
        triggerList=self.startTrigger(triggerList) #====>End
        sleep(0.1)

        length=f['data'].shape[0]
        #length=50 ######!!!!!! REMOVE This line Later on!!!
        #for idx in range(f['data'].shape[0]):
        #Chunked appending to data
        batchSize=10
        if(not os.path.exists(root+'/net/SVM/'+modelName)):os.mkdir(root+'/net/SVM/'+modelName)
        if(not os.path.exists(root+'/net/SVM/'+modelName+'/test')):os.mkdir(root+'/net/SVM/'+modelName+'/test')
        open(root+'/net/SVM/'+modelName+'/test/'+dataName,'w').write('')

        for batchIdx in range(0,length,batchSize):
            testx=[]
            testy=[]
            for idx in range(batchSize):
                if(batchIdx+idx)>=length: #Write Remaining
                    self.appendData(modelName,dataName,testx,testy)
                    break;
                #If ends
                row=np.array(f['data'][batchIdx+idx],dtype=np.float32).flatten().tolist()
                row=dict(zip(range(1,len(row)+1),row))
                testx.append(row)
                row=np.array(f['label'][batchIdx+idx],dtype=np.float32).flatten().tolist()[0]
            #row=dict(zip(range(len(row)),row))
                testy.append(row)
            self.appendData(modelName,dataName,testx,testy)

	########### Writing to Script
        if(option==True):
            #model=svmutil.svm_train(trainy,trainx,'-c 4')
            with open(root+'/net/SVM/'+modelName+'/test/'+dataName+'.sh','w') as f:
                testpath=root+'/net/SVM/'+modelName+'/test/'+dataName
		modelpath=root+'/net/SVM/'+modelName

                execpath=root+'/tools/libsvm-3.20'

		# svm-scale -r scaling-param-file-created-during-training test-features-file > scaled-test-features-file
		# predict -c C test-features-file trainining-model predicted-file

                f.write(execpath+'/svm-scale -r '+modelpath+'.range '+testpath+' > '+testpath+'_scaled\n')
                f.write(execpath+'/svm-predict '+testpath+'_scaled '+modelpath+'.model '+testpath+'.predict >'+testpath+'_out\n')
		#print open(testpath+'_out').read()
                f.close()
            #svmutil.svm_save_model(root+'/net/SVM/models/'+name+'_svm.model',model)
        elif(option==False):
            with open(root+'/net/SVM/'+modelName+'/test/'+dataName+'.sh','w') as f:
                testpath=root+'/net/SVM/'+modelName+'/test/'+dataName
		modelpath=root+'/net/SVM/'+modelName+'/'+modelName
                execpath=root+'/tools/liblinear-1.96'
                execpathold=root+'/tools/libsvm-3.20'

                f.write(execpathold+'/svm-scale -r '+modelpath+'.range '+testpath+' > '+testpath+'_scaled\n')
                f.write(execpath+'/predict '+testpath+'_scaled '+modelpath+'.model '+testpath+'.predict >'+testpath+'_out\n')
		#print open(testpath+'_out').read()
                f.close()
      

        # Executing the Scripts and Displaying the results
        ##########################################
        folderpath=root+'/net/SVM/'+modelName
        p=Process(target=self.callback,args=(dataName,folderpath))
        p.start()
        p.join()
        sleep(0.5)
        accuracyVal=open(folderpath+'/test/'+dataName+'_out').read()
	accuracyVal=accuracyVal.split('Accuracy = ')[-1]
	self.signalUpdateTrigger.emit(accuracyVal)
        triggerList[4]=open(folderpath+'/test/'+dataName+'_out').read()
        self.endTrigger(triggerList) #====>End
        ##########################################

	




    def appendData(self,filename,dataName,trainx,trainy):
        #Appends to a file
        #print trainx,'TRAINX'
        #print trainy,'TRAINY' 
        writebuf='';
        for i in range(len(trainy)):
            writebuf=writebuf+str(int(trainy[i]))+' '+str(trainx[i]).replace(',','').replace(': ',':').replace('{','').replace('}','\n')

        open(root+'/net/SVM/'+filename+'/test/'+dataName,'a').write(writebuf)


        pass
    def callback(self,dataName,folderpath):
        #Call the subprocess accordingly
        print 'Work in progress'
        subprocess.call(['sh',folderpath+'/test/'+dataName+'.sh'])


    def refreshTrigger(self):
	self.initiallize()
	
    def createTriggerList(self,name):
        triggerList=[]
        triggerList.append('Train View')
        triggerList.append('Training SVM Data')
        triggerList.append(name+'_'+str(time.time()))
        triggerList.append(0)
        triggerList.append('Testing of Data has started with name '+name)
        triggerList.append(0)
        return triggerList

    def startTrigger(self,triggerList):
        print triggerList
        self.signalStartedTrigger.emit(triggerList)
        print '############## Start Emitted  ###########'
        return triggerList

    def endTrigger(self,triggerList):
        triggerList[3]=1
        triggerList[4].replace('started','completed')
        triggerList[5]=100
        self.signalCompleteTrigger.emit(triggerList)





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

