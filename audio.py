from audio_ui import Audio_widget
from PyQt4 import QtCore, QtGui
from tumblr import Api, TumblrError
import string

class Audio(Audio_widget):
    def __init__(self,parent=None):
        super(Audio,self).__init__(parent)        
        self.setupUi()
        self.api = parent.api
        #Conectar eventos 
        self.connect(self.bt_cancel, QtCore.SIGNAL('clicked()'), self.OnCancel)
        self.connect(self.bt_post, QtCore.SIGNAL('clicked()'), self.OnPost)
        self.connect(self.lb_useurl, QtCore.SIGNAL("linkActivated(QString)"), self.OnUseUrl)
        self.connect(self.bt_browse, QtCore.SIGNAL("clicked()"), self.OnBrowse)

    def OnCancel(self):
        self.close()
    
    def OnPost(self):
        self.data = unicode(self.le_file.text()).encode('utf-8')
    	if not self.data:
    		self.data =None
    	    
    	self.source = unicode(self.le_audiourl.text()).encode('utf-8')
    	if not self.source:
    		self.source = None    	
    	if self.te_description.toPlainText().isEmpty():
	    self.caption = ''
	else:
	    self.caption = unicode(self.te_description.toPlainText()).encode('utf-8')
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

        if self.data or self.source:
            #self.format = None
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_audio(self.data, self.source, self.caption)
            except:
                print "posteado en blog principal"
            self.close()
        else:
            QtGui.QMessageBox.warning(self,"Error","Audio is required",QtGui.QMessageBox.Ok)
    
    def OnBrowse(self):
        ImageDialog = QtGui.QFileDialog(self)
        filename = ImageDialog.getOpenFileName(self,'Select an Audio File',QtCore.QDir.homePath(),'Audio Files (*.MP3 *.AIFF *.mp3 *.aiff)')        
        self.le_file.setText(filename)
    
    def OnUseUrl(self,href):
        if href == 'willUseURL':
            self.lb_useurl.setText(' <strong>MP3s only.</strong> The file will be streamed from this URL, <strong>not</strong> hosted by Tumblr. <a href=willUseFile>Upload a file instead</a>')
            self.le_file.setVisible(False)
            self.le_audiourl.setVisible(True)
            self.bt_browse.setVisible(False)            
            self.le_file.setText('')
        else:
            self.lb_useurl.setText('<a href=willUseURL>Use an externally hosted audio file</a>')
            self.le_file.setVisible(True)
            self.le_audiourl.setVisible(False)
            self.bt_browse.setVisible(True)            
            self.le_audiourl.setText('')
    