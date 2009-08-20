from PyQt4 import QtCore, QtGui
from advancedoptions import AdvancedOptions_widget

class Photo_widget(QtGui.QDialog):
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
            linedit.setMaximumSize(QtCore.QSize(16777215, 28))
            font = QtGui.QFont()
            font.setPointSize(10)
            linedit.setFont(font)
            return linedit
    
    def CreateButton(self,text):
            button = QtGui.QPushButton(text)
            sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)                        
            button.setMaximumSize(QtCore.QSize(16777215, 28))
            button.setSizePolicy(sizePolicy)
            return button 
        
    def setupUi(self):
            self.setWindowTitle("Opemtumblr Photo")
            self.resize(655,386)
            
            #Top layout
            Hbox = QtGui.QHBoxLayout()
            self.Vbox = QtGui.QVBoxLayout()
                        
            #Labels
            self.lb_Add = self.CreateLabel("<h1>Upload a Photo</h1>")
            self.lb_photo = self.CreateLabel("<big>Photo</big>")
            self.lb_limitations = self.CreateLabel("Supports JPEG, GIF, PNG and BMP. <strong>Max photo size is 10 MB.</strong>")
            self.lb_caption = self.CreateLabel("<big>Caption</big> (optional)")
            self.lb_url = self.CreateLabel("Clicking this photo links to the URL:")
            self.lb_useurl = self.CreateLabel("<strong><a href=algo>Use url instead</a></strong>")
            
            #Line edit y button to browse files
            self.FileHBox = QtGui.QHBoxLayout()        
            #            
            self.le_file = self.CreateLineEdit()            
            self.bt_browse = self.CreateButton("Browse")
            self.bt_browse.setMaximumWidth(100)
            self.le_imageurl = self.CreateLineEdit()
            self.le_imageurl.setVisible(False)        
            self.FileHBox.addWidget(self.le_file)
            self.FileHBox.addWidget(self.bt_browse)
            #Caption
            self.te_caption = QtGui.QTextEdit()
            self.te_caption.setAcceptRichText(True)
            self.le_link = self.CreateLineEdit()
            
            #button box
            self.BtBox = QtGui.QHBoxLayout()    
            #Botones post y cancel
            self.bt_post = self.CreateButton("Create Post")
            self.bt_post.setStyleSheet("color: green")
            self.bt_cancel = self.CreateButton("Cancel")
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
            self.Vbox.addWidget(self.te_caption)
            self.Vbox.addWidget(self.lb_url)
            self.Vbox.addWidget(self.le_link)
            self.Vbox.addLayout(self.BtBox)
            
            #Advanced options
            self.advanced = AdvancedOptions_widget()
            
            #Adding widgets hbox layout
            Hbox.addLayout(self.Vbox)
            Hbox.addLayout(self.advanced)
            
            self.setLayout(Hbox)
        
        

        
        
        
        
        
        
        