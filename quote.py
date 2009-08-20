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
        self.connect(self.bt_cancel, QtCore.SIGNAL("clicked()"), self.OnCancel)
        self.connect(self.bt_post, QtCore.SIGNAL("clicked()"), self.OnPost)
        
    def OnCancel(self):
        self.close()
    
    def OnPost(self):
        self.quote = self.tc_quote.GetValue().encode('utf-8')
    	self.source = self.tc_source.GetValue().encode('utf-8')
        self.tags = self.tc_tag.GetValue().encode('utf-8')
        self.tags = string.replace(self.tags,' ', ',')
        self.date = self.tc_date.GetValue().encode('utf-8')

        if self.cb_publishing.GetValue() == 'private':
        	self.private = 1
        else:
        	self.private = 0
        
        if self.quote:
            #self.format = None
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_quote(self.quote, self.source)
            except:
                print "posteado en el blog primario"
            self.Close()
        else:
            Message('Quote is required')