import sys;
import os
caffe_root=os.getenv('CAFFE_ROOT')
sys.path.append(caffe_root+'/python/caffe/proto')
from google.protobuf import text_format
import caffe_pb2

#TopDict is dictionary of top blobs and thier simulated sizes
#BottomDict is dictionary of bottom blobs (empty/filled)
#argDict is list of arguments requried eg{stride:3,max} 

def operate(bottomDict,layerParameter):
    paramdict={}
    return getDim(bottomDict[bottomDict.keys()[0]]["dim"],**paramdict) 

def getDim(old_dim,num_output=0,size=1,stride=1,pad=0,group=1):
    dim=old_dim
    return dim

