import h5py
import subprocess
import scipy
import scipy.misc
import numpy as np
import Image

datapath="/home/jaley/Projects/expresso/tutorials/data/MSRA10k/images"
labelpath="/home/jaley/Projects/expresso/tutorials/data/MSRA10k/ground_truth"
comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
def getList(path):
    proc=subprocess.Popen('ls '+path,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err=proc.communicate()
    strary=out.split('\n')
    strary.remove('')
    return strary
dataList=getList(datapath)
labelList=getList(labelpath)

prefix="jdata"
for batchIdx in range(1):
    with h5py.File(prefix+'_'+str(batchIdx)+'.hdf5',"w") as f:
	dh=f.create_dataset("data",(100,3,513,513),**comp_kwargs)
	lh=f.create_dataset("label",(100,1,93,93),**comp_kwargs)
	for idx in range(100):
	    dh[idx]=scipy.misc.imresize(np.array(Image.open(datapath+'/'+dataList[batchIdx*100+idx]),dtype='float32'),[513,513]).transpose([2,0,1])
	    lh[idx]=np.reshape(scipy.misc.imresize(np.array(Image.open(labelpath+'/'+labelList[batchIdx*100+idx]),dtype='float32'),[93,93]),[1,93,93])


	    
	

print len(dataList)
print len(labelList)

#h5py.File(datapath+'',"")

