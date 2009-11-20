#!/usr/bin/python
from PyQt4 import QtCore, QtGui
from advancedoptions import AdvancedOptions_widget
from TumblrTextEdit import TumblrTextEdit

class Audio_widget(QtGui.QDialog):
    def CreateLabel(self,text,parent):
        etiqueta  = QtGui.QLabel(text,parent)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
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
    
    def CreateLineEdit(self,parent):                
        linedit = QtGui.QLineEdit(parent)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(linedit.sizePolicy().hasHeightForWidth())
        linedit.setSizePolicy(sizePolicy)
        linedit.setMaximumSize(QtCore.QSize(16777215, 58))
        font = QtGui.QFont()
        font.setPointSize(10)
        linedit.setFont(font)
        return linedit
    
    def setupUi(self,parent):
        self.setWindowTitle('Opemtumblr-qt Audio')
        self.resize(655,386)
        
        #window Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/share/pixmaps/opentumblr-qt/dashboard/opentumblr_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        Hbox = QtGui.QHBoxLayout()
        self.Vbox = QtGui.QVBoxLayout()
        
        #labels
        self.lb_Add = self.CreateLabel('<h1>Add an Audio Post</h1>',parent)
        self.lb_file = self.CreateLabel('<big>Audio File</big>',parent)        
        self.lb_description = self.CreateLabel('<big>Description</big> (optional)',parent)
        self.lb_useurl = self.CreateLabel('<a href=willUseURL>Use an externally hosted audio file</a>',parent)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lb_useurl.setFont(font)
        
        #input objects
        #Line edit y button to browse files
        self.FileHBox = QtGui.QHBoxLayout()        
        #            
        self.le_file = self.CreateLineEdit(parent)            
        self.bt_browse = self.CreateButton("Browse",parent)
        self.bt_browse.setMaximumWidth(100)
        self.le_audiourl = self.CreateLineEdit(parent)
        self.le_audiourl.setVisible(False)
        
        self.FileHBox.addWidget(self.le_file)
        self.FileHBox.addWidget(self.le_audiourl)
        self.FileHBox.addWidget(self.bt_browse)

        #Description
        self.te_description = TumblrTextEdit()
        
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
        self.Vbox.addWidget(self.lb_file)
        self.Vbox.addLayout(self.FileHBox)
        self.Vbox.addWidget(self.lb_useurl)
        self.Vbox.addWidget(self.lb_description)
        self.Vbox.addLayout(self.te_description)
        self.Vbox.addLayout(self.BtBox)
                            
        #Advanced options
        self.advanced = AdvancedOptions_widget()
        
        #Adding widgets hbox layout
        Hbox.addLayout(self.Vbox)
        Hbox.addLayout(self.advanced)
        
        self.setLayout(Hbox)
        
        
        
        
        