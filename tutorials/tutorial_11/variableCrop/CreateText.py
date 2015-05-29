import os
root=os.getenv("EXPRESSO_ROOT")

with open(root+'/tutorials/tutorial_11/variableCrop/variableCropInclude.txt','w') as f:
	f.write(root+'/tutorials/data/MSRA9 '+root+'/tutorials/tutorial_11/variableCrop/crops\n')
	f.write('010001.jpg\n')
	f.write('010002.jpg\n')
	f.write('010003.jpg')
	f.close()




