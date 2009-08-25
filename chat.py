from chat_ui import Chat_widget
from PyQt4 import QtCore, QtGui
from tumblr import Api, TumblrError
import string

class Chat(Chat_widget):
    def __init__(self,parent=None):
        super(Chat,self).__init__(parent)        
        self.setupUi()
        self.api = parent.api
        #Conectar eventos 
        self.connect(self.bt_cancel, QtCore.SIGNAL('clicked()'), self.OnCancel)
        self.connect(self.bt_post, QtCore.SIGNAL('clicked()'), self.OnPost)

    def OnCancel(self):
        self.close()

    def OnPost(self):
        if self.le_title.text().isEmpty():
            self.title = ''
        else:
            self.title = unicode(self.le_title.text()).encode('utf-8')
        self.conversation = unicode(self.te_chat.toPlainText()).encode('utf-8')
        if self.advanced.te_tags.toPlainText().isEmpty():
            self.tags = ''
        else:
            self.tags = unicode(self.advanced.te_tags.toPlainText()).encode('utf-8')
        self.tags = string.replace(self.tags,' ', ',')
        self.date = self.advanced.le_date.text()

        if self.advanced.cb_publish.currentText() == 'private':
            self.private = 1
        else:
            self.private = 0 

        if self.conversation:
            #self.format = None
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_conversation(self.title, self.conversation)
            except:
                print 'posteado en blog principal'
            self.close()
        else:
            QtGui.QMessageBox.warning(self,'Error','Conversation is required',QtGui.QMessageBox.Ok)