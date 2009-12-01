#!/usr/bin/python
from PyQt4 import QtCore, QtGui
from advancedoptions import AdvancedOptions_widget
from TumblrTextEdit import TumblrTextEdit

class Quote_widget(QtGui.QDialog):
    
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
    
    def setupUi(self,parent):
        self.setWindowTitle('Opemtumblr-qt Quote')
        self.resize(655,386)
        
        #window Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/share/pixmaps/opentumblr-qt/dashboard/opentumblr_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        Hbox = QtGui.QHBoxLayout()
        self.Vbox = QtGui.QVBoxLayout()
        
        #Labels
        self.lb_Add = self.CreateLabel('<h1>Add a Quote</h1>',parent)
        self.lb_quote = self.CreateLabel('<big>Quote</big>',parent)
        self.lb_source = self.CreateLabel('<big>Source</big> (optional)',parent)
        
        #textedit
        self.te_quote = QtGui.QTextEdit(parent)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.te_quote.setFont(font)        
        self.te_source = TumblrTextEdit()
        self.te_source.pariente = parent  
        
        #button box
        self.BtBox = QtGui.QHBoxLayout()
        #Botones post y cancel
        self.bt_post = self.CreateButton('Create Post',parent)
        self.bt_post.setStyleSheet('color: green')
        self.bt_cancel = self.CreateButton('Cancel',parent)
        self.bt_cancel.setStyleSheet('color: red')
        #Agregamos al Btbox
        self.BtBox.addWidget(self.bt_post)
        self.BtBox.addStretch()
        self.BtBox.addWidget(self.bt_cancel)
        
        self.Vbox.addWidget(self.lb_Add)
        self.Vbox.addWidget(self.lb_quote)
        self.Vbox.addWidget(self.te_quote)
        self.Vbox.addWidget(self.lb_source)
        self.Vbox.addLayout(self.te_source)
        self.Vbox.addLayout(self.BtBox)
        
        #Advanced options
        self.advanced = AdvancedOptions_widget()
            
        #Adding widgets hbox layout
        Hbox.addLayout(self.Vbox)
        Hbox.addLayout(self.advanced)
        
        self.setLayout(Hbox)
        
        
        