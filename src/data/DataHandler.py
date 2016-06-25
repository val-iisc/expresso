import h5py
import Image
import numpy as np
import scipy
import scipy.misc
import scipy.io as sio
import readdb
import os
import shutil
import subprocess
#import leveldB
root=os.getenv('EXPRESSO_ROOT')

def text2HDF5(name,sourceloc,destfolderloc,hasLabel=False,dimx=227,dimy=227,dimz=3):
    f=h5py.File(destfolderloc+'/'+name+'.hdf5','w')

    folderloc='';
    strary=open(sourceloc).read().splitlines()
    size=len(strary)-1;
    dset=f.create_dataset("data",(size,dimz,dimx,dimy),compression="gzip")

    if(len(strary)==1):return #No data at all
    hasLabel= True if len(strary[1].strip().split())>1 else False

    if(hasLabel):dset1=f.create_dataset("label",(size,1),compression="gzip")

    for  idx,d in enumerate(strary):
         if(idx==0):
            folderloc=d
         elif(len(d.strip())>1):
            print d
	    #Check If It has Label
	    print d.strip().split(),'iiiiiiiiii'
	    hasLabel= True if len(d.strip().split())>1 else False
	    #Check If It has Label ends
            x=scipy.misc.imresize(np.array(Image.open(folderloc+'/'+d.strip().split()[0]),dtype='float32'),[dimx,dimy]).transpose([2,0,1])
            dset[idx-1,]=x.reshape(1,dimz,dimx,dimy)
            print x.shape

            if(hasLabel):y=np.array(d.strip().split()[1],dtype='float32').reshape(1,1,1,1)#Label Aspect
            if(hasLabel):dset1[idx-1]=y

    f.close();
    pass

def folder2HDF5(name,sourceloc,destfolderloc,hasLabel=False,dimx=227,dimy=227,dimz=3):
    f=h5py.File(destfolderloc+'/'+name+'.hdf5','w')
    strary=os.listdir(sourceloc)
    #Sort it by name
    proc=subprocess.Popen('ls '+sourceloc,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out,err=proc.communicate()
    strary=out.split('\n')
    strary.remove('')

    #End Sort    
    size=len(strary);
    dset=f.create_dataset("data",(size,dimz,dimx,dimy),compression="gzip")
    for  idx,d in enumerate(strary):
        if(len(d.strip())>1 and len(d.split("."))>0 and  d.split(".")[-1] in ['jpg','png','gif','bmp','tiff','jpeg']):

            print d
	    x=scipy.misc.imresize(np.array(Image.open(str(sourceloc)+'/'+d.strip().split()[0]),dtype='float32'),[dimx,dimy])
            if(len(x.shape)==3):
		x=x.transpose([2,0,1])
		dset[idx]=x.reshape(1,dimz,dimx,dimy)
	    else:
		dset[idx]=x.reshape(1,1,dimx,dimy)

    f.close();
    pass





def mat2HDF5(name,sourceloc,destfolderloc,hasLabel=False,dimx=None,dimy=None,dimz=None):
    print 'REACHED HERE'
    f=h5py.File(destfolderloc+'/'+name+'.hdf5','w')
    print  sourceloc
    dataval=sio.loadmat(str(sourceloc))
    print dataval.keys()
    print dataval['data'].shape
    f.create_dataset("data",data=np.array(dataval['data']).astype(np.float32),compression="gzip")
    if(hasLabel):f.create_dataset("label",data=np.array(dataval['label']).astype(np.float32),compression="gzip")
    f.close()

def leveldb2HDF5(name,sourceloc,destfolderloc,hasLabel=False,dimx=None,dimy=None,dimz=None):
    print 'reached here for leveldb'
    readdb.leveldb2HDF5(str(name),str(sourceloc),str(destfolderloc))


def HDF52HDF5(name,sourceloc,destfolderloc,hasLabel=False,dimx=227,dimy=227,dimz=3):
    shutil.copy(sourceloc,destfolderloc+'/'+name+'.hdf5');





def HDF52mat():
    pass


#def HDF52HDF5train():
#    pass


def exportAsMat(filename,hdf5name):
    handle=h5py.File(root+'/data/'+hdf5name+'.hdf5','r') 
    keys=handle.keys()
    matDict={}
    matDict['data']=np.array(handle['data'])
    if 'label' in handle.keys():
	matDict['label']=np.array(handle['label']).astype(np.float32)
    print filename
    print matDict.keys()
    print matDict['data'].shape

    sio.savemat(str(filename),matDict)


    handle.close()
