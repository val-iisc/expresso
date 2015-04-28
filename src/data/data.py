# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data.ui'
#
# Created: Wed Feb  4 00:46:43 2015
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

class Ui_Data(object):
    def setupUi(self, Data):
        Data.setObjectName(_fromUtf8("Data"))
        Data.resize(351, 227)
        self.label_4 = QtGui.QLabel(Data)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.widget = QtGui.QWidget(Data)
        self.widget.setGeometry(QtCore.QRect(130, 60, 181, 95))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEditData = QtGui.QLineEdit(self.widget)
        self.lineEditData.setObjectName(_fromUtf8("lineEditData"))
        self.verticalLayout.addWidget(self.lineEditData)
        self.lineEditFolderData = QtGui.QLineEdit(self.widget)
        self.lineEditFolderData.setObjectName(_fromUtf8("lineEditFolderData"))
        self.verticalLayout.addWidget(self.lineEditFolderData)
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout.addWidget(self.comboBox)
        self.widget1 = QtGui.QWidget(Data)
        self.widget1.setGeometry(QtCore.QRect(10, 60, 101, 91))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.widget1)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.widget2 = QtGui.QWidget(Data)
        self.widget2.setGeometry(QtCore.QRect(10, 170, 301, 29))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonData = QtGui.QPushButton(self.widget2)
        self.pushButtonData.setObjectName(_fromUtf8("pushButtonData"))
        self.horizontalLayout.addWidget(self.pushButtonData)
        self.buttonBox = QtGui.QDialogButtonBox(self.widget2)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Data)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Data.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Data.reject)
        QtCore.QMetaObject.connectSlotsByName(Data)

    def retranslateUi(self, Data):
        Data.setWindowTitle(_translate("Data", "Dialog", None))
        self.label_4.setText(_translate("Data", "Upload Data", None))
        self.label.setText(_translate("Data", "Name", None))
        self.label_2.setText(_translate("Data", "Folder Name", None))
        self.label_3.setText(_translate("Data", "Type", None))
        self.pushButtonData.setText(_translate("Data", "Options", None))

    def 

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Data = QtGui.QDialog()
    ui = Ui_Data()
    ui.setupUi(Data)
    Data.show()
    sys.exit(app.exec_())

