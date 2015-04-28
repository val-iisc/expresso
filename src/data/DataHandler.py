import h5py
import Image
import numpy as np
import scipy
import scipy.misc
import scipy.io as sio
import readdb
import os
#import leveldB
root=os.getenv('EXPRESSO_ROOT')

def text2HDF5(name,sourceloc,destfolderloc,hasLabel=False,dimx=225,dimy=227,dimz=3):
    f=h5py.File(destfolderloc+'/'+name+'.hdf5','w')

    folderloc='';
    strary=open(sourceloc).read().splitlines()
    size=len(strary)-1;
    dset=f.create_dataset("data",(size,dimz,dimx,dimy),compression="gzip")
    if(hasLabel):dset1=f.create_dataset("label",(size,1),compression="gzip")

    for  idx,d in enumerate(strary):
         if(idx==0):
            folderloc=d
         elif(len(d.strip())>1):
            print d
            x=scipy.misc.imresize(np.array(Image.open(folderloc+'/'+d.strip().split()[0]),dtype='float64'),[dimx,dimy]).transpose([2,0,1])
            dset[idx-1,]=x.reshape(1,dimz,dimx,dimy)
            print x.shape

            if(hasLabel):y=np.array(d.strip().split()[1],dtype='float64').reshape(1,1,1,1)#Label Aspect
            if(hasLabel):dset1[idx-1]=y

    f.close();
    if(hasLabel):f1.close()
    pass

def folder2HDF5(name,sourceloc,destfolderloc,hasLabel=False,dimx=227,dimy=227,dimz=3):
    f=h5py.File(destfolderloc+'/'+name+'.hdf5','w')
    strary=os.listdir(sourceloc)
    size=len(strary);
    dset=f.create_dataset("data",(size,dimz,dimx,dimy),compression="gzip")
    for  idx,d in enumerate(strary):
        if(len(d.strip())>1 and len(d.split("."))>0 and  d.split(".")[-1] in ['jpg','png','gif','bmp','tiff','jpeg']):

            print d
            x=scipy.misc.imresize(np.array(Image.open(str(sourceloc)+'/'+d.strip().split()[0]),dtype='float64'),[dimx,dimy]).transpose([2,0,1])
	
            dset[idx]=x.reshape(1,dimz,dimx,dimy)

    f.close();
    pass



def mat2HDF5(name,sourceloc,destfolderloc,hasLabel=False):
    print 'REACHED HERE'
    f=h5py.File(destfolderloc+'/'+name+'.hdf5','w')
    print  sourceloc
    dataval=sio.loadmat(str(sourceloc))
    print dataval.keys()
    print dataval['data'].shape
    f.create_dataset("data",data=np.array(dataval['data']).astype(np.float32),compression="gzip")
    if(hasLabel):f.create_dataset("label",data=np.array(dataval['label']).astype(np.float32),compression="gzip")
    f.close()

def leveldb2HDF5(name,sourceloc,destfolderloc,hasLabel=False):
    print 'reached here for leveldb'
    readdb.leveldb2HDF5(str(name),str(sourceloc),str(destfolderloc))


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
