from PyQt4 import QtCore, QtGui

try:
    from qtumblr.gui.dashboard_ui import Dashboard_widget
    from qtumblr import *
except ImportError:
    from gui.dashboard_ui import Dashboard_widget
    from text import Text
    from photo import Photo
    from quote import Quote
    from link import Link
    from chat import Chat
    from audio import Audio
    from video import Video

class Dashboard(Dashboard_widget):
    def __init__(self,parent=None):
        super(Dashboard, self).__init__(parent)        
        self.setupUi()  
        self.api = parent.api
        
        #conectar eventos        
        QtCore.QObject.connect(self.bt_text, QtCore.SIGNAL('clicked()'), self.OnText)
        QtCore.QObject.connect(self.bt_photo, QtCore.SIGNAL('clicked()'), self.OnPhoto)
        QtCore.QObject.connect(self.bt_quote, QtCore.SIGNAL('clicked()'), self.OnQuote)
        QtCore.QObject.connect(self.bt_url, QtCore.SIGNAL('clicked()'), self.OnUrl)
        QtCore.QObject.connect(self.bt_chat, QtCore.SIGNAL('clicked()'), self.OnChat)
        QtCore.QObject.connect(self.bt_audio, QtCore.SIGNAL('clicked()'), self.OnAudio)
        QtCore.QObject.connect(self.bt_video, QtCore.SIGNAL('clicked()'), self.OnVideo)
        QtCore.QObject.connect(self.bt_logout, QtCore.SIGNAL('clicked()'), self.OnLogout)
        
    def OnText(self):
        text = Text(self)
        text.show()
    
    def OnPhoto(self):
        photo = Photo(self)
        photo.show()
    
    def OnQuote(self):
        quote = Quote(self)
        quote.show()
    
    def OnUrl(self):
        link = Link(self)
        link.show()
    
    def OnChat(self):
        chat = Chat(self)
        chat.show()
    
    def OnAudio(self):
        audio = Audio(self)
        audio.show()
    
    def OnVideo(self):
        video = Video(self)
        video.show()
    
    def OnLogout(self):
        self.close()       