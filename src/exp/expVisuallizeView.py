# -*- coding: utf-8 -*-
##############
# Written by : Jaley Dholakiya
# Video Analytics Lab,IISc
#############


# Form implementation generated from reading ui file 'expVisuallizeView.ui'
#
# Created: Tue Apr  7 15:59:44 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

import os
import sys
root =os.getenv('EXPRESSO_ROOT')
import h5py
import numpy as np
#OPERATION HANDLER FOR ALL OPERATIONS
import scipy
import scipy.misc
#import OperationHandler


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self,parent=None):
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 591)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(150,150,90);"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(330, 0, 271, 33))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(90,90,57);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox_2 = QtGui.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(40, 38, 171, 27))
        self.comboBox_2.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);\n"
"font: 10pt \"Ubuntu Condensed\";"))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 0, 271, 33))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";color:rgb(230,240,210);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.comboBox_3 = QtGui.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(320, 37, 81, 27))
        self.comboBox_3.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);\n"
"font: 10pt \"Ubuntu Condensed\";"))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_4 = QtGui.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(410, 37, 131, 27))
        self.comboBox_4.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);\n"
"font: 10pt \"Ubuntu Condensed\";"))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(219, 40, 90, 24))
        self.comboBox.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);\n"
"font: 10pt \"Ubuntu Condensed\";"))
        self.comboBox.setObjectName(_fromUtf8("spinBox"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 80, 500, 500))
        self.widget.setObjectName(_fromUtf8("widget"))
	self.widget.setStyleSheet('background-color:rgba(230,240,210,0)')
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

	#Name Mapping
	#spinBox => imageNumber
	#comboBox_2=>Experiment Selector
	#comboBox_3=>Max Pooling/MinPooling
	#comboBox_4=>Layers in the Experiment 
	#widget=> Container for the label


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", "Feature Visuallization", None))
        self.label_6.setText(_translate("Form", "Deploy Net Selection", None))
	#Initiallize the Combo Boxes
	self.comboBox.addItems(['PER LAYER','PER IMAGE'])
	self.comboBox_3.addItems(['MAX POOL','SUM POOL'])
	for elem in os.listdir(root+'/exp/data'):
	    print elem	
	    if elem.endswith('.hdf5'):self.comboBox_2.addItem(elem[0:-5])
	#Initiallize last ComboBox by index 0 Element
	print 'FIRST',self.comboBox_2.itemText(0)
	if(self.comboBox_2.currentText().__str__()!=""):
	    with h5py.File(root+'/exp/data/'+self.comboBox_2.currentText().__str__()+'.hdf5','r') as f:self.comboBox_4.addItems(f.keys())
	
	self.initiallizeTriggers();
	#self.comboBox_2.currentIndexChang
        pixmap = QtGui.QPixmap(root+'/res/exp/icon.png')
        lbl = QtGui.QLabel(self.widget)
        lbl.setPixmap(pixmap.scaled(500,500,QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.FastTransformation))

    def fillList(self):
	self.comboBox_2.clear()
	for elem in os.listdir(root+'/exp/data'):
	    print elem	
	    if elem.endswith('.hdf5'):self.comboBox_2.addItem(elem[0:-5])
	self.expChangedSlot()

    def initiallizeTriggers(self):
	self.comboBox_2.currentIndexChanged.connect(self.expChangedSlot)
	self.comboBox.currentIndexChanged.connect(self.viewChangedSlot)	
	self.comboBox_3.currentIndexChanged.connect(self.commonSlot)
	self.comboBox_4.currentIndexChanged.connect(self.commonSlot)

    def disconnectTriggers(self):
	self.comboBox_2.currentIndexChanged.disconnect(self.expChangedSlot)
	self.comboBox.currentIndexChanged.disconnect(self.viewChangedSlot)	
	self.comboBox_3.currentIndexChanged.disconnect(self.commonSlot)
	self.comboBox_4.currentIndexChanged.disconnect(self.commonSlot)


    def expChangedSlot(self,index=0):
	self.comboBox_4.clear()
	self.comboBox.setCurrentIndex(0)
	self.comboBox_3.setCurrentIndex(0)
	if(self.comboBox_2.currentText().__str__()==""):return
	with h5py.File(root+'/exp/data/'+self.comboBox_2.currentText().__str__()+'.hdf5','r') as f:self.comboBox_4.addItems(f.keys())
	self.commonSlot()

    def viewChangedSlot(self,index=0):
	self.comboBox_4.clear()
	if(index==0):
	    if(self.comboBox_2.currentText().__str__()==""):return
	    with h5py.File(root+'/exp/data/'+self.comboBox_2.currentText().__str__()+'.hdf5','r') as f:	
	    	lst=f.keys()
		if 'label' in f.keys(): lst.remove('label')
		self.comboBox_4.addItems(lst)
	if(index==1):
	    if(self.comboBox_2.currentText().__str__()==""):return
	    with h5py.File(root+'/exp/data/'+self.comboBox_2.currentText().__str__()+'.hdf5','r') as f:self.comboBox_4.addItems([str(x) for x in range(f[f.keys()[0]].shape[0])])
	self.commonSlot()

    def commonSlot(self,index=0):
	pass
	#CommonSlot
	#Case I  = PER LAYER
	if(self.comboBox.currentIndex()==0):
	    if(self.comboBox_2.currentText().__str__()==""):return
	    with h5py.File(root+'/exp/data/'+self.comboBox_2.currentText().__str__()+'.hdf5','r') as f: 
		if(self.comboBox_4.currentText().__str__() not in f.keys()): return
		self.vis_square(f[self.comboBox_4.currentText().__str__()],pooltype=self.comboBox_3.currentIndex())
	    return
	#Case II = PER IMAGE
	if(self.comboBox.currentIndex()==1):
	    if(self.comboBox_2.currentText().__str__()=="" or self.comboBox_4.currentText().__str__()==""):return
	    with h5py.File(root+'/exp/data/'+self.comboBox_2.currentText().__str__()+'.hdf5','r') as f: 
		#Idea is to create data array for sending it to vis_square as layers x width x height for a particular image
		data=[]
		lst=f.keys();
		if 'label' in lst:lst.remove('label')
		for k in lst:
		    if(self.comboBox_3.currentIndex()==0):
		        data.append(scipy.misc.imresize(f[k][self.comboBox_4.currentText()].max(axis=0),[500,500]))
		    else:
		        data.append(scipy.misc.imresize(f[k][self.comboBox_4.currentText()].sum(axis=0),[500,500]))

		data=np.array(data,np.float32)

		self.vis_square(data)

