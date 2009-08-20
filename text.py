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
        QtCore.QObject.connect(self.bt_cancel, QtCore.SIGNAL("clicked()"), self.OnCancel)
        QtCore.QObject.connect(self.bt_post, QtCore.SIGNAL("clicked()"), self.OnPost)
        
    def OnCancel(self):
        self.close()
    
    def OnPost(self):
        self.title = self.le_title.text()
        self.body = unicode(self.te_post.toPlainText())
        self.tags = unicode(self.advanced.te_tags.toPlainText())
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
                print "Posteado en blog primario"
                #print "Posteado en " % self.post
                #assert False,dir(self.post.values)
            self.close()
        else:
            QtGui.QMessageBox.warning(self,"Error","Text Post is required",QtGui.QMessageBox.Ok)
    
    