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
        pass