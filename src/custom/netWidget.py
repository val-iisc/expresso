# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'netcreator.ui'
#
# Created: Tue Feb 10 16:53:48 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

#Jaley Start
import sys
import os
caffe_root=os.getenv('CAFFE_ROOT')
sys.path.append(caffe_root+'/python/caffe/proto')
from google.protobuf import text_format
import caffe_pb2

root=os.getenv('EXPRESSO_ROOT')
sys.path.append(root+'/src/net/config')
sys.path.append(root+'/src/net')
import layerView
import netConfig_pb2
import inspect


#Jaley End
sys.path.append(root+'/src/custom/layers')
#import conv

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class MyForm(QtGui.QWidget):
    def __init__(self,myloc,mylist=None,parent=None,trainMode=False,readOnly=False):
        super(MyForm, self).__init__(parent)
	self.trainMode=trainMode
        self.deployloc=myloc
        self.layerlist=mylist
	self.readOnlyFlag=readOnly
        self.setupUi(self)
    def changeLayout(self,mylist):
        self.layerlist=mylist
        self.loadTreeWidget()
    def setupUi(self, Form):
	self.index=0
        self.root=root
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 591)
        self.treeWidget = QtGui.QTreeWidget(Form)
        self.treeWidget.setGeometry(QtCore.QRect(0,0, 611, 591))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setText(0, _fromUtf8("1"))
        #Jaley Start
	self.dim=[100,3,227,227]
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.myContextMenu)
	self.treeWidget.header().setStyleSheet("font:12pt")
	self.treeWidget.setStyleSheet("font:12pt")
        #Jaley End
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 90, 611, 591))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

	self.isNewLayer=False
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        #Jaley Start

        ##Save Path Has to be prespecified beforehand
        ##self.lineEditSavePath.setText(QtGui.QFileDialog.getSaveFileName(self,self.tr("Open File"),str(self.root+'/Data'),'*.prototxt'))
        #self.treeWidget.setVisible(False)
        self.treeWidget.setColumnCount(6)
        self.treeWidget.setColumnWidth(0,220)
        self.treeWidget.setColumnWidth(1,100)
        self.treeWidget.setColumnWidth(2,69)
        self.treeWidget.setColumnWidth(3,60)
        self.treeWidget.setColumnWidth(4,60)
        self.treeWidget.setColumnWidth(5,60)

        self.treeWidget.setHeaderLabels(['Layer #','Name','batchsize','depth','width','height'])
	#'name'
	#,'#Elements','Depth','Width','Height'])

        self.protohandler=caffe_pb2.NetParameter()
        self.textEdit.setVisible(False)
        text_format.Merge(open(self.deployloc).read(),self.protohandler)
        self.textEdit.setText(self.protohandler.__str__())
        #self.treeWidget.doubleClicked.connect(self.changeLayer)#Change Layer
	self.treeWidget.itemChanged.connect(self.onItemChangedSlot)
        self.loadTreeWidget()
        #Jaley Ends

    def insertLayer(self,handle,pos,data):
	#Step 1: Assign Net Parameter
	c=caffe_pb2.NetParameter()
	text_format.Merge(data,c)
	for idx in range(len(c.layer)):handle.layer.add()
	#Step 2:
	length=len(handle.layer)

	for idx in range(length-1,pos-1,-1):
	    h=caffe_pb2.LayerParameter()
	    text_format.Merge(handle.layer[idx-len(c.layer)].__str__(),h)
	    handle.layer[idx].CopyFrom(h)

	for idx in range(pos,pos+len(c.layer)):
	    handle.layer[idx].CopyFrom(c.layer[idx-pos])



    def eventFilter(self, source, event):
        import sys

        if event.type() == QtCore.QEvent.Close:
            print 'Closed'
            print self.treeWidget.currentIndex().row()
            #self.lineEditSavePath.setText(self.newWidget.toPlainText())
            self.layerhandler=caffe_pb2.NetParameter();
            #print self.newWidget.toPlainText()
	    if(self.isNewLayer==True and self.newWidget.isSubmitted==True):
            	text_format.Merge(self.newWidget.textEdit.toPlainText().__str__(),self.layerhandler)
	    	self.textEdit.setText(str(self.protohandler))
		self.insertLayer(self.protohandler,self.treeWidget.currentIndex().row(),self.layerhandler.__str__())
		print '--------------------------------------------------------------'
		print self.protohandler
            	self.textEdit.setText(str(self.protohandler))
		self.loadTreeWidget()
		self.isNewLayer=False
	    else:
		if(self.newWidget.isSubmitted==False):return
		text_format.Merge(self.newWidget.textEdit.toPlainText().__str__(),self.layerhandler)
		self.protohandler.layer[self.treeWidget.currentIndex().row()-1].CopyFrom(self.layerhandler.layer[0]);
            	self.textEdit.setText(str(self.protohandler))
           	self.loadTreeWidget()

        if event.type() == QtCore.QEvent.MouseButtonPress:
            self.lineEditSavePath.setText(QtGui.QFileDialog.getSaveFileName(self,self.tr("Open File"),str(self.root+'/net/data'),'*.prototxt'))
        return QtGui.QWidget.eventFilter(self, source, event)

    def saveFileName(self):
        if(str(self.lineEditSavePath.text())==''):
            self.lineEditSavePath.setText(QtGui.QFileDialog.getSaveFileName(self,self.tr("Save File"),str(self.root+'/net/data'),'*.prototxt'))
        if(str(self.lineEditSavePath.text()).endswith('.prototxt')):
            f=open(str(self.lineEditSavePath.text()),'w')
            f.write(str(self.textEdit.toPlainText()))
            return
        f=open(str(self.lineEditSavePath.text())+'.prototxt','w')
        f.write(str(self.textEdit.toPlainText()))

    def saveFile(self,filename):
	if os.path.exists(root+'/net/models/deploy/'+filename.lower()+'.prototxt'):
	    reply = QtGui.QMessageBox.question(self, 'Message','Do you want to overwrite Existing File?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
	    if(reply==QtGui.QMessageBox.No):return False
	
	f=open(root+'/net/models/deploy/'+filename.lower()+'.prototxt','w')
	f.write(str(self.textEdit.toPlainText()))
	return True


    def loadFromListSlot(self,index):
	self.index=index
        self.netHandler=netConfig_pb2.Param();
        self.data=open(root+'/net/netData.prototxt').read()
        text_format.Merge(self.data,self.netHandler)
       	if(self.trainMode==True):
	    if(self.index!=None):    
	        self.loadpath=self.netHandler.net[index].trainpath
		self.dim=[self.netHandler.net[index].tdim0,self.netHandler.net[index].tdim1,self.netHandler.net[index].tdim2,self.netHandler.net[index].tdim3];
	    else:
		self.loadpath=root+'/src/custom/'+'defaultTrain.prototxt'
		self.dim=[100,3,227,227];

	else:
	    if(self.index!=None):    
	    	self.loadpath=self.netHandler.net[index].protopath
	    else:
		self.loadpath=root+'/src/custom/'+'defaultDeploy.prototxt'
	self.protohandler=caffe_pb2.NetParameter()
        text_format.Merge(open(self.loadpath).read(),self.protohandler)
	print self.protohandler
        self.textEdit.clear()
        self.textEdit.setText(self.protohandler.__str__())
        self.loadTreeWidget()



    def loadFileName(self):
        self.loadpath=QtGui.QFileDialog.getOpenFileName(self,self.tr("Open File"),str(self.root+'/net/data'),'*.prototxt')
        self.protohandler=caffe_pb2.NetParameter()
        text_format.Merge(open(self.loadpath).read(),self.protohandler)
        self.textEdit.clear()
        self.textEdit.setText(self.protohandler.__str__())
        self.loadTreeWidget()


    def myContextMenu(self,position):
        menu =QtGui.QMenu()
        self.positionval=position
	print self.readOnlyFlag
	if(self.readOnlyFlag==True):return
	menu.addAction(self.tr("Add a new layer below"),self.newLayer)
	if(self.treeWidget.currentIndex().row()!=0):
            menu.addAction(self.tr("Edit"),self.changeLayer)
	    menu.addAction(self.tr("Delete"),self.deleteLayer)
	menu.exec_(self.treeWidget.viewport().mapToGlobal(position))


    def newLayer(self):
	self.isNewLayer=True

	self.newWidget=layerView.Ui_Form()
        #self.newWidget=QtGui.QTextEdit()
        self.newWidget.textEdit.setText('layer{\nbottom:\"'+self.treeWidget.currentItem().text(0).__str__().strip().split()[-1]+'\"\n}')
        self.newWidget.setStyleSheet("background-color:rgb(115,115,115)")
        globalpnt=self.newWidget.mapToGlobal(self.positionval)
        print self.positionval.y(),self.positionval.x()
        print self.cursor().pos().x()
        self.newWidget.setGeometry(self.cursor().pos().x(),self.cursor().pos().y(),554,367)
	
        #self.newWidget.move(self.cursor().pos().x(),self.cursor().pos().y())
        #self.newWidget.move(self.pos().x()+self.positionval.x(),self.pos().y()+self.positionval.y())
        self.newWidget.installEventFilter(self)
        self.newWidget.show()
	

    def deleteLayer(self):
	del self.protohandler.layer[self.treeWidget.currentIndex().row()-1]
        self.textEdit.setText(str(self.protohandler))
        self.loadTreeWidget()



    def changeLayer(self):
	#===== INTERFACING =========
	#self.newWidget=QtGui.QWidget()
	#self.newWidget.setGeometry(QtCore.QRect(0,0,510,438))
	#self.newWidget.setStyleSheet("background-color:rgb(90,120,90)")
	#self.innerWidget=conv.Ui_Form(self.newWidget)
	
 	


	#===== END OF INTERFACING ==
        self.newWidget=layerView.Ui_Form()
        self.newWidget.textEdit.setText('layer{\n'+self.loadCurrentData()+'\n}')
	self.newWidget.setStyleSheet("background-color:rgb(115,115,115);")
        globalpnt=self.newWidget.mapToGlobal(self.positionval)
        print self.positionval.y(),self.positionval.x()
        print self.cursor().pos().x()
        self.newWidget.setGeometry(self.cursor().pos().x(),self.cursor().pos().y(),554,367)
	
        #self.newWidget.move(self.cursor().pos().x(),self.cursor().pos().y())
        #self.newWidget.move(self.pos().x()+self.positionval.x(),self.pos().y()+self.positionval.y())
        self.newWidget.installEventFilter(self)
        self.newWidget.show()






    def loadTreeWidget(self,dim=None):
        l=[]
        self.treeWidget.clear()
        self.protohandler=caffe_pb2.NetParameter()
        text_format.Merge(str(self.textEdit.toPlainText()),self.protohandler)
	self.treeWidget.setFont(QtGui.QFont('Ubuntu Condensed',12))
        #First Layer Start
	idx=0;
	if(self.trainMode==False):
            layername=QtGui.QTreeWidgetItem()
            layername.setText(0,'Data')
            layername.setText(2,str(self.protohandler.input_dim[0]))
            layername.setText(3,str(self.protohandler.input_dim[1]))
            layername.setText(4,str(self.protohandler.input_dim[2]))
            layername.setText(5,str(self.protohandler.input_dim[3]))
	    layername.setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable)

            l.append(layername)
        else:
	    layername=QtGui.QTreeWidgetItem()
	    layername.setText(0,'Data')
            layername.setText(2,str(self.dim[0]))
            layername.setText(3,str(self.dim[1]))
            layername.setText(4,str(self.dim[2]))
            layername.setText(5,str(self.dim[3]))
	    layername.setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable)
            l.append(layername)
     
	idx=1
        #First Layer Ends
	
        #text_format.Merge(str(self.textEdit.toPlainText()),self.protohandler)
        for layer in self.protohandler.layer:
            if self.layerlist!=None:
	        if layer.name not in self.layerlist:continue
            layername=QtGui.QTreeWidgetItem()
            layername.setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)

            layername.setText(0,str(idx)+'\t'+layer.name)
            idx=idx+1;
            #Adding Static Params
            top=QtGui.QTreeWidgetItem()
            top.setText(0,'top')
            toplist=[];
            for name in layer.top:
                topelem=QtGui.QTreeWidgetItem()
                topelem.setFlags(topelem.flags()& ~QtCore.Qt.ItemIsEnabled )
                topelem.setText(0,name)
                toplist.append(topelem)
            top.addChildren(toplist)
            top.setFlags(top.flags()& ~QtCore.Qt.ItemIsEnabled )

            layername.addChild(top)

            bottom=QtGui.QTreeWidgetItem()
            bottom.setText(0,'bottom')
            bottomlist=[];
            for name in layer.bottom:
                bottomelem=QtGui.QTreeWidgetItem()
                bottomelem.setFlags(bottomelem.flags()& ~QtCore.Qt.ItemIsEnabled )
                bottomelem.setText(0,name)
                bottomlist.append(bottomelem)
            bottom.addChildren(bottomlist)
            bottom.setFlags(layername.flags()& ~QtCore.Qt.ItemIsEnabled )

            layername.addChild(bottom)

            layername.setForeground(1,QtGui.QBrush(QtCore.Qt.white))
            layername.setBackground(1,QtGui.QBrush(QtGui.QColor(45,60,45))) #Text is Red

            layername.addChildren
            #Adding Dynamic Params
            if(layer.type=="Convolution"):        #CONV
                layername.setText(1,'CONV')
                layername.setBackground(0,QtGui.QBrush(QtGui.QColor(180,180,150)))
                layername.setBackground(1,QtGui.QBrush(QtGui.QColor(135,135,120)))
		for i in range(4):layername.setBackground(2+i,QtGui.QBrush(QtGui.QColor(180,180,150)))

                self.paramiter(layer.convolution_param,layername,l)
            elif(layer.type=="Pooling"):       #POOL
                layername.setText(1,'POOL')
                layername.setBackground(0,QtGui.QBrush(QtGui.QColor(120,150,120)))
                layername.setBackground(1,QtGui.QBrush(QtGui.QColor(60,90,60)))
		for i in range(4):layername.setBackground(2+i,QtGui.QBrush(QtGui.QColor(120,150,120)))

                self.paramiter(layer.pooling_param,layername,l)
            elif(layer.type=="InnerProduct"):       #IP
                layername.setText(1,'IP')
                layername.setBackground(0,QtGui.QBrush(QtGui.QColor(210,225,150)))
                layername.setBackground(1,QtGui.QBrush(QtGui.QColor(135,150,90)))
		for i in range(4):layername.setBackground(2+i,QtGui.QBrush(QtGui.QColor(210,225,150)))


                self.paramiter(layer.inner_product_param,layername,l)
                layername.setText(2,l[len(l)-1].text(2))
                layername.setText(3,str(layer.inner_product_param.num_output))
                layername.setText(4,'1')
                layername.setText(5,'1')
            elif(layer.type=="ReLu"):       #RELU
                layername.setText(1,'RELU')
                layername.setBackground(0,QtGui.QBrush(QtGui.QColor(150,180,165)))
                layername.setBackground(1,QtGui.QBrush(QtGui.QColor(90,108,99)))
		for i in range(4):layername.setBackground(2+i,QtGui.QBrush(QtGui.QColor(150,180,165)))

                self.getDim(l,layername)
                self.paramiter(layer.relu_param,layername,l)
            elif(layer.type=="Softmax"):       #SOFTMAX
                layername.setText(1,'SOFTMAX')
		layername.setBackground(0,QtGui.QBrush(QtGui.QColor(75,90,75)))
                layername.setBackground(1,QtGui.QBrush(QtGui.QColor(45,60,45)))
		for i in range(4):layername.setBackground(2+i,QtGui.QBrush(QtGui.QColor(75,90,75)))



                layername.setForeground(0,QtGui.QBrush(QtCore.Qt.white))
                layername.setForeground(1,QtGui.QBrush(QtCore.Qt.white))
                for i in range(4): layername.setForeground(2+i,QtGui.QBrush(QtCore.Qt.white))

                self.getDim(l,layername)
                self.paramiter(layer.softmax_param,layername,l)
            else:
                layername.setText(1,'OTHER')
                self.getDim(l,layername)

            l.append(layername)

        #### OLD VERSION STARTS

        #text_format.Merge(str(self.textEdit.toPlainText()),self.protohandler)
        for layer in self.protohandler.layers:
            if self.layerlist!=None:
	        if layer.name not in self.layerlist:continue
            layername=QtGui.QTreeWidgetItem()
            layername.setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)

            layername.setText(0,str(idx)+'\t'+layer.name)
            idx=idx+1;
            #Adding Static Params
            top=QtGui.QTreeWidgetItem()
            top.setText(0,'top')
            toplist=[];
            for name in layer.top:
                topelem=QtGui.QTreeWidgetItem()
                topelem.setFlags(topelem.flags()& ~QtCore.Qt.ItemIsEnabled )
                topelem.setText(0,name)
                toplist.append(topelem)
            top.addChildren(toplist)
            top.setFlags(top.flags()& ~QtCore.Qt.ItemIsEnabled )

            layername.addChild(top)

            bottom=QtGui.QTreeWidgetItem()
            bottom.setText(0,'bottom')
            bottomlist=[];
            for name in layer.bottom:
                bottomelem=QtGui.QTreeWidgetItem()
                bottomelem.setFlags(bottomelem.flags()& ~QtCore.Qt.ItemIsEnabled )
                bottomelem.setText(0,name)
                bottomlist.append(bottomelem)
            bottom.addChildren(bottomlist)
            bottom.setFlags(layername.flags()& ~QtCore.Qt.ItemIsEnabled )

            layername.addChild(bottom)

            layername.setForeground(1,QtGui.QBrush(QtCore.Qt.white))
            layername.setBackground(1,QtGui.QBrush(QtGui.QColor(45,60,45))) #Text is Red

            layername.addChildren
            #Adding Dynamic Params
            if(layer.type==4):        #CONV
                layername.setText(1,'CONV')
                layername.setBackground(0,QtGui.QBrush(QtGui.QColor(180,180,150)))
                layername.setBackground(1,QtGui.QBrush(QtGui.QColor(135,135,120)))
		for i in range(4):layername.setBackground(2+i,QtGui.QBrush(QtGui.QColor(180,180,150)))

                self.paramiter(layer.convolution_param,layername,l)
            elif(layer.type==17):       #POOL
                layername.setText(1,'POOL')
                layername.setBackground(0,QtGui.QBrush(QtGui.QColor(120,150,120)))
                layername.setBackground(1,QtGui.QBrush(QtGui.QColor(60,90,60)))
		for i in range(4):layername.setBackground(2+i,QtGui.QBrush(QtGui.QColor(120,150,120)))

                self.paramiter(layer.pooling_param,layername,l)
            elif(layer.type==14):       #IP
                layername.setText(1,'IP')
                layername.setBackground(0,QtGui.QBrush(QtGui.QColor(210,225,150)))
                layername.setBackground(1,QtGui.QBrush(QtGui.QColor(135,150,90)))
		for i in range(4):layername.setBackground(2+i,QtGui.QBrush(QtGui.QColor(210,225,150)))


                self.paramiter(layer.inner_product_param,layername,l)
                layername.setText(2,l[len(l)-1].text(2))
                layername.setText(3,str(layer.inner_product_param.num_output))
                layername.setText(4,'1')
                layername.setText(5,'1')
            elif(layer.type==18):       #RELU
                layername.setText(1,'RELU')
                layername.setBackground(0,QtGui.QBrush(QtGui.QColor(150,180,165)))
                layername.setBackground(1,QtGui.QBrush(QtGui.QColor(90,108,99)))
		for i in range(4):layername.setBackground(2+i,QtGui.QBrush(QtGui.QColor(150,180,165)))

                self.getDim(l,layername)
                self.paramiter(layer.relu_param,layername,l)
            elif(layer.type==20):       #SOFTMAX
                layername.setText(1,'SOFTMAX')
		layername.setBackground(0,QtGui.QBrush(QtGui.QColor(75,90,75)))
                layername.setBackground(1,QtGui.QBrush(QtGui.QColor(45,60,45)))
		for i in range(4):layername.setBackground(2+i,QtGui.QBrush(QtGui.QColor(75,90,75)))



                layername.setForeground(0,QtGui.QBrush(QtCore.Qt.white))
                layername.setForeground(1,QtGui.QBrush(QtCore.Qt.white))
                for i in range(4): layername.setForeground(2+i,QtGui.QBrush(QtCore.Qt.white))

                self.getDim(l,layername)
                self.paramiter(layer.softmax_param,layername,l)
            else:
                layername.setText(1,'OTHER')
                self.getDim(l,layername)

            l.append(layername)




	#### OLD VERSION ENDS

        self.treeWidget.addTopLevelItems(l)

    def paramiter(self,handle,layername,l):

        params={}
        for elem in handle.ListFields():
            childval=QtGui.QTreeWidgetItem()
            childval.setFlags(layername.flags()& ~QtCore.Qt.ItemIsEnabled )
            childval.setText(0,str(elem[0].name))
            childval.setText(1,str(elem[1]))
            layername.addChild(childval)
            if elem[0].name=='kernel_size':params['size']=elem[1]
            if elem[0].name=='pad':params['pad']=elem[1]
            #if elem[0].name=='group':params['group']=elem[1]   #GROUP DOES NOT CHANGE THE RESPONSE, ONLY WEIGHTS CHANGE
            if elem[0].name=='stride':params['stride']=elem[1]
            if elem[0].name=='num_output':params['num_output']=elem[1]

        print len(l)
        self.getDim(l,layername,**params)
        return layername


    def getDim(self,l,layername,num_output=0,size=1,stride=1,pad=0,group=1):
        dim=[int(l[len(l)-1].text(2)),int(l[len(l)-1].text(3)),int(l[len(l)-1].text(4)),int(l[len(l)-1].text(5))]
        dim[1]=num_output/group if num_output>0 else dim[1]/group
        dim[2]=(dim[2]-size+2*pad)/stride+1
        dim[3]=(dim[3]-size+2*pad)/stride+1
        layername.setText(2,str(dim[0]))
        layername.setText(3,str(dim[1]))
        layername.setText(4,str(dim[2]))
        layername.setText(5,str(dim[3]))
        print dim


    def onIndexChange(self,i):
        if(i==0):
            self.loadTreeWidget()
            self.treeWidget.setVisible(True)
            self.textEdit.setVisible(False)
            return
        if(i==1):
            self.treeWidget.setVisible(False)
            self.textEdit.setVisible(True)
            return
    def loadCurrentData(self):
        return self.protohandler.layer[self.treeWidget.currentIndex().row()-1].__str__()
    def setCurrentData(self):
        pass
    def onItemChangedSlot(self):
	if(self.trainMode==False):
	    self.protohandler.input_dim[0]=int(str(self.treeWidget.currentItem().text(2)))
	    self.protohandler.input_dim[1]=int(str(self.treeWidget.currentItem().text(3)))
	    self.protohandler.input_dim[2]=int(str(self.treeWidget.currentItem().text(4)))
	    self.protohandler.input_dim[3]=int(str(self.treeWidget.currentItem().text(5)))
	    self.textEdit.setText(self.protohandler.__str__())
	    self.loadTreeWidget()

	else:

	    self.dim=[int(str(self.treeWidget.currentItem().text(2))),\
	    int(str(self.treeWidget.currentItem().text(3))),\
	    int(str(self.treeWidget.currentItem().text(4))),\
	    int(str(self.treeWidget.currentItem().text(5)))]
	    self.textEdit.setText(self.protohandler.__str__())
   
 
	    self.loadTreeWidget()

if __name__== "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = MyForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

