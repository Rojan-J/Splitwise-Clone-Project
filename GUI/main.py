########################################################################
## IMPORTS
########################################################################
import sys
import os
from PySide2 import *


########################################################################
# IMPORT GUI FILE
from login_page import Ui_MainWindow as LoginPageUI
from interface import Ui_MainWindow as InterfacePageUI
########################################################################

########################################################################
# IMPORT Custom widgets


import ctypes
import os
os.chdir("Project/Splitwise-Clone-Project/GUI")

# Explicitly load the cairo DLL
cairo_path = r"C:/Program Files/GTK3-Runtime Win64/bin/libcairo-2.dll"
ctypes.CDLL(cairo_path)

from Custom_Widgets import *
from PyQt5.QtWidgets import QApplication

########################################################################
## MAIN WINDOW CLASS
########################################################################
current_script = os.path.dirname(os.path.realpath(sys.argv[0]))
json_path = "Project/Splitwise-Clone-Project/GUI/style.json"

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = LoginPageUI()  # Create an instance of the login page UI
        self.ui.setupUi(self)
        self.ui.loginBtn.clicked.connect(self.open_interface_page)  # Assuming the button is named "login_button"
        self.ui.signupBtn.clicked.connect(self.sign_up)

    def sign_up(self):
        self.ui.loginTitle.setText( "ُSign Up:")
        self.ui.noAccount.setText("Already have an account?")
        self.ui.signupBtn.setText("Login")
        self.ui.loginBtn.setText("Sign Up")


    def open_interface_page(self):
        # Create an instance of the interface page window
        self.interface_window = MainWindow()
        self.close()

    
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = InterfacePageUI()
        self.ui.setupUi(self)


        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################

        ########################################################################

        self.show()
        #CenterMenu Expanding
        self.ui.SettingsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.InfoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.HelpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        #RightMenuExpanding
        self.ui.RightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.ProfileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())

        #NotificationExpanding
        self.ui.ClosePopUpBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())



########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
