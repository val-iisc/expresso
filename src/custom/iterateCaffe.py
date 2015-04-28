import sys
import os
from google.protobuf.descriptor import FieldDescriptor
from google.protobuf import text_format
import inspect

sys.path.append(os.getenv('HOME')+'/caffe/python/caffe/proto')
import caffe_pb2
import google.protobuf.descriptor as desc


message=caffe_pb2.NetParameter()
message2=caffe_pb2.NetParameter()
classmembers=inspect.getmembers(caffe_pb2,inspect.isclass)

for elem in caffe_pb2.LayerParameter().LayerType.DESCRIPTOR.values_by_name.keys():
	#print elem
	pass

text_format.Merge("layers{\ntype:CONVOLUTION\nconvolution_param{\n}\n}\
		layers{\ntype:CONVOLUTION\nconvolution_param{\n}\n}",message)
text_format.Merge("layers{\ntype:CONVOLUTION\nconvolution_param{\n}\n}\
		layers{\ntype:CONVOLUTION\nconvolution_param{\n}\n}",message2)


for elem in inspect.getmembers(message.layers[0]): print elem

def insert(handle,pos,data):
    #Step 1: Assign Net Parameter
    c=caffe_pb2.NetParameter()
    text_format.Merge(data,c)
    for idx in range(len(c.layers)):handle.layers.add()
    #Step 2:
 
    length=len(handle.layers)

    for idx in range(length-1,pos-1,-1):
	h=caffe_pb2.LayerParameter()
	text_format.Merge(handle.layers[idx-len(c.layers)].__str__(),h)
	handle.layers[idx].CopyFrom(h)

    for idx in range(pos,pos+len(c.layers)):
	handle.layers[idx].CopyFrom(c.layers[idx-pos])




    


a=message.layers.add()
a.name="abra"
insert(message,1,'\nlayers{type:CONVOLUTION\n}\nlayers{type:CONVOLUTION\n}')
print message


"""
for elem in message.layers[0].DESCRIPTOR.fields: print elem.name
for elem in message.layers[0].DESCRIPTOR.fields:
	 if elem.name=='convolution_param':message=elem.message_type


for elem in message.fields:
	print elem.name
"""

"""
for idx,elem in  enumerate(caffe_pb2.LayerParameter().DESCRIPTOR.fields):
	#print elem.name, elem.label
	if(elem.name=='name'):
		for e in inspect.getmembers(elem):
			print e
	#print type(elem.name)
	

for idx, elem in enumerate(classmembers):
	if(idx==0):
		for e in inspect.getmembers(elem[1]):
			#print e
			pass
"""
