# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importView2.ui'
#
# Created: Sat Apr  4 23:50:49 2015
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 255)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(115, 115, 115)"))
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(380, 10, 211, 231))
        self.widget_2.setStyleSheet(_fromUtf8(";background-color:rgb(200, 200, 200)"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_4 = QtGui.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 71, 17))
        self.label_4.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.progressBar = QtGui.QProgressBar(self.widget_2)
        self.progressBar.setGeometry(QtCore.QRect(10, 20, 191, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.widget = QtGui.QWidget(self.widget_2)
        self.widget.setGeometry(QtCore.QRect(60, 90, 18, 18))
        self.widget.setStyleSheet(_fromUtf8("background-color:rgb(255, 0, 0)"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label_5 = QtGui.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(115, 100, 71, 21))
        self.label_5.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210);background-color:rgb(115, 115, 115)"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.widget_3 = QtGui.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(10, 120, 191, 101))
        self.widget_3.setStyleSheet(_fromUtf8("background-color:rgb(115, 115, 115)"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.textEdit = QtGui.QTextEdit(self.widget_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 171, 81))
        self.textEdit.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 120, 101, 27))
        self.pushButton.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(60, 120, 161, 28))
        self.comboBox.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.textEdit1 = QtGui.QTextEdit(Form)
        self.textEdit1.setGeometry(QtCore.QRect(60, 160, 281, 78))
        self.textEdit1.setStyleSheet(_fromUtf8("background-color:rgb(200,200,200)"))
        self.textEdit1.setObjectName(_fromUtf8("textEdit1"))
        self.lineEditData = QtGui.QLineEdit(Form)
        self.lineEditData.setGeometry(QtCore.QRect(130, 34, 211, 32))
        self.lineEditData.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";background-color:rgb(210, 225, 210)"))
        self.lineEditData.setObjectName(_fromUtf8("lineEditData"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(60, 80, 51, 22))
        self.label_3.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 40, 61, 22))
        self.label.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.widget1 = QtGui.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(140, 80, 201, 28))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setStyleSheet(_fromUtf8("color:rgb(200,200,200)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.toolButton = QtGui.QToolButton(self.widget1)
        self.toolButton.setStyleSheet(_fromUtf8("background-color:rgb(200,200,200)"))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_4.setText(_translate("Form", "Status", None))
        self.label_5.setText(_translate("Form", "  Details", None))
        self.pushButton.setText(_translate("Form", "Import", None))
        self.textEdit1.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can import data in<span style=\" font-weight:600;\"> format</span> specified in combobox.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Data will  be stored internally, as specified in <span style=\" font-weight:600;\">name</span> text field.</p></body></html>", None))
        self.label_3.setText(_translate("Form", "Type", None))
        self.label.setText(_translate("Form", "Name", None))
        self.label_2.setText(_translate("Form", "No Path", None))
        self.toolButton.setText(_translate("Form", "...", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

