# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transformationView.ui'
#
# Created: Fri Apr 17 14:46:43 2015
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
    def __init__(self, parent=None,dataName=None):
        super(Ui_Form, self).__init__(parent)
	self.dataName=dataName
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(422, 359)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 421, 351))
        self.tabWidget.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(327, 300, 71, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 300, 71, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.checkBox_5 = QtGui.QCheckBox(self.tab)
        self.checkBox_5.setGeometry(QtCore.QRect(70, 70, 141, 22))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_11 = QtGui.QCheckBox(self.tab)
        self.checkBox_11.setGeometry(QtCore.QRect(10, 30, 97, 22))
        self.checkBox_11.setObjectName(_fromUtf8("checkBox_11"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.checkBox_4 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_4.setGeometry(QtCore.QRect(70, 180, 97, 22))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.layoutWidget = QtGui.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 130, 204, 35))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.checkBox_3 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_3.setGeometry(QtCore.QRect(70, 100, 97, 22))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.layoutWidget_5 = QtGui.QWidget(self.tab_2)
        self.layoutWidget_5.setGeometry(QtCore.QRect(90, 210, 204, 35))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.layoutWidget_5)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.layoutWidget_5)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.layoutWidget_6 = QtGui.QWidget(self.tab_2)
        self.layoutWidget_6.setGeometry(QtCore.QRect(300, 130, 91, 35))
        self.layoutWidget_6.setObjectName(_fromUtf8("layoutWidget_6"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget_6)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.layoutWidget_6)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.checkBox = QtGui.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(10, 30, 97, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab_2)
        self.checkBox_2.setGeometry(QtCore.QRect(70, 70, 97, 22))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.pushButton_2.clicked.connect(self.closedSlot)


        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton.setText(_translate("Form", "Ok", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))
        self.checkBox_5.setText(_translate("Form", "Subtract Mean", None))
        self.checkBox_11.setText(_translate("Form", "Apply ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Photometric", None))
        self.checkBox_4.setText(_translate("Form", "3. Zoom", None))
        self.label.setText(_translate("Form", "R.List", None))
        self.checkBox_3.setText(_translate("Form", "2. Rotate", None))
        self.label_3.setText(_translate("Form", "Z.List", None))
        self.label_2.setText(_translate("Form", "Pad", None))
        self.checkBox.setText(_translate("Form", "Apply ", None))
	self.checkBox.setCheckState(2)
        self.checkBox_2.setText(_translate("Form", "1. Mirror", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Geometric", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Default", None))
	self.checkBox.stateChanged.connect(self.onGeometricApplyChanged)

	
    def onGeometricApplyChanged(self,state):
	print state
	if(state==0):
            self.checkBox_4.hide()
	    self.checkBox_3.hide()
	    self.checkBox_2.hide()
	    self.layoutWidget_5.hide()
	    self.layoutWidget.hide()
	    self.layoutWidget_6.hide()
	else:
            self.checkBox_4.show()
	    self.checkBox_3.show()
	    self.checkBox_2.show()
	    self.layoutWidget_5.show()
	    self.layoutWidget.show()
	    self.layoutWidget_6.show()
        pass
 
    def closedSlot(self):
	self.close()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

