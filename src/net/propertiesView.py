# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'propertiesView.ui'
#
# Created: Thu Apr 30 15:36:19 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os;
import sys
root=os.getenv('EXPRESSO_ROOT')
sys.path.append(root+'/src/net/config')
import netConfig_pb2
from google.protobuf import text_format


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
    def __init__(self,parent=None,netName=None):
        super(Ui_Form,self).__init__(parent)
	self.netName=netName
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(531, 446)
        Form.setStyleSheet(_fromUtf8("background-color:rgba(255,255,255,255)"))
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 481, 31))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgba(0,0,0,45)"))
        self.lineEdit.setText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
	self.lineEdit.setReadOnly(True)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 14, 151, 31))
        self.label.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";background-color:rgba(0,0,0,0)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 114, 151, 31))
        self.label_2.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";background-color:rgba(0,0,0,0)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 150, 481, 31))
        self.lineEdit_2.setStyleSheet(_fromUtf8("background-color:rgba(0,0,0,45)"))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
	self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 246, 481, 31))
        self.lineEdit_3.setStyleSheet(_fromUtf8("background-color:rgba(0,0,0,45)"))
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
	self.lineEdit_3.setReadOnly(True)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 151, 31))
        self.label_3.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";background-color:rgba(0,0,0,0)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 314, 151, 31))
        self.label_4.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";background-color:rgba(0,0,0,0)"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 350, 481, 31))
        self.lineEdit_4.setStyleSheet(_fromUtf8("background-color:rgba(0,0,0,45)"))
        self.lineEdit_4.setText(_fromUtf8(""))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
	self.lineEdit_4.setReadOnly(True)
        self.pushButtonOk = QtGui.QPushButton(Form)
        self.pushButtonOk.setGeometry(QtCore.QRect(430, 400, 71, 27))
        self.pushButtonOk.setStyleSheet(_fromUtf8("background-color:rgba(255,255,255,255)"))
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Train Path", None))
        self.label_2.setText(_translate("Form", "Deploy Path", None))
        self.label_3.setText(_translate("Form", "Model Path", None))
        self.label_4.setText(_translate("Form", "Mean Path", None))
        self.pushButtonOk.setText(_translate("Form", "Ok", None))
	self.pushButtonOk.clicked.connect(self.submit)
	self.setPath()


    def setPath(self):
	if(self.netName==None):return
        self.data=open(root+'/net/netData.prototxt').read()
	self.netHandler=netConfig_pb2.Param();  
        text_format.Merge(self.data,self.netHandler)
	currentNet=None
	for elem in self.netHandler.net:
	    if elem.name==self.netName.upper():currentNet=elem
	if(currentNet==None):return
	if(currentNet.HasField('trainpath') and currentNet.trainpath!=''):self.lineEdit.setText(currentNet.trainpath)
	if(currentNet.HasField('protopath') and currentNet.modelpath!=''):self.lineEdit_2.setText(currentNet.protopath)
	if(currentNet.HasField('modelpath') and currentNet.modelpath!=''):self.lineEdit_3.setText(currentNet.modelpath)
	if(currentNet.HasField('meanpath') and currentNet.meanpath!=''):self.lineEdit_4.setText(currentNet.meanpath)
	
	
	#Setting the paths
	
 
    def submit(self):
	self.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

