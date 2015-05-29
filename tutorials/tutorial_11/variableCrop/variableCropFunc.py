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
    cropFolderPath=staticArg.split(" ")[-1].replace('\n','') # Path where crops dims are stored
    filename=line.replace('.jpg\n','.txt')
    return len(open(cropFolderPath+'/'+filename,'r').readlines()) #returns total number of lines in each crop file, i.e 010001.txt,etc



def operate(line,fileName,lineStart,dim,staticArg=None,arg1=None,arg2=None):
    """
    main function which returns concatinated data blobs
    """
    #Recives lines one by one
    cropFolderPath=staticArg.split(" ")[-1].replace('\n','') # Path where crops dims are stored
    filename=line.replace('.jpg\n','.txt')
    folderpath=staticArg.split(" ")[0].replace('\n','')
    path=folderpath+'/'+line.replace("\n","")
    storage=[]
    #Step 2 : Creating Blob 
    print dim
    image=np.array(Image.open(path),dtype=np.float32)
    #Reading from Crop File
    for elem in open(cropFolderPath+'/'+filename,'r').readlines():
	print 'ELEM',elem
        cropDim=[int(e) for e in elem.split(',')[0].split(" ")]
	cropDim[2],cropDim[3]=cropDim[2]+cropDim[0],cropDim[3]+cropDim[1]
	print cropDim
        img=scipy.misc.imresize(np.array(image[cropDim[0]:cropDim[2],cropDim[1]:cropDim[3],:],dtype='float32'),[dim[1],dim[2]]).transpose([2,0,1])
	storage.append(img)


    return np.array(storage,dtype=np.float32)

def getLabels(line,fileName,lineStart,dim,staticArg=None,arg1=None,arg2=None):
    """
    returns the labels for a given line
    """
    label=[]
    filename=line.replace('.jpg\n','.txt')
    cropFolderPath=staticArg.split(" ")[-1].replace('\n','') # Path where crops dims are stored
     
    for elem in open(cropFolderPath+'/'+filename,'r').readlines():
         label.append([int(elem.split(',')[-1].replace('\n',''))]);

    return np.array(label,dtype=np.float32)

def arg1Name():
    return None

def arg2Name():
    return None

