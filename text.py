from text_ui import Text_widget
from PyQt4 import QtCore, QtGui
from tumblr import Api, TumblrError
import string

class Text(Text_widget):
    def __init__(self,parent=None):
        super(Text_widget,self).__init__(parent)        
        self.setupUi()
        self.api = parent.api
        #Conectar eventos
        QtCore.QObject.connect(self.bt_cancel, QtCore.SIGNAL('clicked()'), self.OnCancel)
        QtCore.QObject.connect(self.bt_post, QtCore.SIGNAL('clicked()'), self.OnPost)
        
    def OnCancel(self):
        self.close()
    
    def OnPost(self):
        if self.le_title.text().isEmpty():
            self.le_title = ''
        else:            
            self.title = unicode(self.le_title.text()).encode('utf-8')
        
        self.body = unicode(self.te_post.toPlainText())
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
        #print self.cb_publishing.GetValue()
        if self.advanced.cb_publish.currentText() == 'add to queue':
            self.date = 'on.2'

        if self.body:
            #self.format = None
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_regular(self.title, self.body)
            except:
                print 'posteado en blog principal'
                #print 'Posteado en ' % self.post
                #assert False,dir(self.post.values)
            self.close()
        else:
            QtGui.QMessageBox.warning(self,'Error','Text Post is required',QtGui.QMessageBox.Ok)
    
    