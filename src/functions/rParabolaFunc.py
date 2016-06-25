import numpy as np
defaultParam1=1
defaultParam2=0

def operate(data,param1=None,param2=None):
	
    param1=defaultParam1 if param1==None else param1*0.1
    param2=defaultParam1 if param2==None else param2*0.1
    print 'param1',param1
    maxVal=np.amax(data)
    minVal=np.amin(data)
    data=data-np.amin(data)
    data=param1*data+param2*(data*data)
    data=data/np.amax(data)
    return data
