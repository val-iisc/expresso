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
    inner_product_param= layerHandler.inner_product_param
    paramdict={}
    if(inner_product_param.HasField("num_output")):paramdict["num_output"]=inner_product_param.num_output



    return getDim(bottomDict[bottomDict.keys()[0]]["dim"],**paramdict) 

def getDim(old_dim,num_output=0,size=1,stride=1,pad=0,group=1):
    dim=old_dim
    dim[0]=old_dim[0]
    dim[1]=num_output/group if num_output>0 else old_dim[1]/group
    dim[2]=1
    dim[3]=1
    return dim

