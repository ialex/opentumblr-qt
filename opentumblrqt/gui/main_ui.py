#!/usr/bin/python
from PyQt4 import QtCore, QtGui

class Main_widget(QtGui.QDialog):
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
                
        def setupUi(self):
                self.setWindowTitle("Opentumblr-qt")
                self.resize(341,418)
                
                #window Icon
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("/usr/share/pixmaps/opentumblr-qt/dashboard/opentumblr_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.setWindowIcon(icon)
                
                #Layout de la ventana
                self.Vbox = QtGui.QVBoxLayout(self)
                
                #Creamos etiquetas
                self.lb_mail = self.CreateLabel("Mail")
                self.lb_password = self.CreateLabel("Password")
                self.lb_url = self.CreateLabel("Login")
                self.lb_rememberme = self.CreateLabel("Remember Me")
                
                
                #Creamos Cajas de texto
                self.le_mail = self.CreateLineEdit()
                self.le_password = self.CreateLineEdit()                
                self.le_url = self.CreateLineEdit()                
                
                #Modo password el line edit password
                self.le_password.setEchoMode(QtGui.QLineEdit.Password)
                
                #Boton login
                self.bt_login = QtGui.QPushButton("Log in")
                sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)                        
                self.bt_login.setMaximumSize(QtCore.QSize(16777215, 58))
                self.bt_login.setSizePolicy(sizePolicy)
                
                #Remember me Checkbox
                self.rememberme = QtGui.QCheckBox()
                
                #Agregamos los wigdets a layout :D
                self.Vbox.addWidget(self.lb_mail)
                self.Vbox.addWidget(self.le_mail)
                self.Vbox.addWidget(self.lb_password)
                self.Vbox.addWidget(self.le_password)
                self.Vbox.addWidget(self.lb_url)
                self.Vbox.addWidget(self.le_url)
                self.Vbox.addWidget(self.lb_rememberme)
                self.Vbox.addWidget(self.rememberme)                        
                self.Vbox.addWidget(self.bt_login)
                
                #Definimos layout de la ventana
                self.setLayout(self.Vbox)
                                
