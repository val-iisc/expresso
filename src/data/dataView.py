# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataView.ui'
#
# Created: Thu Mar 12 01:15:02 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

#Imports begin
import sys
import os
root=os.getenv('EXPRESSO_ROOT')
import h5py
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import DataHandler
import transformationView
import splitView
import attachLabelView
import exportView

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):
    signalRefreshTrigger=QtCore.pyqtSignal(object)
    def __init__(self, parent=None):
        super(Ui_Form, self).__init__(parent)
        self.root=root
        self.setupUi(self)
        ## Jaley Start


    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 336)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(115, 115, 115)"))
        self.tableWidgetData = QtGui.QTableWidget(Form)
        self.tableWidgetData.setGeometry(QtCore.QRect(10, 50, 341, 261))
        self.tableWidgetData.setStyleSheet(_fromUtf8("background-color:rgb(200, 200, 200);font: 12pt \"Ubuntu Condensed\";QHeaderView::section { font:6 pt;}"))
        self.tableWidgetData.setObjectName(_fromUtf8("tableWidgetData"))
        self.tableWidgetData.setColumnCount(5)
        self.tableWidgetData.setRowCount(0)
        ##Added by Jaley
        self.tableWidgetData.setColumnWidth(0,99);
        self.tableWidgetData.setColumnWidth(1,72);
        self.tableWidgetData.setColumnWidth(2,45);
        self.tableWidgetData.setColumnWidth(3,45);
        self.tableWidgetData.setColumnWidth(4,45);

        self.tableWidgetData.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidgetData.customContextMenuRequested.connect(self.tableWidgetSlot)

        self.tableWidgetData.setHorizontalHeaderLabels(['name','#Elements','Depth','Width','Height'])
	

        self.widget = pg.GraphicsLayoutWidget(Form)
        self.widget.setGeometry(QtCore.QRect(360, 20, 231, 231))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalSlider = QtGui.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(440, 260, 151, 29))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 201, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 31, 31))
        self.label_2.setStyleSheet(_fromUtf8("color:rgb(0,0,0); \n"
"background-color:rgb(255,255,255,75%);\n"
"font: 18pt \"Ubuntu Condensed\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(360, 260, 81, 27))
        self.spinBox.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255)"))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
	#View
	self.view = self.widget.addViewBox()
	self.view.setAspectLocked(True)
	self.img = pg.ImageItem(border='w')
	self.view.addItem(self.img)
	self.data = np.random.randint(255, size=(100, 100, 3))
	self.img.setImage(self.data)
	#Triggers
	self.tableWidgetData.itemSelectionChanged.connect(self.changeContent)
	self.horizontalSlider.valueChanged.connect(self.changeView)
	self.spinBox.valueChanged.connect(self.changeView)	
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
	


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "View/Select  Data", None))
        self.label_2.setText(_translate("Form", "Type of Clubbing", None))
	self.refreshtable()
	#self.changeView()

    def changeContent(self):
        print self.tableWidgetData.currentRow()
        #name=str(self.tableWidgetData.itemAt(QtCore.QPoint(self.tableWidgetData.currentRow(),0)).text())
	name=str(self.tableWidgetData.currentItem().text())
        #name=str(self.tableWidgetData.itemAt(0,0).text())
        print name
        f=h5py.File(self.root+'/data/'+name+'.hdf5','r')
	self.horizontalSlider.setMaximum(f['data'].shape[0]-2)
	self.spinBox.setMaximum(f['data'].shape[0]-2)
	self.changeView()


    def changeView(self,index=0):
	print index
	print self.tableWidgetData.currentRow()
	self.horizontalSlider.setValue(index)
	self.spinBox.setValue(index)
	#name=str(self.tableWidgetData.itemAt(QtCore.QPoint(self.tableWidgetData.currentRow(),0)).text())
	#name=str(self.tableWidgetData.itemAt(0,0).text())
	name=str(self.tableWidgetData.currentItem().text())
	print self.root+'/data/'+name+'.hdf5'
	f=h5py.File(self.root+'/data/'+name+'.hdf5','r')
	data=np.array(f['data'][index],dtype=np.float32)
	#Data Display Stuff
	if(data.shape[0]!=3):
	    data=np.max(data,axis=0)
	    self.data=np.array(data*255/np.amax(data),dtype='uint8');
	    self.img.setImage(self.data)
	    if('label' in f.keys()):
		self.label_2.setText(str(f['label'][index]))

	    return
	#Data Display Stuff ends
	data=data.astype('uint8')
	self.data=np.transpose(np.array(data),[1,2,0])
        self.img.setImage(self.data)
	if('label' in f.keys()):
	    self.label_2.setText(str(f['label'][index]))
		

    def refreshtable(self,extra=None):
	print 'reached here'
	print self.root+'/data'
        #Remove previous entries of table
        cnt=self.tableWidgetData.rowCount();
        for i in range(cnt):self.tableWidgetData.removeRow(0)
        #Remove previous entries ends
        for files in os.listdir(self.root+'/data'):
	    print files
            if(files.endswith('.hdf5')):
                #Add to the table
                print files
                j=self.tableWidgetData.rowCount();
                f=h5py.File(self.root+'/data/'+files,'r')
		if('data' not in f.keys()):continue
                shape= f['data'].shape
                self.tableWidgetData.insertRow(self.tableWidgetData.rowCount());
                self.tableWidgetData.setItem(j,0,QtGui.QTableWidgetItem(files.split('.')[0] ));
                self.tableWidgetData.setItem(j,1,QtGui.QTableWidgetItem(str(shape[0])));
                self.tableWidgetData.setItem(j,2,QtGui.QTableWidgetItem(str(shape[1])));
                self.tableWidgetData.setItem(j,3,QtGui.QTableWidgetItem(str(shape[2])));
                self.tableWidgetData.setItem(j,4,QtGui.QTableWidgetItem(str(shape[3])));
		
		self.tableWidgetData.item(j,0).setBackground(QtGui.QColor(210,210,180))
		self.tableWidgetData.item(j,1).setBackground(QtGui.QColor(210,210,180))
		self.tableWidgetData.item(j,2).setBackground(QtGui.QColor(210,210,180))
		self.tableWidgetData.item(j,3).setBackground(QtGui.QColor(210,210,180))
		self.tableWidgetData.item(j,4).setBackground(QtGui.QColor(210,210,180))
		if('label' in f.keys()):
		    self.tableWidgetData.item(j,0).setBackground(QtGui.QColor(165,180,150))
		    self.tableWidgetData.item(j,1).setBackground(QtGui.QColor(165,180,150))
		    self.tableWidgetData.item(j,2).setBackground(QtGui.QColor(165,180,150))
		    self.tableWidgetData.item(j,3).setBackground(QtGui.QColor(165,180,150))
		    self.tableWidgetData.item(j,4).setBackground(QtGui.QColor(165,180,150))
		    

    def tableWidgetSlot(self,position):
        menu =QtGui.QMenu()
        exportMenu=menu.addAction(self.tr("Export"),self.exportSlot)
	#exportMenu.addAction(self.tr("Mat"),self.dataExportSlot)
	self.positionVal=position;
	#transformMenu=menu.addAction(self.tr("Photometric"),self.photometricSlot)
	splitMenu=menu.addAction(self.tr("Split"),self.splitSlot)
	attachMenu=menu.addAction(self.tr("Attach/Change Label"),self.attachLabelSlot)
	#mergeMenu=menu.addAction(self.tr("Merge Data"),self.mergeSlot)
	randomizeMenu=menu.addAction(self.tr("Randomize"),self.randomizeSlot)
	renameMenu=menu.addAction(self.tr("Rename"),self.renameSlot)
	removeMenu=menu.addAction(self.tr("Remove"),self.removeSlot)
        menu.exec_(self.tableWidgetData.viewport().mapToGlobal(position))

    def exportSlot(self):
	name=str(self.tableWidgetData.currentItem().text())
	print 'Exporting Slot'
	self.exportWidget=exportView.Ui_Form(dataName=name)
	self.exportWidget.setGeometry(self.cursor().pos().x(),self.cursor().pos().y(),421,183)
	self.exportWidget.show()


    def dataExportSlot(self):
	print 'Exporting . . . '
	filename = QtGui.QFileDialog.getSaveFileName(self, 'Dialog Title',root, selectedFilter='*.mat')
	if filename.endsWith('.mat'):
	    name=str(self.tableWidgetData.currentItem().text())
	    DataHandler.exportAsMat(filename=filename,hdf5name=name)

    def photometricSlot(self):
	print 'Photometric Slot'
	self.photometricWidget=transformationView.Ui_Form()
	self.photometricWidget.setGeometry(self.cursor().pos().x(),self.cursor().pos().y(),422,359)
	self.photometricWidget.show()

    def splitSlot(self):
	name=str(self.tableWidgetData.currentItem().text())
	print 'Splitting Slot'
	self.splitWidget=splitView.Ui_Form(dataName=name)
	self.splitWidget.setGeometry(self.cursor().pos().x(),self.cursor().pos().y(),421,232)
	self.splitWidget.show()

    def randomizeSlot(self):
	print 'Randomize Slot'

    def attachLabelSlot(self):
	name=str(self.tableWidgetData.currentItem().text())
	print 'Attach Slot'
	self.attachLabelWidget=attachLabelView.Ui_Form(dataName=name)
	self.attachLabelWidget.setGeometry(self.cursor().pos().x(),self.cursor().pos().y(),421,183)
	self.attachLabelWidget.show()

    def mergeSlot(self):
	print 'Merge Slot'
			

    def renameSlot(self):
	print 'Rename Slot'

    def removeSlot(self):
	print 'Remove Slot'
	name=str(self.tableWidgetData.currentItem().text())
	os.remove(root+'/data/'+name+'.hdf5')
	self.refreshtable()
	self.signalRefreshTrigger.emit('Data with name '+name+' removed')


    def refreshTrigger(self,extra=None):
	self.refreshtable()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

