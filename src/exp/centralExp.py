# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'centralDefault.ui'
#
# Created: Sat Mar  7 00:20:05 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import os

root=os.getenv('EXPRESSO_ROOT')
print root
sys.path.append(root+'/src/custom')
import netWidget
sys.path.append(root+'/src/exp')
sys.path.append(root+'/src/custom')
sys.path.append(root+'/src/data')
import finalView
import centralData
import expChooseView
import expView
import expVisuallizeView
import expTesting
sys.path.append(root+'/src/exp/SVM')
import testSVMView
import denseCRFView
import denseCRFCalc
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
        Form.resize(611, 591)
	

        self.stackedWidget = QtGui.QStackedWidget(Form)
	self.stackedWidget.setGeometry(QtCore.QRect(0,0,611,591))
	self.addPages()
        #self.widget.setGeometry(QtCore.QRect(0, 0, 611, 591))
        #self.widget.setObjectName(_fromUtf8("widget"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

    def addPages(self):
	self.addPage0()
	self.addPage1()
	self.addPage2()
	self.addPage3()
	self.addPage4()
	self.addPage5()
	self.addPage6()
	self.currentIndex=0

    def addPage0(self):
        self.page0Container=QtGui.QWidget(self)
        self.page0Container.setGeometry(0,0,611,591)
        self.page0Container.setStyleSheet("background-color:rgb(150,150,90);")
        self.page0Widget=expChooseView.Ui_Form(self.page0Container)
        self.page0Widget.setGeometry(0,0,611,591)
        #self.page1Container.setWidget(self.page1Widget)
        self.stackedWidget.addWidget(self.page0Container)



    def addPage0Old(self):
	self.page0Layout=QtGui.QVBoxLayout()
	self.page0Widget=QtGui.QWidget(self)  #Widget
	self.page0Widget.setLayout(self.page0Layout) #Layout
	self.page0Widget.setGeometry(QtCore.QRect(10,10,100,100))
	self.page0ButtonGroup=QtGui.QButtonGroup(self.page0Widget)
	self.page0ButtonNew=QtGui.QRadioButton("Create New Experiment")
	self.page0ButtonVis=QtGui.QRadioButton("Visualize Old Experiment")
	self.page0ButtonGroup.addButton(self.page0ButtonNew)
	self.page0ButtonGroup.addButton(self.page0ButtonVis)
	self.page0Layout.addWidget(self.page0ButtonNew)
	self.page0Layout.addWidget(self.page0ButtonVis)
	self.stackedWidget.addWidget(self.page0Widget)	

    def addPage1(self):
        self.page1Container=QtGui.QWidget(self)
        self.page1Container.setGeometry(0,0,611,591)
        self.page1Container.setStyleSheet("background-color:rgb(150,150,90);")
        self.page1Widget=expView.Ui_Form(parent=self.page1Container)
        self.page1Widget.setGeometry(0,0,611,591)
        #self.page1Container.setWidget(self.page1Widget)
        self.stackedWidget.addWidget(self.page1Container)



    def addPage1Old(self):
	self.page1Layout=QtGui.QVBoxLayout()
	self.page1Layout.setGeometry(QtCore.QRect(0,0,611,591))
	#Box for Net
	self.page1Widget=QtGui.QWidget(self)  #Widget

	self.page1Widget.setLayout(self.page1Layout) #Layout
	self.page1Widget.setGeometry(QtCore.QRect(0,0,611,591))
	self.page1NetBox=QtGui.QComboBox(self)
	#Box for Data
	self.page1Layout1=QtGui.QHBoxLayout()
	self.page1Widget1=QtGui.QWidget()
	self.page1Widget1.setGeometry(0,0,611,591)
	self.page1Widget1.setStyleSheet("background-color:rgb(210,225,210);")

	self.page1Widget1.setLayout(self.page1Layout1)
	


	#Insert 2 Vertical Box inside it

	#Final Settings
	


	self.page1Layout.addWidget(self.page1NetBox)
	self.page1Layout.addWidget(self.page1Widget1)
	self.stackedWidget.addWidget(self.page1Widget)	

    def addPage2(self):
	self.page2Container=QtGui.QWidget(self)
        self.page2Container.setGeometry(0,0,611,591)
	self.page2Container.setStyleSheet("background-color:rgb(150,150,90);")
	self.page2Widget=expVisuallizeView.Ui_Form(self.page2Container)
	self.page2Widget.setGeometry(0,0,691,591)
	self.stackedWidget.addWidget(self.page2Container)


    def addPage3(self):
	self.page3Container=QtGui.QWidget(self)
        self.page3Container.setGeometry(0,0,611,591)
	self.page3Container.setStyleSheet("background-color:rgb(150,150,90);")
	self.page3Widget=expTesting.Ui_Form(self.page3Container)
	self.page3Widget.setGeometry(0,0,691,591)
	self.stackedWidget.addWidget(self.page3Container)

    def addPage4(self):
	self.page4Container=QtGui.QWidget(self)
        self.page4Container.setGeometry(0,0,611,591)
	self.page4Container.setStyleSheet("background-color:rgb(0,0,0);")
	#self.page4Widget=QtGui.QWidget(self.page4Container)
	self.page4Widget=denseCRFView.Ui_Form(self.page4Container)
	self.page4Widget.setGeometry(0,0,691,591)
	self.stackedWidget.addWidget(self.page4Container)


    def addPage5(self):
	self.page5Container=QtGui.QWidget(self)
        self.page5Container.setGeometry(0,0,611,591)
	self.page5Container.setStyleSheet("background-color:rgb(150,150,90);")
	self.page5Widget=testSVMView.Ui_Form(self.page5Container)
	self.page5Widget.setGeometry(0,0,691,591)
	self.stackedWidget.addWidget(self.page5Container)

    def addPage6(self):
	self.page6Container=QtGui.QWidget(self)
        self.page6Container.setGeometry(0,0,611,591)
	self.page6Container.setStyleSheet("background-color:rgb(150,150,90);")
	self.page6Widget=denseCRFCalc.Ui_Form(self.page6Container)
	self.page6Widget.setGeometry(0,0,691,591)
	self.stackedWidget.addWidget(self.page6Container)



    def pushButtonNextSlot(self):
	if self.currentIndex==3:return
	print 'Next Clicked: '+str(self.currentIndex)
	self.currentIndex=self.currentIndex+1
	self.stackedWidget.setCurrentIndex(self.currentIndex)

    def pushButtonBackSlot(self):
	print 'back clicked'
	if self.currentIndex==0:return
	self.currentIndex=0
	self.stackedWidget.setCurrentIndex(self.currentIndex)

    def switchToPage1(self):
	self.currentIndex=1
	self.stackedWidget.setCurrentIndex(self.currentIndex)
    def switchToPage2(self):
	self.currentIndex=2
	self.stackedWidget.setCurrentIndex(self.currentIndex)

    def switchToPage3(self):
	self.currentIndex=3
	self.stackedWidget.setCurrentIndex(self.currentIndex)

    def switchToPage4(self):
	self.currentIndex=4
	self.stackedWidget.setCurrentIndex(self.currentIndex)


    def switchToPage5(self):
	self.currentIndex=5
	self.stackedWidget.setCurrentIndex(self.currentIndex)

    def switchToPage6(self):
	self.currentIndex=6
	self.stackedWidget.setCurrentIndex(self.currentIndex)

 

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

