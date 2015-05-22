import numpy as np
from scipy.special import expit
defaultParam1=0
defaultParam2=1
def operate(data,param1=None,param2=None):
    param1=defaultParam1 if param1==None else param1*0.1
    param2=defaultParam2 if param2==None else param2*0.1
    data=np.array(data,dtype=np.float32)
    data=data-np.amin(data)
    param1=param1*np.amax(data)/100;
    print data.flatten()[0:10]
    data=1/(1+np.exp(-1*param2*(-1*param1+data)))
    print data.flatten()[0:10]
    return data
