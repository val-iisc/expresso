# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'netButtonView.ui'
#
# Created: Sat Mar 14 01:25:13 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

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
    def __init__(self,parent=None):
        super(Ui_Form,self).__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 61)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(210,225,210)"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 23, 141, 27))
        self.comboBox.setStyleSheet(_fromUtf8("background-color:rgb(120,180,120);\n"
"font: 16pt \"Ubuntu Condensed\";color:rgb(210,225,210)"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(170, 0, 3, 61))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(180, 0, 3, 61))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(190, 0, 3, 61))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(210, 20, 391, 31))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setStyleSheet(_fromUtf8("font: 16pt \"Ubuntu Condensed\";color:rgb(45,60,45)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255);\n"
"font: 16pt \"Ubuntu Condensed\";color:rgb(45,60,45)"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setStyleSheet(_fromUtf8("background-color:rgb(120,180,120);\n"
"font: 16pt \"Ubuntu Condensed\";color:rgb(210,225,210)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
	
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.comboBox.setItemText(0, _translate("Form", "Custom View", None))
        self.comboBox.setItemText(1, _translate("Form", "Text View", None))
        self.label.setText(_translate("Form", "Name", None))
        self.pushButton.setText(_translate("Form", "Save New", None))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

