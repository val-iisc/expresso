# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solverView.ui'
#
# Created: Fri Mar 13 20:38:43 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os


root=os.getenv('EXPRESSO_ROOT')
#Jaley Start
import sys

sys.path.append(os.getenv('CAFFE_ROOT')+'/python/caffe/proto')
from google.protobuf import text_format
import caffe_pb2

sys.path.append(root+'/src/net/config')
import netConfig_pb2


import os


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
    def __init__(self,parent=None,index=None):
        super(Ui_Form,self).__init__(parent)
	self.index=index
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 591)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(120, 180, 120)"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 10, 551, 91))
        self.widget.setStyleSheet(_fromUtf8("background-color:rgb(150,195,150)"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 481, 17))
        self.label_2.setStyleSheet(_fromUtf8("font: oblique 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.widget1 = QtGui.QWidget(self.widget)
        self.widget1.setGeometry(QtCore.QRect(20, 10, 291, 35))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(45, 60, 45)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEditTestIteration = QtGui.QLineEdit(self.widget1)
        self.lineEditTestIteration.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.lineEditTestIteration.setObjectName(_fromUtf8("lineEditTestIteration"))
        self.horizontalLayout.addWidget(self.lineEditTestIteration)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(20, 110, 551, 91))
        self.widget_2.setStyleSheet(_fromUtf8("background-color:rgb(150,195,150)"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_3 = QtGui.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 501, 17))
        self.label_3.setStyleSheet(_fromUtf8("font: oblique 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.layoutWidget = QtGui.QWidget(self.widget_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 291, 35))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(45, 60, 45)"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEditTestInterval = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditTestInterval.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.lineEditTestInterval.setObjectName(_fromUtf8("lineEditTestInterval"))
        self.horizontalLayout_2.addWidget(self.lineEditTestInterval)
        self.widget_3 = QtGui.QWidget(Form)
        self.widget_3.setGeometry(QtCore.QRect(20, 210, 551, 91))
        self.widget_3.setStyleSheet(_fromUtf8("background-color:rgb(150,195,150)"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.label_7 = QtGui.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 501, 17))
        self.label_7.setStyleSheet(_fromUtf8("font: oblique 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.layoutWidget_3 = QtGui.QWidget(self.widget_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 10, 141, 31))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_8 = QtGui.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(45, 60, 45)"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_4.addWidget(self.label_8)
        self.lineEditBaseLr = QtGui.QLineEdit(self.layoutWidget_3)
        self.lineEditBaseLr.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.lineEditBaseLr.setObjectName(_fromUtf8("lineEditBaseLr"))
        self.horizontalLayout_4.addWidget(self.lineEditBaseLr)
        self.layoutWidget_4 = QtGui.QWidget(self.widget_3)
        self.layoutWidget_4.setGeometry(QtCore.QRect(170, 10, 161, 34))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_9 = QtGui.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(45, 60, 45)"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_5.addWidget(self.label_9)
        self.lineEditMomentum = QtGui.QLineEdit(self.layoutWidget_4)
        self.lineEditMomentum.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.lineEditMomentum.setObjectName(_fromUtf8("lineEditMomentum"))
        self.horizontalLayout_5.addWidget(self.lineEditMomentum)
        self.layoutWidget_5 = QtGui.QWidget(self.widget_3)
        self.layoutWidget_5.setGeometry(QtCore.QRect(340, 10, 191, 34))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_10 = QtGui.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(45, 60, 45)"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_6.addWidget(self.label_10)
        self.lineEditWeightDecay = QtGui.QLineEdit(self.layoutWidget_5)
        self.lineEditWeightDecay.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.lineEditWeightDecay.setObjectName(_fromUtf8("lineEditWeightDecay"))
        self.horizontalLayout_6.addWidget(self.lineEditWeightDecay)
        self.widget_4 = QtGui.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(20, 310, 551, 171))
        self.widget_4.setStyleSheet(_fromUtf8("background-color:rgb(150,195,150)"))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.label_11 = QtGui.QLabel(self.widget_4)
        self.label_11.setGeometry(QtCore.QRect(20, 60, 511, 17))
        self.label_11.setStyleSheet(_fromUtf8("font: oblique 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.layoutWidget_6 = QtGui.QWidget(self.widget_4)
        self.layoutWidget_6.setGeometry(QtCore.QRect(20, 10, 141, 34))
        self.layoutWidget_6.setObjectName(_fromUtf8("layoutWidget_6"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_7.setMargin(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_12 = QtGui.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(45, 60, 45)"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_7.addWidget(self.label_12)
        self.lineEditDisplay = QtGui.QLineEdit(self.layoutWidget_6)
        self.lineEditDisplay.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.lineEditDisplay.setObjectName(_fromUtf8("lineEditDisplay"))
        self.horizontalLayout_7.addWidget(self.lineEditDisplay)
        self.layoutWidget_7 = QtGui.QWidget(self.widget_4)
        self.layoutWidget_7.setGeometry(QtCore.QRect(170, 10, 161, 34))
        self.layoutWidget_7.setObjectName(_fromUtf8("layoutWidget_7"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_8.setMargin(0)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label_13 = QtGui.QLabel(self.layoutWidget_7)
	#Added Later
	self.pushButtonUpload = QtGui.QPushButton(Form)
        self.pushButtonUpload.setGeometry(QtCore.QRect(460, 438, 100, 32))
        self.pushButtonUpload.setStyleSheet(_fromUtf8("font: 12pt \"Ubuntu Condensed\";background-color:rgb(225, 225, 210)"))
	#Added Later Ends

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(45, 60, 45)"))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_8.addWidget(self.label_13)
        self.lineEditMaxIteration = QtGui.QLineEdit(self.layoutWidget_7)
        self.lineEditMaxIteration.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.lineEditMaxIteration.setObjectName(_fromUtf8("lineEditMaxIteration"))
        self.horizontalLayout_8.addWidget(self.lineEditMaxIteration)
        self.layoutWidget_8 = QtGui.QWidget(self.widget_4)
        self.layoutWidget_8.setGeometry(QtCore.QRect(340, 10, 191, 34))
        self.layoutWidget_8.setObjectName(_fromUtf8("layoutWidget_8"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_14 = QtGui.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(45, 60, 45)"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_9.addWidget(self.label_14)
        self.lineEditSnapshot = QtGui.QLineEdit(self.layoutWidget_8)
        self.lineEditSnapshot.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.lineEditSnapshot.setObjectName(_fromUtf8("lineEditSnapshot"))
        self.horizontalLayout_9.addWidget(self.lineEditSnapshot)
        self.label_15 = QtGui.QLabel(self.widget_4)
        self.label_15.setGeometry(QtCore.QRect(20, 80, 511, 17))
        self.label_15.setStyleSheet(_fromUtf8("font: oblique 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.widget_4)
        self.label_16.setGeometry(QtCore.QRect(20, 100, 511, 17))
        self.label_16.setStyleSheet(_fromUtf8("font: oblique 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.layoutWidget_9 = QtGui.QWidget(self.widget_4)
        self.layoutWidget_9.setGeometry(QtCore.QRect(20, 130, 146, 34))
        self.layoutWidget_9.setObjectName(_fromUtf8("layoutWidget_9"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.layoutWidget_9)
        self.horizontalLayout_10.setMargin(0)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_17 = QtGui.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(45, 60, 45)"))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_10.addWidget(self.label_17)
        self.comboBoxSelectModel = QtGui.QComboBox(self.layoutWidget_9)
        self.comboBoxSelectModel.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210);selection-color:rgb(0,0,0);selection-background-color:rgba(255,255,255,100);"))
        self.comboBoxSelectModel.setObjectName(_fromUtf8("comboBoxSelectModel"))
        self.horizontalLayout_10.addWidget(self.comboBoxSelectModel)
        self.label_18 = QtGui.QLabel(self.widget_4)
        self.label_18.setGeometry(QtCore.QRect(180, 140, 511, 17))
        self.label_18.setStyleSheet(_fromUtf8("font: oblique 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.widget_6 = QtGui.QWidget(Form)
        self.widget_6.setGeometry(QtCore.QRect(20, 500, 551, 71))
        self.widget_6.setStyleSheet(_fromUtf8("background-color:rgb(180,195,150)"))
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.pushButtonSave = QtGui.QPushButton(self.widget_6)
        self.pushButtonSave.setGeometry(QtCore.QRect(450, 30, 75, 32))
        self.pushButtonSave.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(225, 225, 210)"))
        self.pushButtonSave.setObjectName(_fromUtf8("pushButtonSave"))
	self.widget_6.hide()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_2.setText(_translate("Form", "Total number of Forward passes a test has to carry out", None))
        self.label.setText(_translate("Form", "Test Iteration         ", None))
        self.label_3.setText(_translate("Form", "Total number of training iterations, after which Testing is conducted", None))
        self.label_4.setText(_translate("Form", "Test Interval            ", None))
        self.label_7.setText(_translate("Form", "The base learning rate, momentum and the weight decay of the network.", None))
        self.label_8.setText(_translate("Form", "Base Lr", None))
        self.label_9.setText(_translate("Form", "Momentum", None))
        self.label_10.setText(_translate("Form", "Weight Decay", None))
        self.label_11.setText(_translate("Form", "Display contains value of iterations after which, current state is displayed", None))
        self.label_12.setText(_translate("Form", "Display", None))
        self.label_13.setText(_translate("Form", "Max Iteration", None))
        self.label_14.setText(_translate("Form", "Snapshot", None))
        self.label_15.setText(_translate("Form", "Max Iterations  is upper limit for training iterations", None))
        self.label_16.setText(_translate("Form", "Snapshot is interval after which intermediate paramters are stored", None))
        self.label_17.setText(_translate("Form", "lr policy", None))
        self.comboBoxSelectModel.addItems(['fixed','step'])
        #self.label_18.setText(_translate("Form", "Internal Method for learning", None))
        self.pushButtonSave.setText(_translate("Form", "Save", None))
        self.pushButtonUpload.setText(_translate("Form", "Upload/Change", None))
	self.loadSolverParameters()
	#Added by Jaley 
	self.labelGamma=QtGui.QLabel(Form)
	self.labelGamma.setText("Gamma")
	self.labelGamma.setGeometry(QtCore.QRect(230,430,150,50))
        self.labelGamma.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(45, 60, 45);background-color:rgba(0,0,0,0)"))
	self.lineEditGamma = QtGui.QLineEdit(Form)
        self.lineEditGamma.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
	self.lineEditGamma.setGeometry(QtCore.QRect(290,437,150,33))
	
	self.pushButtonUpload.clicked.connect(self.onUploadClicked)	


	#Added by Jaley Ends

	self.fillData()	

    def loadSolverParameters(self):
	self.data=open(root+'/net/netData.prototxt').read()
	self.netHandler=netConfig_pb2.Param();
        text_format.Merge(self.data,self.netHandler)
	self.protoHandler=caffe_pb2.SolverParameter()
	if(self.index!=None and len(self.netHandler.net)>0):
	    text_format.Merge(open(self.netHandler.net[self.index].solverpath).read(),self.protoHandler)
	else:
	    text_format.Merge(open(root+'/src/custom/defaultSolver.prototxt').read(),self.protoHandler)
	print self.protoHandler



    def fillData(self):
	if(len(self.protoHandler.test_iter)>0):self.lineEditTestIteration.setText(str(self.protoHandler.test_iter[0]))
	else:self.lineEditTestIter.setText("")
	if(self.protoHandler.HasField('test_interval')):self.lineEditTestInterval.setText(str(self.protoHandler.test_interval))
	else:self.lineEditTestInterval.setText("")
	if(self.protoHandler.HasField('momentum')):self.lineEditMomentum.setText(str(self.protoHandler.momentum))
	else:self.lineEditMomentum.setText("")
	if(self.protoHandler.HasField('base_lr')):self.lineEditBaseLr.setText(str(self.protoHandler.base_lr))
	else:self.lineEditBaseLr.setText("")
	if(self.protoHandler.HasField('weight_decay')):self.lineEditWeightDecay.setText(str(self.protoHandler.weight_decay))
	else:self.protoHandler.setText("")
	if(self.protoHandler.HasField('display')):self.lineEditDisplay.setText(str(self.protoHandler.display))
	else:self.lineEditDisplay.setText("")
	self.lineEditMaxIteration.setText(str(self.protoHandler.max_iter))
	if(self.protoHandler.HasField('snapshot')):self.lineEditSnapshot.setText(str(self.protoHandler.snapshot))
	else:self.lineEditSnapshot.setText("")
	#self.lineEditSnapshot.setText(str(self.protoHandler.snapshot))
	if(self.protoHandler.HasField('gamma')):self.lineEditGamma.setText(str(self.protoHandler.gamma))
	else:self.lineEditGamma.setText("")
	
	
    def updateHandle(self):
	if self.lineEditTestIteration.text().__str__()!="":self.protoHandler.test_iter[0]=int(self.lineEditTestIteration.text().__str__())

	if self.lineEditTestInterval.text().__str__()!="":self.protoHandler.test_interval=int(self.lineEditTestInterval.text().__str__())

	if self.lineEditMomentum.text().__str__()!="":self.protoHandler.momentum=float(self.lineEditMomentum.text().__str__())

	if self.lineEditBaseLr.text().__str__()!="":self.protoHandler.base_lr=float(self.lineEditBaseLr.text().__str__())

	if self.lineEditWeightDecay.text().__str__()!="":self.protoHandler.weight_decay=float(self.lineEditWeightDecay.text().__str__())

	if self.lineEditDisplay.text().__str__()!="":self.protoHandler.display=int(self.lineEditDisplay.text().__str__())


	if self.lineEditMaxIteration.text().__str__()!="":self.protoHandler.max_iter=int(self.lineEditMaxIteration.text().__str__())

	if self.lineEditSnapshot.text().__str__()!="":self.protoHandler.snapshot=int(self.lineEditSnapshot.text().__str__())

	if self.lineEditGamma.text().__str__()!="":self.protoHandler.gamma=float(self.lineEditGamma.text().__str__())



	#Set Fields
	pass
		
    def onUploadClicked(self):
	print 'Upload Button Clicked'
	path=QtGui.QFileDialog.getOpenFileName(self,self.tr("Open File"),root)	
	if(path!="" and path.endsWith(".prototxt")):
	    print path
	    if(not os.path.exists(path)): return
	    with open(path,'r') as f:
		print path,'EXISTS'
	        self.protoHandler=caffe_pb2.SolverParameter()
	        text_format.Merge(f.read(),self.protoHandler)
	        self.fillData()
		print 'DATA FILLED'


	print 'Help'	
    def saveConfig(self,filename):
	self.updateHandle()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

