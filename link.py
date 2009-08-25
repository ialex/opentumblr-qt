from link_ui import Link_widget
from PyQt4 import QtCore, QtGui
from tumblr import Api, TumblrError
import string

class Link(Link_widget):
    def __init__(self,parent=None):
        super(Link,self).__init__(parent)        
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
        if  self.te_description.toPlainText().isEmpty():
            self.te_description = ''
        else:
            self.description = unicode(self.te_description.toPlainText()).encode('utf-8')
        if self.advanced.te_tags.toPlainText().isEmpty():
            self.tags = ''
        else:
            self.tags = unicode(self.advanced.te_tags.toPlainText()).encode('utf-8')
        self.tags = string.replace(self.tags,' ', ',')
        self.date = self.advanced.le_date.text()
        self.urllink = self.le_URL.text()

        if self.advanced.cb_publish.currentText() == 'private':
            self.private = 1
        else:
            self.private = 0

        if self.urllink:
            #self.format = None
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_link(self.title,self.urllink,self.description)
            except:
                print 'posteado en blog principal'
            self.close()
        else:
            QtGui.QMessageBox.warning(self,'Error','URL is required',QtGui.QMessageBox.Ok)
