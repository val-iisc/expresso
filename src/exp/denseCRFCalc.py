# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'denseCRFCalc.ui'
#
# Created: Mon Jun  1 23:05:53 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import os
import sys
import numpy as np
root=os.getenv('EXPRESSO_ROOT')


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
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
	self.denseExpName=''
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 586)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(150,150,90)"))
        self.widget = pg.PlotWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 310, 251, 251))
        self.widget.setStyleSheet(_fromUtf8("background-color:rgb(210,210,150)"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 270, 201, 31))
        self.label.setStyleSheet(_fromUtf8("color:rgb(255,255,225);\n"
"font: 14pt \"Ubuntu Condensed\";"))
        self.label.setObjectName(_fromUtf8("label"))
	self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(320, 410, 81, 31))
        self.label_3.setStyleSheet(_fromUtf8("color:rgb(255,255,225);\n"
"font: 18pt \"Ubuntu Condensed\";"))
        self.label_3.setObjectName(_fromUtf8("label_4"))

        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(320, 460, 81, 31))
        self.label_4.setStyleSheet(_fromUtf8("color:rgb(255,255,225);\n"
"font: 18pt \"Ubuntu Condensed\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(190, 20, 231, 31))
        self.label_5.setStyleSheet(_fromUtf8("color:rgb(255,255,225);\n"
"font: 24pt \"Ubuntu Condensed\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(320, 510, 121, 31))
        self.label_6.setStyleSheet(_fromUtf8("color:rgb(255,255,225);\n"
"font: 18pt \"Ubuntu Condensed\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(480, 460, 91, 27))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgb(225,225,180)"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 510, 91, 27))
        self.lineEdit_2.setStyleSheet(_fromUtf8("background-color:rgb(225,225,180)"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(110, 160, 161, 31))
        self.comboBox.setStyleSheet(_fromUtf8("background-color:rgb(225,225,180)"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
	self.doubleSpinBox=QtGui.QDoubleSpinBox(Form)
	self.doubleSpinBox.setGeometry(480, 410, 91, 27)
	self.doubleSpinBox.setStyleSheet(_fromUtf8("background-color:rgb(225,225,180)"))
	self.doubleSpinBox.setMaximum(1)
	self.doubleSpinBox.setMinimum(0)
	self.doubleSpinBox.setValue(0.5)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 160, 81, 31))
        self.label_7.setStyleSheet(_fromUtf8("color:rgb(255,255,225);\n"
"font: 18pt \"Ubuntu Condensed\";"))
        self.label_7.setObjectName(_fromUtf8("label_7"))

	self.pushButtonRefresh=QtGui.QPushButton(Form)
	self.pushButtonRefresh.setGeometry(QtCore.QRect(360,160,100,30))
	self.pushButtonRefresh.setStyleSheet("color:rgb(255,255,255);background-color:rgb(120,120,75)")
	self.comboBox.addItem('iou(50%)')
	self.pushButtonRefresh.setText("Refresh")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Accuracy Curve", None))
	self.label_3.setText("IOU")
        self.label_4.setText(_translate("Form", "Accuracy", None))
        self.label_5.setText(_translate("Form", "Dense CRF Results", None))
        self.label_6.setText(_translate("Form", "Avg Overlap", None))
        self.label_7.setText(_translate("Form", "Metric", None))
	self.dataExpName=""
	self.initialize()

    def refreshTrigger(self,denseExpName=""):
	self.denseExpName=denseExpName
	self.initialize()

    def initialize(self):
	if(self.denseExpName==''):return
	self.dataLen=0;
	self.data={}
	self.data['unionVal']=[]
	self.data['intersectionVal']=[]
	self.data['totalAreaGT']=[]
	self.data['totalAreaDenseCRF']=[]
	self.data['overallArea']=[]
	
	for idx,elem in enumerate(open(root+'/exp/denseCRF/data/'+self.denseExpName+'/results.txt','r').readlines()):
	    if(idx==0):continue
	    elem=elem.replace('\n','')
	    dataIter=[int(items) for items in elem.split(' ')]
	    self.data['unionVal'].append(dataIter[0])
	    self.data['intersectionVal'].append(dataIter[1])
	    self.data['totalAreaGT'].append(dataIter[2])
	    self.data['totalAreaDenseCRF'].append(dataIter[3])
	    self.data['overallArea'].append(dataIter[4])
	self.dataLen=len(self.data['overallArea'])    
	self.plotPrecisionRecall()

    def plotPrecisionRecall(self):
	if(self.dataLen==0):return
	iouArray=[float(self.data['intersectionVal'][i])/float(self.data['unionVal'][i]) for i in range(self.dataLen)]
	thresholdArray=np.arange(0,1,0.01)
	resultArray=[]
	for elem in thresholdArray:
	    correct=sum([int(item>elem) for item in iouArray])
	    resultArray.append(float(correct)/float(self.dataLen))
	self.widget.clear()
	self.widget.plot(resultArray,thresholdArray)

	overlapPerc=float(sum(self.data['intersectionVal']))/float(sum(self.data['unionVal']))
	accuracy50=float(sum([elem>float(self.doubleSpinBox.value()) for elem in iouArray]))/float(len(iouArray))

	self.lineEdit_2.setText(str(float("{0:.9f}".format(overlapPerc))*100))
	self.lineEdit.setText(str(float("{0:.9f}".format(accuracy50))*100))

	

    def plotHistogram(self):
	pass	
		
	

	    

    def changeView(self):
	line=np.sin(np.arange(255)*0.1)
        plothandle=self.widget.plot(np.array(range(len(line)))*10,line, clear=True)
	



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

