import pickle as cPickle
import numpy as np
import h5py
import os
import matplotlib.pyplot as plt

def unpickle(file):
    import cPickle
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict


if __name__=='__main__':
    if not (os.path.exists('cifar_10')):os.mkdir('cifar_10')
    with h5py.File('cifar_10/cifar_10_train.hdf5','w') as f:
	dset=f.create_dataset('data',(50000,3,32,32),dtype='float')
	dset[0:10000]=np.reshape(np.array(unpickle('cifar-10-batches-py/data_batch_1')['data']),[10000,3,32,32])
	dset[10000:20000]=np.reshape(np.array(unpickle('cifar-10-batches-py/data_batch_2')['data']),[10000,3,32,32])
	dset[20000:30000]=np.reshape(np.array(unpickle('cifar-10-batches-py/data_batch_3')['data']),[10000,3,32,32])
	dset[30000:40000]=np.reshape(np.array(unpickle('cifar-10-batches-py/data_batch_4')['data']),[10000,3,32,32])
	dset[40000:50000]=np.reshape(np.array(unpickle('cifar-10-batches-py/data_batch_5')['data']),[10000,3,32,32])

	dset1=f.create_dataset('label',(50000,1),dtype='float')		
	dset1[0:10000]=np.reshape(np.array(unpickle('cifar-10-batches-py/data_batch_1')['labels']),[10000,1])
	dset1[10000:20000]=np.reshape(np.array(unpickle('cifar-10-batches-py/data_batch_2')['labels']),[10000,1])
	dset1[20000:30000]=np.reshape(np.array(unpickle('cifar-10-batches-py/data_batch_3')['labels']),[10000,1])
	dset1[30000:40000]=np.reshape(np.array(unpickle('cifar-10-batches-py/data_batch_4')['labels']),[10000,1])
	dset1[40000:50000]=np.reshape(np.array(unpickle('cifar-10-batches-py/data_batch_5')['labels']),[10000,1])

    with h5py.File('cifar_10/cifar_10_test.hdf5','w') as f:
	dset=f.create_dataset('data',(10000,3,32,32),dtype='float')
	dset[0:10000]=np.reshape(np.array(unpickle('cifar-10-batches-py/test_batch')['data']),[10000,3,32,32])
	dset1=f.create_dataset('label',(10000,1),dtype='float')		
	dset1[0:10000]=np.reshape(np.array(unpickle('cifar-10-batches-py/test_batch')['labels']),[10000,1])

