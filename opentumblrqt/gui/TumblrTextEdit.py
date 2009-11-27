#!/usr/bin/python
from PyQt4 import QtCore, QtGui
'''
Created on 06/11/2009

@author: iAlex
'''

class TumblrTextEdit(QtGui.QVBoxLayout):
    '''
    Especial Text Editor for Tumblr it allow to create bold,italic,strike text as well
    insert links and image it includes a preview 
    '''
    pariente = None
    
    def __init__(self,parent=None):
        super(TumblrTextEdit, self).__init__(parent) 
        self.setupWidget(parent)
        self.connect(self.bt_bold, QtCore.SIGNAL('clicked()'), self.OnBold)
        self.connect(self.bt_strike, QtCore.SIGNAL('clicked()'), self.OnStrike)
        self.connect(self.bt_italic, QtCore.SIGNAL('clicked()'), self.OnItalic)
        self.connect(self.bt_anchor, QtCore.SIGNAL('clicked()'), self.OnAnchor)
        self.connect(self.bt_image, QtCore.SIGNAL('clicked()'), self.OnImage)
        self.connect(self.bt_more, QtCore.SIGNAL('clicked()'), self.OnMore)
        self.connect(self.bt_preview, QtCore.SIGNAL('clicked()'), self.OnPreview)
        self.connect(self.bt_close_preview, QtCore.SIGNAL('clicked()'), self.OnClosePreview)
        self.text_source = ""                    
    
    def CreateButton(self,icon,parent):
        button = QtGui.QPushButton(parent)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(24, 24))
        button.setFixedSize(25,25)
        return button
    
    def CreateIcon(self,archivo):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/share/pixmaps/opentumblr-qt/dashboard/" + archivo), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon
            
    def setupWidget(self,parent):
                
        self.MenuBar = QtGui.QHBoxLayout(parent)
        
        self.bt_bold = self.CreateButton(self.CreateIcon("bold.png"),parent)    
        self.bt_strike = self.CreateButton(self.CreateIcon("strike.png"),parent)
        self.bt_italic = self.CreateButton(self.CreateIcon("italic.png"),parent)
        self.bt_anchor = self.CreateButton(self.CreateIcon("link_editor.png"),parent)
        self.bt_image = self.CreateButton(self.CreateIcon("image.png"),parent)
        self.bt_more = self.CreateButton(self.CreateIcon("more.png"),parent)
        self.bt_preview = self.CreateButton(self.CreateIcon("preview.png"),parent)
        self.bt_close_preview = self.CreateButton(self.CreateIcon("close.png"),parent)
        self.bt_close_preview.setVisible(False)
        
        self.te_post = QtGui.QTextEdit(parent)
        self.te_post.setAcceptRichText(True)
         
        self.MenuBar.addWidget(self.bt_bold)        
        self.MenuBar.addWidget(self.bt_italic)
        self.MenuBar.addWidget(self.bt_strike)
        self.MenuBar.addWidget(self.bt_anchor)
        self.MenuBar.addWidget(self.bt_image)        
        self.MenuBar.addWidget(self.bt_more)
        self.MenuBar.addWidget(self.bt_preview)
        self.MenuBar.addWidget(self.bt_close_preview)
        
        self.addLayout(self.MenuBar)
        self.addWidget(self.te_post)
        
    def OnBold(self):
        self.cursor = self.te_post.textCursor()       
        if self.cursor.hasSelection():  
                                                                
            self.cursor.beginEditBlock()                        
            self.cursor.insertText("<b>" + self.cursor.selectedText() + "</b>")            
            self.cursor.endEditBlock()                    
                        
    def OnStrike(self):
        self.cursor = self.te_post.textCursor()       
        if self.cursor.hasSelection():  
                                                                
            self.cursor.beginEditBlock()                        
            self.cursor.insertText("<strike>" + self.cursor.selectedText() + "</strike>")            
            self.cursor.endEditBlock()  
    
    def OnItalic(self):
        self.cursor = self.te_post.textCursor()       
        if self.cursor.hasSelection():  
                                                                
            self.cursor.beginEditBlock()                        
            self.cursor.insertText("<i>" + self.cursor.selectedText() + "</i>")            
            self.cursor.endEditBlock()  
    
    def OnAnchor(self):
        self.cursor = self.te_post.textCursor()
        if self.cursor.hasSelection():            
            url,ok = QtGui.QInputDialog.getText(self.pariente,"Insert an Url","URL:")
            if url != "" and ok == True:
                self.cursor.insertText('<a href="' + url + '">' + self.cursor.selectedText() + '</a>')
    
    def OnImage(self):        
        self.cursor = self.te_post.textCursor()        
        url,ok = QtGui.QInputDialog.getText(self.pariente,"Insert Image Url","Image URL:",QtGui.QLineEdit.Normal,"")
        if url != "":
            self.cursor.insertText('<img src="' + url + '" />')
    
    def OnPreview(self):
        self.text_source = self.te_post.toPlainText()
        self.text_html = self.te_post.toPlainText().replace('\n','<br>')                
        self.te_post.setReadOnly(True)
        self.te_post.clear()
        self.te_post.insertHtml(self.text_html)
        
        self.bt_preview.setVisible(False)
        self.bt_close_preview.setVisible(True)
    
    def OnClosePreview(self):
        self.te_post.setReadOnly(False)
        self.te_post.clear()
        self.te_post.insertPlainText(self.text_source)
                
        self.bt_preview.setVisible(True)
        self.bt_close_preview.setVisible(False)
        
    def OnMore(self):
        self.cursor = self.te_post.textCursor()
        if self.te_post.toPlainText().__contains__('<!-- more -->'):
            pass
        else:
            self.cursor.insertText('<!-- more -->')
    
    
    
    


    
        