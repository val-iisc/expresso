#Extract Features
#Format : python extractFeatures.py expname netName batchsize layername dataname

import sys
import os
root=os.getenv('EXPRESSO_ROOT')
root='/home/jaley/Projects/expresso'
caffe_root=os.getenv('CAFFE_ROOT')
caffe_root='/home/jaley/Documents/caffefresh/caffe-master'
sys.path.append(root+'/src/net/config')
sys.path.append(caffe_root+'/python')
sys.path.append(caffe_root+'/python/caffe/proto')
import netConfig_pb2
import caffe
import caffe_pb2
import numpy as np
import h5py
import scipy
import scipy.misc
import matplotlib.pyplot as plt
from google.protobuf import text_format

print sys.argv

#Step 0 : Initialize Parameters
expName=sys.argv[1]
netName=str(sys.argv[2])
batchSize=int(sys.argv[3])
layerName=sys.argv[4]
dataName=sys.argv[5]
netIdx=None


netHandler=netConfig_pb2.Param()
text_format.Merge(open(root+'/net/netData.prototxt').read(),netHandler)
for idx,elem in enumerate(netHandler.net):
    if(netName==elem.name):netIdx=idx
currentNet=netHandler.net[netIdx]


saveName=root+'/net/temp/temp_'+str(currentNet.name)+'_'+dataName+'_'+expName+'_'+str(batchSize)+'.prototxt'
logName=root+'/net/temp/temp_'+str(currentNet.name)+'_'+dataName+'_'+expName+'_'+str(batchSize)+'_log.txt'




#Step 1 : Create Deploy unto that layer
handle=caffe_pb2.NetParameter()
text_format.Merge(open(currentNet.protopath).read(),handle)


"""
Fills the Net upto the layername
"""
def fillNet(handle,layerName):
    tick=False
    layerIdx=None
    layerLen=len(handle.layer)
    for idx,layers in enumerate(handle.layer):
        if(tick==True):
	    layerIdx=idx;
	    break
        if(layers.name==layerName):tick=True
    if(layerIdx==None):return handle
    for idx in range(layerIdx,layerLen):del handle.layer[-1]
    return handle

handle=fillNet(handle,layerName)
open(saveName,'w').write(str(handle))

raw_input()
#Step 2 : Create Net

channel_swap=(2,1,0) if currentNet.channel_swap else None
if(currentNet.gpu==False):
    caffe.set_mode_cpu()
else:
    caffe.set_mode_gpu()
if(currentNet.has_mean==True):
    dataShape=h5py.File(root+'/data/'+dataName+'.hdf5','r')['data'].shape    
    mean=np.load(str(currentNet.meanpath))
    if(mean.shape!=dataShape[1:]):
        mean=np.transpose(scipy.misc.imresize(np.transpose(mean,[1,2,0]),[dataShape[2],dataShape[3]]),[2,0,1])
    print mean.shape,'MEANPATH'
    print mean
    raw_input()
    net=caffe.Classifier(model_file=str(saveName),pretrained_file=str(currentNet.modelpath),mean=mean,raw_scale=int(currentNet.raw_scale),channel_swap=channel_swap) 
else:
    net=caffe.Classifier(model_file=str(saveName),pretrained_file=str(currentNet.modelpath),raw_scale=int(currentNet.raw_scale),channel_swap=channel_swap) 
    print 'PROTOPATH : ',saveName
    print 'MODELPATH : ',currentNet.modelpath
    print 'RAW_SCALE : ',currentNet.raw_scale
    print 'CHANNEL SWAP : ',channel_swap

#Step 3 : Execute in batches

def operate(expName,layerName,net,currentNet,batchSize,dataName):
    logHandle=open(logName,'a');
    expHandle=h5py.File(root+'/exp/data/'+expName+'.hdf5','a')
    if(layerName in expHandle.keys()):return
    comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
    dataset=None;
    # Load Data
    name=root+'/data/'+dataName +'.hdf5'
    with h5py.File(name,'r') as f:
        if ('label' in f.keys()) and ('label' not in expHandle.keys()):expHandle.create_dataset('label',data=f['label'],**comp_kwargs)
	out=[]
        if currentNet.channel_swap==True:data=np.array(f['data'])[:,[2,1,0],:,:]
        else:
            data=np.array(f['data'])
	    print data
	    print 'FORMAT', data.dtype
        ################ REAL OPERATION  ################
	lastEnded=0
	print data.shape[0]
        for i in range(data.shape[0]//batchSize):

            #out=net.forward_all(**{'data':data[i*batchSize]}).values()[0]
            ##out=net.forward_all(**{'data':data[i*batchSize:(i+1)*batchSize]}).values()[0]
	    net.blobs['data'].data[...]=np.array([data[i]])
            out=net.predict([np.transpose(data[i],[1,2,0])])
	    
	    print net.blobs['data'].data
	    print [np.transpose(data[i],[1,2,0])]
	    raw_input()

	    if(len(out.shape)==2):out=np.reshape(out,[out.shape[0],out.shape[1],1,1])
            if(dataset==None):dataset=expHandle.create_dataset(layerName,(f['data'].shape[0],out.shape[1],out.shape[2],out.shape[3]),**comp_kwargs)
            dataset[i*batchSize:(i+1)*batchSize]=out
	    lastEnded=(i+1)*batchSize
	    logHandle.write(str(lastEnded)+'/'+str(data.shape[0])+' '+layerName+'\n')
            print str(lastEnded)+'/'+str(data.shape[0])+' '+layerName+'\n' 
        out=net.forward_all(**{'data':data[len(out):data.shape[0]]}).values()[0]
	if(len(out.shape)==2):out=np.reshape(out,[out.shape[0],out.shape[1],1,1])
	if(dataset==None):dataset=expHandle.create_dataset(layerName,(f['data'].shape[0],out.shape[1],out.shape[2],out.shape[3]),**comp_kwargs)
	dataset[lastEnded:data.shape[0]]=out
	logHandle.write(str(data.shape[0])+'/'+str(data.shape[0])+' '+layerName+'\n')
        print str(data.shape[0])+'/'+str(data.shape[0])+' '+layerName+'\n' 
    expHandle.close()	
    logHandle.close()
    return out

operate(expName,layerName,net,currentNet,batchSize,dataName)


#Step 4 : Save the data, and use a+ mode for hdf5

if __name__=='__main__':
    print 'Data'
