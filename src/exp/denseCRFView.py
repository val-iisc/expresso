#-*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'denseCRFView.ui'
#
# Created: Sun May  3 21:55:23 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui

import os
import sys
import h5py
import numpy as np
import scipy
import scipy.misc
from PIL import Image
from time import sleep

root=os.getenv('EXPRESSO_ROOT')
root='/home/jaley/Projects/expresso'
import pipelineView
sys.path.append(root+'/src/functions')
import FunctionHandler
from qtutils import inthread
import subprocess

import denseCRFDialog

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
    signalUpdateTriggered=QtCore.pyqtSignal(object)
    signalChangeIndexTriggered=QtCore.pyqtSignal(object)
    def __init__(self,parent=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(610, 591)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 611, 591))
        self.widget.setObjectName(_fromUtf8("widget"))
	self.widget.setStyleSheet('background-color:rgb(0,0,0)')
        self.widget_2 = pg.GraphicsLayoutWidget(Form) 
        self.widget_2.setGeometry(QtCore.QRect(20, 90, 251, 251))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.widget_3 = pg.GraphicsLayoutWidget(Form) 
        self.widget_3.setGeometry(QtCore.QRect(280, 150, 141, 141))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.widget_5 = pg.GraphicsLayoutWidget(Form) 
        self.widget_5.setGeometry(QtCore.QRect(450, 150, 141, 141))
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.widget_6 = pg.GraphicsLayoutWidget(Form) 
        self.widget_6.setGeometry(QtCore.QRect(280, 0, 181, 161))
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
	self.widget_4_parent=QtGui.QWidget(Form)
	self.widget_4_parent.setStyleSheet('background-color:rgb(150,150,90)')
        self.widget_4_parent.setGeometry(QtCore.QRect(0, 325, 291, 281))
        self.widget_4 = pipelineView.Ui_Form(self.widget_4_parent)
        self.widget_4.setGeometry(QtCore.QRect(0, -28, 301, 301))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
	self.widget_4.setStyleSheet('background-color:rgb(150,150,90)')
	self.widget_7_parent=QtGui.QWidget(Form)
	self.widget_7_parent.setStyleSheet('background-color:rgb(150,150,90)')
        self.widget_7_parent.setGeometry(QtCore.QRect(330, 325, 291, 281))
        self.widget_7 = pipelineView.Ui_Form(self.widget_7_parent)
        self.widget_7.setGeometry(QtCore.QRect(0, -28, 301, 301))
        self.widget_7.setObjectName(_fromUtf8("widget_7"))
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(450, 290, 141, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
	self.comboBox.setStyleSheet('background-color:rgb(150,150,150)')
        self.comboBox_2 = QtGui.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(280, 290, 141, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
	self.comboBox_2.setStyleSheet('background-color:rgb(150,150,150)')
        self.comboBox_3 = QtGui.QComboBox(self.widget)
        self.comboBox_3.setGeometry(QtCore.QRect(130, 10, 121, 24))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
	self.comboBox_3.setStyleSheet('background-color:rgb(150,150,150)')
	self.comboBox_3.hide()
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(24,18, 101, 17))
        self.label_2.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(175,175,175)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox_4 = QtGui.QComboBox(self.widget)
        self.comboBox_4.setGeometry(QtCore.QRect(130, 10, 121, 24))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
	self.comboBox_4.setStyleSheet('background-color:rgb(150,150,150)')
	self.pushButtonRefresh = QtGui.QPushButton(self.widget)
        self.pushButtonRefresh.setGeometry(QtCore.QRect(150, 39,100, 24))
        self.pushButtonRefresh.setObjectName(_fromUtf8("pushButton"))
	self.pushButtonRefresh.setStyleSheet('background-color:rgb(90,90,60);color:rgb(255,255,255)')
	self.pushButtonRefresh.setText('Refresh')
	self.pushButtonRefresh.clicked.connect(self.submit)
	self.horizontalSlider=QtGui.QSlider(Form)
	self.horizontalSliderLabel=QtGui.QLabel()
	self.horizontalSlider.setGeometry(QtCore.QRect(461,20,135,20))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
	self.horizontalSlider.valueChanged.connect(self.changeDataView)	
	#Horizontal Slider
	self.spinBoxId=QtGui.QSpinBox(Form)
	self.spinBoxId.setGeometry(QtCore.QRect(461,60,75,30))
	self.spinBoxId.setStyleSheet('background-color:rgb(255,255,255)')
	self.spinBoxId.valueChanged.connect(self.changeDataView)
	self.horizontalSlider.valueChanged.connect(self.spinBoxId.setValue)
	self.spinBoxId.valueChanged.connect(self.horizontalSlider.setValue)
	### Data View ###
        self.dataView = self.widget_6.addViewBox()
        self.dataView.setAspectLocked(True)
        self.dataImg = pg.ImageItem(border='w')
        self.dataView.addItem(self.dataImg)
	### Three HeatMaps ###
	self.heatLeftView=self.widget_3.addViewBox()
	self.heatRightView=self.widget_5.addViewBox()
	self.heatOutView=self.widget_2.addViewBox()
	self.heatLeftImg=pg.ImageItem(border='w')
	self.heatRightImg=pg.ImageItem(border='w')
	self.heatOutImg=pg.ImageItem(border='w')

	self.heatLeftView.addItem(self.heatLeftImg)
	self.heatRightView.addItem(self.heatRightImg)
	self.heatOutView.addItem(self.heatOutImg)
	self.heatOutImg.setImage(np.arange(300).astype(np.float32).reshape(10,10,3))	
	self.heatLeftStorage=None
	self.heatRightStorage=None
	self.dataStorage=None
	self.signalUpdateTriggered.connect(self.heatOutImg.setImage)
	### Pipeline Related	
	self.functionHandler=FunctionHandler.FunctionHandler()
	self.funcLeftList=self.widget_4.funcList
	self.funcRightList=self.widget_7.funcList
	### Initiallize
	self.initiallize(Form)
	self.spinBoxId.valueChanged.connect(self.onIndexChanged)
	self.horizontalSlider.valueChanged.connect(self.onIndexChanged)
	#self.signalChangeIndexTriggered.connect(self.spinBoxId.setValue)
	#Final Submit(Functionality) Starts
	self.pushButtonFinalSubmit=QtGui.QPushButton(Form)
	self.pushButtonFinalSubmit.setGeometry(QtCore.QRect(20, 39,100, 24))
        self.pushButtonFinalSubmit.setObjectName(_fromUtf8("pushButton"))
	self.pushButtonFinalSubmit.setStyleSheet('background-color:rgb(90,90,60);color:rgb(255,255,255)')
	self.pushButtonFinalSubmit.setText('Submit')
	self.pushButtonFinalSubmit.clicked.connect(self.onFinalSubmit)
	self.dialogBox=denseCRFDialog.Ui_Form()
	self.dialogBox.setGeometry(100,100,491,246)
	self.dialogBox.signalCompleteTrigger.connect(self.finalSubmit)	
	#Final Submit(Functionality) Ends


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", "Select Feature", None))
    def initiallize(self,Form):
	#Fill comboBox_3 with data List
        #Triggers for ExpList
	self.comboBox_4.clear()
	for elem in os.listdir(root+'/exp/data'):
            if elem.endswith('.hdf5'):
		#Find cardinality of experiment images
                f=h5py.File(root+'/exp/data/'+elem,'r')
		if(f.keys()==[] or 'input_data' not in f.keys()):continue
		self.comboBox_4.addItem(elem[:-5])
		print 'added ', elem[:-5]

	self.fillOnVerification()
	self.comboBox_2.currentIndexChanged.connect(self.onDataChanged)
	self.comboBox.currentIndexChanged.connect(self.onDataChanged)
	self.widget_4.signalUpdateTriggered.connect(self.onPipelineChanged)
	self.widget_7.signalUpdateTriggered.connect(self.onPipelineChanged)

	self.onDataChanged()	
	self.submit()


     #On bieng verified by the Confirm button
    def fillOnVerification(self):
	self.comboBox.clear()
	self.comboBox_2.clear()
	print 'Confirm Clicked'
	self.expName=self.comboBox_4.currentText().__str__()
	if(self.expName==None or self.expName==''):return
	with h5py.File(root+'/exp/data/'+self.expName+'.hdf5','r') as f:
	    self.comboBox.addItems(f.keys())
	    self.comboBox_2.addItems(f.keys())
	self.changeDataView()
    ################### DATA SECTION ########################
    def onDataChanged(self):
        name=str(self.comboBox_4.currentText())
        print name
	if(name==''):return
        f=h5py.File(root+'/exp/data/'+name+'.hdf5','r')
	self.dataShape=f['input_data'].shape
        self.horizontalSlider.setMaximum(f['input_data'].shape[0]-1)
        self.spinBoxId.setMaximum(f['input_data'].shape[0]-1)
	self.spinBoxId.setMinimum(0)
	f.close()
        self.changeDataView()

    def changeDataView(self,index=None):
	if(index==None):index=self.spinBoxId.value()
	if(index==None):return
        name=str(self.comboBox_4.currentText())
	if name==None or name=='':return
	print name,'NAME'
	
	with h5py.File(root+'/exp/data/'+name+'.hdf5') as f :
	    self.dataShape=f['input_data'].shape
	    data=np.array(f['input_data'][index],dtype=np.float32)
	    data=np.transpose(data,[1,2,0])
	    self.dataImg.setImage(data)
	    self.dataStorage=data
	###Left Heat Map
	#If Experiment exists then just initiallize it
	if(self.comboBox_2.count()==0 or self.comboBox_2.currentText()==None or self.comboBox_2.currentText().__str__()==''):
	    return
        else:
	    keyName=self.comboBox_2.currentText().__str__()
	    expName=self.comboBox_4.currentText().__str__()
	    print 'Exp Name',expName
	    with h5py.File(root+'/exp/data/'+expName+'.hdf5','r') as f:
		if(f[f.keys()[0]].shape[0]!=self.dataShape[0]):return
		data=f[keyName][self.spinBoxId.value()]
		data=self.functionHandler.operate(self.funcLeftList,data=data)
		data=np.max(data,axis=0)
		self.heatLeftImg.setImage(data)
		self.heatLeftStorage=data
	###Right Heat Map
	if(self.comboBox.count()==0 or self.comboBox.currentText()==None or self.comboBox.currentText().__str__()==''):
	    return
        else:
	    keyName=self.comboBox.currentText().__str__()
	    expName=self.comboBox_4.currentText().__str__()
	    print 'Exp Name',expName
	    with h5py.File(root+'/exp/data/'+expName+'.hdf5','r') as f:
		print 'DataShape : @@@ ',str(self.dataShape)
		print 'Keys of f : ### ',str(f.keys())
		if(f[f.keys()[0]].shape[0]!=self.dataShape[0]):return
		data=f[keyName][self.spinBoxId.value()]
		data=self.functionHandler.operate(self.funcRightList,data=data)
		data=np.max(data,axis=0)
		self.heatRightImg.setImage(data)
		self.heatRightStorage=data	


    #################### PIPELINE SECTION ###################
    def onPipelineChanged(self,extra=None):
	self.funcLeftList=self.widget_4.funcList
	self.funcRightList=self.widget_7.funcList
   	self.onDataChanged()

    def onIndexChanged(self,extra=None):
	self.onPipelineChanged()
	self.submit()

    ################### SUBMIT SECTION ########################
 

    def submit(self):
	if(self.heatLeftStorage==None or self.heatRightStorage==None or self.dataStorage==None):return
	shape=self.dataShape
	inthread(self.runParallel,self.dataStorage,self.heatLeftStorage,self.heatRightStorage,shape)

    def runParallel(self,data,leftHeatMap,rightHeatMap,shape):
	print shape,'My SHAPE'
	leftHeatMap=scipy.misc.imresize(leftHeatMap,[shape[2],shape[3]])
	rightHeatMap=scipy.misc.imresize(rightHeatMap,[shape[2],shape[3]])
	leftMax=np.amax(leftHeatMap)
	rightMax=np.amax(rightHeatMap)
	### PATHS
	execpath=root+'/tools/densecrf/build/examples/dense_inference'
	ppmpath=root+'/exp/denseCRF/input.ppm'
	potentialpath=root+'/exp/denseCRF/unary.txt'
	outpath=root+'/exp/denseCRF/output.txt'

	###Saving Image as PIL
	im=Image.fromarray(data.astype('uint8')).save(ppmpath)

	###Saving ends
	#Step1: Write it down to textFiles in /exp/denseCRF
	with open(potentialpath,'w') as f:
	    indexList=[(i,j) for i in range(shape[2]) for j in range(shape[3])]

	    print leftHeatMap.shape
	    print rightHeatMap.shape
	    for elem in indexList:
		f.write(str(-1*leftHeatMap[elem[0],elem[1]])+'\n')
		f.write(str(-1*rightHeatMap[elem[0],elem[1]])+'\n')
	    subprocess.call([execpath,ppmpath,potentialpath,outpath])

	outputHeatMap=np.zeros([shape[2],shape[3]]);
	print outputHeatMap.shape 

	with open(outpath,'r') as f:
	    for elem in indexList:outputHeatMap[elem[0],elem[1]]=float(f.readline())
	self.signalUpdateTriggered.emit(outputHeatMap)

    def onFinalSubmit(self):
	self.dialogBox.refresh()
	self.dialogBox.show()

    def finalSubmit(self,extra=None):
	print self.dialogBox.lineEdit.text()
	#Args 1. FuncLeftList
	#Args 2. FuncRightList
	#Args 3. Exp Name
	#Args 4. Layer Names
	#Args 5. Ground Truth Name
	#Args 6. Evaluation Metric
	args={}
	args['funcLists']=[self.funcLeftList,self.funcRightList]
	args['expName']=self.expName;
	l1,l2=self.comboBox_2.currentText().__str__(),self.comboBox.currentText().__str__()
	args['layerName']=[l1,l2]
	args['groundTruth']=self.dialogBox.comboBox.currentText().__str__()
	args['evaluationMetric']=self.dialogBox.comboBox_2.currentText().__str__()
	args['denseExpName']=self.dialogBox.lineEdit.text().__str__()
	args['pipelineHandler']=self.functionHandler
	#Finally Running the Batch Processing
	inthread(self.runFinalParallel,**args)



    def runFinalParallel(self,funcLists,expName,layerName,groundTruth,evaluationMetric,denseExpName,pipelineHandler):
	#Step 1 : Loop in for each blob of data
	fData=h5py.File(root+'/exp/data/'+self.expName+'.hdf5','r');
	fGT=h5py.File(root+'/data/'+groundTruth+'.hdf5','r')
	if('input_data' not in fData.keys()):return
	if(not os.path.exists(root+'/exp/denseCRF/data/'+denseExpName)):os.mkdir(root+'/exp/denseCRF/data/'+denseExpName)
	execpath=root+'/tools/densecrf/build/examples/dense_inference'
	ppmpath=root+'/exp/denseCRF/data/'+denseExpName+'/input.ppm'
	potentialpath=root+'/exp/denseCRF/data/'+denseExpName+'/unary.txt'
	outpath=root+'/exp/denseCRF/data/'+denseExpName+'/output.txt'
	logpath=root+'/exp/denseCRF/data/'+denseExpName+'/results.txt'
	open(logpath,'w').write('unionVal intersectionVal totalAreaGT totalAreaDenseCRF overallArea\n')

	for i in range(fData['input_data'].shape[0]):
	    dataIter=np.transpose(np.array(fData['input_data'][i],dtype=np.float32),[1,2,0])
	    leftData=scipy.misc.imresize(np.max(np.array(fData[layerName[0]][i],dtype=np.float32),axis=0),fData['input_data'].shape[2:4])
	    rightData=scipy.misc.imresize(np.max(np.array(fData[layerName[1]][i],dtype=np.float32),axis=0),fData['input_data'].shape[2:4])
	    leftHeatMap=pipelineHandler.operate(funcLists[0],leftData)
	    rightHeatMap=pipelineHandler.operate(funcLists[1],rightData)
 	    ### PATHS

	    ###Saving Image as PIL
	    im=Image.fromarray(dataIter.astype('uint8')).save(ppmpath)
	    ###Saving ends
	    #Step1: Write it down to textFiles in /exp/denseCRF
	    shape=fData['input_data'].shape
	    indexList=[(l,j) for l in range(shape[2]) for j in range(shape[3])]
	    with open(potentialpath,'w') as f:
	        for elem in indexList:
		    f.write(str(-1*leftHeatMap[elem[0],elem[1]])+'\n')
		    f.write(str(-1*rightHeatMap[elem[0],elem[1]])+'\n')
	   
	    subprocess.call([execpath,ppmpath,potentialpath,outpath])
	    groundTruthMap=np.array(fGT['data'][i],dtype=np.float32)
	    outputHeatMap=np.zeros([shape[2],shape[3]]);
	    with open(outpath,'r') as f:
	        for elem in indexList:outputHeatMap[elem[0],elem[1]]=float(f.readline())
	    output=self.computeAccuracyAndPrecision(groundTruthMap,outputHeatMap)
	    output=[str(item) for item in output ]
	    open(logpath,'a').write(' '.join(output)+'\n')
	    #self.signalUpdateTriggered.emit(np.reshape(groundTruthMap,[227,227]))
	    self.signalUpdateTriggered.emit(groundTruthMap)
	    sleep(0.3)
	    #out=np.array([outputHeatMap,groundTruthMap,np.zeros([groundTruthMap.shape[0],groundTruthMap[1]])])
	    out=np.array([outputHeatMap*255,groundTruthMap[0],outputHeatMap*255]).transpose([1,2,0])
	    print out.shape
	    self.signalUpdateTriggered.emit(out)

	    #self.signalChangeIndexTriggered.emit(i)
	    
	fData.close()
	fGT.close()
	
	pass
    """
	Format of the output will be (intersection,union,totalareaGt,totalAreaDense,totalArea)
    """
    def computeAccuracyAndPrecision(self,groundTruthMap,denseMap):
	print 'Ground Truth Shape : ',groundTruthMap.shape
	print 'Dense CRF Shape : ',denseMap.shape

	groundTruthMap=groundTruthMap.flatten()
	denseMap=denseMap.flatten()
	if(len(groundTruthMap)!=len(denseMap)):return [0,0,0,0]
	unionVal,intersectionVal=0,0;
	totalAreaGT,totalAreaDenseCRF=0,0;
	
	for i in range(len(groundTruthMap)):
	    if(i<5):print groundTruthMap[i],denseMap[i]
	    if(groundTruthMap[i]>0.0 and denseMap[i]>0.0):intersectionVal=intersectionVal+1
	    if(groundTruthMap[i]>0.0 or denseMap[i]>0.0):unionVal=unionVal+1
	    if(groundTruthMap[i]>0.0):totalAreaGT=totalAreaGT+1
	    if(denseMap[i]>0.0):totalAreaDenseCRF=totalAreaDenseCRF+1
	print  [unionVal,intersectionVal,totalAreaGT,totalAreaDenseCRF,len(groundTruthMap)]; 

	return [unionVal,intersectionVal,totalAreaGT,totalAreaDenseCRF,len(groundTruthMap)];
    def refreshTrigger(self):
	self.comboBox_4.clear()
	for elem in os.listdir(root+'/exp/data'):
            if elem.endswith('.hdf5'):
		#Find cardinality of experiment images
                f=h5py.File(root+'/exp/data/'+elem,'r')
		if(f.keys()==[] or 'input_data' not in f.keys()):continue
		self.comboBox_4.addItem(elem[:-5])
		print 'added ', elem[:-5]



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

