import os
root=os.getenv("EXPRESSO_ROOT")

with open(root+'/tutorials/tutorial_11/multiLabel/multiLabelInclude.txt','w') as f:
	f.write(root+'/tutorials/data/MSRA9\n')
	f.write('010001.jpg 0 1 2\n')
	f.write('010002.jpg 0 2\n')
	f.write('010003.jpg 6')
	f.close()




