# -*- coding: utf-8 -*-
##############
# Written by : Jaley Dholakiya
# Video Analytics Lab,IISc
#############


# Form implementation generated from reading ui file 'pipelineView.ui'
#
# Created: Tue Apr  7 15:57:03 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import sys
import os
sys.path.append(os.getenv('EXPRESSO_ROOT')+'/src/functions')
import FunctionHandler

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
    signalUpdateTriggered=QtCore.pyqtSignal(object)
    def __init__(self,parent=None):
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(291, 301)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(150,150,90);"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 121, 111))
        self.listWidget.setStyleSheet(_fromUtf8("font: 11pt \"Ubuntu Condensed\";background-color:rgb(230,240,210);color:rgb(45,60,45)"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 221, 31))
        self.label.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget_2 = QtGui.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(160, 30, 121, 111))
        self.listWidget_2.setStyleSheet(_fromUtf8("font: 11pt \"Ubuntu Condensed\";background-color:rgb(230,240,210);color:rgb(45,60,45)"))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(134, 42, 23, 20))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))

	self.toolButton.setStyleSheet('color:rgba(255,255,255,175);background-color:rgba(0,0,0,100);')
        self.toolButton_2 = QtGui.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(134, 81, 23, 20))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
	self.toolButton_2.setStyleSheet('color:rgba(255,255,255,175);background-color:rgba(0,0,0,100);')
        self.toolButton_3 = QtGui.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(134, 121, 23, 20))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.toolButton_5 = QtGui.QToolButton(Form)
        self.toolButton_5.setGeometry(QtCore.QRect(54, 165, 75, 20))
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
	self.toolButton_5.setStyleSheet('color:rgba(255,255,255,175);background-color:rgba(0,0,0,100);')
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 162, 41, 61))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.layoutWidget_2 = QtGui.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 240, 71, 62))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.spinBoxMax = QtGui.QSpinBox(self.layoutWidget_2)
        self.spinBoxMax.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);"))
        self.spinBoxMax.setObjectName(_fromUtf8("spinBoxMax"))
        self.verticalLayout_2.addWidget(self.spinBoxMax)
        self.spinBoxMin = QtGui.QSpinBox(self.layoutWidget_2)
        self.spinBoxMin.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);"))
        self.spinBoxMin.setObjectName(_fromUtf8("spinBoxMin"))
	self.spinBoxMax.hide()
	self.spinBoxMin.hide()
	self.layoutWidget_2.hide()


        self.verticalLayout_2.addWidget(self.spinBoxMin)
        self.layoutWidget_3 = QtGui.QWidget(Form)
        self.layoutWidget_3.setGeometry(QtCore.QRect(50, 240, 81, 66))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalSliderAlpha = QtGui.QSlider(self.layoutWidget_3)
        self.horizontalSliderAlpha.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderAlpha.setObjectName(_fromUtf8("horizontalSliderAlpha"))
        self.verticalLayout_4.addWidget(self.horizontalSliderAlpha)
        self.horizontalSliderBeta = QtGui.QSlider(self.layoutWidget_3)
        self.horizontalSliderBeta.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderBeta.setObjectName(_fromUtf8("horizontalSliderBeta"))
	self.horizontalSliderAlpha.setMaximum(1000)
	self.horizontalSliderBeta.setMaximum(1000)
        self.verticalLayout_4.addWidget(self.horizontalSliderBeta)
        self.layoutWidget_4 = QtGui.QWidget(Form)
        self.layoutWidget_4.setGeometry(QtCore.QRect(3, 235, 51, 71))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
	self.labelParameters=QtGui.QLabel(Form)
	self.labelParameters.setGeometry(QtCore.QRect(10,210,100,20))
	self.labelParameters.setText('Parameters')
        self.labelParameters.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
	
	
        self.label_2 = QtGui.QLabel(self.layoutWidget_4)
        self.label_2.setStyleSheet(_fromUtf8("font: 11pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget_4)
        self.label_3.setStyleSheet(_fromUtf8("font: 11pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(3, 141, 97, 22))
        self.checkBox.setStyleSheet(_fromUtf8("font: 12pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
	#Plot Widget Starts
        self.plotwidget = pg.PlotWidget(Form)
        self.plotwidget.setGeometry(QtCore.QRect(135, 147, 153, 153))
        self.plotwidget.setObjectName(_fromUtf8("plot"))
	self.funcList=[]
	#Plot Widget Ends
	#Function Handler Based Starts
	self.functionHandler=FunctionHandler.FunctionHandler()
	self.listWidget.addItems(self.functionHandler.getList())
	#Function Handler Based Ends
	self.lastClicked='left'
	self.initiallize();

	self.plotFunction()


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def plotFunction(self):
	if(self.param1==None):
	    self.label_2.setText('a(None)')
	else:
	    self.label_2.setText('a('+str(0.1*float(self.param1))+')')
	    self.horizontalSliderAlpha.setValue(self.param1)

	if(self.param2==None):
	    self.label_3.setText('b(None)')
	else:
	    self.label_3.setText('b('+str(0.1*float(self.param2))+')')
	    self.horizontalSliderBeta.setValue(self.param2)
        line=np.arange(100)
	if(self.funcName==None):
            plothandle=self.plotwidget.plot(line,line,clear=True)
	else:
            plothandle=self.plotwidget.plot(self.functionHandler.operate([[self.funcName,self.param1,self.param2]],data=line),clear=True)
	self.plotwidget.setXRange(0,100)
        if(self.checkBox.checkState()==2):self.signalUpdateTriggered.emit(self.funcList)

    def initiallize(self):
	self.funcName=None
	self.param1=None
	self.param2=None
	self.listWidget.clicked.connect(self.plotFromLeft)
	self.listWidget_2.clicked.connect(self.plotFromRight)
	self.horizontalSliderAlpha.valueChanged.connect(self.onParam1Changed)
	self.horizontalSliderBeta.valueChanged.connect(self.onParam2Changed)
	self.toolButton.clicked.connect(self.moveToRight)
	self.toolButton_2.clicked.connect(self.removeFromRight)
	self.toolButton_5.clicked.connect(self.submit)

    def onParam1Changed(self,value):
	self.param1=self.horizontalSliderAlpha.value()
	if(self.lastClicked=='right'):self.funcList[self.listWidget_2.currentRow()][1]=self.param1
	self.plotFunction()

    def onParam2Changed(self,value):
	self.param2=self.horizontalSliderBeta.value()
	if(self.lastClicked=='right'):self.funcList[self.listWidget_2.currentRow()][2]=self.param2
	self.plotFunction()


    def plotFromLeft(self):
	self.funcName=self.listWidget.currentItem().text().__str__()
	self.param1=None
	self.param2=None
	self.lastClicked='left'
	self.plotFunction()

    def plotFromRight(self):
	self.funcName=self.listWidget_2.currentItem().text().__str__()
	self.param1=self.funcList[self.listWidget_2.currentRow()][1]
	self.param2=self.funcList[self.listWidget_2.currentRow()][2]
	self.lastClicked='right'
	self.plotFunction()

    def submit(self):
	self.signalUpdateTriggered.emit(self.funcList)

    def moveToRight(self):
	self.funcList.append([self.funcName,self.param1,self.param2])
	self.listWidget_2.addItem(self.funcName)

	pass
    def removeFromRight(self):
	del self.funcList[self.listWidget_2.currentRow()]
	self.refreshRightList()

    def refreshRightList(self):
	self.listWidget_2.clear()
	self.listWidget_2.addItems([elem[0] for elem in self.funcList])

	   



    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Pipeline Operation", None))
        self.toolButton.setText(_translate("Form", "=>", None))
        self.toolButton_2.setText(_translate("Form", "x", None))
        self.toolButton_3.setText(_translate("Form", "r", None))
	self.toolButton_3.hide()
        self.toolButton_5.setText(_translate("Form", "Apply", None))
        self.label_4.setText(_translate("Form", "Max", None))
        self.label_5.setText(_translate("Form", "Min", None))
	self.label_4.hide()
	self.label_5.hide()
        self.label_2.setText(_translate("Form", "a", None))
        self.label_3.setText(_translate("Form", "b", None))
        self.checkBox.setText(_translate("Form", "On Fly", None))




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

