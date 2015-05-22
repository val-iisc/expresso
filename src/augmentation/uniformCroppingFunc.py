import numpy as np
import scipy
import scipy.misc
import h5py
from PIL import Image
import os
root=os.getenv('EXPRESSO_ROOT')

def getLines(line,dim,staticArg=None,arg1=None,arg2=None):
    if(dim[1]==dim[2]):return 1
    return 0;
    pass


def operate(line,fileName,lineStart,dim,staticArg=None,arg1=None,arg2=None):
    print staticArg[:-1]+'/'+line.strip().split()[0]
    print lineStart,'lineStart'
    print dim,'dim'
    name=staticArg[:-1]+'/'+line.strip().split()[0]   
    #Step 2 : Creating Blob 
    image=np.array(Image.open(name),dtype=np.float32);
    imgdim=image.shape
    s=1.5 if arg1=None or arg1='' else int(arg1)
    newdim=(s*dim[1],s*int(dim[1]*imgdim[1]/float(imgdim[0]))) if imgdim[0]<imgdim[1] else (s*int(dim[1]*imgdim[0]/float(imgdim[1])),s*dim[1]);
    
    storage=scipy.misc.imresize(np.array(image,dtype='float32'),newdim);
    imgdim=storage.shape

    topleftcrop=storage[,int((imgdim[1]-imgdim[0])/2):int((imgdim[1]+imgdim[0])/2),:] if imgdim[0]<imgdim[1] else storage[(imgdim[0]-imgdim[1])//2:(imgdim[0]+imgdim[1])//2,:,:]; 
    storage=storage.transpose([2,0,1])
    print storage.shape
    return storage



def arg1Name():
    return None

def arg2Name():
    return None
   
