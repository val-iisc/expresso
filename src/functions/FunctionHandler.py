import sys
import os
sys.path.append(os.getenv('EXPRESSO_ROOT')+'/src/functions')
import sigmoidFunc
import logFunc
import expFunc
import invertFunc
import rLogFunc
from  qtutils import inthread

class FunctionHandler:
    def __init__(self):
	#Add your function here
	self.funcDict={}
	self.funcDict['sigmoid']=sigmoidFunc.operate
	self.funcDict['log']=logFunc.operate
	self.funcDict['relative Log']=rLogFunc.operate
	self.funcDict['exponent']=expFunc.operate
	self.funcDict['invert']=invertFunc.operate

    #Format[ ['func1',param1,param2],['func2',param1,param2], . . . ]
    def operate(self,funcList,data):
	for elem in funcList:
	    data=self.funcDict[elem[0]](data=data,param1=elem[1],param2=elem[2])
	return data

    def getList(self):
	return self.funcDict.keys()



