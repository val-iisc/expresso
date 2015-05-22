import numpy as np
defaultParam1=1
defaultParam2=0

def operate(data,param1=None,param2=None):
    maxVal=np.amax(data)	
    minVal=np.amin(data)	
    print maxVal
    print minVal
    data=np.array(data,dtype=np.float32)*(-1)

    return data


