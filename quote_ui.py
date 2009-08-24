from PyQt4 import QtCore, QtGui
from advancedoptions import AdvancedOptions_widget

class Quote_widget(QtGui.QDialog):
    
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
    
    def setupUi(self):
        self.setWindowTitle("Opemtumblr Quote")
        self.resize(655,386)
        
        Hbox = QtGui.QHBoxLayout()
        self.Vbox = QtGui.QVBoxLayout()
        
        #Labels
        self.lb_Add = self.CreateLabel("<h1>Add a Quote</h1>")
        self.lb_quote = self.CreateLabel("<big>Quote</big>")
        self.lb_source = self.CreateLabel("<big>Source</big> (optional)")
        
        #textedit
        self.te_quote = QtGui.QTextEdit()
        font = QtGui.QFont()
        font.setPointSize(18)
        self.te_quote.setFont(font)
        self.te_source = QtGui.QTextEdit()
        
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
        self.Vbox.addWidget(self.lb_quote)
        self.Vbox.addWidget(self.te_quote)
        self.Vbox.addWidget(self.lb_source)
        self.Vbox.addWidget(self.te_source)
        self.Vbox.addLayout(self.BtBox)
        
        #Advanced options
        self.advanced = AdvancedOptions_widget()
            
        #Adding widgets hbox layout
        Hbox.addLayout(self.Vbox)
        Hbox.addLayout(self.advanced)
        
        self.setLayout(Hbox)
        
        
        