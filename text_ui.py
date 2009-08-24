from PyQt4 import QtGui, QtCore
from advancedoptions import AdvancedOptions_widget

class Text_widget(QtGui.QDialog):
        def CreateLabel(self,text):
                etiqueta  = QtGui.QLabel(text)
                sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                etiqueta.setSizePolicy(sizePolicy)
                return etiqueta
    
        def CreateLineEdit(self):                
                linedit = QtGui.QLineEdit()
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
            
        def CreateButton(self,text):
                button = QtGui.QPushButton(text)
                sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)                        
                button.setMaximumSize(QtCore.QSize(16777215, 58))
                button.setSizePolicy(sizePolicy)
                return button   
 
        def setupUi(self):
                self.setWindowTitle('Opentumblr  Text')
                self.resize(655,576)
                
                #Top layout
                Hbox = QtGui.QHBoxLayout()
                self.Vbox = QtGui.QVBoxLayout()
                #Futuro Horizontal box para botones del editor 
                #HboxButtons = QtGui.QHBoxLayout()    
                
                #Line_edit and Buttons
                self.lb_Add = self.CreateLabel('<h1>Add a Text Post</h1>')
                self.lb_title = self.CreateLabel('<strong><big>Text</big></strong>(optional)')
                self.lb_post = self.CreateLabel('<strong><h2>Post</h2></strong>')        
                self.le_title = self.CreateLineEdit()                
                self.te_post = QtGui.QTextEdit()
                self.te_post.setAcceptRichText(True)
                
                #button box
                self.BtBox = QtGui.QHBoxLayout()    
                #Botones post y cancel
                self.bt_post = self.CreateButton('Create Post')
                self.bt_post.setStyleSheet('color: green')
                self.bt_cancel = self.CreateButton('Cancel')
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
                self.Vbox.addWidget(self.te_post)
                self.Vbox.addLayout(self.BtBox)

                #Advanced Options
                self.advanced = AdvancedOptions_widget()                
                #Vbox lo agregamos a Hbox
                Hbox.addLayout(self.Vbox)
                Hbox.addLayout(self.advanced)
                
                self.setLayout(Hbox)
                
        
    
        