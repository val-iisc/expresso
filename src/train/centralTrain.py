# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'centralDefault.ui'
#
# Created: Sat Mar  7 00:20:05 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os
import shutil
root=os.getenv('EXPRESSO_ROOT')
from subprocess import Popen
from multiprocessing import Process,Queue
import subprocess
from multiprocessing import Pool
sys.path.append(os.getenv('CAFFE_ROOT')+'/python/caffe/proto')
import caffe_pb2
from google.protobuf import text_format
import trainChooseView
from qtutils import inmain_later,inthread,inmain
import time
import datetime

print root
sys.path.append(root+'/src/custom')

import netWidget
print root
sys.path.append(root+'/src/train')
sys.path.append(root+'/src/train/SVM')
sys.path.append(root+'/src/net')
sys.path.append(root+'/src/net/config')
import trainingProgressView
import solverView
import socketView
import netConfig_pb2
import trainSVMView
from google.protobuf import text_format
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
    signalUpdateTrigger=QtCore.pyqtSignal(object)
    signalRefreshTrigger=QtCore.pyqtSignal(object)
    signalCompleteTrigger=QtCore.pyqtSignal(object)
    signalStartedTrigger=QtCore.pyqtSignal(object)

    def __init__(self,parent=None):
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 591)
	

        self.stackedWidget = QtGui.QStackedWidget(Form)
	self.stackedWidget.setGeometry(QtCore.QRect(0,0,611,591))
	self.addPages()
        #self.widget.setGeometry(QtCore.QRect(0, 0, 611, 591))
        #self.widget.setObjectName(_fromUtf8("widget"))
	self.signalUpdateTrigger.connect(self.addToNetConfiguration)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

    def addPages(self):
	self.addPage0()
	self.addPage1()
	self.addPage2()
	self.addPage3()
	self.addPage4()
	self.addPageSVM()
	self.currentIndex=0

    def addPage0Old(self):
	self.label=QtGui.QLabel(self)
	self.pixmap=QtGui.QPixmap(root+"/src/train/images/training.jpg")
	self.label.setPixmap(self.pixmap.scaled(611,611,QtCore.Qt.IgnoreAspectRatio,QtCore.Qt.FastTransformation))
	self.stackedWidget.addWidget(self.label)	

    def addPage0(self):
	self.page0Container=QtGui.QWidget(self)
	self.page0Widget=trainChooseView.Ui_Form(parent=self.page0Container)
	self.page0Widget.setGeometry(QtCore.QRect(0,0,611,591))
	self.page0Container.setStyleSheet("background-color:rgb(120,180,120);")
	self.page0Widget.setStyleSheet("background-color:rgb(120,180,120);")

	self.page0Widget.setGeometry(QtCore.QRect(0,0,611,591))
	self.stackedWidget.addWidget(self.page0Container)

    def addPageSVM(self):
	self.pageSVMContainer=QtGui.QWidget(self)
	self.pageSVMWidget=trainSVMView.Ui_Form(parent=self.pageSVMContainer)
	self.pageSVMWidget.setGeometry(QtCore.QRect(0,0,611,591))
	self.pageSVMContainer.setStyleSheet("background-color:rgb(120,180,120);")
	self.pageSVMWidget.setStyleSheet("background-color:rgb(120,180,120);")

	self.pageSVMWidget.setGeometry(QtCore.QRect(0,0,611,591))
	self.stackedWidget.addWidget(self.pageSVMContainer)
	#Don't forget to add further fillers in left1 and left2 views after page0


    def addPage1(self):
	self.widget=QtGui.QScrollArea(self)
	self.page1NetEditor=netWidget.MyForm(parent=self.widget,mylist=None,myloc=root+'/src/custom/defaultTrain.prototxt',trainMode=True,readOnly=True)
	self.page1NetEditor.treeWidget.clear()
	self.widget.setGeometry(QtCore.QRect(0,0,611,591))
	self.page1NetEditor.setStyleSheet("background-color:rgb(180,210,180);")
	self.page1NetEditor.setGeometry(QtCore.QRect(0,0,611,591))
	self.page1NetEditor.treeWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
	self.stackedWidget.addWidget(self.widget)

    def addPage2(self):
        self.page2Container=QtGui.QWidget(self)
        self.page2Container.setGeometry(0,0,611,591)
        self.page2Container.setStyleSheet("background-color:rgb(120,180,120);")
        self.page2Widget=solverView.Ui_Form(self.page2Container,index=self.page1NetEditor.index)

        self.page2Widget.setGeometry(0,0,611,591)
        self.stackedWidget.addWidget(self.page2Container)
 
    def addPage3(self):
        self.page3Container=QtGui.QWidget(self)
        self.page3Container.setGeometry(0,0,611,591)
        self.page3Container.setStyleSheet("background-color:rgb(120,180,120);")
        self.page3Widget=socketView.Ui_Form(self.page3Container)
        self.page3Widget.setGeometry(0,0,611,591)
        self.stackedWidget.addWidget(self.page3Container)

    def addPage4(self):
        self.page4Container=QtGui.QWidget(self)
        self.page4Container.setGeometry(0,0,611,591)
        self.page4Container.setStyleSheet("background-color:rgb(120,180,120);")
        self.page4Widget=trainingProgressView.Ui_Form(self.page4Container)
        self.page4Widget.setGeometry(0,0,611,591)
        self.stackedWidget.addWidget(self.page4Container)


    def pushButtonNextSlot(self):
	if self.currentIndex==4:return
	if self.currentIndex==3:
	    self.createConfiguration()
	    self.currentIndex=0
	    self.stackedWidget.setCurrentIndex(self.currentIndex)
	    return
	   
	print 'Next Clicked: '+str(self.currentIndex)
	self.currentIndex=self.currentIndex+1
	self.stackedWidget.setCurrentIndex(self.currentIndex)

    def pushButtonBackSlot(self):
	print 'back clicked'
	if self.currentIndex==5:
	    self.currentIndex=0;
	    self.stackedWidget.setCurrentIndex(self.currentIndex)
	    return; 
	if self.currentIndex==0:return
	self.currentIndex=self.currentIndex-1
	self.stackedWidget.setCurrentIndex(self.currentIndex)


    def createConfiguration(self,extra=None):
	name=self.page3Widget.lineEditConfigName.text().__str__().lower()		
	path=root+'/net/train/'+self.page3Widget.lineEditConfigName.text().__str__().lower()
	self.path=path
	print 'PATH!!!',path
	# 1. Create Folder in train
	if(os.path.exists(path)==False):os.mkdir(root+'/net/train/'+self.page3Widget.lineEditConfigName.text().__str__().lower())
	# 2. Add train_net,solver,etc into it.
	self.index= self.page1NetEditor.index
	self.maxIterations=10000
        self.netHandler=netConfig_pb2.Param();
        self.data=open(root+'/net/netData.prototxt').read()
        text_format.Merge(self.data,self.netHandler)
	print self.netHandler.net[self.index]
	open(path+'/'+name+'_train.prototxt','w').write(open(self.netHandler.net[self.index].trainpath,'r').read())
	with open(path+'/'+name+'_solver.prototxt','w') as f:
	    solverHandle=caffe_pb2.SolverParameter()
	    #Loading it instant 
	    self.page2Widget.updateHandle()
	    text_format.Merge(self.page2Widget.protoHandler.__str__(),solverHandle)
	    #Loading it instant ends
	    #text_format.Merge(open(self.netHandler.net[self.index].solverpath,'r').read(),solverHandle)
	    solverHandle.snapshot_prefix=(path+'/'+name);
	    solverHandle.net=(path+'/'+name+'_train.prototxt')
	    if(self.netHandler.net[self.index].gpu==True):
		solverHandle.solver_mode=1
	    else:
		solverHandle.solver_mode=0
	    #Getting solver maximum iterations
	    self.maxIterations=solverHandle.max_iter
	    #Getting solver iterations ends
	    open(self.netHandler.net[self.index].solverpath,'w').write(solverHandle.__str__())
	    f.write(solverHandle.__str__())
	
	### FINETUNE STARTS
	self.isFinetune=False
	if(self.netHandler.net[self.index].modelpath!=""):
	    reply=QtGui.QMessageBox.question(self, 'Message',
                        "Do you want to finetune using existing weights?", QtGui.QMessageBox.Yes | 
                        QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if(reply==QtGui.QMessageBox.Yes):self.isFinetune=True
	### FINETUNE ENDS
	trainDataName=self.page3Widget.widget.comboBoxTraining.currentText()
	validationDataName=self.page3Widget.widget.comboBoxValidation.currentText()
	shutil.copy(root+'/data/'+trainDataName+'.hdf5',path+'/'+name+'_train.hdf5')
	shutil.copy(root+'/data/'+validationDataName+'.hdf5',path+'/'+name+'_val.hdf5')
	with open(path+'/'+name+'_trainscript.sh','w') as f:
	    f.write("#!/usr/bin/env sh\n")
	    #f.write("cd $CAFFE_ROOT\n")
	    otherarguments=' -weights '+self.netHandler.net[self.index].modelpath if self.isFinetune==True else ''
	    if(self.netHandler.net[self.index].gpu==True):otherarguments=otherarguments+' -gpu '+str(self.netHandler.net[self.index].gpu_index)
	    f.write(os.getenv('CAFFE_ROOT')+'/build/tools/caffe train --solver='+path+'/'+name+'_solver.prototxt'+otherarguments+'\n')
	    f.write('echo \'Train Completed \'')  
	with open(path+'/'+name+'_train.txt','w') as f:
	    f.write(path+'/'+name+'_train.hdf5')
	with open(path+'/'+name+'_val.txt','w') as f:
	    f.write(path+'/'+name+'_val.hdf5')
	
	#Change The train_test prototxt to associate right data
	handle=caffe_pb2.NetParameter()
	text_format.Merge(open(path+'/'+name+'_train.prototxt').read(),handle)
	######### NEW VERSION #########################
	if len(handle.layers)==0:
	    if(True):
		if(True):
		#if(handle.layers[0].type in [5,12,29,24]):
		    #del handle.layers[0].data_param
		    layerHandle=caffe_pb2.LayerParameter()
		    text_format.Merge(open(root+'/net/defaultHDF5TrainDataNew.prototxt').read(),layerHandle)
		    #if(self.netHandler.net[self.index].has_mean==True):
			#layerHandle.transform_param
			#layerHandle.transform_param.mean_file=self.netHandler.net[self.index].meanpath
		    #else: 
			#layerHandle.ClearField('transform_param')
		    handle.layer[0].CopyFrom(layerHandle)
		    handle.layer[0].name=name.lower()
		    #BatchSize Starts
		    batchSize=self.page3Widget.widget.lineEditBatchSizeTraining.text().__str__()
		    batchSize=100 if batchSize=="" else int(batchSize)
		    handle.layer[0].hdf5_data_param.batch_size=batchSize
		    #BatchSize Ends
		    handle.layer[0].hdf5_data_param.source=path+'/'+name+'_train.txt'
		    print handle.layer[0]

		if(self.page3Widget.widget.checkBoxValidation.checkState()>0): 
		#if(handle.layers[1].type in [5,12,29,24]):#handle.layers[1].type="HDF5Data"
		    layerHandle=caffe_pb2.LayerParameter()
		    text_format.Merge(open(root+'/net/defaultHDF5TestDataNew.prototxt').read(),layerHandle)
		    handle.layer[1].CopyFrom(layerHandle)
		    handle.layer[1].name=name
		    #BatchSize Starts
		    batchSize=self.page3Widget.widget.lineEditBatchSizeValidation.text().__str__()
		    batchSize=100 if batchSize=="" else int(batchSize)
		    handle.layer[1].hdf5_data_param.batch_size=batchSize
		    #BatchSize Ends
		    handle.layer[1].hdf5_data_param.source=path+'/'+name+'_val.txt'
		    print handle.layer[1]
		else:
		    del handle.layer[1] 
		    for layerIdx,layer in enumerate(handle.layer):
			for incIdx,inc in enumerate(layer.include):
			    if inc.HasField('phase'):
			        if(inc.phase==0): del handle.layer[layerIdx].include[incIdx]
			    #Check Later what happens if only 'phase' is removed.
			        else: del handle.layer[layerIdx]

		    #if(self.netHandler.net[self.index].has_mean==True):
			#layerHandle.transform_param
			#layerHandle.transform_param.mean_file=self.netHandler.net[self.index].meanpath
		    #else:
			#layerHandle.ClearField('transform_param')


	################ OLD VERSION #########################
	else:
	    if(True):
		if(True):
		#if(handle.layers[0].type in [5,12,29,24]):
		    #del handle.layers[0].data_param
		    layerHandle=caffe_pb2.LayerParameter()
		    text_format.Merge(open(root+'/net/defaultHDF5TrainData.prototxt').read(),layerHandle)
		    handle.layers[0].name=name.lower()
		    if(self.netHandler.net[self.index].has_mean==True):

			#layerHandle.transform_param
			layerHandle.transform_param.mean_file=self.netHandler.net[self.index].meanpath
		    else:
			layerHandle.ClearField('transform_param')


		    handle.layers[0].CopyFrom(layerHandle)
		    #BatchSize Starts
		    batchSize=self.page3Widget.widget.lineEditBatchSizeTraining.text().__str__()
		    batchSize=100 if batchSize=="" else int(batchSize)
		    handle.layer[0].hdf5_data_param.batch_size=batchSize
		    #BatchSize Ends

		    handle.layers[0].hdf5_data_param.source=path+'/'+name+'_train.txt'
		    print handle.layers[0]

		if(self.page3Widget.widget.checkBoxValidation.checkState()>0): 
		#if(handle.layers[1].type in [5,12,29,24]):#handle.layers[1].type="HDF5Data"
		    layerHandle=caffe_pb2.LayerParameter()
		    text_format.Merge(open(root+'/net/defaultHDF5TestData.prototxt').read(),layerHandle)
		    handle.layers[1].name=name
		    handle.layers[1].CopyFrom(layerHandle)
		    #BatchSize Starts
		    batchSize=self.page3Widget.widget.lineEditBatchSizeValidation.text().__str__()
		    batchSize=100 if batchSize=="" else int(batchSize)
		    handle.layer[1].hdf5_data_param.batch_size=batchSize
		    #BatchSize Ends
		    handle.layers[1].hdf5_data_param.source=path+'/'+name+'_val.txt'
		    print handle.layers[1]
		    if(self.netHandler.net[self.index].has_mean==True):
			#layerHandle.transform_param
			layerHandle.transform_param.mean_file=self.netHandler.net[self.index].meanpath
		    else:
			layerHandle.ClearField('transform_param')
		else:
		    del handle.layers[1]

	####### REMODIFICATION OF FIRST TWO LAYERS START

	open(path+'/'+name+'_train.prototxt','w').write(handle.__str__())
	print 'PATH BEFORE PROGRESS',path

	
	triggerList=self.createTriggerList()
	inthread(self.runParallel,name,path,triggerList,self.maxIterations,str(self.netHandler.net[self.index]))
	#Finally run the process


    def runParallel(self,name,path,triggerList,maxIterations,netParam):
	p=Process(target=self.callback,args=(name,path))
	inthread(self.sidethread,p,triggerList,maxIterations)
	p.start()
	p.join()
	sleep(0.5)
	self.signalUpdateTrigger.emit([name,netParam]);
	self.signalRefreshTrigger.emit(name)
        self.endTrigger(triggerList) #====>End
	return

    def callback(self,name,path):
	print 'Work in progress'
	print path+'/'+name+'_trainscript.sh'	
	subprocess.call(['sh',path+'/'+name+'_trainscript.sh'])


    def callingSlot(self,x):
	print 'Hello World',x
	
    def createTriggerList(self):
	name=self.page3Widget.lineEditConfigName.text().__str__().lower()
        triggerList=[]
        triggerList.append('Train View')
        triggerList.append('Training Data')
        triggerList.append(name+'_'+str(time.time()))
        triggerList.append(0)
        triggerList.append('Training of Data has started with name '+name)
        triggerList.append(0)
	triggerList.append(None)
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


    def sidethread(self,p,triggerList,maxIterations):
	print '############## Start Emitted  ###########'
	#Side Thread for testing the status
	l=[(datetime.datetime.now()+datetime.timedelta(seconds=i)).strftime('%Y%m%d-%H%M%S') for i in range(5)]
	print l
        triggerList=self.startTrigger(triggerList) #====>End
	sleep(2)
        while(p.is_alive()):
            sleep(0.5)
            triggerList[3]=2;
	    result=self.getAccuracyAndPrecision(l)
	    print result[1][1],'%%%%%%%%%%%%','IterationList'
	    print maxIterations,'%%%%%%%%','MaxIterations'
            triggerList[5]=0 if len(result[1][1])==0 else int(100*float(int(result[1][1][-1]))/float(int(maxIterations)))
	    triggerList[4]=result[0]
	    triggerList[6]=result[1]+[result[2]]
	    print result[2], 'FILENAME !!!!!!!!!!!!!!!!!!!'
	    print result[1]
            self.startTrigger(triggerList)
            print 'is alive'
            sleep(0.5)


    def getAccuracyAndPrecision(self,times):
        import socket
        hostname=str(socket.gethostname())
        import getpass
        username=str(getpass.getuser())
        foldername='/tmp'
        locationprefix='caffe.'+hostname+'.'+username+'.log.INFO.'

        filename=''
        print '#############'
        print 'prefix',locationprefix
	print  times
        print '#############'

	
        for files in os.listdir(foldername):
            if files.startswith(locationprefix):
		#print '###FILES===> ',files
		#print '###times===> ',times
		
		for elem in times:
		    if elem in files:
                        print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
                        print files
                        print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
                        filename=files
                        break;
        print filename
        if(filename!=''):
            lines=open(foldername+'/'+filename,'r').readlines()
	    print '%%%%%%%%%%%%% Reached Here %%%%'
            print lines[-3:-1] 
            return [' '.join(lines[-3:-1]),self.getInformation('/tmp/'+filename),filename]
	    
        return [' ',None]



    def getInformation(self,filename):
	with open(filename) as f:
	    lossList=[]
	    lossIter=[]
	    testAccuracyList=[]
	    testLossList=[]
	    testIterList=[]

	    for lines in f.readlines():
		if 'Iteration' in lines and 'loss' in lines:
		    #print lines
		    lossIter.append(lines.split('loss')[0].split('Iteration ')[-1][:-2])
		    lossList.append(lines.split('loss = ')[-1][:-1])
		if 'accuracy' in lines and 'Test net' in lines:
		    testAccuracyList.append(lines.split('accuracy = ')[-1][:-1])
		if 'loss' in lines and 'Test net' in lines:
		    testLossList.append(lines.split('loss = ')[-1].split('(')[0])
		if 'Iteration' in lines and 'Testing net' in lines:
		    testIterList.append(lines.split('Iteration ')[-1].split(',')[0])
	return [lossList,lossIter,testAccuracyList,testLossList,testIterList]


    def switchToPageSVM(self):
	print 'SVM Page in central'
	self.stackedWidget.setCurrentIndex(5)
	self.currentIndex=5

    def addToNetConfiguration(self,params):
	name=str(params[0]).lower()
	config=params[1]
	handle=netConfig_pb2.NetParam()
	text_format.Merge(config,handle)
	saveHandle=netConfig_pb2.NetParam()
	#subprocess.call(['sh',path+'/'+name+'_trainscript.sh'])
	proc=subprocess.Popen('ls '+root+'/net/train/'+name+' -tr *.caffemodel | tail -1',shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)	
	out,err=proc.communicate()
	lastGeneratedModel=out.split('\n')[0]

	print 'LAST MODEL : ',lastGeneratedModel

	if(err!=''):print 'ERROR LOG',err
	if(lastGeneratedModel==''):return



	### Create Entry in netConfig and Add Appropreate Folders
	#Create a new folder root+'/net/data/'
	if(os.path.exists(root+'/net/data/'+name.lower())==False):os.mkdir(root+'/net/data/'+name)
	dirpath=root+'/net/data/'+name

	#Deploy Path
	if(handle.protopath!=""):
	    shutil.copyfile(handle.protopath,root+'/net/data/'+name+'/'+name+'_deploy.prototxt')
	    saveHandle.protopath=root+'/net/data/'+name+'/'+name+'_deploy.prototxt'
	else:
	    saveHandle.protopath=""

	#Train Path
	if(handle.trainpath!=""):
	    shutil.copyfile(handle.trainpath,root+'/net/data/'+name+'/'+name+'_train.prototxt')
	    saveHandle.trainpath=root+'/net/data/'+name+'/'+name+'_train.prototxt'
	else:
	    saveHandle.trainpath=""

	if(handle.solverpath!=""):
	    shutil.copyfile(handle.solverpath,root+'/net/data/'+name+'/'+name+'_solver.prototxt')
	    saveHandle.solverpath=root+'/net/data/'+name+'/'+name+'_solver.prototxt'

	else:
	    saveHandle.solverpath=""

	
	##Edit Later
	shutil.copyfile(root+'/net/train/'+name+'/'+lastGeneratedModel,root+'/net/data/'+name+'/'+name+'_model.caffemodel');
	saveHandle.modelpath=root+'/net/data/'+name+'/'+name+'_model.caffemodel';

	saveHandle.has_mean=handle.has_mean
	saveHandle.meanpath=handle.meanpath
	saveHandle.channel_swap=handle.channel_swap
	saveHandle.gpu=handle.gpu
	name=name.upper()
	saveHandle.name=name;
	
	open(root+'/net/netData.prototxt','a').write('\nnet{\n'+str(saveHandle)+'\n}')




	### Ad

	

   

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

