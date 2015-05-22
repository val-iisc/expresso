# -*- coding: utf-8 -*-
##############
# Written by : Jaley Dholakiya
# Video Analytics Lab,IISc
#############

# Form implementation generated from reading ui file 'configListView.ui'
#
# Created: Fri Mar 13 20:40:16 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sys
import os
import h5py
root=os.getenv('EXPRESSO_ROOT')
import exportExperimentView


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
    signalRefreshTrigger=QtCore.pyqtSignal(object)
    def __init__(self,parent=None):
        super(Ui_Form,self).__init__(parent)
	self.root=root
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(291, 301)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(120, 180, 120)"))
        self.treeWidget = QtGui.QTreeWidget(Form)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.treeWidgetSlot)
        self.treeWidget.setGeometry(QtCore.QRect(10, 40, 271, 261))
        self.treeWidget.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";background-color:rgb(175, 192, 150);color:rgb(75,75,45)"))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 221, 31))
        self.label.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label.setObjectName(_fromUtf8("label"))
	self.treeWidget.header().close()

	self.fillList()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def fillList(self):
	self.treeWidget.clear();
	itemList=[]
	for elem in os.listdir(root+'/exp/data'):
	    if elem.endswith('.hdf5'):
		experiment=QtGui.QTreeWidgetItem()
		elem=elem[0:len(elem)-5]
		experiment.setText(0,elem)
		# Add Layers as child #
		with h5py.File(root+'/exp/data/'+elem+'.hdf5') as f:
		    for k in f.keys():
			layer=QtGui.QTreeWidgetItem()
			layer.setText(0,k)
			layer.setForeground(0,QtGui.QBrush(QtGui.QColor(255,255,255)))
        		layer.setFont(0,QtGui.QFont('Ubuntu Condensed',12))
                	layer.setFlags(layer.flags()& ~QtCore.Qt.ItemIsEnabled )

			experiment.addChild(layer)
		itemList.append(experiment)
	print len(itemList)
	self.treeWidget.addTopLevelItems(itemList)


	
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Experiment List", None))

    def appendConfig(self,filename):
	self.data=open(root+'/net/netData.prototxt').read()
        self.netHandler=netConfig_pb2.Param();	
        text_format.Merge(self.data,self.netHandler)
	newnet=self.netHandler.net.add()
	text_format.Merge(self.netHandler.net[self.treeWidget.currentRow()].__str__(),newnet)
	newnet.protopath=root+'/net/models/deploy/'+filename+'.prototxt'
	newnet.name=filename.upper()
	open(root+'/net/netData.prototxt','w').write(self.netHandler.__str__())
	print self.netHandler
	self.fillList()	
	print 'append Config',filename	


    def treeWidgetSlot(self,position):
        menu =QtGui.QMenu()
        menu.addAction(self.tr("Remove"),self.removeCurrent)
        #menu.addAction(self.tr("Export"),self.exportCurrent)
	menu.addAction(self.tr("Move to Data"),self.moveToDataSlot)
	#menu.addAction(self.tr("Remove "),self.removeSlot)
        menu.exec_(self.treeWidget.viewport().mapToGlobal(position))



    def exportCurrent(self):	
	print self.treeWidget.currentItem().text(0)

	#Exporting to required Format
	pass    

    def moveToDataSlot(self):
	name= self.treeWidget.currentItem().text(0).__str__()
        print 'Move to Data Slot'
        self.exportToDataWidget=exportExperimentView.Ui_Form(expName=name)
        self.exportToDataWidget.setGeometry(self.cursor().pos().x(),self.cursor().pos().y(),225,271)
        self.exportToDataWidget.show()
	self.exportToDataWidget.installEventFilter(self)
	pass

    def eventFilter(self, source, event):
        import sys
        if event.type()==QtCore.QEvent.Close:
	    self.signalRefreshTrigger.emit('Export of data Complete')
	    print 'Complete'

        return QtGui.QWidget.eventFilter(self, source, event)




    def removeCurrent(self):
	name= self.treeWidget.currentItem().text(0).__str__()
	print 'REMOVING ',name
	for elem in os.listdir(root+'/exp/data'):
	    if elem==name+'.hdf5':
		os.remove(root+'/exp/data/'+name+'.hdf5')
		self.signalRefreshTrigger.emit('Removed features named '+name)
    def refreshTrigger(self):
	self.fillList()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

