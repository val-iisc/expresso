# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importMultipleFoldersView.ui'
#
# Created: Fri May  1 14:59:58 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os
root=os.getenv('EXPRESSO_ROOT')
import h5py


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
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(507, 300)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 80, 331, 31))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgba(0,0,0,45)"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
	self.lineEdit.setReadOnly(True)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 80, 121, 31))
        self.label.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";background-color:rgba(0,0,0,0)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(450, 80, 31, 31))
        self.toolButton.setStyleSheet(_fromUtf8("background-color:rgba(0,0,0,100);color:rgb(255,255,255)"))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(Form)
        self.doubleSpinBox.setGeometry(QtCore.QRect(140, 140, 62, 27))
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 130, 121, 51))
        self.label_2.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";background-color:rgba(0,0,0,0)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(333, 240, 71, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(410, 240, 71, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
	self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 261, 31))
        self.label_3.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";background-color:rgba(0,0,0,0)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 30, 201, 31))
        self.lineEdit_2.setStyleSheet(_fromUtf8("background-color:rgba(0,0,0,45)"))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Folder Path", None))
        self.toolButton.setText(_translate("Form", "...", None))
        self.label_2.setText(_translate("Form", "Percentage of \n"
" Train,Test Split", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))
        self.pushButton.setText(_translate("Form", "Ok", None))
	self.label_3.setText(_translate("Form", "Name by which you want to save", None))
	

	#Initiallization of widgets
	self.doubleSpinBox.setMaximum(100)
	self.doubleSpinBox.setMinimum(0)
	self.pushButton.clicked.connect(self.submit)
	self.pushButton_2.clicked.connect(self.reject)
	self.folderLocation=''
	self.toolButton.clicked.connect(self.getFolderLocation)


    def getFolderLocation(self):
        self.dialogHandle=QtGui.QFileDialog()
	self.folderLocation=self.dialogHandle.getExistingDirectory(self,self.tr("Open File"),root).__str__()
	self.lineEdit.setText(self.folderLocation)





    def submit(self):
	self.name=self.lineEdit_2.text().__str__()

	if(self.folderLocation==''):return
	if(self.name==''):return
	#Main Operation Begins
	f=open(self.folderLocation+'/classList.txt','w')
	classDict={}
	idx=0
	for foldername in os.listdir(self.folderLocation):
	    if(os.path.isdir(self.folderLocation+'/'+foldername)==False):continue	   
	    idx=idx+1
	    classDict[foldername]
	    print foldername


	#Main Operation Ends
	

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

