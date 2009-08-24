from quote_ui import Quote_widget
from PyQt4 import QtCore, QtGui
from tumblr import Api, TumblrError
import string

class Quote(Quote_widget):
    def __init__(self,parent=None):
        super(Quote,self).__init__(parent)        
        self.setupUi()
        self.api = parent.api
        #Conectar eventos
        self.connect(self.bt_cancel, QtCore.SIGNAL('clicked()'), self.OnCancel)
        self.connect(self.bt_post, QtCore.SIGNAL('clicked()'), self.OnPost)

    def OnCancel(self):
        self.close()

    def OnPost(self):
        self.quote = unicode(self.te_quote.toPlainText()).encode('utf-8')
        if self.te_source.document().isEmpty:
            self.te_source = ''
        else:            
            self.source = unicode(self.te_source.toPlainText()).encode('utf-8')
        if self.advanced.te_tags.document().isEmpty():
            self.tags = ''
        else:
            self.tags = unicode(self.advanced.te_tags.toPlainText()).encode('utf-8')
        self.tags = string.replace(self.tags,' ', ',')
        self.date = self.advanced.le_date.text()

        if self.advanced.cb_publish.currentText() == 'private':
            self.private = 1
        else:
            self.private = 0

        if self.quote:
            #self.format = None
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_quote(self.quote, self.source)
            except:
                print 'Puta madre hubo un error'
            self.close()
        else:
            QtGui.QMessageBox.warning(self,'Error','Quote is required',QtGui.QMessageBox.Ok)