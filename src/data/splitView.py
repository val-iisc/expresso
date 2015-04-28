# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splitView.ui'
#
# Created: Fri Apr 17 20:40:25 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import os
root=os.getenv('EXPRESSO_ROOT')
import h5py
import numpy as np
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

class Ui_Form(QtGui.QWidget):
    def __init__(self, parent=None,dataName=None):
        super(Ui_Form, self).__init__(parent)
        self.dataName=dataName
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(421, 232)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 161, 31))
        self.label.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(330, 150, 62, 27))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.horizontalSlider = QtGui.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(30, 90, 351, 29))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(90, 150, 81, 27))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 150, 61, 31))
        self.label_2.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(240, 150, 111, 31))
        self.label_3.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 190, 131, 31))
        self.label_4.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_4 = QtGui.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(263, 200, 71, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 200, 71, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Split Data", None))
        self.label_2.setText(_translate("Form", "Split", None))
        self.label_3.setText(_translate("Form", "Percentage", None))
        self.label_4.setText(_translate("Form", "Total : ", None))
        self.pushButton_4.setText(_translate("Form", "Cancel", None))
        self.pushButton_3.setText(_translate("Form", "Ok", None))
	self.fillData()
	self.horizontalSlider.valueChanged.connect(self.onHorizontalSliderValueChanged)
	self.spinBox.valueChanged.connect(self.onSpinBoxValueChanged)
	self.doubleSpinBox.valueChanged.connect(self.onDoubleSpinBoxValueChanged)
	self.pushButton_3.clicked.connect(self.onOkClicked)
    def fillData(self):
	if(self.dataName==None):return
	dataPath=root+'/data/'+self.dataName+'.hdf5'
	if(not os.path.exists(dataPath)): return
	#Initiallize the data
	self.hasLabel=False
	with h5py.File(dataPath,'r') as f:
	    if('label' in f.keys()):self.hasLabel=True
	    dataSize=f['data'].shape[0]
	    self.dataSize=dataSize
	    self.label_4.setText("Total : "+str(dataSize))
	    self.horizontalSlider.setMaximum(dataSize)
	    self.doubleSpinBox.setMaximum(100)
	    self.spinBox.setMaximum(dataSize)
	    self.horizontalSlider.setMinimum(0)
	    self.spinBox.setMinimum(0)
	    self.doubleSpinBox.setMinimum(0) 


    def onHorizontalSliderValueChanged(self,value):
	self.horizontalSlider.setValue(value)
	self.spinBox.setValue(value)
	self.doubleSpinBox.setValue(100*float(value)/float(self.dataSize))
		
    def onSpinBoxValueChanged(self,value):
	self.horizontalSlider.setValue(value)
	self.spinBox.setValue(value)
	self.doubleSpinBox.setValue(100*float(value)/float(self.dataSize))


	
    def onDoubleSpinBoxValueChanged(self,value):
	sliderVal=self.horizontalSlider.setValue(int(value*self.dataSize/100))
	spinBoxVal=self.spinBox.setValue(int(value*self.dataSize/100))
	doubleSpinBoxVal=self.doubleSpinBox.setValue(value)

    def onOkClicked(self):
	#On Ok Clicked
	value=self.horizontalSlider.value()

	with h5py.File(root+'/data/'+self.dataName+'_split1.hdf5','w') as fw:
	    f=h5py.File(root+'/data/'+self.dataName+'.hdf5','r')
            comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
	    #Writing the data
	    fw.create_dataset('data',data=f['data'][:value],**comp_kwargs)
	    if('label' in f.keys()):fw.create_dataset('label',data=f['label'][:value],**comp_kwargs)

	    #Writing the data Ends
	    f.close()
	with h5py.File(root+'/data/'+self.dataName+'_split2.hdf5','w') as fw:
	    f=h5py.File(root+'/data/'+self.dataName+'.hdf5','r')
            comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
	    #Writing the data
	    fw.create_dataset('data',data=f['data'][value:],**comp_kwargs)	
	    if('label' in f.keys()):fw.create_dataset('label',data=f['label'][value:],**comp_kwargs)
	    #Writing the data Ends
	    f.close()

	self.closeSlot()

    def closeSlot(self):
	print 'Widget Closed'
	self.close()
	

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