############## VISUALIZING ############################

    def vis_square(self,data, padsize=1, padval=0,pooltype=None):
	print 'Entered Vis_square'
        import matplotlib.pyplot as plt
	#First of All do the Pooling operation on third Dimension
	data=np.array(data,dtype=np.float32)
	if(len(data.shape)==2):return
	if(pooltype!=None):
	    data=data.max(axis=1) if pooltype==0 else data.sum(axis=1)
	print data.shape
	#Pooling Ends
        print data.min()
        data -= data.min()
        data /= data.max()

        # force the number of filters to be square
        n = int(np.ceil(np.sqrt(data.shape[0])))
        padding = ((0, n ** 2 - data.shape[0]), (0, padsize), (0, padsize)) + ((0, 0),) * (data.ndim - 3)
        data = np.pad(data, padding, mode='constant', constant_values=(padval, padval))

        # tile the filters into an image
        data = data.reshape((n, n) + data.shape[1:]).transpose((0, 2, 1, 3) + tuple(range(4, data.ndim + 1)))
        data = data.reshape((n * data.shape[1], n * data.shape[3]) + data.shape[4:])
        plt.axis('off')


        plt.imshow(data)
        #Jaley Start
        plt.savefig('temp.png',bbox_inches='tight')
        self.update_display()
        #Jaley End
#Updating Display
    def update_display(self):
        pixmap = QtGui.QPixmap('temp.png')
        lbl = QtGui.QLabel(self.widget)
        lbl.setPixmap(pixmap.scaled(500,500,QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.FastTransformation))
        lbl.show()

    def refreshTrigger(self):
	self.disconnectTriggers()	
	self.comboBox_2.clear()
	for elem in os.listdir(root+'/exp/data'):
	    print elem	
	    if elem.endswith('.hdf5'):self.comboBox_2.addItem(elem[0:-5])
	#Initiallize last ComboBox by index 0 Element
	print 'FIRST',self.comboBox_2.itemText(0)
	if(self.comboBox_2.currentText().__str__()!=""):
	    with h5py.File(root+'/exp/data/'+self.comboBox_2.currentText().__str__()+'.hdf5','r') as f:self.comboBox_4.addItems(f.keys())

	self.initiallizeTriggers();



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

