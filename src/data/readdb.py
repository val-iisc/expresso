import leveldb
import sys
import numpy as np
import os
caffe_root=os.getenv('CAFFE_ROOT')
sys.path.append(caffe_root+'/python/caffe/proto')
sys.path.append(caffe_root+'/python/caffe')
sys.path.append(caffe_root+'/python')
import caffe
import caffe_pb2
import h5py



def getdim(filepath):
	db = leveldb.LevelDB(filepath)
	length=0;
		

	for idx,(k,v) in enumerate(db.RangeIter()):
		d=v
		length=idx+1
	
	
	
	channels=caffe_pb2.Datum.FromString(d).channels.__str__()
	width=caffe_pb2.Datum.FromString(d).width.__str__()
	height= caffe_pb2.Datum.FromString(d).height.__str__()
	return (length,int(channels),int(width),int(height))
	
def leveldb2HDF5(filename,filepath,folderpath):
	print folderpath+'/'+filename+'.hdf5'

	f=h5py.File(folderpath+'/'+filename+'.hdf5','w')
	
	#LevelDB Operation
	dim=getdim(filepath)
	db = leveldb.LevelDB(filepath)
	print dim
	dset,dset1=np.zeros([dim[0],dim[1],dim[2],dim[3]]),np.zeros([dim[0],1])
	#dset=f.create_dataset('data',dim,compression="gzip",compression_opts= 1)
	#dset1=f.create_dataset('label',(dim[0],1),compression="gzip",compression_opts= 1)
	for idx,(k,v) in enumerate(db.RangeIter()):
		#print caffe_pb2.Datum.FromString(v).__str__()	
		d=bytearray(caffe_pb2.Datum.FromString(v).data.__str__())
		#print
		l= int(caffe_pb2.Datum.FromString(v).label.__str__())
		#print l
		dset[idx]=np.array(d,dtype='uint8').reshape([1,dim[1],dim[2],dim[3]])
		dset1[idx]=np.array([l],dtype='int').reshape([1,1])
		#print dset
		#print dset1
	dset=np.array(dset,dtype=np.float32)
	dset1=np.array(dset1,dtype=np.float32)

	comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
	f.create_dataset('data',data=dset,**comp_kwargs)	
	f.create_dataset('label',data=dset1,**comp_kwargs)
			#for data in range(len(d)):
			#	pass
	f.close()





if __name__=='__main__':
	leveldb2HDF5('cifar10_test','./cifar10_test_leveldb','.')
	
