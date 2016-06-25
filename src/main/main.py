

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Mar  6 22:18:35 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from qtutils import inmain_later,inthread,inmain
from time import sleep
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

import sys
import os
import numpy as np
# env_dict=np.load('../../env_variables.npy')
# print env_dict,'ENVIRONMENT DICTIONARY'

# for idx in range(len(env_dict)//2):
#    os.environ[env_dict[idx]]=env_dict[idx+len(env_dict)//2]

root=str(os.getenv('EXPRESSO_ROOT'))
print root,'ROOT'
import deleteView



sys.path.append(root+'/src/default')
sys.path.append(root+'/src/data')
sys.path.append(root+'/src/net')
sys.path.append(root+'/src/exp')
sys.path.append(root+'/src/train')

#Default Imports
import centralDefault
import bottomDefault
import left1Default
import left2Default

#Data Imports
import centralData
import bottomData
import left1Data
import left2Data

#Net Imports
import centralNet
import bottomNet
import left1Net
import left2Net


#Exp Imports
import centralExp
import bottomExp
import left1Exp
import left2Exp

#Train Imports
import centralTrain
import bottomTrain
import left1Train
import left2Train

#Notification Import
import notificationListItemWidget
from notificationHandler import NotificationHandler

#Settings Import
import settingsView
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    signalCompleteTrigger=QtCore.pyqtSignal(object)
    signalMessageOpacityTrigger=QtCore.pyqtSignal(object)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1054, 819)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedCentral = QtGui.QStackedWidget(self.centralwidget)
        self.stackedCentral.setGeometry(QtCore.QRect(330, 80, 611, 591))
        self.stackedCentral.setObjectName(_fromUtf8("stackedCentral"))
        self.stackedBottom = QtGui.QStackedWidget(self.centralwidget)
        self.stackedBottom.setGeometry(QtCore.QRect(330, 690, 611, 61))
        self.stackedBottom.setObjectName(_fromUtf8("stackedBottom"))
        self.stackedLeft2 = QtGui.QStackedWidget(self.centralwidget)
        self.stackedLeft2.setGeometry(QtCore.QRect(20, 450, 291, 301))
        self.stackedLeft2.setObjectName(_fromUtf8("stackedLeft2"))
        self.stackedLeft1 = QtGui.QStackedWidget(self.centralwidget)
        self.stackedLeft1.setGeometry(QtCore.QRect(20, 80, 291, 351))
        self.stackedLeft1.setObjectName(_fromUtf8("stackedLeft1"))
        self.pushButtonData = QtGui.QPushButton(self.centralwidget)
        self.pushButtonData.setGeometry(QtCore.QRect(170, 10, 120, 60))
	self.pushButtonData.setStyleSheet("background-color:rgba(255,255,255,0)")
        self.pushButtonData.setObjectName(_fromUtf8("pushButtonData"))
	self.pushButtonData.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonNet = QtGui.QPushButton(self.centralwidget)
        self.pushButtonNet.setGeometry(QtCore.QRect(305, 10, 120, 60))
	self.pushButtonNet.setStyleSheet("background-color:rgba(255,255,255,0)")
	self.pushButtonNet.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonNet.setObjectName(_fromUtf8("pushButtonNet"))
        self.pushButtonExp = QtGui.QPushButton(self.centralwidget)
        self.pushButtonExp.setGeometry(QtCore.QRect(575, 10, 120, 60))
        self.pushButtonExp.setObjectName(_fromUtf8("pushButtonExp"))
	self.pushButtonExp.setStyleSheet("background-color:rgba(255,255,255,0)")
	self.pushButtonExp.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonTrain = QtGui.QPushButton(self.centralwidget)
        self.pushButtonTrain.setGeometry(QtCore.QRect(440, 10, 120, 60))
        self.pushButtonTrain.setObjectName(_fromUtf8("pushButtonTrain"))
	self.pushButtonTrain.setStyleSheet("background-color:rgba(255,255,255,0)")
	self.pushButtonTrain.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonDataDefault = QtGui.QPushButton(self.centralwidget)
        self.pushButtonDataDefault.setGeometry(QtCore.QRect(35, 10, 120, 60))
        self.pushButtonDataDefault.setObjectName(_fromUtf8("pushButtonDataDefault"))
	self.pushButtonDataDefault.setStyleSheet("background-color:rgba(255,255,255,0)")
	self.pushButtonDataDefault.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonNotification = QtGui.QPushButton(self.centralwidget)
        self.pushButtonNotification.setGeometry(QtCore.QRect(990, 25, 45, 45))
        self.pushButtonNotification.setObjectName(_fromUtf8("pushButtonDataDefault"))
	self.pushButtonNotification.setStyleSheet("background-color:rgba(255,255,255,0)")
	self.pushButtonNotification.setFocusPolicy(QtCore.Qt.NoFocus)

	#Settings
        self.pushButtonSettings = QtGui.QPushButton(self.centralwidget)
        self.pushButtonSettings.setGeometry(QtCore.QRect(940, 39, 30, 30))
        self.pushButtonSettings.setObjectName(_fromUtf8("pushButtonDataDefault"))
	self.pushButtonSettings.setStyleSheet("background-color:rgba(255,255,255,0)")
	self.pushButtonSettings.setFocusPolicy(QtCore.Qt.NoFocus)


	#Delete
        self.pushButtonDelete = QtGui.QPushButton(self.centralwidget)
        self.pushButtonDelete.setGeometry(QtCore.QRect(900, 39, 30, 30))
        self.pushButtonDelete.setObjectName(_fromUtf8("pushButtonDataDefault"))
	self.pushButtonDelete.setStyleSheet("background-color:rgba(255,255,255,0)")
	self.pushButtonDelete.setFocusPolicy(QtCore.Qt.NoFocus)


	self.labelNotification=QtGui.QLabel(self.centralwidget)
	self.labelNotification.setGeometry(QtCore.QRect(1015,20,27,27))
	self.labelNotification.setStyleSheet("background-color:rgb(255,0,0);\
  						border: 1.5px solid  white;\
						border-radius: 6px;\
						font:14pt \"Ubuntu Condensed\";\
						color:rgb(255,255,255)")
	self.labelNotification.setText(" 0")
	self.listViewNotification=QtGui.QListWidget(self.centralwidget)
	self.listViewNotification.setGeometry(QtCore.QRect(620,75,414,400))
	self.listViewNotification.setStyleSheet("background-color:rgba(200,200,200,0);\
  						border: 0px solid  grey;\
						border-radius: 0px;\
						selection-background-color:rgba(0,0,0,0);\
						font:14pt \"Ubuntu Condensed\";\
						color:rgb(0,0,0)")
	self.listViewNotification.setFocusPolicy(QtCore.Qt.NoFocus)	
	#self.listViewNotification.addItem("WELCOME\nThis is Notification Panel")
	#Start doing it
	#Main Page Work


	self.labelDefaultTitle=QtGui.QLabel(self.centralwidget)
	self.labelDefaultTitle.setText("Task View (Notifications)")
	self.labelDefaultTitle.setGeometry(QtCore.QRect(400,150,450,70))
	self.labelDefaultTitle.setStyleSheet("font:36pt \"Ubuntu Condensed\";")	


	
	#self.listViewNotification.addItem(notificationItem)
	#self.listViewNotification.setItemWidget(,self.listViewNotification)

	#End Doing It



        """
	self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(940, 670, 120, 80))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.stackedWidget.addWidget(self.page_2)
        """
	MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1054, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
	#Extra Functions begin
	self.changeLook()
	self.addDefaultView()
	self.addDataView()
	self.addNetView()
	self.addExpView()
	self.addTrainView()
	#Adding Triggers
	self.addButtonTriggers()
	self.addTrainTriggers()
	self.addExpTriggers()
	self.addDataTriggers()
	self.addNetTriggers()
	self.addRefreshTriggers()
	#Icon Related
	self.currentView=0; 
	self.initiallizeIcons()
	self.updateIcons()
	#NotificationRelated
	self.notificationTristate=0; #Tristate=0/1 clicked/unclicked,2 for new
	self.initiallizeNotifications()
	self.addNotificationTriggers()
	#Extra Functions End
	self.notificationList=[]
	#self.refreshNotificationList()
	self.notificationHandler=NotificationHandler()
	
	#Message Alert
	self.messageAlert=QtGui.QTextEdit(self.centralwidget)
	self.messageAlert.setGeometry(QtCore.QRect(713,15,180,60))
	self.messageAlert.setStyleSheet("background-color:rgba(255,255,255,0);font:14pt \"Ubuntu Condensed\";border-width:0px;color:rgba(0,0,0,0);");
	self.messageAlert.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);
	self.messageAlert.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff);

	self.messageAlert.setReadOnly(True)
	self.messageAlert.setFrameShape(QtGui.QFrame.NoFrame)
	self.signalMessageOpacityTrigger.connect(self.changeMessageOpacity)
	#Message Alert Ends

	#Settings Related
	self.initiallizeSettings()
	#Delete Related
	self.initiallizeGroupDelete()

        self.retranslateUi(MainWindow)

	self.onMainView()
	# May 15 Starts (Temporary Hiding of Task/Main/Default View)
	self.onPushButtonDataClicked()
	self.pushButtonDataDefault.hide()
	## May 15 Ends
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def runprogress(self,value):
	self.notificationItem.progressBar.setValue(int(value)*10)

	
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        #self.pushButtonData.setText(_translate("MainWindow", "Data View", None))
        #self.pushButtonNet.setText(_translate("MainWindow", "Net View", None))
        #self.pushButtonExp.setText(_translate("MainWindow", "Exp View", None))
        #self.pushButtonTrain.setText(_translate("MainWindow", "Train View", None))
        #self.pushButtonDataDefault.setText(_translate("MainWindow", "Default", None))
	self.signalCompleteTrigger.connect(self.runprogress)	

    def changeLook(self):
        self.p = MainWindow.palette()

	self.p.setColor(MainWindow.backgroundRole(), QtGui.QColor(51,161,201))
        MainWindow.setPalette(self.p)
	#self.stackedCentral.setStyleSheet("background-color: rgb(235,250,235);")
	#self.stackedBottom.setStyleSheet("background-color: rgb(235,250,235);")
	#self.stackedLeft1.setStyleSheet("background-color: rgb(235,250,235);")
	#self.stackedLeft2.setStyleSheet("background-color: rgb(235,250,235);")


    def addDefaultView(self):
 	self.pageCentralDefault=centralDefault.Ui_Form(self)
	self.pageBottomDefault=bottomDefault.Ui_Form(self)
	self.pageLeft1Default=left1Default.Ui_Form(self)
	self.pageLeft2Default=left2Default.Ui_Form(self)


        self.stackedCentral.addWidget(self.pageCentralDefault)
        self.stackedBottom.addWidget(self.pageBottomDefault)
        self.stackedLeft1.addWidget(self.pageLeft1Default)
        self.stackedLeft2.addWidget(self.pageLeft2Default)
		


    def addDataView(self):
 	self.pageCentralData = centralData.Ui_Form(self)
	self.pageBottomData=bottomData.Ui_Form(self)
	self.pageLeft1Data=left1Data.Ui_Form(self)
	self.pageLeft2Data=left2Data.Ui_Form(self)

        self.stackedCentral.addWidget(self.pageCentralData)
        self.stackedBottom.addWidget(self.pageBottomData)
        self.stackedLeft1.addWidget(self.pageLeft1Data)
        self.stackedLeft2.addWidget(self.pageLeft2Data)
	
    def addNetView(self):
 	self.pageCentralNet = centralNet.Ui_Form(self)
	self.pageBottomNet=bottomNet.Ui_Form(self)
	self.pageLeft1Net=left1Net.Ui_Form(self)
	self.pageLeft2Net=left2Net.Ui_Form(self)

        self.stackedCentral.addWidget(self.pageCentralNet)
        self.stackedBottom.addWidget(self.pageBottomNet)
        self.stackedLeft1.addWidget(self.pageLeft1Net)
        self.stackedLeft2.addWidget(self.pageLeft2Net)

    def addExpView(self):
 	self.pageCentralExp = centralExp.Ui_Form(self)
	self.pageBottomExp=bottomExp.Ui_Form(self)
	self.pageLeft1Exp=left1Exp.Ui_Form(self)
	self.pageLeft1Exp.setStyleSheet('background-color:rgba(255,255,255,0)')
	self.pageLeft2Exp=left2Exp.Ui_Form(self)

        self.stackedCentral.addWidget(self.pageCentralExp)
        self.stackedBottom.addWidget(self.pageBottomExp)
        self.stackedLeft1.addWidget(self.pageLeft1Exp)
        self.stackedLeft2.addWidget(self.pageLeft2Exp)
	
    def addTrainView(self):
 	self.pageCentralTrain = centralTrain.Ui_Form(self)
	self.pageBottomTrain=bottomTrain.Ui_Form(self)
	self.pageLeft1Train=left1Train.Ui_Form(self)
	self.pageLeft2Train=left2Train.Ui_Form(self)

        self.stackedCentral.addWidget(self.pageCentralTrain)
        self.stackedBottom.addWidget(self.pageBottomTrain)
        self.stackedLeft1.addWidget(self.pageLeft1Train)
        self.stackedLeft2.addWidget(self.pageLeft2Train)
    def addButtonTriggers(self):
	self.pushButtonTrain.clicked.connect(self.onPushButtonTrainClicked)
	self.pushButtonExp.clicked.connect(self.onPushButtonExpClicked)
	self.pushButtonData.clicked.connect(self.onPushButtonDataClicked)
	self.pushButtonNet.clicked.connect(self.onPushButtonNetClicked)
	self.pushButtonDataDefault.clicked.connect(self.onPushButtonDefaultClicked)
	
    def onPushButtonTrainClicked(self):
	self.currentView=4
	self.updateIcons()
	self.stackedLeft1.setCurrentIndex(4)
	self.stackedCentral.setCurrentIndex(4)
	self.stackedBottom.setCurrentIndex(4)
	self.stackedLeft2.setCurrentIndex(4)
	self.p.setColor(MainWindow.backgroundRole(), QtGui.QColor(120,180,120))
        MainWindow.setPalette(self.p)
	self.onOtherThanMainView()

    def onPushButtonExpClicked(self):
	self.currentView=3
	self.updateIcons()
	self.stackedLeft1.setCurrentIndex(3)
	self.stackedCentral.setCurrentIndex(3)
	self.stackedLeft2.setCurrentIndex(3)
	self.stackedBottom.setCurrentIndex(3)
	self.pageCentralExp.pushButtonBackSlot()
	self.pageLeft2Exp.pushButtonBackSlot()
	self.p.setColor(MainWindow.backgroundRole(), QtGui.QColor(150,150,90))
        MainWindow.setPalette(self.p)
	self.onOtherThanMainView()
	self.pageBottomExp.pushButtonBackSlot()
	self.pageBottomExp.pushButtonViewResults.hide()

    def onPushButtonDataClicked(self):
	self.currentView=1
	self.updateIcons()
	self.stackedLeft1.setCurrentIndex(1)
	self.stackedCentral.setCurrentIndex(1)
	self.stackedLeft2.setCurrentIndex(1)
	self.stackedBottom.setCurrentIndex(1)
	self.p.setColor(MainWindow.backgroundRole(), QtGui.QColor(115,115,115))
        MainWindow.setPalette(self.p)
	self.onOtherThanMainView()

    def onPushButtonNetClicked(self):
	self.currentView=2
	self.updateIcons()
	self.stackedCentral.setCurrentIndex(2)
	self.stackedLeft2.setCurrentIndex(2)
	self.stackedLeft1.setCurrentIndex(2)
	self.stackedBottom.setCurrentIndex(2)
	self.p.setColor(MainWindow.backgroundRole(), QtGui.QColor(49,74,93))
        MainWindow.setPalette(self.p)
	self.onOtherThanMainView()

    def onPushButtonDefaultClicked(self):
	self.currentView=0
	self.updateIcons()
	self.stackedCentral.setCurrentIndex(0)
	self.stackedLeft1.setCurrentIndex(0)
	self.stackedLeft2.setCurrentIndex(0)
	self.stackedBottom.setCurrentIndex(0)
	self.p.setColor(MainWindow.backgroundRole(), QtGui.QColor(51,161,201))
        MainWindow.setPalette(self.p)
	self.onMainView()
	pass

    def onMainView(self):
	self.notificationTristate=1;
	self.updateNotifications()
	self.listViewNotification.setGeometry(QtCore.QRect(400,250,414,400))
	self.listViewNotification.show()
	self.labelDefaultTitle.show()
	self.pushButtonNotification.hide()
	self.labelNotification.hide()
	self.labelNotification.setText(" 0")

    def onOtherThanMainView(self):
	self.listViewNotification.setGeometry(QtCore.QRect(620,75,414,400))
	self.listViewNotification.hide()
	self.pushButtonNotification.show()
	self.labelDefaultTitle.hide()

    def addTrainTriggers(self):
	### Flow 1 : Train Wizard Flow ###
	self.pageBottomTrain.pushButtonNext.clicked.connect(self.pageCentralTrain.pushButtonNextSlot)
	self.pageBottomTrain.pushButtonBack.clicked.connect(self.pageCentralTrain.pushButtonBackSlot)
	#Left2 Triggers
	self.pageBottomTrain.pushButtonNext.clicked.connect(self.pageLeft2Train.pushButtonNextSlot)
	self.pageBottomTrain.pushButtonBack.clicked.connect(self.pageLeft2Train.pushButtonBackSlot)
	#Central Triggers
	self.pageCentralTrain.page3Widget.pushButtonFinish.clicked.connect(self.pageCentralTrain.pushButtonBackSlot)
	
	self.pageCentralTrain.page3Widget.pushButtonFinish.clicked.connect(self.pageCentralTrain.createConfiguration)
	#Net List Based
	self.pageLeft2Train.page1Widget.listWidget.currentRowChanged.connect(self.pageCentralTrain.page1NetEditor.loadFromListSlot)
	#To save a new Net
	###self.pageBottomTrain.page1Widget.pushButton.clicked.connect(self.saveDeployNet)
	#Save the solver to solverpath, as soon as save button is clicked

    ####### Intermediate Train Triggers ################
	self.pageCentralTrain.page0Widget.pushButton_3.clicked.connect(self.pageCentralTrain.switchToPageSVM)

	self.pageCentralTrain.page0Widget.pushButton_3.clicked.connect(self.pageBottomTrain.switchToPageSVM)
	self.pageCentralTrain.page0Widget.pushButton_3.clicked.connect(self.pageLeft2Train.switchToPageSVM)

	self.pageCentralTrain.page0Widget.pushButton.clicked.connect(self.pageCentralTrain.pushButtonNextSlot)
	self.pageCentralTrain.page0Widget.pushButton.clicked.connect(self.pageBottomTrain.pushButtonNextSlot)
	self.pageCentralTrain.page0Widget.pushButton.clicked.connect(self.pageLeft2Train.pushButtonNextSlot)
	

    def saveDeployNet(self):
	#filename=str(self.pageBottomTrain.page1Widget.lineEdit.text())
	#reply=self.pageCentralTrain.page1NetEditor.saveFile(filename)
	reply=self.pageCentralTrain.page2Widget.saveConfig(filename)
	if(reply==True):
	    self.pageLeft2Train.page1Widget.appendConfig(filename)


    def testing(self,index=0):
	print 'hello',index
    def addExpTriggers(self):
	self.pageLeft2Exp.page2Widget.signalUpdateTriggered.connect(self.pageCentralExp.page2Widget.applyFuncList)
	### Flow 2 : Experiments Button Triggers ###
	#self.pageLeft1Exp.pushButtonNext.clicked.connect(self.pageCentralExp.pushButtonNextSlot)
	self.pageBottomExp.pushButtonBack.clicked.connect(self.pageCentralExp.pushButtonBackSlot)
	#Left2 Triggers
	#self.pageLeft1Exp.pushButtonNext.clicked.connect(self.pageLeft2Exp.pushButtonNextSlot)
	self.pageBottomExp.pushButtonBack.clicked.connect(self.pageLeft2Exp.pushButtonBackSlot)
	self.pageBottomExp.pushButtonBack.clicked.connect(self.pageBottomExp.pushButtonBack.hide)
	self.pageCentralExp.page0Widget.pushButton_4.clicked.connect(self.pageBottomExp.pushButtonViewResults.show)
	self.pageBottomExp.pushButtonBack.clicked.connect(self.pageBottomExp.pushButtonViewResults.hide)
	self.pageBottomExp.pushButtonViewResults.clicked.connect(self.pageCentralExp.switchToPage6)
	self.pageBottomExp.pushButtonViewResults.clicked.connect(self.pageLeft2Exp.switchToPage6)

	#RefreshDisplay of Dense CRF Results Start
	self.pageLeft2Exp.page6Widget.signalCompleteTrigger.connect(self.pageCentralExp.page6Widget.refreshTrigger)
	self.pageCentralExp.page6Widget.pushButtonRefresh.clicked.connect(self.pageLeft2Exp.page6Widget.refreshTrigger)
	#self.pageBottomExp.pushButtonViewResults.clicked.connect(self.pageCentralExp.page6Widget.refresh)

	#RefreshDisplay of Dense CRF Results Ends
	




	#Bottom Triggers
	#self.pageLeft1Exp.pushButtonNext.clicked.connect(self.pageBottomExp.pushButtonNextSlot)
	###self.pageLeft1Exp.pushButtonBack.clicked.connect(self.pageBottomExp.pushButtonBackSlot) #Commented on May 15
	#SaveFile
	#Net List Based
	#self.pageLeft2Exp.page1Widget.listWidget.currentRowChanged.connect(self.pageCentralExp.page1Widget.loadFromListSlot)
	self.pageCentralExp.page1Widget.signalCompleteTrigger.connect(self.pageLeft2Exp.page1Widget.fillList)
	self.pageCentralExp.page1Widget.signalCompleteTrigger.connect(self.pageCentralExp.page2Widget.fillList)

	self.pageCentralExp.page0Widget.pushButton.clicked.connect(self.pageCentralExp.switchToPage1)
	self.pageCentralExp.page0Widget.pushButton_2.clicked.connect(self.pageCentralExp.switchToPage2)
	self.pageCentralExp.page0Widget.pushButton_3.clicked.connect(self.pageCentralExp.switchToPage3)
	self.pageCentralExp.page0Widget.pushButton_4.clicked.connect(self.pageCentralExp.switchToPage4)
	self.pageCentralExp.page0Widget.pushButton_5.clicked.connect(self.pageCentralExp.switchToPage5)

	self.pageCentralExp.page0Widget.pushButton.clicked.connect(self.pageLeft2Exp.switchToPage1)
	self.pageCentralExp.page0Widget.pushButton_2.clicked.connect(self.pageLeft2Exp.switchToPage2)
	self.pageCentralExp.page0Widget.pushButton_3.clicked.connect(self.pageLeft2Exp.switchToPage3)
	#self.pageCentralExp.page0Widget.pushButton_4.clicked.connect(self.pageLeft2Exp.switchToPage4)
	#self.pageCentralExp.page0Widget.pushButton_5.clicked.connect(self.pageLeft2Exp.switchToPage5)


	# Make Back Reappear
	self.pageCentralExp.page0Widget.pushButton.clicked.connect(self.pageBottomExp.pushButtonBack.show)
	self.pageCentralExp.page0Widget.pushButton_2.clicked.connect(self.pageBottomExp.pushButtonBack.show)
	self.pageCentralExp.page0Widget.pushButton_3.clicked.connect(self.pageBottomExp.pushButtonBack.show)
	self.pageCentralExp.page0Widget.pushButton_4.clicked.connect(self.pageBottomExp.pushButtonBack.show)
	self.pageCentralExp.page0Widget.pushButton_5.clicked.connect(self.pageBottomExp.pushButtonBack.show)
	






    def refreshAllScreens(self,data=None):
	#Refreshing Data Flows
	sleep(0.1)
	if(data!=None):self.popMessage(str(data))
	self.pageCentralData.dataViewWidget.refreshTrigger()
	self.pageLeft2Net.widget.refreshTrigger()
	self.pageCentralExp.page1Widget.refreshTrigger()
	self.pageCentralExp.page2Widget.refreshTrigger()
	self.pageCentralExp.page3Widget.refreshTrigger()
	self.pageCentralExp.page4Widget.refreshTrigger()#Dense CRF Refresh
	self.pageCentralExp.page5Widget.refreshTrigger()
	self.pageLeft2Exp.page1Widget.refreshTrigger()
	self.pageCentralTrain.pageSVMWidget.refreshTrigger()
	self.pageCentralTrain.page3Widget.widget.refreshTrigger()
	self.pageLeft2Train.page1Widget.refreshTrigger()
	self.pageCentralNet.page0Widget.refreshTrigger()
	#Refreshing Net Flows	

    def addDataTriggers(self):
	### Flow 3 : Import Data
	pass

    def addRefreshTriggers(self):
	self.pageCentralData.importViewWidget.signalRefreshTrigger.connect(self.refreshAllScreens)
	self.pageCentralData.dataViewWidget.signalRefreshTrigger.connect(self.refreshAllScreens)
	self.pageCentralExp.page1Widget.signalRefreshTrigger.connect(self.refreshAllScreens)
	self.pageLeft2Exp.page1Widget.signalRefreshTrigger.connect(self.refreshAllScreens)
	#self.pageLeft2Exp.page1Widget.signalRefreshTrigger.connect(self.refreshAllScreens)

	#Net Triggers
	self.pageCentralNet.page0Widget.signalRefreshTrigger.connect(self.refreshAllScreens)
	self.pageLeft2Net.widget.signalRefreshTrigger.connect(self.refreshAllScreens)
	#Train Triggers
	self.pageCentralTrain.signalRefreshTrigger.connect(self.refreshAllScreens)
	self.pageCentralTrain.pageSVMWidget.signalRefreshTrigger.connect(self.refreshAllScreens)
	


    def addNotificationTriggers(self):

	self.pageCentralData.importViewWidget.signalStartedTrigger.connect(self.addNotificationItem)
	self.pageCentralData.importViewWidget.signalCompleteTrigger.connect(self.addNotificationItem)
	self.pageCentralTrain.signalStartedTrigger.connect(self.addNotificationItem)
	self.pageCentralTrain.signalCompleteTrigger.connect(self.addNotificationItem)
	self.pageCentralTrain.pageSVMWidget.signalStartedTrigger.connect(self.addNotificationItem)
	self.pageCentralTrain.pageSVMWidget.signalCompleteTrigger.connect(self.addNotificationItem)
	self.pageCentralExp.page1Widget.signalStartedTrigger.connect(self.addNotificationItem)
	self.pageCentralExp.page1Widget.signalCompleteTrigger.connect(self.addNotificationItem)
	self.pageCentralExp.page5Widget.signalStartedTrigger.connect(self.addNotificationItem)
	self.pageCentralExp.page5Widget.signalCompleteTrigger.connect(self.addNotificationItem)

    def addNetTriggers(self):
	
	self.pageLeft2Net.widget.listWidget.itemClicked.connect(self.netListTriggerFunc)
	self.pageLeft2Net.widget.signalNewConfigTrigger.connect(self.pageCentralNet.page0Widget.onNewConfigClickedSlot)
	###Inspect the bellow Trigger
	self.pageCentralNet.page0Widget.signalCompleteTrigger.connect(self.pageLeft2Net.widget.updateList)

    def netListTriggerFunc(self,extra=None):
	row=self.pageLeft2Net.widget.listWidget.currentRow()
	self.pageCentralNet.page0Widget.onIndexChanged(row)


    def addNotificationItem(self,l):
	self.notificationHandler.addNotificationItem(l)
	self.refreshNotificationList()
	#Update Tab
	if(l[3]!=2):#If not update type notification
	    self.labelNotification.setText(" "+str(int(self.labelNotification.text())+1))
	    self.notificationTristate=2
	    self.updateNotifications()


    def refreshNotificationList(self):
	self.listViewNotification.clear()
	for elem in self.notificationHandler.notificationList:
	    print elem
	    #Add Items iteratively
	    notificationListItem = QtGui.QListWidgetItem(self.listViewNotification)
	    notificationListItem.setSizeHint(QtCore.QSize(414,108))
	    #notificationListItem.setStyleSheet("border:0px")
	    #notificationListItem.setBackground(QtGui.QColor(115,115,115))
	    self.listViewNotification.addItem(notificationListItem)
	    notificationItem=notificationListItemWidget.Ui_Form(self.listViewNotification,elem)#Passing data in constructor itself
	    self.listViewNotification.setItemWidget(notificationListItem,notificationItem)
	    notificationItem.signalToggledTrigger.connect(self.notificationHandler.changeWidgetState)
 

	    





    def addNotificationItemOld(self,l):
	self.notificationTristate=2
	self.labelNotification.setText(" "+str(int(self.labelNotification.text())+1))
	notificationListItem = QtGui.QListWidgetItem(self.listViewNotification)
	notificationListItem.setSizeHint(QtCore.QSize(414,104))
	notificationListItem.setBackground(QtGui.QColor(115,115,115))
	self.listViewNotification.addItem(notificationListItem)
	notificationItem=notificationListItemWidget.Ui_Form(self.listViewNotification)

	notificationItem.label.setText(l[1])
	notificationItem.label_4.setText(l[0])
	notificationItem.plainTextEdit.setText(l[4])

	notificationItem.setGeometry(QtCore.QRect(0,0,414,104))
	self.listViewNotification.setItemWidget(notificationListItem,notificationItem)
	self.updateNotifications()


	

    def initiallizeIcons(self):
	#On Buttons
	self.iconMainOn=QtGui.QIcon()
	self.iconMainOn.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/buttons/mainOnButton.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	self.iconDataOn=QtGui.QIcon()
	self.iconDataOn.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/buttons/dataOnButton.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	self.iconNetOn=QtGui.QIcon()
	self.iconNetOn.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/buttons/netOnButton.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	self.iconExpOn=QtGui.QIcon()
	self.iconExpOn.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/buttons/expOnButton.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	self.iconTrainOn=QtGui.QIcon()
	self.iconTrainOn.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/buttons/trainOnButton.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	#Off Buttons
	self.iconMainOff=QtGui.QIcon()
	self.iconMainOff.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/buttons/mainOffButton.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)


	self.iconDataOff=QtGui.QIcon()
	self.iconDataOff.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/buttons/dataOffButton.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	self.iconNetOff=QtGui.QIcon()
	self.iconNetOff.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/buttons/netOffButton.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	self.iconExpOff=QtGui.QIcon()
	self.iconExpOff.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/buttons/expOffButton.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	self.iconTrainOff=QtGui.QIcon()
	self.iconTrainOff.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/buttons/trainOffButton.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)

    def initiallizeNotifications(self):
	#On Buttons
	self.iconNotificationDefault=QtGui.QIcon()
	self.iconNotificationDefault.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/notifications/notificationDefault.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	self.iconNotificationClicked=QtGui.QIcon()
	self.iconNotificationClicked.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/notifications/notificationClicked.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	self.iconNotificationNew=QtGui.QIcon()
	self.iconNotificationNew.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/notifications/notificationNew.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)



	self.pushButtonNotification.setIcon(self.iconNotificationDefault)
	self.pushButtonNotification.setIconSize(QtCore.QSize(45,45))
	self.pushButtonNotification.clicked.connect(self.onNotificationClicked)
	self.listViewNotification.hide()
	self.labelNotification.hide()
	self.notificationTristate=1;

    def initiallizeSettings(self):
	self.iconSettings=QtGui.QIcon()
	self.iconSettings.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/settings/settings.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	self.pushButtonSettings.setIcon(self.iconSettings)
	self.pushButtonSettings.setIconSize(QtCore.QSize(30,30))
	#self.settingsWidget.show()
	self.pushButtonSettings.clicked.connect(self.onSettingsClicked)


    def initiallizeGroupDelete(self):
	self.iconDelete=QtGui.QIcon()
	self.iconDelete.addPixmap(QtGui.QPixmap(_fromUtf8(root+'/res/main/delete/delete.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	self.pushButtonDelete.setIcon(self.iconDelete)
	self.pushButtonDelete.setIconSize(QtCore.QSize(30,30))
	#self.settingsWidget.show()
	self.pushButtonDelete.clicked.connect(self.onDeleteClicked)


    

    def onSettingsClicked(self):
	
	self.settingsWidget=settingsView.Ui_Form()
	self.settingsWidget.setStyleSheet("background-color:rgb(255,255,255)")
	self.settingsWidget.setGeometry(QtCore.QRect(620,75,414,275))
	self.settingsWidget.show()


    def onDeleteClicked(self):
	
	self.deleteWidget=deleteView.Ui_Form()
	self.deleteWidget.setStyleSheet("background-color:rgb(255,255,255)")
	self.deleteWidget.setGeometry(QtCore.QRect(620,75,414,275))
	self.deleteWidget.signalRefreshTrigger.connect(self.refreshAllScreens)
	self.deleteWidget.show()



    def updateNotifications(self):
	self.refreshNotificationList()
	if(int(self.labelNotification.text())==0):
	    self.labelNotification.hide()

	if(self.notificationTristate==2):
	    self.pushButtonNotification.setIcon(self.iconNotificationNew)
	    self.labelNotification.show()
	if(self.notificationTristate==1):
	    self.pushButtonNotification.setIcon(self.iconNotificationDefault)
	    self.labelNotification.hide()
	    self.listViewNotification.hide()
	if(self.notificationTristate==0):
	    self.pushButtonNotification.setIcon(self.iconNotificationClicked)
	    self.listViewNotification.show()
	    self.labelNotification.hide()
	    self.labelNotification.setText(" 0")

    def onNotificationClicked(self):
	self.notificationTristate=0 if self.notificationTristate>0 else 1
	self.updateNotifications()

    def onNewNotification(self,text1,text2):
	self.notificationTristate=2
	self.listViewNotification.addItem(text1+' \n'+text2)
	self.updateNotifications()



    def importStartedNotification(self):
	self.labelNotification.setText(" "+str(int(self.labelNotification.text())+1))
	self.onNewNotification("DATA IMPORT","Import Started . . . ")

    def importCompletedNotification(self):
	self.labelNotification.setText(" "+str(int(self.labelNotification.text())+1))
	self.onNewNotification("DATA IMPORT","Import Ends . . . ")

    def updateIcons(self):
	if self.currentView==0:
	    self.pushButtonDataDefault.setIcon(self.iconMainOn)
	else:
	    self.pushButtonDataDefault.setIcon(self.iconMainOff)

	if self.currentView==1:
	    self.pushButtonData.setIcon(self.iconDataOn)
	else:
	    self.pushButtonData.setIcon(self.iconDataOff)

	if self.currentView==2:
	    self.pushButtonNet.setIcon(self.iconNetOn)
	else:
	    self.pushButtonNet.setIcon(self.iconNetOff)

	if self.currentView==3:
	    self.pushButtonExp.setIcon(self.iconExpOn)
	else:
	    self.pushButtonExp.setIcon(self.iconExpOff)


	if self.currentView==4:
	    self.pushButtonTrain.setIcon(self.iconTrainOn)
	else:
	    self.pushButtonTrain.setIcon(self.iconTrainOff)


	

	self.pushButtonDataDefault.setIconSize(QtCore.QSize(120,60))
	self.pushButtonData.setIconSize(QtCore.QSize(120,60))
	self.pushButtonNet.setIconSize(QtCore.QSize(120,60))
	self.pushButtonExp.setIconSize(QtCore.QSize(120,60))
	self.pushButtonTrain.setIconSize(QtCore.QSize(120,60))


    def popMessage(self,text='default'):
	self.messageAlert.setText(text)
	inthread(self.iterateMessage,text)

    def iterateMessage(self,text):
	for i in range(64):
	    sleep(.02)
	    self.signalMessageOpacityTrigger.emit(i*4)
	for i in range(64):
	    sleep(0.02)
	    self.signalMessageOpacityTrigger.emit(255-i*4)
	sleep(0.02)	
	self.signalMessageOpacityTrigger.emit(0)

	
    def changeMessageOpacity(self,a):
	self.messageAlert.setStyleSheet("background-color:rgba(255,255,255,"+str(a)+");font:12pt \"Ubuntu Condensed\";border-width:0px;color:rgba(0,0,0,+"+str(a)+")")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show() 
    sys.exit(app.exec_())

