#!/usr/bin/python
from PyQt4 import QtCore, QtGui
import string

try:
    from opentumblrqt.gui.video_ui import Video_widget
    from opentumblrqt.tumblr import Api, TumblrError
except ImportError:
    from gui.video_ui import Video_widget
    from tumblr import Api, TumblrError


class Video(Video_widget):
    def __init__(self,parent=None):
        super(Video,self).__init__(parent)        
        self.setupUi(self)
        self.api = parent.api
        #Conectar eventos 
        self.connect(self.bt_cancel, QtCore.SIGNAL('clicked()'), self.OnCancel)
        self.connect(self.bt_post, QtCore.SIGNAL('clicked()'), self.OnPost)

    def OnCancel(self):
        self.hide()

    def OnPost(self):
        self.embed = unicode(self.te_videourl.toPlainText()).encode('utf-8')
        if self.te_caption.te_post.toPlainText().isEmpty():
            self.caption = ''
        else:
            self.caption = unicode(self.te_caption.te_post.toPlainText()).encode('utf-8')
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

        if self.embed:
            #self.format = None
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_video(self.embed, self.caption)
            except:
                print "posteado en el blog primario"
            self.close()
        else:
            QtGui.QMessageBox.warning(self,'Error','Embeded Video is required',QtGui.QMessageBox.Ok)
    
    def closeEvent(self,event):
        event.ignore()
        self.hide()