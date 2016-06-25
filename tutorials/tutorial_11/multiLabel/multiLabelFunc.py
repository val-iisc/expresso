import numpy as np
import scipy
import scipy.misc
import h5py
from PIL import Image
import os
root=os.getenv('EXPRESSO_ROOT')
import  matplotlib.pyplot as plt

#staticArg: First line of the text file
#dim : dimension as supplied from GUI
#lineStart: index of the begining of blob in the overall hdf5 file.
#arg1,arg2 : argument given by user via GUI


def getLines(line,dim,staticArg=None,arg1=None,arg2=None):
    """
    return the total number of crops by reading appropriate text file
    """
    return len(line.split(" "))-1 



def operate(line,fileName,lineStart,dim,staticArg=None,arg1=None,arg2=None):
    """
    main function which returns concatinated data blobs
    """
    #Recives lines one by one
    filename=line.split(" ")[0];
    folderpath=staticArg.replace('\n','')
    path=folderpath+'/'+filename
    storage=[]
    #Step 2 : Creating Blob 
    print dim
    image=np.array(Image.open(path),dtype=np.float32)
    img=scipy.misc.imresize(np.array(image,dtype='float32'),[dim[1],dim[2]]).transpose([2,0,1])
    #Append same data such that depth=#labels
    for idx in range(len(line.split(" "))-1):
	storage.append(img)

    return np.array(storage,dtype=np.float32)

def getLabels(line,fileName,lineStart,dim,staticArg=None,arg1=None,arg2=None):
    """
    returns the labels for a given line
    """
    label=[ [int(elem)] for elem in line.replace("\n","").split(" ")[1:]]

    return np.array(label,dtype=np.float32)

def arg1Name():
    return None

def arg2Name():
    return None

