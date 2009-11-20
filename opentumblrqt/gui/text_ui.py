#!/usr/bin/python
from PyQt4 import QtGui, QtCore
from advancedoptions import AdvancedOptions_widget
from TumblrTextEdit import TumblrTextEdit

class Text_widget(QtGui.QDialog):
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
      linedit.setMaximumSize(QtCore.QSize(16777215, 58))
      font = QtGui.QFont()
      font.setPointSize(18)
      linedit.setFont(font)
      return linedit
            
   def CreateButton(self,text,parent):
      button = QtGui.QPushButton(text,parent)
      sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)                        
      button.setMaximumSize(QtCore.QSize(16777215, 58))
      button.setSizePolicy(sizePolicy)
      return button   
 
   def setupUi(self,parent):
      self.setWindowTitle('Opentumblr-qt Text')
      self.resize(655,576)
      
      #window Icon
      icon = QtGui.QIcon()
      icon.addPixmap(QtGui.QPixmap("/usr/share/pixmaps/opentumblr-qt/dashboard/opentumblr_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
      self.setWindowIcon(icon)
      
      #Top layout
      Hbox = QtGui.QHBoxLayout()
      self.Vbox = QtGui.QVBoxLayout()
      
      #Line_edit and Buttons
      self.lb_Add = self.CreateLabel('<h1>Add a Text Post</h1>',parent)
      self.lb_title = self.CreateLabel('<strong><big>Text</big></strong>(optional)',parent)
      self.lb_post = self.CreateLabel('<strong><h2>Post</h2></strong>',parent)        
      self.le_title = self.CreateLineEdit(parent)                
      self.te_post = TumblrTextEdit()
      self.te_post.pariente = parent      
      
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
      
      #widgets Vbox
      self.Vbox.addWidget(self.lb_Add)
      self.Vbox.addWidget(self.lb_title)
      self.Vbox.addWidget(self.le_title)
      self.Vbox.addWidget(self.lb_post)
      self.Vbox.addLayout(self.te_post)
      self.Vbox.addLayout(self.BtBox)
         
      #Advanced Options
      self.advanced = AdvancedOptions_widget()                
      #Vbox lo agregamos a Hbox
      Hbox.addLayout(self.Vbox)
      Hbox.addLayout(self.advanced)
      
      
      self.setLayout(Hbox)
                
        
    
        