# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteView.ui'
#
# Created: Thu Apr 30 17:12:36 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import DeleteHandler
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
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(202, 261)
        self.checkBoxAll = QtGui.QCheckBox(Form)
        self.checkBoxAll.setGeometry(QtCore.QRect(20, 50, 97, 22))
        self.checkBoxAll.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.checkBoxAll.setObjectName(_fromUtf8("checkBoxAll"))
        self.checkBoxNet = QtGui.QCheckBox(Form)
        self.checkBoxNet.setGeometry(QtCore.QRect(20, 100, 97, 22))
        self.checkBoxNet.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.checkBoxNet.setObjectName(_fromUtf8("checkBoxNet"))
        self.checkBoxData = QtGui.QCheckBox(Form)
        self.checkBoxData.setGeometry(QtCore.QRect(20, 80, 97, 22))
        self.checkBoxData.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.checkBoxData.setObjectName(_fromUtf8("checkBoxData"))
        self.checkBoxTrain = QtGui.QCheckBox(Form)
        self.checkBoxTrain.setGeometry(QtCore.QRect(20, 120, 121, 22))
        self.checkBoxTrain.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.checkBoxTrain.setObjectName(_fromUtf8("checkBoxTrain"))
        self.checkBoxExp = QtGui.QCheckBox(Form)
        self.checkBoxExp.setGeometry(QtCore.QRect(20, 140, 121, 22))
        self.checkBoxExp.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.checkBoxExp.setObjectName(_fromUtf8("checkBoxExp"))
        self.checkBoxCache = QtGui.QCheckBox(Form)
        self.checkBoxCache.setGeometry(QtCore.QRect(20, 180, 97, 22))
        self.checkBoxCache.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.checkBoxCache.setObjectName(_fromUtf8("checkBoxCache"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 31))
        self.label.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(43, 220, 71, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 220, 71, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.checkBoxSVM = QtGui.QCheckBox(Form)
        self.checkBoxSVM.setGeometry(QtCore.QRect(20, 160, 97, 22))
        self.checkBoxSVM.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.checkBoxSVM.setObjectName(_fromUtf8("checkBoxSVM"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.checkBoxAll.setText(_translate("Form", "All", None))
        self.checkBoxNet.setText(_translate("Form", "Net", None))
        self.checkBoxData.setText(_translate("Form", "Data", None))
        self.checkBoxTrain.setText(_translate("Form", "Training Data", None))
        self.checkBoxExp.setText(_translate("Form", "Experiments", None))
        self.checkBoxCache.setText(_translate("Form", "Cache", None))
        self.label.setText(_translate("Form", "Group Delete", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))
        self.pushButton.setText(_translate("Form", "Ok", None))
        self.checkBoxSVM.setText(_translate("Form", "SVM", None))
	self.checkBoxAll.stateChanged.connect(self.selectAll)
	self.checkBoxData.stateChanged.connect(self.selectOne)
	self.checkBoxNet.stateChanged.connect(self.selectOne)
	self.checkBoxExp.stateChanged.connect(self.selectOne)
	self.checkBoxTrain.stateChanged.connect(self.selectOne)
	self.checkBoxCache.stateChanged.connect(self.selectOne)
	self.checkBoxSVM.stateChanged.connect(self.selectOne)
        self.pushButton.clicked.connect(self.submit)
	self.pushButton_2.clicked.connect(self.reject)

    def selectAll(self):
	self.checkBoxData.stateChanged.disconnect(self.selectOne)
	self.checkBoxNet.stateChanged.disconnect(self.selectOne)
	self.checkBoxExp.stateChanged.disconnect(self.selectOne)
	self.checkBoxTrain.stateChanged.disconnect(self.selectOne)
	self.checkBoxCache.stateChanged.disconnect(self.selectOne)
	self.checkBoxSVM.stateChanged.disconnect(self.selectOne)
	if(self.checkBoxAll.checkState()==2):
	    self.checkBoxData.setCheckState(2)
	    self.checkBoxNet.setCheckState(2)
	    self.checkBoxExp.setCheckState(2)
	    self.checkBoxTrain.setCheckState(2)
	    self.checkBoxCache.setCheckState(2)
	    self.checkBoxSVM.setCheckState(2)
	elif(self.checkBoxAll.checkState()==0):
	    self.checkBoxData.setCheckState(0)
	    self.checkBoxNet.setCheckState(0)
	    self.checkBoxExp.setCheckState(0)
	    self.checkBoxTrain.setCheckState(0)
	    self.checkBoxCache.setCheckState(0)
	    self.checkBoxSVM.setCheckState(0)
	self.checkBoxData.stateChanged.connect(self.selectOne)
	self.checkBoxNet.stateChanged.connect(self.selectOne)
	self.checkBoxExp.stateChanged.connect(self.selectOne)
	self.checkBoxTrain.stateChanged.connect(self.selectOne)
	self.checkBoxCache.stateChanged.connect(self.selectOne)
	self.checkBoxSVM.stateChanged.connect(self.selectOne)

    def selectOne(self):
	
	self.checkBoxAll.setCheckState(1)

    def submit(self):
        reply = QtGui.QMessageBox.question(self, 'Message', "Are you sure you want to delete data?\n Data Recovery is not possible after this operation", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if(reply==QtGui.QMessageBox.No):
	    self.close()
	    return
	if(self.checkBoxData.isChecked()):DeleteHandler.deleteData()
	if(self.checkBoxNet.isChecked()):DeleteHandler.deleteNet()
	if(self.checkBoxExp.isChecked()):DeleteHandler.deleteExp()
	if(self.checkBoxTrain.isChecked()):DeleteHandler.deleteTrain()
	if(self.checkBoxCache.isChecked()):DeleteHandler.deleteCache()
	if(self.checkBoxSVM.isChecked()):DeleteHandler.deleteSVM()
	self.signalRefreshTrigger.emit('Cleared some data')
	self.close()

    def reject(self):
	self.close()




if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

