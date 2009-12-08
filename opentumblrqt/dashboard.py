#!/usr/bin/python
from PyQt4 import QtCore, QtGui

try:
        from opentumblrqt.gui.dashboard_ui import Dashboard_widget
        from opentumblrqt.text import Text
        from opentumblrqt.photo import Photo
        from opentumblrqt.quote import Quote
        from opentumblrqt.link import Link
        from opentumblrqt.chat import Chat
        from opentumblrqt.audio import Audio
        from opentumblrqt.video import Video
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
                self.connect(self.bt_text, QtCore.SIGNAL('clicked()'), self.OnText)
                self.connect(self.bt_photo, QtCore.SIGNAL('clicked()'), self.OnPhoto)
                self.connect(self.bt_quote, QtCore.SIGNAL('clicked()'), self.OnQuote)
                self.connect(self.bt_url, QtCore.SIGNAL('clicked()'), self.OnUrl)
                self.connect(self.bt_chat, QtCore.SIGNAL('clicked()'), self.OnChat)
                self.connect(self.bt_audio, QtCore.SIGNAL('clicked()'), self.OnAudio)
                self.connect(self.bt_video, QtCore.SIGNAL('clicked()'), self.OnVideo)
                self.connect(self.bt_logout, QtCore.SIGNAL('clicked()'), self.OnLogout)
                                                

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
                audio = Audio(self,self.api)
                audio.show()

        def OnVideo(self):
                video = Video(self)
                video.show()

        def OnLogout(self):
                self.hide()
        
        def closeEvent(self,event):
            event.ignore()
            self.hide()
            
            
        
                            
