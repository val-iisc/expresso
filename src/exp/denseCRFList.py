# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'denseCRFList.ui'
#
# Created: Tue Jun  2 15:08:05 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
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
    signalCompleteTrigger=QtCore.pyqtSignal(object)
    def __init__(self,parent=None):
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(291, 301)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(150,150,90)"))
	self.label=QtGui.QLabel(Form)
	self.label.setGeometry(QtCore.QRect(10,10,271,30))
	self.label.setText('Dense CRF Exp')
        self.label.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu Condensed\";"))
	
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 45, 271, 246))
        self.listWidget.setStyleSheet(_fromUtf8("background-color:rgb(210,210,150);\n"
"font: 16pt \"Ubuntu Condensed\";"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
	self.initialize()
	self.listWidget.itemClicked.connect(self.onIndexChanged)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

    def refreshTrigger(self):
	self.initialize()

    def initialize(self):
	self.listWidget.clear()
	for elem in os.listdir(root+'/exp/denseCRF/data'):
	    if(os.path.exists(root+'/exp/denseCRF/data/'+elem+'/results.txt')):
	        self.listWidget.addItem(elem)

    def onIndexChanged(self):
	self.signalCompleteTrigger.emit(self.listWidget.currentItem().text().__str__())
	

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

