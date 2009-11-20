#!/usr/bin/python
from PyQt4 import QtCore, QtGui
from advancedoptions import AdvancedOptions_widget
from TumblrTextEdit import TumblrTextEdit

class Photo_widget(QtGui.QDialog):
    def CreateLabel(self,text,parent):
            etiqueta  = QtGui.QLabel(text,parent)
            sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            etiqueta.setSizePolicy(sizePolicy)
            return etiqueta
    
    def CreateLineEdit(self,parent):                
            linedit = QtGui.QLineEdit(parent)
            sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(linedit.sizePolicy().hasHeightForWidth())
            linedit.setSizePolicy(sizePolicy)
            linedit.setMaximumSize(QtCore.QSize(16777215, 28))
            font = QtGui.QFont()
            font.setPointSize(10)
            linedit.setFont(font)
            return linedit
    
    def CreateButton(self,text,parent):
            button = QtGui.QPushButton(text,parent)
            sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)                        
            button.setMaximumSize(QtCore.QSize(16777215, 28))
            button.setSizePolicy(sizePolicy)
            return button 
        
    def setupUi(self,parent):
            self.setWindowTitle("Opemtumblr-qt Photo")
            self.resize(655,386)
            
            #window Icon
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("/usr/share/pixmaps/opentumblr-qt/dashboard/opentumblr_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.setWindowIcon(icon)
            
            #Top layout
            Hbox = QtGui.QHBoxLayout()
            self.Vbox = QtGui.QVBoxLayout()
                        
            #Labels
            self.lb_Add = self.CreateLabel("<h1>Upload a Photo</h1>",parent)
            self.lb_photo = self.CreateLabel("<big>Photo</big>",parent)
            self.lb_limitations = self.CreateLabel("Supports JPEG, GIF, PNG and BMP. <strong>Max photo size is 10 MB.</strong>",parent)            
            self.lb_caption = self.CreateLabel("<big>Caption</big> (optional)",parent)
            self.lb_url = self.CreateLabel("Clicking this photo links to the URL:",parent)
            self.lb_useurl = self.CreateLabel("<a href=algo>Use url instead</a>",parent)
            font = QtGui.QFont()
            font.setPointSize(8)
            self.lb_useurl.setFont(font)
            
            #Line edit y button to browse files
            self.FileHBox = QtGui.QHBoxLayout()        
            #            
            self.le_file = self.CreateLineEdit(parent)            
            self.bt_browse = self.CreateButton("Browse",parent)
            self.bt_browse.setMaximumWidth(100)
            self.le_imageurl = self.CreateLineEdit(parent)
            self.le_imageurl.setVisible(False)        
            self.FileHBox.addWidget(self.le_file)
            self.FileHBox.addWidget(self.le_imageurl)
            self.FileHBox.addWidget(self.bt_browse)
            #Caption
            self.te_caption = TumblrTextEdit()            
            self.le_link = self.CreateLineEdit(parent)
            
            #button box
            self.BtBox = QtGui.QHBoxLayout()    
            #Botones post y cancel
            self.bt_post = self.CreateButton("Create Post",parent)
            self.bt_post.setStyleSheet("color: green")
            self.bt_cancel = self.CreateButton("Cancel",parent)
            self.bt_cancel.setStyleSheet("color: red")
            #Agregamos al Btbox
            self.BtBox.addWidget(self.bt_post)
            self.BtBox.addStretch()
            self.BtBox.addWidget(self.bt_cancel)
            
            #Adding widgets to vbox layout
            self.Vbox.addWidget(self.lb_Add)
            self.Vbox.addWidget(self.lb_photo)
            self.Vbox.addLayout(self.FileHBox)            
            self.Vbox.addWidget(self.le_imageurl)
            self.Vbox.addWidget(self.lb_limitations)
            self.Vbox.addWidget(self.lb_useurl)
            self.Vbox.addWidget(self.lb_caption)
            self.Vbox.addLayout(self.te_caption)
            self.Vbox.addWidget(self.lb_url)
            self.Vbox.addWidget(self.le_link)
            self.Vbox.addLayout(self.BtBox)
            
            #Advanced options
            self.advanced = AdvancedOptions_widget()
            
            #Adding widgets hbox layout
            Hbox.addLayout(self.Vbox)
            Hbox.addLayout(self.advanced)
            
            self.setLayout(Hbox)
        
        

        
        
        
        
        
        
        