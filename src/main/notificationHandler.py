##
# notificationList is list of notificationItems
# Each notificationItem is nothing but a List of 5 Elements
# 0. View
# 1. Notification Name
# 2. Unique Id
# 3. Type of Trigger(0->Start , 1->End , 2-> Update)
# 4. Description 
# 5. Other(Optional)
#



class NotificationHandler:
    def __init__(self):
	self.notificationList=[]
	#Contains List of Lists()

    def addNotificationItem(self,l):
	if(l==None): return
	if(len(l)<5):return
	found=False
	if(l[3]!=0):#If not start
	    for idx,elem in enumerate(self.notificationList):
		if(elem[2]==l[2]):
		    if(elem[3]==2):return #If already completed Process
		    l.append(elem[-1]); #Check what previous state was
		    found=True
		    del self.notificationList[idx]
		    break;
	if(found==True or (found==False and l[3]==0)):	
	    if(found==False): l.append(False) #Default the current state
	    self.notificationList.append(l)
	    self.updateNotificationList()

    def updateNotificationList(self):
	pass


    def changeWidgetState(self,packet):
	for idx,elem in enumerate(self.notificationList):
	    if(elem[2]==packet[0]):
		print packet
		self.notificationList[idx][-1]=True if packet[1]==1 else False
	    	return
