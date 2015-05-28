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
    layerHandler=caffe_pb2.LayerParameter()
    text_format.Merge(layerParameter,layerHandler)
    paramdict={}
    print bottomDict
    print '*******************'
    dimArray=[bottomDict[k]["dim"] for k in bottomDict.keys()]
    print dimArray
    return getDim(dimArray,**paramdict) 

def getDim(dimArray,axis=1):
    dim=[0,0,0,0];
    print 'DIM',dim
    for elem in dimArray:
	dim[1]=dim[1]+elem[1]
	print 'IN LOOP : ',elem[1]
    dim[0]=dimArray[0][0]
    dim[2]=dimArray[0][2]
    dim[3]=dimArray[0][3]
    return dim




