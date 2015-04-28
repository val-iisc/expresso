# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subpanel.ui'
#
# Created: Tue Mar  3 18:46:36 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#Jaley Start for Range Editor

from google.protobuf import text_format
from time import sleep

import sys
sys.path.append('/home/jaley/Final/simple')
import OperationHandler
import jaleyexp_pb2

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from qtutils import inthread,inmain_later
#Jaley Ends




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
    signalTriggered=QtCore.pyqtSignal(object)

    def __init__(self,parent=None):
	super(Ui_Form,self).__init__(parent)
       #INITIALLIZE ENDS
	self.setupUi(self)
	inthread(self.inloop)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(414, 108)

        self.plotwidget = pg.PlotWidget(Form)
        self.plotwidget.setGeometry(QtCore.QRect(0, 0, 414, 108))
        self.plotwidget.setObjectName(_fromUtf8("plot"))
	self.signalTriggered.connect(self.addValueSlot)
	self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

    def inloop(self):
	for i in range(10):
	    sleep(1)
	    self.signalTriggered.emit(i)

    def addValueSlot(self,value):
        line=np.sin(np.arange(255))
        plothandle=self.plotwidget.plot(line, clear=True)
	self.plotwidget.setXRange(0+value,100+value)
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

