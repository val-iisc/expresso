import os
import shutil
import sys

root=os.getenv('EXPRESSO_ROOT')

def deleteData():
    if(root==None):return
    shutil.rmtree(root+'/data')
    os.mkdir(root+'/data')

def deleteNet():
    if(root==None):return
    os.remove(root+'/net/netData.prototxt')
    open(root+'/net/netData.prototxt','w').close()
    shutil.rmtree(root+'/net/data')
    os.mkdir(root+'/net/data')

def deleteExp():
    if(root==None):return
    shutil.rmtree(root+'/exp/data')
    os.mkdir(root+'/exp/data')
    shutil.rmtree(root+'/net/data')
    os.mkdir(root+'/net/data')
  

def deleteTrain():
    if(root==None):return
    shutil.rmtree(root+'/net/train')
    os.mkdir(root+'/net/train')



def deleteCache():
    if(root==None):return
    shutil.rmtree(root+'/net/temp')
    os.mkdir(root+'/net/temp')



def deleteSVM():
    if(root==None):return
    shutil.rmtree(root+'/net/SVM')
    os.mkdir(root+'/net/SVM')


