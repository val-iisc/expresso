# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layerView.ui'
#
# Created: Fri Apr  3 01:51:54 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os
root=os.getenv('EXPRESSO_ROOT')
sys.path.append(root+'/src/custom')
import autocomplete as ac


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
    def __init__(self,parent=None):
        super(Ui_Form, self).__init__(parent)
	self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(554, 367)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(115, 115, 115)"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(245, 20, 301, 291))
        self.widget.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255)"))
        self.widget.setObjectName(_fromUtf8("widget"))
	completer=ac.DictionaryCompleter()
	self.textEdit=ac.CompletionTextEdit(self.widget)
	self.textEdit.setCompleter(completer)
	self.textEdit.setGeometry(QtCore.QRect(0, 0, 301, 291))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(9, 20, 225, 291))
        self.listWidget.setStyleSheet(_fromUtf8("background-color:rgb(116, 175, 211); \n"
"font: 12pt \"Ubuntu Condensed\";\n"
"color:rgb(255,255,255)"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
	self.isSubmitted=False
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "convolution_param", None))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "input_dim", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
	self.textEdit.cursorPositionChanged.connect(self.updateList)
	#Adding push Buttons
	self.pushButtonOk=QtGui.QPushButton(Form)
	self.pushButtonOk.setGeometry(QtCore.QRect(301,321,100,30))
	self.pushButtonOk.setStyleSheet('background-color:rgb(175,175,175);color:rgb(75,75,75)')
	self.pushButtonOk.setText('Ok')

	self.pushButtonCancel=QtGui.QPushButton(Form)
	self.pushButtonCancel.setGeometry(QtCore.QRect(425,321,100,30))
	self.pushButtonCancel.setStyleSheet('background-color:rgb(175,175,175);color:rgb(75,75,75)')
	self.pushButtonCancel.setText('Cancel')
	self.pushButtonOk.clicked.connect(self.submit)
	self.pushButtonCancel.clicked.connect(self.reject)
	

    def submit(self):
	self.isSubmitted=True
	self.close()
	pass
    def reject(self):
	self.isSubmitted=False
	self.close()
	pass


    def updateList(self):
	self.listWidget.clear()
	self.listWidget.addItems(self.textEdit.getHListData())


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

