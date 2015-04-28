##############
# Written by : Jaley Dholakiya
# Video Analytics Lab,IISc
#############

import groupexp_pb2
import sys
import os
import matplotlib
#matplotlib.use('Agg')
import h5py

import matplotlib.pyplot as plt

from google.protobuf import text_format



caffe_root=os.getenv('CAFFE_ROOT')
sys.path.append(caffe_root+'/'+'python');
import caffe
import numpy as np
import scipy
import scipy.misc

# Depends on few thing jaleynet.prototxt, protofile
#

plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['image.interpolation'] = 'nearest'
#plt.rcParams['image.cmap'] = 'gray'
caffe.set_phase_test()
caffe.set_mode_cpu()

class experiment:
	def __init__(self,protofilename,data_input_option):
		self.protofilename=protofilename
		self.name=self.protofilename.split('.')[0]
		print 'experiment created'
		#LOAD DATA
		if(data_input_option==1):
			self.load_input_folder_data()	
		else:
			self.load_input_filelist_data()
		#LOAD ENDS
		#NET CONFIG BEGIN
		netlist=groupexp_pb2.Param()
		text_format.Merge(open("jaleynet.prototxt").read(),netlist)
		for elem in netlist.net:
			if elem.name==self.netname:
				self.nethandle=elem
				self.load_net()
				
		#NET CONFIG_ENDS
		self.store_data()

	def load_net(self):
		caffe.set_phase_test()
		# input preprocessing: 'data' is the name of the input blob == net.inputs[0]

		#scores = net.predict([caffe.io.load_image(caffe_root + 'examples/images/cat.jpg')])


		channel_swap=(2,1,0) if self.nethandle.channel_swap else None
		self.net=caffe.Classifier(str(self.nethandle.protopath),str(self.nethandle.modelpath),mean=np.load(str(self.nethandle.meanpath)),gpu=False,raw_scale=int(self.nethandle.raw_scale),channel_swap=channel_swap)
		#print str(self.nethandle.protopath),str(self.nethandle.modelpath),'mean=',np.load(str(self.nethandle.meanpath)),'gpu=',False,'raw_scale=',int(self.nethandle.raw_scale),'channel_swap=',channel_swap 
		#self.net=caffe.Classifier(str(self.nethandle.protopath),str(self.nethandle.modelpath),mean=np.load(str(self.nethandle.meanpath)),gpu=False,channel_swap=(2,1,0))
		print 
		f=open(self.outpath+'/'+self.name+'_paramslist.txt','w')
		self.paramslist=self.net.params.keys()
		f.write("\n".join(self.net.params.keys()))
		f.close()
		f=open(self.outpath+'/'+self.name+'_blobslist.txt','w')
		self.blobslist=self.net.blobs.keys()
		f.write("\n".join(self.net.blobs.keys()))
		f.close()



	#Sets netname,fileloclist,filenamelist,inputdata array
	def load_input_folder_data(self):
		handle=groupexp_pb2.FolderParam()
		text_format.Merge(open(self.protofilename).read(),handle)  
		self.netname=handle.deploy_net_name;
		self.outpath=handle.output_loc
		pass


	def load_input_filelist_data(self):
		handle=groupexp_pb2.FileParam()
		text_format.Merge(open(self.protofilename).read(),handle)  
		self.netname=handle.deploy_net_name;
		self.outpath=handle.output_loc	
		self.filenamelist,self.fileloclist=[],[]
		for elem in handle.file_loc:
			name= str(elem).split(".")[0].split('/')[-1]
			self.filenamelist.append(name)
			self.fileloclist.append(str(elem))
		#SAVING FILELISTS
		print self.outpath
		f=open(self.outpath+'/'+self.name+'_filenamelist.txt','w')
		f.write("\n".join(self.filenamelist))
		f.close()
		f=open(self.outpath+'/'+self.name+'_fileloclist.txt','w')
		f.write("\n".join(self.fileloclist))
		f.close()
		f=open(self.outpath+'/'+self.name+'_netname.txt','w')
		f.write(self.netname)
		f.close()

		#SAVING ENDS


	#Resize image data in 3x500x500 and store it
	def store_data(self):
		comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
		with h5py.File(self.outpath+'/'+self.name+'_data.hdf5','w') as f:
			#SAVE WEIGHTS
			for elem in self.paramslist:f.create_dataset('params_'+elem, data=self.net.params[elem][0].data, **comp_kwargs)
			#SAVE DATA
			for idx in range(len(self.filenamelist)):
				data=scipy.misc.imresize(caffe.io.load_image(self.fileloclist[idx]),[500,500,3])
				print data.shape
				f.create_dataset('data_'+self.filenamelist[idx], data=data, **comp_kwargs)

			#SAVE RESPONSE TO DATA FOR EACH LAYER
				# input preprocessing: 'data' is the name of the input blob == net.inputs[0]

				scores=self.net.predict([caffe.io.load_image(self.fileloclist[idx])])
				for elem in self.blobslist:
					print 'blob name is ',elem
					f.create_dataset('blobs_'+elem+'_'+self.filenamelist[idx],data=self.net.blobs[elem].data,**comp_kwargs)
					print elem, 'done for ',self.filenamelist[idx]
					print self.net.blobs[elem].data.shape	
					#plt.imshow(np.array(self.net.blobs[elem].data[0].max(axis=0)))



if __name__=='__main__':
	exp=experiment('fileexp.prototext',0)

