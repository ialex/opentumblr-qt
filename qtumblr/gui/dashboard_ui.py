
from PyQt4 import QtCore, QtGui

class Dashboard_widget(QtGui.QDialog):
    def CreateIcon(self,archivo):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/share/pixmaps/qtumblr/dashboard/" + archivo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon
    
    def CreateButton(self,icon):
        button = QtGui.QPushButton()
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(64, 64))
        return button
    
    def setupUi(self):
        self.setWindowTitle("Opentumblr  Dashboard")
        self.resize(341,418)
        
        #Grid
        grid = QtGui.QGridLayout()
        
        
        #Creamos iconos
        self.bt_text = self.CreateButton(self.CreateIcon("text.png"))
        self.bt_photo = self.CreateButton(self.CreateIcon("photo.png"))
        self.bt_audio = self.CreateButton(self.CreateIcon("audio.png"))
        self.bt_url = self.CreateButton(self.CreateIcon("link.png"))
        self.bt_quote = self.CreateButton(self.CreateIcon("quote.png"))
        self.bt_chat = self.CreateButton(self.CreateIcon("chat.png"))
        self.bt_video = self.CreateButton(self.CreateIcon("video.png"))
        
        #Icono LogOUt
        self.bt_logout = QtGui.QPushButton("Log Out")
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)                        
        self.bt_logout.setMaximumSize(QtCore.QSize(16777215, 58))
        self.bt_logout.setSizePolicy(sizePolicy)
        
        #Los agregamos al Grid
        grid.addWidget(self.bt_text, 1, 1)
        grid.addWidget(self.bt_photo, 1, 2)
        grid.addWidget(self.bt_quote, 1, 3)
        grid.addWidget(self.bt_url, 2, 1)
        grid.addWidget(self.bt_chat, 2, 2)
        grid.addWidget(self.bt_audio, 2, 3)
        grid.addWidget(self.bt_video, 3, 2)
        grid.addWidget(self.bt_logout,4,1,1,3)
        
        self.setLayout(grid)
        
