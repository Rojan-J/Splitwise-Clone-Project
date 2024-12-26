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
json_path = "style2.json"

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = LoginPageUI()  # Create an instance of the login page UI
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui, jsonFiles = ["style2.json"])
        self.show()
        self.ui.loginBtn.clicked.connect(self.open_interface_page)  # Assuming the button is named "login_button"
        self.ui.signupBtn.clicked.connect(self.sign_up)

    def sign_up(self):
        if self.ui.loginTitle.text() == "Login:":
            self.ui.loginTitle.setText( "ُSign Up:")
            self.ui.noAccount.setText("Already have an account?")
            self.ui.signupBtn.setText("Login")
            self.ui.loginBtn.setText("Sign Up")
        else:
            self.ui.loginTitle.setText( "Login:")
            self.ui.noAccount.setText("Don't have an account?")
            self.ui.signupBtn.setText("Sign Up")
            self.ui.loginBtn.setText("Login")


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

        #RightMenuExpanding
        self.ui.ProfileMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.ProfileMenuBtn.clicked.connect(lambda: self.ui.label_7.setText("Profile"))
        self.ui.addGrpBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.addGrpBtn.clicked.connect(lambda: self.ui.label_7.setText("New Group"))
        self.ui.AddExpensesBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.AddExpensesBtn.clicked.connect(lambda: self.ui.label_7.setText("Add Expense"))

        #NotificationExpanding
        self.ui.ClosePopUpBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())



########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
