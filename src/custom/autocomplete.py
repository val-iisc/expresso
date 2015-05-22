from PyQt4 import QtGui,QtCore

import sys
import os
root=os.getenv('EXPRESSO_ROOT')
sys.path.append(os.getenv('CAFFE_ROOT')+'/python/caffe/proto')
import caffe_pb2
from google.protobuf import text_format
#from google.protobuf.descriptor import fielddescriptor
import inspect

class DictionaryCompleter(QtGui.QCompleter):
    def __init__(self, parent=None):
        words = []
        try:
            f = open("/usr/share/dict/words","r")
            for word in f:
                words.append(word.strip())
            f.close()
	    self.model=QtGui.QStringListModel(words,parent)

        except IOError:
            print "dictionary not in anticipated location"
        QtGui.QCompleter.__init__(self, self.model, parent)

class CompletionTextEdit(QtGui.QTextEdit):
    def __init__(self, parent=None):
        super(CompletionTextEdit, self).__init__(parent)
        #self.setMinimumWidth(400)
        self.setPlainText("")
        self.completer = None
        self.moveCursor(QtGui.QTextCursor.End)
	self.handle=caffe_pb2.NetParameter()
	self.appendData=''
	self.moveBack=0


    def setCompleter(self, completer):
        if self.completer:
            self.disconnect(self.completer, 0, self, 0)
        if not completer:
            return

        completer.setWidget(self)
        completer.setCompletionMode(QtGui.QCompleter.PopupCompletion)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer = completer
        self.connect(self.completer,
            QtCore.SIGNAL("activated(const QString&)"), self.insertCompletion)

    def insertCompletion(self, completion):
        tc = self.textCursor()
        extra = (completion.length() -
            self.completer.completionPrefix().length())
        tc.movePosition(QtGui.QTextCursor.Left)
        tc.movePosition(QtGui.QTextCursor.EndOfWord)
	##################Jaley Start
	#Basically gets the current cursor, and adds necessary stuff
        tc.insertText(completion.right(extra)+self.appendData)
	tc.setPosition(tc.position()-self.moveBack)
        self.setTextCursor(tc)
	self.postProcessing(completion)


	

    def postProcessing(self,completion):
	insertData=""
	moveBack=0
	tc=self.textCursor()
	if(self.lastWord()=='\"Convolution'):
	    insertData="\"\n\tconvolution_param{\n\t\tnum_output:10\n\t\tpad: 0\n\t\tkernel_size: 3\n\t\tstride: 1\n\t}"
	    moveBack=2
        if(self.lastWord()=='\"Pooling'):
	    insertData="\"\n\tpooling_param{\n\t\tpool:MAX\n\t\tkernel_size:3\n\t\tstride:2\n\t}"
        if(self.lastWord()=='\"InnerProduct'):
	    insertData="\"\n\tinner_product_param{\n\t\tnum_output:4096\n\t}"
	tc.insertText(insertData)
	#self.textCursor().setPosition(tc.position()+len(insertData)-moveBack)
	hList=self.getHierarchyList()
	#Intention is to autocomplete based on context
	bracketedData=self.getBracketedData()
	currLine=self.getCurrentLine()
	print 'HLIST',hList
	print 'COMPLETION',completion
	#If in layer context
	if('type:' not in currLine):
	    #Do Normal Operations
	    self.correctAppend(completion)	    
        """
	    self.setTextCursor(tc)
		    if(elem.message_type==None):
		        self.appendData=':'
		        self.moveBack=0
		    else:
		        self.appendData="{\n\t\n\t}"
			self.moveBack=2

        """
  

    def correctAppend(self,completion):
	hList=self.getHierarchyList()
	if(len(hList)==0):
	    return None
	if(len(hList)==1):
	    handle=caffe_pb2.LayerParameter()
	    bracketedData=self.getBracketedData()[1:-1]
	    lst=bracketedData.splitlines()
	    lst.remove(self.getCurrentLine())
	    bracketedData='\n'.join(lst)
	    text_format.Merge(bracketedData,handle)
	    print 'HList: Message Type : ',handle
	    if(completion in [elem.name for elem in handle.DESCRIPTOR.fields if elem.message_type is not None]):
						 
		print 'I am in'
		self.textCursor().deletePreviousChar()
		self.textCursor().insertText('{\n\t\n\t}\n')
	if(len(hList)>1):
	    print 'Size more than 1'
	

	#For Deciding between ':'or '{}'
    def lastWord(self):
	return self.toPlainText().__str__()[:self.textCursor().position()].split()[-1].split(':')[-1]

	##################Jaley Ends
    def textUnderCursor(self):
        tc = self.textCursor()
        tc.select(QtGui.QTextCursor.WordUnderCursor)
        return tc.selectedText()
 
    def focusInEvent(self, event):
        if self.completer:
            self.completer.setWidget(self);
        QtGui.QTextEdit.focusInEvent(self, event)

    def keyPressEvent(self, event):
        if self.completer and self.completer.popup().isVisible():
            if event.key() in (
            QtCore.Qt.Key_Enter,
            QtCore.Qt.Key_Return,
            QtCore.Qt.Key_Escape,
            QtCore.Qt.Key_Tab,
            QtCore.Qt.Key_Backtab):
                event.ignore()
                return

           ## has ctrl-E been pressed??
        isShortcut = (event.modifiers() == QtCore.Qt.ControlModifier and
                      event.key() == QtCore.Qt.Key_E)
        if (not self.completer or not isShortcut):
            QtGui.QTextEdit.keyPressEvent(self, event)

        ## ctrl or shift key on it's own??
        ctrlOrShift = event.modifiers() in (QtCore.Qt.ControlModifier ,
                QtCore.Qt.ShiftModifier)
        if ctrlOrShift and event.text().isEmpty():
            # ctrl or shift key on it's own
            return

        eow = QtCore.QString("~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-=") #end of word

        hasModifier = ((event.modifiers() != QtCore.Qt.NoModifier) and
                        not ctrlOrShift)

        completionPrefix = self.textUnderCursor()

        if (not isShortcut and (hasModifier or event.text().isEmpty() or
        completionPrefix.length() < 2 or
        eow.contains(event.text().right(1)))):
            self.completer.popup().hide()
            return

        if (completionPrefix != self.completer.completionPrefix()):
	    self.completer.model.setStringList(self.setList())
            self.completer.setCompletionPrefix(completionPrefix)
            popup = self.completer.popup()
            popup.setCurrentIndex(
                self.completer.completionModel().index(0,0))

        cr = self.cursorRect()
        cr.setWidth(self.completer.popup().sizeHintForColumn(0)
            + self.completer.popup().verticalScrollBar().sizeHint().width())
        self.completer.complete(cr) ## popup it up!
	

    #My Functions

    def setList(self):
	#Set Initial Strings
	totalData=str(self.toPlainText())
	partialData=str(self.toPlainText())[:self.textCursor().position()]
	print 'partialData',partialData
	#If incorrect Brackets
	if(totalData.count('{')!=totalData.count('}')):
		return []
	#If level=0
	if(partialData.count('{')==partialData.count('}')):
		self.appendData='{\n\n}'
		self.moveBack=2
		return ['layer']
	#If level!=0
	#EXTRA INITIALLIZATIONS
	bracketedData=self.getBracketedData()
	hList=self.getHierarchyList()
	currLine=self.getCurrentLine()
	#If level=1 
	if(len(hList)==1):
	    if(':' not in currLine):
		self.appendData=":"
		self.moveBack=0
		return self.getHListData()				
	    print currLine
	    if("type" in currLine and ":" in currLine):
		lst=[]
		for elem in ["Convolution","Pooling","InnerProduct"]:
		    lst.append(str(elem))
		    print 'LIST',lst
		self.appendData=""
		self.moveBack=0
		return lst
	
	if(len(hList)>1):
	    if(':' not in currLine):
	    #Hiararchial Data
		self.appendData=":"
		self.moveBack=0
		return self.getHListData()
	    pass


	return []
    def getCurrentLine(self):
	return self.toPlainText().__str__()[:self.textCursor().position()].splitlines()[-1]

  

    def getHierarchyList(self):
	lst=[]
	for a in self.toPlainText()[:self.textCursor().position()].__str__().replace(" ","").split():
		if '{' in a:lst.append(a[:-1].replace(" ",""))
		if '}' in a:lst.pop()
	print "%%%%%%%%%%%%%%%%", lst
	return lst
		
    def getBracketedData(self):
	    data=str(self.toPlainText())
	    pos=self.textCursor().position()
	    for i in range(pos-1,-1,-1):
		if data[i]=='{':startpos=i
	    for i in range(pos,len(data)):
		if data[i]=='}':endpos=i
	    return data[startpos:endpos+1]
	   

    def getHListData(self):
	#For Finding Additional Options
	hList=self.getHierarchyList()
	returnList=[]
	if(len(hList)==0):
	    return []
	if(len(hList)>=1):
	    handle=caffe_pb2.LayerParameter()
	    bracketedData=self.getBracketedData()[1:-1]
	    lst=bracketedData.splitlines()
	    if(self.getCurrentLine() in lst):lst.remove(self.getCurrentLine())
	    bracketedData='\n'.join(lst)
	    text_format.Merge(bracketedData,handle)
	    print 'HList: Message Type : ',handle
	    if(len(hList)==1):
	    	return [elem.name for elem in handle.DESCRIPTOR.fields]

	    descriptor=caffe_pb2.LayerParameter().DESCRIPTOR
	    if(len(hList)>1):
	    #Elements Except for layers
		for elem in hList[1:]:
		    print 'extra',elem
		    for e  in descriptor.fields:
			if(e.name==elem):descriptor=e.message_type

		for elem in descriptor.fields:
		    print elem.name,'$$$$$$'
		    
	    return [elem.name for elem in descriptor.fields ]

						 
		
	if(len(hList)>1):
	    print 'Size more than 1'
	
	pass



   

if __name__ == "__main__":

    app = QtGui.QApplication([])
    completer = DictionaryCompleter()
    te = CompletionTextEdit()
    te.setCompleter(completer)
    te.show()
    app.exec_()
