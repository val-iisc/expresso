import numpy as np
import scipy
import scipy.misc
import h5py
from PIL import Image
import os
root=os.getenv('EXPRESSO_ROOT')

def getLines(line,dim,staticArg=None,arg1=None,arg2=None):
    return 2;
    pass


def operate(line,fileName,lineStart,dim,staticArg=None,arg1=None,arg2=None):
    print staticArg[:-1]+'/'+line.strip().split()[0]
    print lineStart,'lineStart'
    print dim,'dim'
    name=staticArg[:-1]+'/'+line.strip().split()[0]   
    #Step 2 : Creating Blob 
    storage=scipy.misc.imresize(np.array(Image.open(name),dtype='float32'),[dim[1],dim[2]]).transpose([2,0,1])
    storage=np.array([storage,storage],dtype='float32')
    print storage.shape
    return storage

def arg1Name():
    return None

def arg2Name():
    return None
   
