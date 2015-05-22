import numpy as np
defaultParam1=1
defaultParam2=1

def operate(data,param1=None,param2=None):
	
    param1=defaultParam1 if param1==None else param1*0.1
    param2=defaultParam2 if param2==None else param2*0.1
    print 'param1',param1

    return np.exp(param1*data/np.amax(data)+param2)


