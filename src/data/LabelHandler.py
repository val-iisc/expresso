import h5py
import numpy as np


def text2hdf5(sourceloc,destloc):
	label=[[float(elem.strip().split()[0])] for elem in open(sourceloc).readlines()]
	label=np.array(label,dtype=np.float32)
	comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
	with h5py.File(destloc,'a') as f:
	    if('label' in f.keys()): del f['label']
	    f.create_dataset('label',data=label,**comp_kwargs)

	

