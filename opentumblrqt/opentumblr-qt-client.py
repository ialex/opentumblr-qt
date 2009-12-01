#!/usr/bin/python
from PyQt4 import QtCore, QtGui
import sys,urllib2

try:        
    from opentumblrqt.gui.main_ui import Main_widget
    from opentumblrqt.tumblr import Api,TumblrAuthError
    from opentumblrqt.dashboard import Dashboard
except ImportError:
    from gui.main_ui import Main_widget
    from tumblr import Api,TumblrAuthError
    from dashboard import Dashboard

errors = {'403':'Login o password incorrectos','404':'Tumblrlog incorrecto','urlopen':'no ingreso su tumblrlog'}

class Cliente_Opentumblr(Main_widget):
    def __init__(self,parent=None):
        super(Main_widget, self).__init__(parent)
        self.setupUi()                             
        #Conectar eventos
        self.connect(self.bt_login, QtCore.SIGNAL('clicked()'),self.OnAuthTumblr)                                                    
        self.rememberme.setCheckState(QtCore.Qt.Unchecked)                                                        
        
        if(QtCore.QFile().exists(QtCore.QDir().homePath() + '/.opentumblr')):
            file = open(QtCore.QDir().homePath() + '/.opentumblr','r')
            self.le_mail.setText(file.readline())                                                
            self.le_url.setText(file.readline())
                                                                                    

    def OnAuthTumblr(self):
        self.User = self.le_mail.text().trimmed()                
        self.Password = self.le_password.text()
        self.Blog = self.le_url.text().trimmed()        
        self.error = None
        if not self.User.isEmpty() | self.Password.isEmpty() | self.Blog.isEmpty():
            self.api = Api(self.Blog,self.User,self.Password)

            try:
                self.auth = self.api.auth_check()
                                        
                #Abrir la ventana del dashboard
                dashboard = Dashboard(self)                                                                  
                self.hide()
                dashboard.show()                                
                if self.rememberme.checkState() == 2:
                    file = open(QtCore.QDir().homePath() + '/.opentumblr','w')
                    file.write(self.le_mail.text() + '\n')
                    file.write(self.le_url.text() + '\n')
                             
            except TumblrAuthError:	    		
                self.error = errors['403']
            except urllib2.HTTPError:
                self.error = errors['404']
            except urllib2.URLError:
                self.error = errors['urlopen']
            finally:
                if self.error != None:
                    QtGui.QMessageBox.warning(self,'Error','Occurrio un error: \n' + self.error,QtGui.QMessageBox.Ok)			    
        else:
            QtGui.QMessageBox.warning(self,'Error','Todos los Campos son necesarios',QtGui.QMessageBox.Ok)		            
            
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    tumblr_client = Cliente_Opentumblr()        
    tumblr_client.show()     
    app.connect(app, QtCore.SIGNAL('lastWindowClosed()'), app, QtCore.SLOT('quit()'))
    sys.exit(app.exec_())
