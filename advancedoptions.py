from PyQt4 import QtCore,QtGui

class AdvancedOptions_widget(QtGui.QVBoxLayout):
    def __init__(self,parent=None):
        super(AdvancedOptions_widget, self).__init__(parent)        
        self.setupUi()
        #Conectar eventos
        self.connect(self.cb_publish, QtCore.SIGNAL("currentIndexChanged(int)"), self.OnIndexChanged)
        
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
        font.setPointSize(8)
        linedit.setFont(font)
        return linedit
            
    def setupUi(self):        
        #widgets =D
        self.lb_Advanced = self.CreateLabel("<strong>Advanced Options</strong>")
        #self.gb_Advanced = QtGui.QGroupBox("Advanced Options")
        
        self.lb_publish = self.CreateLabel("Publishing options:")
        self.lb_date = self.CreateLabel("Date this post:")
        self.lb_tag = self.CreateLabel("Tag this post:")
        
        self.le_date = self.CreateLineEdit()
        self.le_date.setText("now")
        
        self.cb_publish = QtGui.QComboBox()
        self.options = QtCore.QStringList()
        self.options.append(QtCore.QString("publish now")) 
        self.options.append(QtCore.QString("publish on"))
        self.options.append(QtCore.QString("private"))
        self.cb_publish.addItems(self.options)
        
        self.te_tags = QtGui.QTextEdit()
        self.te_tags.setMaximumSize(QtCore.QSize(150,100))
        
        #Agregamos widgets al vbox
        self.addWidget(self.lb_Advanced)
        self.addWidget(self.lb_publish)
        self.addWidget(self.cb_publish)
        self.addWidget(self.lb_date)
        self.addWidget(self.le_date)
        self.addWidget(self.lb_tag)
        self.addWidget(self.te_tags)
        
        
        #self.setLayout(Vbox) 
    
    def OnIndexChanged(self,index):
        if (index == 0):
            self.le_date.setText("now")
            self.le_date.setVisible(True)
        elif (index == 1):
            self.le_date.setText("next Tuesday, 10 am")
            self.le_date.setVisible(True)
        else:
            self.le_date.setText("")
            self.le_date.setVisible(False)
    
    
    
    

