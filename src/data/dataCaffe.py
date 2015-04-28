# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data.ui'
#
# Created: Wed Feb  4 00:06:28 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
## Jaley Start
import sys
import os
import DataHandler
import augmentoption

import configHandler
pathdict=configHandler.caffeConf().getdict()


## Jaley end

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

class DataMainWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(DataMainWidget, self).__init__(parent)
        self.setupUi(self)
        ## Jaley Start
        self.root=pathdict['default']

        ## Jaley end


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
        #self.buttonBox = QtGui.QDialogButtonBox(self.widget2)
        #self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        #self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.pushButtonOk=QtGui.QPushButton(self)
        self.pushButtonOk.setText("Ok")
        self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOK"))
        self.horizontalLayout.addWidget(self.pushButtonOk)

        #Added by Jaley start
        self.checkbox = QtGui.QCheckBox(Data);
        self.checkbox.setGeometry(QtCore.QRect(10, 152, 100, 15))
        self.checkbox.setObjectName(_fromUtf8("checkbox"))
        self.checkbox.setText('Has Label')
        #Added by Jaley Ends

        self.retranslateUi(Data)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Data.accept)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Data.reject)
        #QtCore.QMetaObject.connectSlotsByName(Data)

    def retranslateUi(self, Data):
        Data.setWindowTitle(_translate("Data", "Dialog", None))
        self.label_4.setText(_translate("Data", "Upload Data", None))
        self.label.setText(_translate("Data", "Name", None))
        self.label_2.setText(_translate("Data", "Folder Name", None))
        self.label_3.setText(_translate("Data", "Type", None))
        self.pushButtonData.setText(_translate("Data", "Options", None))
        #Jaley Start
        self.lineEditFolderData.installEventFilter(self)
        self.comboBox.addItem("Text")
        self.comboBox.addItem("LevelDB")
        self.comboBox.addItem("Mat")
        self.comboBox.addItem("HDF5")
        self.comboBox.addItem("PKL")
        self.comboBox.addItem("NPY")
        self.comboBox.currentIndexChanged.connect(self.onIndexChange)
        self.pushButtonOk.clicked.connect(self.pushButtonOkClicked)
        self.pushButtonData.clicked.connect(self.showWidget)


        #self.


    def onIndexChange(self,i):
        print i

    def pushButtonOkClicked(self):
        if self.lineEditData.text()=='' or self.lineEditFolderData.text()=='':
            QtGui.QMessageBox.about(self,'Incomplete Conversion','Data Left Out\nCheck Form again')
        #For TEXT option
        if(self.comboBox.currentIndex()==0 and str(self.lineEditData.text())!='' and self.lineEditFolderData.text()!=''):

            if(os.path.exists(self.lineEditFolderData.text()+'/test.txt')==0):
                QtGui.QMessageBox.about(self,'File Not Found',self.lineEditFolderData.text()+'/test.txt\n Does not Exist')
                return
            DataHandler.text2HDF5(str(self.lineEditData.text()), self.lineEditFolderData.text()+'/test.txt',self.root+'/Data',hasLabel=self.checkbox.isChecked())
            return
        #Jaley End

        if(self.comboBox.currentIndex()==2 and str(self.lineEditData.text())!='' and self.lineEditFolderData.text()!=''):
            if(os.path.exists(self.lineEditFolderData.text()+'/test.mat')==0):
                QtGui.QMessageBox.about(self,'File Not Found',self.lineEditFolderData.text()+'/test.mat\n Does not Exist')
                return
            DataHandler.mat2HDF5(str(self.lineEditData.text()), self.lineEditFolderData.text()+'/test.mat',self.root+'/Data',hasLabel=self.checkbox.isChecked())
            return

        if(self.comboBox.currentIndex()==1 and str(self.lineEditData.text())!='' and self.lineEditFolderData.text()!=''):
            if(os.path.exists(self.lineEditFolderData.text()+'/test_leveldb')==0):
                QtGui.QMessageBox.about(self,'File Not Found',self.lineEditFolderData.text()+'/test_leveldb\n Does not Exist')
                return
            DataHandler.leveldb2HDF5(str(self.lineEditData.text()), self.lineEditFolderData.text()+'/test_leveldb',self.root+'/Data',hasLabel=self.checkbox.isChecked())
            return

        #Jaley End


    def eventFilter(self, source, event):
        import sys
        if event.type() == QtCore.QEvent.MouseButtonPress:
            self.lineEditFolderData.setText(QtGui.QFileDialog.getExistingDirectory(self,self.tr("Open File"),str(self.root+'/Data')))
        return QtGui.QWidget.eventFilter(self, source, event)


    def showWidget(self):
        print 'mamla gadbad hai'
        self.widget1=QtGui.QWidget()
        self.widget2=augmentoption.AugmentOption(self.widget1)
        self.widget1.setGeometry(QtCore.QRect(130, 60, 400, 340))
        self.widget1.show()
        self.widget1.installEventFilter(self)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Data = QtGui.QDialog()
    ui = DataMainWidget()
    ui.setupUi(Data)
    Data.show()
    sys.exit(app.exec_())

