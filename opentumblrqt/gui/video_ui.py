#!/usr/bin/python
from PyQt4 import QtCore, QtGui
from advancedoptions import AdvancedOptions_widget
from TumblrTextEdit import TumblrTextEdit

class Video_widget(QtGui.QDialog):
    def CreateLabel(self,text,parent):
        etiqueta  = QtGui.QLabel(text,parent)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        etiqueta.setSizePolicy(sizePolicy)
        return etiqueta
    
    def CreateButton(self,text,parent):
        button = QtGui.QPushButton(text,parent)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)                        
        button.setMaximumSize(QtCore.QSize(16777215, 28))
        button.setSizePolicy(sizePolicy)
        return button

    def setupUi(self,parent):
        self.setWindowTitle('Opentumblr-qt Video')
        self.resize(655,386)
        
        Hbox = QtGui.QHBoxLayout()
        self.Vbox = QtGui.QVBoxLayout()
        
        #labels
        self.lb_Add = self.CreateLabel('<h1>Add a Video Post</h1>',parent)
        self.lb_limitations = self.CreateLabel("<strong>This can be a URL from video sites like YouTube or Vimeo, or the raw Embed-tag <br />from any video/flash site.</strong> (ie. http://youtube.com/watch?v=oCmAD-z7-mA)",parent)
        self.lb_caption = self.CreateLabel("<big>Caption</big> optional",parent)
        
        self.te_videourl = QtGui.QTextEdit(parent)
        self.te_caption = TumblrTextEdit()
        
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
        
        self.Vbox.addWidget(self.lb_Add)
        self.Vbox.addWidget(self.lb_limitations)
        self.Vbox.addWidget(self.te_videourl)
        self.Vbox.addWidget(self.lb_caption)
        self.Vbox.addLayout(self.te_caption)
        self.Vbox.addLayout(self.BtBox)
        
        #Advanced options
        self.advanced = AdvancedOptions_widget()
        
        #Adding widgets hbox layout
        Hbox.addLayout(self.Vbox)
        Hbox.addLayout(self.advanced)
        
        self.setLayout(Hbox)
        