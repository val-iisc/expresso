import sys
import os
import h5py
root=os.getenv('EXPRESSO_ROOT')


#Format for splitter
#python Splitter.py dataName value
if(len(sys.argv)!=3):print 'Please Enter data in correct format\npython Splitter.py dataName value'

dataName=sys.argv[1]
value=int(sys.argv[2])


with h5py.File(root+'/data/'+dataName+'_split1.hdf5','w') as fw:
    f=h5py.File(root+'/data/'+dataName+'.hdf5','r')
    comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
    #Writing the data
    fw.create_dataset('data',data=f['data'][:value],**comp_kwargs)
    if('label' in f.keys()):fw.create_dataset('label',data=f['label'][:value],**comp_kwargs)
    #Writing the data Ends
    f.close()
with h5py.File(root+'/data/'+dataName+'_split2.hdf5','w') as fw:
    f=h5py.File(root+'/data/'+dataName+'.hdf5','r')
    comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
    #Writing the data
    fw.create_dataset('data',data=f['data'][value:],**comp_kwargs)	
    if('label' in f.keys()):fw.create_dataset('label',data=f['label'][value:],**comp_kwargs)
    #Writing the data Ends
    f.close()


