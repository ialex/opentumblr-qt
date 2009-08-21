from PyQt4 import QtCore, QtGui
from advancedoptions import AdvancedOptions_widget

class Link_widget(QtGui.QDialog):
    def CreateLabel(self,text):
        etiqueta  = QtGui.QLabel(text)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        etiqueta.setSizePolicy(sizePolicy)
        return etiqueta
    
    def CreateButton(self,text):
        button = QtGui.QPushButton(text)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)                        
        button.setMaximumSize(QtCore.QSize(16777215, 28))
        button.setSizePolicy(sizePolicy)
        return button
    
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
    
    def setupUi(self):
        self.setWindowTitle("Opemtumblr Link")
        self.resize(655,386)
        
        Hbox = QtGui.QHBoxLayout()
        self.Vbox = QtGui.QVBoxLayout()
        
        #labels
        self.lb_Add = self.CreateLabel("<h1>Add a Link</h1>")
        self.lb_title = self.CreateLabel("<big>Title</big> (optional)")
        self.lb_url = self.CreateLabel("<big>URL</big>")
        self.lb_description = self.CreateLabel("<big>Description</big> (optional)")
        
        #line edits
        self.le_title = self.CreateLineEdit()
        self.le_URL = self.CreateLineEdit()
        self.te_description = QtGui.QTextEdit()
        
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
        
        self.Vbox.addWidget(self.lb_Add)
        self.Vbox.addWidget(self.lb_title)
        self.Vbox.addWidget(self.le_title)
        self.Vbox.addWidget(self.lb_url)
        self.Vbox.addWidget(self.le_URL)
        self.Vbox.addWidget(self.lb_description)
        self.Vbox.addWidget(self.te_description)
        self.Vbox.addLayout(self.BtBox)
        
        #Advanced options
        self.advanced = AdvancedOptions_widget()
            
        #Adding widgets hbox layout
        Hbox.addLayout(self.Vbox)
        Hbox.addLayout(self.advanced)
        
        self.setLayout(Hbox)
        
        
        