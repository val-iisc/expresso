# -*- coding: utf-8 -*-
##############
# Written by : Jaley Dholakiya
# Video Analytics Lab,IISc
#############


# Form implementation generated from reading ui file 'exportExperimentView.ui'
#
# Created: Sat Apr 18 04:21:11 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
import sys
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
    def __init__(self, parent=None,expName=None):
        super(Ui_Form, self).__init__(parent)
        self.expName=expName
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(225, 271)
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(3, 10, 221, 221))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 240, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(3, 240, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Ok", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))
	self.fillData()
	self.pushButton.clicked.connect(self.onSubmitSlot)

    def fillData(self):
	if(self.expName==None):return
	print 'Filling Data'
	f=h5py.File(root+'/exp/data/'+self.expName+'.hdf5','r')
	
	lst=f.keys()
	if 'label' in lst:
	    lst.remove('label')
	for elem in lst:
            item = QtGui.QListWidgetItem(elem)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)

	f.close()

    def onSubmitSlot(self):
	tickedList=[self.listWidget.item(i).text().__str__() for i in range(self.listWidget.count()) if self.listWidget.item(i).checkState()!=0]
	#Save the data blobs as expName_blobName in data View
	with h5py.File(root+'/exp/data/'+self.expName+'.hdf5','r') as f:
	    for elem in tickedList:
		data=f[elem]
		dataName=self.expName+'_'+elem
		with h5py.File(root+'/data/'+dataName+'.hdf5','w') as fw:
		    comp_kwargs = {'compression': 'gzip', 'compression_opts': 1}
		    fw.create_dataset('data',data=data,**comp_kwargs)
		
		    if('label' in f.keys()):fw.create_dataset('label',data=f['label'],**comp_kwargs)


	print tickedList
	self.closeSlot()

    def closeSlot(self):
	
	self.close()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

