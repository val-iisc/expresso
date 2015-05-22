import croppingFunc
import h5py
import os
import sys
import croppingWithoutStretchingFunc
root=os.getenv('EXPRESSO_ROOT')

class AugmentationHandler:
    def __init__(self):
	#Array of Lines
	self.lineList=None
	#Array of arrays.with each corr to starting point for each one in pipeline
	self.startCountList=[]
	self.endCountList=[]
	self.lineDict={}
	self.operateDict={}
	self.labelDict={}
	self.arg1Dict={}	
	self.arg2Dict={}

	self.operateDict['crop']=croppingFunc.operate
	self.lineDict['crop']=croppingFunc.getLines
	self.labelDict['crop']=croppingFunc.getLabels
	self.arg1Dict['crop']=croppingFunc.arg1Name()
	self.arg2Dict['crop']=croppingFunc.arg2Name()

	self.operateDict['central crop']=croppingWithoutStretchingFunc.operate

	self.lineDict['central crop']=croppingWithoutStretchingFunc.getLines
	self.labelDict['central crop']=croppingWithoutStretchingFunc.getLabels
	self.arg1Dict['central crop']=croppingWithoutStretchingFunc.arg1Name()
	self.arg2Dict['central crop']=croppingWithoutStretchingFunc.arg2Name()

	self.arg1Dict['central crop']=croppingWithoutStretchingFunc.arg1Name()
	self.arg2Dict['central crop']=croppingWithoutStretchingFunc.arg2Name()


	self.totalLines=None

    #Dimention here are depth x length x width
    #ArgArray is [[funcName arg1 arg2],[funcName, arg1,arg2]]
    def operate(self,lineList,fileName,argArray,dim):
	#Doing Dry Run for Lines
	idx=0;
	for line in lineList:
	    startArray=[]
	    endArray=[]
	    for elem in argArray:
		#Append lines for a line for a function in pipeline
		startArray.append(idx);
		idx=idx+self.lineDict[elem[0]](line,dim,elem[3],elem[1],elem[2])
		print idx
		endArray.append(idx)
	    self.startCountList.append(startArray)
	    self.endCountList.append(endArray)
	self.totalLines=idx
	print self.totalLines,'TOTAL LINES'
	#Creating HDF5 File
	with h5py.File(root+'/data/'+fileName+'.hdf5','w') as f:
	    data=f.create_dataset('data',(self.totalLines,dim[0],dim[1],dim[2]),'f');
	    label=f.create_dataset('label',(self.totalLines,1),'f');
	    #Run Operation
	    for idx,line in enumerate(lineList):
		startArray=self.startCountList[idx]
		endArray=self.endCountList[idx]
		for idx2,elem in enumerate(argArray):
		    len2=self.lineDict[elem[0]](line,dim,elem[3],elem[1],elem[2])
		    data[startArray[idx2]:endArray[idx2],:]=self.operateDict[elem[0]](line,fileName,startArray[idx2],dim,elem[3],elem[1],elem[2])
		    label[startArray[idx2]:endArray[idx2],:]=self.labelDict[elem[0]](line,fileName,startArray[idx2],dim,elem[3],elem[1],elem[2])


    def getKeys(self):
	return self.operateDict.keys()

    def getArg1Name(self,name):
	return self.arg1Dict[name]

    def getArg2Name(self,name):
	return self.arg2Dict[name]
