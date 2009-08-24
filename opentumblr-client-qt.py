from main_ui import Main_widget
from PyQt4 import QtCore, QtGui
from tumblr import Api,TumblrAuthError
from dashboard import Dashboard
import sys,urllib2

errors = {'403':'Login o password incorrectos','404':'Tumblrlog incorrecto','urlopen':'no ingreso su tumblrlog'}

class Cliente_Opentumblr(Main_widget):
        def __init__(self,parent=None):
                super(Main_widget, self).__init__(parent)
                self.setupUi()                             
                #Conectar eventos
                QtCore.QObject.connect(self.bt_login, QtCore.SIGNAL('clicked()'), self.OnAuthTumblr)            
                
                #Debug properties                                                                      
                self.le_mail.setText('admin@ialex.org')                                                
                self.le_url.setText('http://ialex.tumblr.com')
                
        def OnAuthTumblr(self):
                self.User = self.le_mail.text()                
                self.Password = self.le_password.text()
                self.Blog = self.le_url.text()	
                self.error = None
                if not self.User.isEmpty() | self.Password.isEmpty() | self.Blog.isEmpty():
                        self.api = Api(self.Blog,self.User,self.Password)
            
                        try:
                                self.auth = self.api.auth_check()
                                #Abrir la ventana del dashboard
                                dashboard = Dashboard(self)                                                                  
                                self.hide()
                                dashboard.show()                                
                                #print 'Te haz logueado'
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