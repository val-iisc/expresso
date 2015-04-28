import numpy as np
import sys

print sys.argv
env_dict={}
env_dict['CAFFE_ROOT']=sys.argv[1]
env_dict['EXPRESSO_ROOT']=sys.argv[2]
env_list=env_dict.keys()+env_dict.values()
np.save('env_variables.npy',env_list)



