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
        self.ui.loginBtn_2.clicked.connect(self.open_interface_page)  # Assuming the button is named "login_button"
        self.ui.SignUpBtn.clicked.connect(self.open_interface_page)



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
        self.ui.InfoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())

        #RightMenuExpanding
        #Group Issues
        self.ui.AddMembersBtn_7.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.AddMembersBtn_7.clicked.connect(lambda: self.ui.label_7.setText("Add New Member"))
        self.ui.addGrpBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.addGrpBtn.clicked.connect(lambda: self.ui.label_7.setText("New Group"))
        self.ui.addGrpBtn.clicked.connect(lambda: self.ui.FinalAddGrpBtn.setText("Add Group"))
        self.ui.EditGrpBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.EditGrpBtn.clicked.connect(lambda: self.ui.label_7.setText("Edit Group"))
        self.ui.EditGrpBtn.clicked.connect(lambda: self.ui.FinalAddGrpBtn.setText("Edit Group"))
        self.ui.AddExpensesBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.AddExpensesBtn.clicked.connect(lambda: self.ui.label_7.setText("Add Expense"))

        #Friend Issues
        self.ui.AddFriendsBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.AddFriendsBtn.clicked.connect(lambda: self.ui.label_7.setText("New Friend"))
        self.ui.AddFriendsBtn.clicked.connect(lambda: self.ui.AddFriendBtn.setText("Add Friend"))
        self.ui.EditFriendBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.EditFriendBtn.clicked.connect(lambda: self.ui.label_7.setText("Edit Friend"))
        self.ui.EditFriendBtn.clicked.connect(lambda: self.ui.AddFriendBtn.setText("Edit Friend"))
        self.ui.AddFriendExpenseBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.AddFriendExpenseBtn.clicked.connect(lambda: self.ui.label_7.setText("Add Expense"))

        #Users
        self.ui.AddRExpenseBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.AddRExpenseBtn.clicked.connect(lambda: self.ui.label_7.setText("New Recurrent Expense"))

        #NotificationExpanding
        self.ui.ClosePopUpBtn.clicked.connect(lambda: self.ui.popupNotificationContainer.collapseMenu())

        self.ui.LogOutBtn.clicked.connect(self.logout)
        self.ui.LogOutProfileBtn.clicked.connect(self.logout)
        

    def logout(self):
        # Create an instance of the interface page window
        self.interface_window = LoginWindow()
        self.close()

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
