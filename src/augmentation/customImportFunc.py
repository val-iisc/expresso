import numpy as np
import scipy
import scipy.misc
import h5py
from PIL import Image
import os
root=os.getenv('EXPRESSO_ROOT')

def getLines(line,dim,staticArg=None,arg1=None,arg2=None):
    return 1;
    pass


def operate(line,fileName,lineStart,dim,staticArg=None,arg1=None,arg2=None):
    name=unicode(line.replace("\r","").replace("\n",""),'utf-8')
    print "###PATH :",name
    #name="/home/jaley/Desktop/tobefed/cat/2008_000112-5/length/without_context/2.png"

    #Step 2 : Creating Blob 
    storage=scipy.misc.imresize(np.array(Image.open(name,'r'),dtype='float32'),[dim[1],dim[2]]).transpose([2,0,1])
    storage=np.array([storage],dtype='float32')
    print storage.shape
    return storage

def getLabels(line,fileName,lineStart,dim,staticArg=None,arg1=None,arg2=None):
    return None


def arg1Name():
    return 'TotalCrops'

def arg2Name():
    return None
   
