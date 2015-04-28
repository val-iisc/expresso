# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configListView.ui'
#
# Created: Fri Mar 13 20:40:16 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sys
import os

root=os.getenv('EXPRESSO_ROOT')
sys.path.append(root+'/src/net/config')


sys.path.append(os.getenv('CAFFE_ROOT')+'/python/caffe/proto')
import caffe_pb2


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
    def __init__(self,parent=None,index=1):
        super(Ui_Form,self).__init__(parent)
	self.root=root
	self.index=index
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(291, 351)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(120, 180, 120)"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget.customContextMenuRequested.connect(self.listWidgetSlot)
        self.listWidget.setGeometry(QtCore.QRect(10, 40, 271, 301))
        self.listWidget.setStyleSheet(_fromUtf8("font: 12pt \"Ubuntu Condensed\";background-color:rgb(210, 230, 210);color:rgb(45,60,45)"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 221, 31))
        self.label.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label.setObjectName(_fromUtf8("label"))


	self.fillList()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def fillList(self):
	self.data=open(root+'/net/netData.prototxt').read()
	self.listWidget.clear()
	self.netHandler=netConfig_pb2.Param();
	self.protoHandler=caffe_pb2.NetParameter()
	text_format.Merge(self.data,self.netHandler)
	text_format.Merge(open(self.netHandler.net[self.index].protopath).read(),self.protoHandler)		
	for elem in self.protoHandler.layers:
	    item = QtGui.QListWidgetItem(elem.name)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
	    self.listWidget.addItem(item)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Configuration Data", None))

    def appendConfig(self,filename):
	self.data=open(root+'/net/netData.prototxt').read()
        self.netHandler=netConfig_pb2.Param();	
        text_format.Merge(self.data,self.netHandler)
	newnet=self.netHandler.net.add()
	text_format.Merge(self.netHandler.net[self.listWidget.currentRow()].__str__(),newnet)
	newnet.protopath=root+'/net/models/deploy/'+filename+'.prototxt'
	newnet.name=filename.upper()
	open(root+'/net/netData.prototxt','w').write(self.netHandler.__str__())
	print self.netHandler
	self.fillList()	
	print 'append Config',filename	

    def listWidgetSlot(self,position):
        menu =QtGui.QMenu()
        menu.addAction(self.tr("Remove"),self.removeCurrent)
        menu.exec_(self.listWidget.viewport().mapToGlobal(position))


    def removeCurrent(self):
	del self.netHandler.net[self.listWidget.currentRow()]
	open(root+'/net/netData.prototxt','w').write(self.netHandler.__str__())
        print self.netHandler
        self.fillList()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

