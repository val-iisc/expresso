# -*- coding: utf-8 -*-
##############
# Written by : Jaley Dholakiya
# Video Analytics Lab,IISc
#############


# Form implementation generated from reading ui file 'pipelineView.ui'
#
# Created: Tue Apr  7 15:57:03 2015
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
        Form.resize(291, 351)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(150,150,90);"))
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 121, 131))
        self.listWidget.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";background-color:rgb(230,240,210);color:rgb(45,60,45)"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 221, 31))
        self.label.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget_2 = QtGui.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(160, 30, 121, 131))
        self.listWidget_2.setStyleSheet(_fromUtf8("font: 18pt \"Ubuntu Condensed\";background-color:rgb(230,240,210);color:rgb(45,60,45)"))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(134, 50, 23, 25))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(134, 80, 23, 25))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton_3 = QtGui.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(134, 110, 23, 25))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.toolButton_5 = QtGui.QToolButton(Form)
        self.toolButton_5.setGeometry(QtCore.QRect(258, 3, 23, 25))
        self.toolButton_5.setObjectName(_fromUtf8("toolButton_5"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 200, 41, 61))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.layoutWidget_2 = QtGui.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 200, 71, 62))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.spinBoxMax = QtGui.QSpinBox(self.layoutWidget_2)
        self.spinBoxMax.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);"))
        self.spinBoxMax.setObjectName(_fromUtf8("spinBoxMax"))
        self.verticalLayout_2.addWidget(self.spinBoxMax)
        self.spinBoxMin = QtGui.QSpinBox(self.layoutWidget_2)
        self.spinBoxMin.setStyleSheet(_fromUtf8("background-color:rgb(230,240,210);"))
        self.spinBoxMin.setObjectName(_fromUtf8("spinBoxMin"))
        self.verticalLayout_2.addWidget(self.spinBoxMin)
        self.layoutWidget_3 = QtGui.QWidget(Form)
        self.layoutWidget_3.setGeometry(QtCore.QRect(50, 270, 81, 66))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalSliderAlpha = QtGui.QSlider(self.layoutWidget_3)
        self.horizontalSliderAlpha.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderAlpha.setObjectName(_fromUtf8("horizontalSliderAlpha"))
        self.verticalLayout_4.addWidget(self.horizontalSliderAlpha)
        self.horizontalSliderBeta = QtGui.QSlider(self.layoutWidget_3)
        self.horizontalSliderBeta.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderBeta.setObjectName(_fromUtf8("horizontalSliderBeta"))
        self.verticalLayout_4.addWidget(self.horizontalSliderBeta)
        self.layoutWidget_4 = QtGui.QWidget(Form)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 270, 41, 71))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(self.layoutWidget_4)
        self.label_2.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget_4)
        self.label_3.setStyleSheet(_fromUtf8("font: 15pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(10, 160, 97, 22))
        self.checkBox.setStyleSheet(_fromUtf8("font: 12pt \"Ubuntu Condensed\";color:rgb(210, 225, 210)"))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Pipeline Operation", None))
        self.toolButton.setText(_translate("Form", ">", None))
        self.toolButton_2.setText(_translate("Form", "x", None))
        self.toolButton_3.setText(_translate("Form", "r", None))
        self.toolButton_5.setText(_translate("Form", "+", None))
        self.label_4.setText(_translate("Form", "Max", None))
        self.label_5.setText(_translate("Form", "Min", None))
        self.label_2.setText(_translate("Form", "a", None))
        self.label_3.setText(_translate("Form", "b", None))
        self.checkBox.setText(_translate("Form", "On Fly", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

