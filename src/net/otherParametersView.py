# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'otherParamtersView.ui'
#
# Created: Thu Apr  9 01:26:08 2015
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
root=os.getenv('EXPRESSO_ROOT')


sys.path.append(root+'/src/net/config')
import netConfig_pb2
from google.protobuf import text_format

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    def __init__(self,parent=None,index=None):
        self.index=index
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(591, 571)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(49,74,93)"))
        self.layoutWidget_10 = QtGui.QWidget(Form)
        self.layoutWidget_10.setGeometry(QtCore.QRect(150, 190, 391, 34))
        self.layoutWidget_10.setObjectName(_fromUtf8("layoutWidget_10"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout_13.setMargin(0)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.lineEditModelPath = QtGui.QLineEdit(self.layoutWidget_10)
        self.lineEditModelPath.setStyleSheet(_fromUtf8("font: 11pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.lineEditModelPath.setObjectName(_fromUtf8("lineEditModelPath"))
        self.horizontalLayout_13.addWidget(self.lineEditModelPath)
        self.pushButtonModelUpload = QtGui.QPushButton(Form)
        self.pushButtonModelUpload.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.pushButtonModelUpload.setGeometry(QtCore.QRect(42, 201, 191, 34))
        self.pushButtonModelUpload.setObjectName(_fromUtf8("pushButtonModelUpload"))
        #self.horizontalLayout_13.addWidget(self.pushButtonModelUpload)
        self.label_15 = QtGui.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(40, 200, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu Condensed\";color:rgb(50, 165, 211)"))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.checkBoxUseGPU = QtGui.QCheckBox(Form)
        self.checkBoxUseGPU.setGeometry(QtCore.QRect(280, 150, 91, 22))
        self.checkBoxUseGPU.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu Condensed\";color:rgb(50, 165, 211)"))
	self.lineEditGPUIndex=QtGui.QLineEdit(Form)
	self.lineEditGPUIndex.setGeometry(QtCore.QRect(410,210,75,27))
	self.lineEditGPUIndex.setStyleSheet('background-color:rgb(210, 225, 210);');
	self.lineEditGPUIndex.setText('0');
	self.lineEditGPUIndex.hide()
	self.labelUseGPUIndex=QtGui.QLabel(Form)
	self.labelUseGPUIndex.setGeometry(QtCore.QRect(300,210,100,27))
	self.labelUseGPUIndex.setText('GPU Index')
	self.labelUseGPUIndex.setStyleSheet('color:rgb(50, 165, 211);font: 16pt \"Ubuntu Condensed\";');
	self.labelUseGPUIndex.hide()
        self.checkBoxUseGPU.setObjectName(_fromUtf8("checkBoxUseGPU"))
        self.checkBoxChannelSwap = QtGui.QCheckBox(Form)
        self.checkBoxChannelSwap.setGeometry(QtCore.QRect(390, 150, 141, 22))
        self.checkBoxChannelSwap.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu Condensed\";color:rgb(50, 165, 211)"))
        self.checkBoxChannelSwap.setObjectName(_fromUtf8("checkBoxChannelSwap"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 150, 171, 34))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_9.setMargin(0)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu Condensed\";color:rgb(50, 165, 211)"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_9.addWidget(self.label_10)
        self.lineEditRawScale = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditRawScale.setStyleSheet(_fromUtf8("font: 11pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.lineEditRawScale.setObjectName(_fromUtf8("lineEditRawScale"))
	self.lineEditRawScale.setText('255')
        self.horizontalLayout_9.addWidget(self.lineEditRawScale)
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(40, 100, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu Condensed\";color:rgb(50, 165, 211)"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.layoutWidget_5 = QtGui.QWidget(Form)
        self.layoutWidget_5.setGeometry(QtCore.QRect(150, 90, 391, 34))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.lineEditMeanPath = QtGui.QLineEdit(self.layoutWidget_5)
        self.lineEditMeanPath.setStyleSheet(_fromUtf8("font: 11pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.lineEditMeanPath.setObjectName(_fromUtf8("lineEditMeanPath"))
        self.horizontalLayout_6.addWidget(self.lineEditMeanPath)
        self.pushButtonMeanUpload = QtGui.QPushButton(self.layoutWidget_5)
        self.pushButtonMeanUpload.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.pushButtonMeanUpload.setObjectName(_fromUtf8("pushButtonMeanUpload"))
        self.horizontalLayout_6.addWidget(self.pushButtonMeanUpload)
        self.checkBoxHasMean = QtGui.QCheckBox(Form)
        self.checkBoxHasMean.setGeometry(QtCore.QRect(440, 50, 101, 22))
        self.checkBoxHasMean.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu Condensed\";color:rgb(50, 165, 211)"))
        self.checkBoxHasMean.setObjectName(_fromUtf8("checkBoxHasMean"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 30, 201, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(255, 255, 255)"))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButtonModelUpload.setText(_translate("Form", "Add New Model", None))
        self.label_15.setText(_translate("Form", "Add New Model", None))
	self.label_15.hide()
        self.checkBoxUseGPU.setText(_translate("Form", "use gpu", None))
	#self.checkBoxUseGPU.hide()#Changed Format is autodoing things


        self.checkBoxChannelSwap.setText(_translate("Form", "channel swap", None))
        self.label_10.setText(_translate("Form", "Raw Scale       ", None))
        self.label_9.setText(_translate("Form", "Mean Path", None))
        self.pushButtonMeanUpload.setText(_translate("Form", "Upload", None))
        self.checkBoxHasMean.setText(_translate("Form", "has mean", None))
        self.label_6.setText(_translate("Form", "Other  Parameters", None))
	self.pushButtonModelUpload.clicked.connect(self.onModelUploadButtonClickedSlot)
	self.pushButtonMeanUpload.clicked.connect(self.onUploadButtonClickedSlot)
	self.lineEditModelPath.hide()
	self.checkBoxUseGPU.stateChanged.connect(self.showhideGPUIndex)

    def clearFields(self):
	self.checkBoxHasMean.setCheckState(QtCore.Qt.Unchecked)
	self.checkBoxUseGPU.setCheckState(QtCore.Qt.Unchecked)
	self.checkBoxChannelSwap.setCheckState(QtCore.Qt.Unchecked)
	self.lineEditModelPath.setText('')
	self.lineEditRawScale.setText('255')
	self.lineEditMeanPath.setText('')
	self.labelUseGPUIndex.hide()
	self.lineEditGPUIndex.hide()


    def onModelUploadButtonClickedSlot(self):
	print 'clicked Upload'
	prevtext=self.lineEditModelPath.text().__str__()
	prevtext=root if prevtext=='' else prevtext

	self.lineEditModelPath.setText(QtGui.QFileDialog.getOpenFileName(self,self.tr("Open File"),prevtext))

    def onUploadButtonClickedSlot(self):
	print 'clicked Upload'
	prevtext=self.lineEditMeanPath.text().__str__()
	prevtext=root if prevtext=='' else prevtext

	self.lineEditMeanPath.setText(QtGui.QFileDialog.getOpenFileName(self,self.tr("Open File"),prevtext))


	
    def setFields(self):
	print 'IDX: ',self.index
	if(self.index==None):
	    self.clearFields()
	else:
	    self.netHandle=netConfig_pb2.Param()
	    text_format.Merge(open(root+'/net/netData.prototxt').read(),self.netHandle)
	    #self.netHandle.has_mean=True
	    cn=self.netHandle.net[self.index]	    
	    #1. Has Mean Setting
	    if(cn.has_mean==True):
		self.checkBoxHasMean.setCheckState(QtCore.Qt.Checked)
	    else:
		self.checkBoxHasMean.setCheckState(QtCore.Qt.Unchecked)
		
	    #2.Mean Path Setting
	    if(cn.HasField('meanpath')):
		self.lineEditMeanPath.setText(cn.meanpath)
	    else:
		self.lineEditMeanPath.setText('')
	    #3. Raw Scale Setting
	    if(cn.HasField('raw_scale')):
		self.lineEditRawScale.setText(str(cn.raw_scale))
	    else:
		self.lineEditRawScale.setText('') 
	    #4. Use GPU
	    if(cn.gpu==True):
		self.checkBoxUseGPU.setCheckState(QtCore.Qt.Checked)
		self.lineEditGPUIndex.setText(str(cn.gpu_index))
		self.lineEditGPUIndex.show()
		self.labelUseGPUIndex.show()
	    else:
		self.checkBoxUseGPU.setCheckState(QtCore.Qt.Unchecked)
		self.lineEditGPUIndex.hide()
		self.labelUseGPUIndex.hide()
	    #5. Channel Swap	
	    if(cn.channel_swap==True):
		self.checkBoxChannelSwap.setCheckState(QtCore.Qt.Checked)
	    else:
		self.checkBoxChannelSwap.setCheckState(QtCore.Qt.Unchecked)
	    #6. Model Path
	    if(cn.HasField('modelpath')):
		self.lineEditModelPath.setText(cn.modelpath)
	    else:
		self.lineEditModelPath.setText('')

    def showhideGPUIndex(self,extra=None):

	if self.checkBoxUseGPU.checkState()==0:
	    self.lineEditGPUIndex.hide()
	    self.labelUseGPUIndex.hide()
	else:
	    self.lineEditGPUIndex.show()
	    self.labelUseGPUIndex.show()
	

	
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

