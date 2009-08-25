from photo_ui import Photo_widget
from PyQt4 import QtCore, QtGui
from tumblr import Api, TumblrError
import string

class Photo(Photo_widget):
    def __init__(self,parent=None):
        super(Photo_widget,self).__init__(parent)        
        self.setupUi()
        self.api = parent.api
        #Conectar eventos
        self.connect(self.bt_cancel, QtCore.SIGNAL("clicked()"), self.OnCancel)
        self.connect(self.bt_post, QtCore.SIGNAL("clicked()"), self.OnPost)
        self.connect(self.bt_browse, QtCore.SIGNAL("clicked()"), self.OnBrowse)
        self.connect(self.lb_useurl, QtCore.SIGNAL("linkActivated(QString)"), self.OnUseUrl)
        
    def OnCancel(self):
        self.close()
    
    def OnPost(self):
        #Source == An URL - Data == A Path to the file on your Computer
        self.source = unicode(self.le_imageurl.text()).encode('utf-8')        
        if not self.source:
            self.source = None    

        self.data = unicode(self.le_file.text()).encode('utf-8')        
        if not self.data:
            self.data = None
        
        if self.te_caption.toPlainText().isEmpty():
            self.caption = ''
        else:
            self.caption = unicode(self.te_caption.toPlainText()).encode('utf-8')
        if self.le_link.text().isEmpty():
            self.click = ''
        else:
            self.click  = unicode(self.le_link.text()).encode('utf-8')
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
        
        if self.source or self.data:
            #self.format = None
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_photo(self.source, self.data, self.caption, self.click)
            except:            
                print "posteado en blog principal"
            self.close()
        else:
            QtGui.QMessageBox.warning(self,"Error","Photo is required",QtGui.QMessageBox.Ok)
        
    def OnBrowse(self):
        ImageDialog = QtGui.QFileDialog(self)
        filename = ImageDialog.getOpenFileName(self,"Select an Image",QtCore.QDir.homePath(),"Image Files (*.png *.jpg *.jpeg *.gif *.bmp)")        
        self.le_file.setText(filename)
    
    def OnUseUrl(self,text):
        self.le_file.setText("")
        self.le_file.setVisible(False)
        self.bt_browse.setVisible(False)
        self.le_imageurl.setVisible(True)
        self.lb_photo.setText("<big>Photo URL</big>")
        self.lb_useurl.setVisible(False)
        self.le_imageurl.setFocus()
        
        
        