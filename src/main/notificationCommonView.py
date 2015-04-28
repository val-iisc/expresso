# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notificationSubMenu.ui'
#
# Created: Fri Apr  3 13:23:44 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from time import sleep
from multiprocessing import Process
from multiprocessing import Pool
import sys
from qtutils import inmain_later

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
    def __init__(self,parent=None,l=None):
        super(Ui_Form, self).__init__(parent)
        self.setupUi(self)
	if l!=None and len(l)>=5:
	    self.label_4.setText(l[0])
	    self.label.setText(l[1])
	    self.plainTextEdit.setText(l[4])
        #self.p=Process(target=self.runprogress())
        #self.p.start()
	#pool = Pool(processes=10)              # Start a worker processes.
	#pool.map(self.runprogress, [1])
    	#result = pool.apply_async(self.runprogress, [], self.callback) # Evaluate "f(10)" asynchronously calling callback when finished.

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(414, 104)
        Form.setStyleSheet(_fromUtf8("background-color:rgb(115,115,115,0); border-width: 0px;"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 40, 261, 23))
        self.progressBar.setStyleSheet(_fromUtf8("QProgressBar{\n"
"    border: 1px solid rgba(255, 255, 255,150);\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color:rgba(255, 255, 255);\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgba(255, 255, 255,100);\n"
"    width: 10px;\n"
"    margin: 1px;\n"
"}\n"
""))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 17))
        self.label.setStyleSheet(_fromUtf8("color:rgb(255,255,255);\n"
"font: 63 15pt \"Ubuntu Condensed\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 81, 111, 17))
        self.label_2.setStyleSheet(_fromUtf8("font: 12pt \"Ubuntu Condensed\"; color:rgb(255,255,255)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 77, 91, 20))
        self.label_3.setStyleSheet(_fromUtf8("background-color:rgba(0,0,0,0);color:rgb(255,255,255,175)"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.plainTextEdit = QtGui.QTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(280, 10, 121, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(_fromUtf8("background-color:rgba(0,0,0,50);\n"
"font: 11pt \"Ubuntu Condensed\";\n"
"color:rgb(255,255,255,175)"))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(170, 10, 91, 20))
        self.label_4.setStyleSheet(_fromUtf8("background-color:rgba(255,255,255,0); color:rgba(255,255,255,175);\n"
"font: 12pt \"Ubuntu Condensed\";\n"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.toolButton = QtGui.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(340, 74, 61, 25))
        self.toolButton.setStyleSheet(_fromUtf8("background-color:rgba(255,255,255,150);  border-width: 0px;"))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Train Data", None))
        self.label_2.setText(_translate("Form", "1 hour 55 minutes", None))
        self.label_3.setText(_translate("Form", " In Progress", None))
        self.plainTextEdit.setText(_translate("Form", "Traing for data \'cifar\' has started.", None))
        self.label_4.setText(_translate("Form", "Train View", None))
        self.toolButton.setText(_translate("Form", "details", None))



    def runprogress(self,temp=0):
        #print self.progressBar.value()
        #print str(self.progressBar.text())
        while(self.progressBar.value()<99):
            #sleep(1)
            self.progressBar.setValue(self.progressBar.value()+5)

        self.progressBar.setValue(100)
        #self.widget.setStyleSheet(_fromUtf8("background-color:rgb(0, 255, 0)"))
        mb=QtGui.QMessageBox.about(None,"Import Completed","Data has Sucessfully been Imported")
        #mb.setText('Process Completed')

    def mydelay(self):
        sleep(1)
        self.progressBar.setValue(self.progressBar.value()+5)
    def callback(self):
	pass

if __name__ == "__main__": 
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

