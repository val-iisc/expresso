##############
# Written by : Jaley Dholakiya
# Video Analytics Lab,IISc
#############

import numpy as np
import h5py
import os
import sys

root=os.getenv('EXPRESSO_ROOT')
sys.path.append(root+'/src/net/config')
import netConfig_pb2
sys.path.append(os.getenv('CAFFE_ROOT')+'/python/caffe/proto')
from google.protobuf import text_format
sys.path.append(os.getenv('CAFFE_ROOT')+'/python')
import caffe_pb2
import caffe
import shutil
import h5py

class NetHandler:

    def __init__(self,netName,netList,batchSize,dataName,saveName):
	self.batchSize=batchSize

        self.netHandler=netConfig_pb2.Param()
        text_format.Merge(open(root+'/net/netData.prototxt').read(),self.netHandler)

	self.currentNet=netConfig_pb2.NetParam()
        for elem in self.netHandler.net:
		print elem.name,netName
                if elem.name==netName:self.currentNet.CopyFrom(elem)


        self.protoHandler=caffe_pb2.NetParameter()
        text_format.Merge(open(self.currentNet.protopath).read(),self.protoHandler)

	
	self.dataName=dataName
	self.saveName=saveName
	self.netList=netList
	self.netName=netName


    def updateNet(self):
        channel_swap=(2,1,0) if self.currentNet.channel_swap else None
        self.net=caffe.Classifier(str(self.currentNet.protopath),str(self.currentNet.modelpath),mean=np.load(str(self.currentNet.meanpath)),gpu=False,raw_scale=int(self.currentNet.raw_scale),channel_swap=channel_swap)

    def operate(self):
      # Load Data
        name=root+'/data/'+self.dataName +'.hdf5'
        print name
        self.opData=h5py.File(name,'r')
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
    def fillNet(self,handle,layername):
        tick=False
        for idx,layers in enumerate(handle.layers):
            if(tick==True):
                print layers.name,'deleted'
                del self.tempHandler.layers[-1]
            if(layers.name==layername):tick=True
        print self.tempHandler




    def start(self):
        self.fileHandle=h5py.File(root+'/exp/data/'+self.saveName+'.hdf5','w')

	savename=root+'/net/temp/temp_'+self.netName+'_'+self.dataName+'_'+self.saveName+'_'+str(self.batchSize)+'.prototxt'
	if(os.path.exists(savename)):return False
        for elem in self.netList:
            self.tempHandler=self.protoHandler.__deepcopy__()
            self.temp=self.tempHandler.__deepcopy__()
            self.fillNet(self.temp,elem)
            open(savename,'w').write(self.tempHandler.__str__())
            #Change Net everytime
            channel_swap=(2,1,0) if self.currentNet.channel_swap else None

	    print savename,'SAVENAME'
	    #self.net=caffe.Classifier(str(savename),str(self.currentNet.modelpath),gpu=False,raw_scale=int(self.currentNet.raw_scale),channel_swap=channel_swap)
 
            self.net=caffe.Classifier(str(savename),str(self.currentNet.modelpath),gpu=False,mean=np.load(str(self.currentNet.meanpath)),raw_scale=int(self.currentNet.raw_scale),channel_swap=channel_swap)

            data=self.operate()
            #Creating and storing in HDF5 file
            # Data=data, key=self.listWidgetNetList.item(i).text()
            # Name is self.lineEditName.text()
            comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
            self.fileHandle.create_dataset(elem,data=data,**comp_kwargs)

        self.opData=h5py.File(root+'/data/'+self.dataName +'.hdf5','r')
	comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
	if('label' in self.opData.keys()):self.fileHandle.create_dataset('label',data=self.opData['label'],**comp_kwargs)
	
        self.fileHandle.close()
	os.remove(savename)

	return True
class SoftMaxAccuracy:
    def __init__(self,netName,netList,dataName):
	if 'label' in netList: netList.remove('label')
	self.netName=netName
	self.netList=netList
	self.dataName=dataName
	print 'SoftMaxAccuracy Class Initiallized'
    def getAccuracy(self):
	if(self.netList==[]):return 0
	lastLayerName=self.netList[-1]
	#Step 1: Get the data from Last Layer
	if 'label' not in h5py.File(root+'/exp/data/'+self.netName,'r').keys(): return 0
	lastLayerData=np.array(h5py.File(root+'/exp/data/'+self.netName,'r')[lastLayerName],dtype=np.float32)
	
	predictedLabels=np.argmax(lastLayerData,axis=1).flatten()
	print predictedLabels
	
	#Step 2: Get the data from Data Blob with label
	actualLabels=np.array(h5py.File(root+'/exp/data/'+self.netName,'r')['label'],dtype=np.float32).flatten()
	
	#Step 3: Calculate Accuracy
	totalLen=actualLabels.shape[0]
	print totalLen
	print predictedLabels
	nonZero=np.absolute(actualLabels-predictedLabels)
	count=0;
	for elem in nonZero:
	    if(int(elem)==0):count=count+1;
	print count
	score=float(count)/float(totalLen)
 	print score
	return score


if  __name__=='__main__':
    handle=NetHandler('CAFFENET',['conv2'],50,'Ashutosh','commandLineExp')
    
    handle.start()



