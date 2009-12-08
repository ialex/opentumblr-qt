from PyQt4 import QtCore,QtGui

try:
    from opentumblrqt.dashboard import Dashboard
    from opentumblrqt.text import Text
    from opentumblrqt.photo import Photo
    from opentumblrqt.quote import Quote
    from opentumblrqt.link import Link
    from opentumblrqt.chat import Chat
    from opentumblrqt.audio import Audio
    from opentumblrqt.video import Video
except ImportError:
    from ..opentumblrqt.dashboard import Dashboard
    from text import Text
    from photo import Photo
    from quote import Quote
    from link import Link
    from chat import Chat
    from audio import Audio
    from video import Video
    
class TumblrTray(QtGui.QSystemTrayIcon):
    
    def __init__(self,parent=None):
        super(TumblrTray, self).__init__(parent)
        self.setupUi(parent)        
        #Dashboard instance
        self.dashboard = Dashboard(parent)
        self.p = parent
        #Connecting events 
        self.connect(self.tray,QtCore.SIGNAL('activated(QSystemTrayIcon::ActivationReason)'),self.OnClick) 
        self.connect(self.Text,QtCore.SIGNAL('triggered()'),self.OnText)    
        self.connect(self.Photo, QtCore.SIGNAL('triggered()'), self.OnPhoto)
        self.connect(self.Quote, QtCore.SIGNAL('triggered()'), self.OnQuote)
        self.connect(self.Url, QtCore.SIGNAL('triggered()'), self.OnUrl)
        self.connect(self.Chat, QtCore.SIGNAL('triggered()'), self.OnChat)
        self.connect(self.Audio, QtCore.SIGNAL('triggered()'), self.OnAudio)
        self.connect(self.Video, QtCore.SIGNAL('triggered()'), self.OnVideo)
        self.connect(self.Exit, QtCore.SIGNAL('triggered()'), self.OnLogout)                            
        
    def setupUi(self,parent):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/share/pixmaps/opentumblr-qt/dashboard/opentumblr_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tray = QtGui.QSystemTrayIcon(parent)
        self.tray.setIcon(icon)
        self.tray.show()
        
        #Creating the context menu  
        self.Traymenu = QtGui.QMenu(parent)
        self.Text = QtGui.QAction("&Text",parent)
        self.Photo = QtGui.QAction("&Photo",parent)
        self.Quote = QtGui.QAction("&Quote",parent)
        self.Url = QtGui.QAction("&Url",parent)
        self.Chat = QtGui.QAction("&Chat",parent)
        self.Audio = QtGui.QAction("&Audio",parent)
        self.Video = QtGui.QAction("&Video",parent)        
        self.Exit = QtGui.QAction("&Exit",parent)
        
        self.Traymenu.addAction(self.Text)
        self.Traymenu.addAction(self.Photo)
        self.Traymenu.addAction(self.Quote)
        self.Traymenu.addAction(self.Url)
        self.Traymenu.addAction(self.Chat)
        self.Traymenu.addAction(self.Audio)
        self.Traymenu.addAction(self.Video)
        self.Traymenu.addAction(self.Exit)
        
        self.setContextMenu(self.Traymenu)
        
    def OnClick(self,reason):
        #Dashboard
        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            if self.dashboard.isVisible():
                self.dashboard.hide()
            else:
                self.dashboard.show()
        #Direct posting options (showing context menu)
        if reason == QtGui.QSystemTrayIcon.Context:
            self.contextMenu().popup(QtGui.QCursor.pos())
    
    def OnText(self):
        text = Text(self.parent())
        text.show()

    def OnPhoto(self):
        photo = Photo(self.parent())
        photo.show()

    def OnQuote(self):
        quote = Quote(self.parent())
        quote.show()

    def OnUrl(self):
        link = Link(self.parent())
        link.show()

    def OnChat(self):
        chat = Chat(self.parent())
        chat.show()

    def OnAudio(self):
        audio = Audio(None,self.parent().api)
        audio.show()

    def OnVideo(self):
        video = Video(self.parent())
        video.show()

    def OnLogout(self):
        self.parent().close()
        
    
    