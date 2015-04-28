# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layerView.ui'
#
# Created: Tue Mar 31 20:06:20 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import sys
import os
root=sys.getenv('HOME')+'/ACM'
sys.path.append(sys.getenv('ROOT')+'/caffe/python/caffe/proto')
import caffe_pb2



from PyQt4 import QtCore, QtGui

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
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 10, 391, 281))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
	self.textEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.textEdit.customContextMenuRequested.connect(self.myContextMenu)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

    def defaultContextFill(self,menu):
	action=QtGui.QAction(W)
	self.handle=caffe_pb2.ConvolutionParameter()
	

    def myContextMenu(self,position):
        menu =QtGui.QMenu()
        self.positionval=position
        menu.addAction(self.tr("New Layer Bellow"))
        menu.exec_(self.textEdit.viewport().mapToGlobal(position))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

