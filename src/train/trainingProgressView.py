# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trainingProgressView.ui'
#
# Created: Fri Mar 13 20:34:36 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

#Imports begin
import sys
import os
root=os.getenv('EXPRESSO_ROOT')
#sys.path.append(root)


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
        self.root=root
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(611, 591)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(120,180,120)"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 340, 241, 31))
        self.label_5.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(60, 90, 60);background-color:rgb(210, 225, 210)"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.widget_4 = QtGui.QWidget(Form)
        self.widget_4.setGeometry(QtCore.QRect(40, 370, 541, 161))
        self.widget_4.setStyleSheet(_fromUtf8("background-color:rgb(210, 225, 210)"))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.textEdit = QtGui.QTextEdit(self.widget_4)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 521, 141))
        self.textEdit.setStyleSheet(_fromUtf8("background-color:rgb(255, 255, 255)"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(30, 20, 551, 241))
        self.widget_2.setStyleSheet(_fromUtf8("background-color:rgb(150,195,150)"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_3 = QtGui.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 501, 17))
        self.label_3.setStyleSheet(_fromUtf8("font: oblique 14pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.layoutWidget = QtGui.QWidget(self.widget_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 291, 35))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(21)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(45, 60, 45)"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_2.addWidget(self.label_6)
        self.progressBar = QtGui.QProgressBar(self.widget_2)
        self.progressBar.setGeometry(QtCore.QRect(20, 100, 511, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_7 = QtGui.QLabel(self.widget_2)
        self.label_7.setGeometry(QtCore.QRect(20, 180, 271, 31))
        self.label_7.setStyleSheet(_fromUtf8("font: oblique 18pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.labelTimeRemaining = QtGui.QLabel(self.widget_2)
        self.labelTimeRemaining.setGeometry(QtCore.QRect(300, 180, 141, 31))
        self.labelTimeRemaining.setStyleSheet(_fromUtf8("font: oblique 18pt \"Ubuntu Condensed\";color:rgb(60, 90, 60)"))
        self.labelTimeRemaining.setObjectName(_fromUtf8("labelTimeRemaining"))
        self.label_4 = QtGui.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(450, 20, 71, 17))
        self.label_4.setStyleSheet(_fromUtf8("font: 14pt \"Ubuntu Condensed\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.widget_3 = QtGui.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(510, 20, 18, 18))
        self.widget_3.setStyleSheet(_fromUtf8("background-color:rgb(255, 0, 0)"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.labelIterationsCompleted = QtGui.QLabel(Form)
        self.labelIterationsCompleted.setGeometry(QtCore.QRect(320, 290, 131, 17))
        self.labelIterationsCompleted.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.labelIterationsCompleted.setObjectName(_fromUtf8("labelIterationsCompleted"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 280, 271, 31))
        self.label_2.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";color:rgb(60, 90, 60)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButtonFinish = QtGui.QPushButton(Form)
        self.pushButtonFinish.setGeometry(QtCore.QRect(440, 540, 141, 31))
        self.pushButtonFinish.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(210, 225, 210);background-color:rgb(105,150,105)"))
        self.pushButtonFinish.setObjectName(_fromUtf8("pushButtonFinish"))
        self.pushButtonBack = QtGui.QPushButton(Form)
        self.pushButtonBack.setGeometry(QtCore.QRect(290, 540, 141, 31))
        self.pushButtonBack.setStyleSheet(_fromUtf8("font: 21pt \"Ubuntu Condensed\";color:rgb(210, 225, 210);background-color:rgb(105,150,105)"))
        self.pushButtonBack.setObjectName(_fromUtf8("pushButtonBack"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_5.setText(_translate("Form", "CommandLine Details", None))
        self.label_3.setText(_translate("Form", "Shows Amount of Training Done", None))
        self.label_6.setText(_translate("Form", "Training Progress", None))
        self.label_7.setText(_translate("Form", "Estimated Time Remaining  : ", None))
        self.labelTimeRemaining.setText(_translate("Form", "12 minutes", None))
        self.label_4.setText(_translate("Form", "Status", None))
        self.labelIterationsCompleted.setText(_translate("Form", "100/60000", None))
        self.label_2.setText(_translate("Form", "Total Iterations Completed", None))
        self.pushButtonFinish.setText(_translate("Form", "Finis", None))
        self.pushButtonBack.setText(_translate("Form", "Back", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

