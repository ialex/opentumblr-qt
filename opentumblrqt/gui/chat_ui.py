#!/usr/bin/python
from PyQt4 import QtCore, QtGui
from advancedoptions import AdvancedOptions_widget
from TumblrTextEdit import TumblrTextEdit

class Chat_widget(QtGui.QDialog):
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
        font.setPointSize(18)
        linedit.setFont(font)
        return linedit
    
    def setupUi(self,parent):
        self.setWindowTitle('Opemtumblr-qt Chat')
        self.resize(655,386)
        
        #window Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/share/pixmaps/opentumblr-qt/dashboard/opentumblr_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        
        Hbox = QtGui.QHBoxLayout()
        self.Vbox = QtGui.QVBoxLayout()
        
        #labels
        self.lb_Add = self.CreateLabel('<h1>Add a Chat Post</h1>',parent)
        self.lb_title = self.CreateLabel('<big>Title</big> (optional)',parent)
        self.lb_dialog = self.CreateLabel('<big>Dialogue</big>',parent)
        self.lb_intructions = self.CreateLabel("<strong>Example</strong><br />Tourist: Could you give us directions to Olive Garden?<br />New Yorker: No, but I could give you directions to an actual Italian restaurant.",parent)
        
        self.le_title = self.CreateLineEdit(parent)
        self.te_chat = QtGui.QTextEdit()
        
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
        self.Vbox.addWidget(self.lb_title)
        self.Vbox.addWidget(self.le_title)
        self.Vbox.addWidget(self.lb_dialog)
        self.Vbox.addWidget(self.lb_intructions)
        self.Vbox.addWidget(self.te_chat)
        self.Vbox.addLayout(self.BtBox)
        
         #Advanced options
        self.advanced = AdvancedOptions_widget()
            
        #Adding widgets hbox layout
        Hbox.addLayout(self.Vbox)
        Hbox.addLayout(self.advanced)
        
        self.setLayout(Hbox)
        