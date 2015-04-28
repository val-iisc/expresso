# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trainValidDataView.ui'
#
# Created: Wed Mar 25 02:40:28 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import os
import h5py
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
        self.root=root
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(551, 311)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(120,180,120);"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(61, 41, 215, 33))
        self.label.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(210,225,210)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.labelTraining = QtGui.QLabel(Form)
        self.labelTraining.setGeometry(QtCore.QRect(60, 90, 381, 17))
        self.labelTraining.setStyleSheet(_fromUtf8("font:italic 15pt  \"Ubuntu Condensed\";color:rgb(45,60,45)"))
        self.labelTraining.setObjectName(_fromUtf8("labelTraining"))
        self.comboBoxTraining = QtGui.QComboBox(Form)
        self.comboBoxTraining.setGeometry(QtCore.QRect(311, 42, 198, 31))
        self.comboBoxTraining.setStyleSheet(_fromUtf8("font: 18 pt \"Ubuntu Condensed\";color:rgb(45,60,45);background-color:rgb(210,225,210)"))
        self.comboBoxTraining.setObjectName(_fromUtf8("comboBoxTraining"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(61, 160, 215, 33))
        self.label_3.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(210,225,210)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.labelValidation = QtGui.QLabel(Form)
        self.labelValidation.setGeometry(QtCore.QRect(60, 210, 381, 17))
        self.labelValidation.setStyleSheet(_fromUtf8("font:italic 15pt  \"Ubuntu Condensed\";color:rgb(45,60,45)"))
        self.labelValidation.setObjectName(_fromUtf8("labelValidation"))
        self.comboBoxValidation = QtGui.QComboBox(Form)
        self.comboBoxValidation.setGeometry(QtCore.QRect(310, 170, 198, 31))
        self.comboBoxValidation.setStyleSheet(_fromUtf8("font: 18 pt \"Ubuntu Condensed\";color:rgb(45,60,45);background-color:rgb(210,225,210)"))
        self.comboBoxValidation.setObjectName(_fromUtf8("comboBoxValidation"))
	self.initiallize()
	self.comboBoxTraining.currentIndexChanged.connect(self.trainingSlot)
	self.comboBoxValidation.currentIndexChanged.connect(self.validationSlot)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Training Blob              ", None))
        self.labelTraining.setText(_translate("Form", "Dimentions are b x c x h x w", None))
        self.label_3.setText(_translate("Form", "Validation Blob", None))
        self.labelValidation.setText(_translate("Form", "Dimentions are b x c x h x w", None))
    def initiallize(self):
	self.comboBoxTraining.clear()
	self.comboBoxValidation.clear()
	for elem in os.listdir(root+'/data'):
	    if(elem.endswith('.hdf5')):
 	    	f=h5py.File(root+'/data/'+elem,'r')
		if 'label' in f.keys():self.comboBoxTraining.addItem(elem[0:-5])
		if 'label' in f.keys():self.comboBoxValidation.addItem(elem[0:-5])
	    	f.close()
	
    def trainingSlot(self,index):
	if(str(self.comboBoxTraining.currentText())==""):return;
	f=h5py.File(root+'/data/'+str(self.comboBoxTraining.currentText())+'.hdf5','r')
	s=f['data'].shape
	self.labelTraining.setText("Dimentions are "+str(s[0])+' x '+str(s[1])+' x '+str(s[2])+' x '+str(s[3]))
	f.close()

    def validationSlot(self,index):
	if(str(self.comboBoxValidation.currentText())==""):return
 	f=h5py.File(root+'/data/'+str(self.comboBoxValidation.currentText())+'.hdf5','r')
	s=f['data'].shape
	self.labelValidation.setText("Dimentions are "+str(s[0])+' x '+str(s[1])+' x '+str(s[2])+' x '+str(s[3]))
	f.close()

    def refreshTrigger(self):
	self.initiallize()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

