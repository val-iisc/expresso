# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'left1Default.ui'
#
# Created: Sat Mar  7 00:20:17 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
root=os.getenv('EXPRESSO_ROOT')
import sys
sys.path.append(root+'/src/wizard')
import wizardView




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
        self.widget = wizardView.Ui_Form(Form,flowName='Net View')
        self.widget.heading1Label.setStyleSheet(_fromUtf8("background-color:rgb(0,0,0,0);color:rgba(255,255,255,175);\n"
"font: 18pt \"Ubuntu Condensed\";"))

        self.widget.setGeometry(QtCore.QRect(0, 0, 291, 351))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

