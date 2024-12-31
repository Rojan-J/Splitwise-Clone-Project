########################################################################
## IMPORTS
########################################################################
import sys
import os
from PySide2 import *
import sqlite3

########################################################################
# IMPORT GUI FILE
from login_page import Ui_MainWindow as LoginPageUI
from interface import Ui_MainWindow as InterfacePageUI
########################################################################

########################################################################
# IMPORT Custom widgets


import ctypes
os.chdir("Project/Splitwise-Clone-Project/GUI")

sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
from db_operations import add_user, get_user_by_email, add_group, get_all_groups, get_all_usernames

# Explicitly load the cairo DLL
cairo_path = r"C:/Program Files/GTK3-Runtime Win64/bin/libcairo-2.dll"
ctypes.CDLL(cairo_path)

from Custom_Widgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from ProfilePage import *
from GroupPage import *

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
        self.user = None
        self.ui.passwordLogin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.loginBtn_2.clicked.connect(self.login)
        self.ui.SignUpBtn.clicked.connect(self.sign_up)

    def open_interface_page(self):
        # Create an instance of the interface page window
        self.interface_window = MainWindow(self.user)
        self.close()

    def sign_up(self):
        usernames = get_all_usernames()
        #regex pattern for validating emails
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        #regex pattern for validating passwords
        pass_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d._]{6,}$'
        balance_check = False

        name = self.ui.NameSignUp.text()
        username = self.ui.UsernameSignUp.text()
        email = self.ui.EmailSignUp.text()
        password = self.ui.PasswordSignUp.text()
        balance = self.ui.BalanceSignUp.text()
        if self.ui.MaleRBtn.isChecked():
            profile = 1
        else:
            profile = 0

        if name == "":
            self.ui.label.setText("Please Enter Your Name!")
            self.ui.label.setStyleSheet("color: red;")

        elif username == "":
            self.ui.label.setText("Please Enter an Username!")
            self.ui.label.setStyleSheet("color: red;")

        elif email =="":
            self.ui.label.setText("Please Enter Your Email!")
            self.ui.label.setStyleSheet("color: red;")

        elif password =="":
            self.ui.label.setText("Please Enter A Password!")
            self.ui.label.setStyleSheet("color: red;")

        elif not re.match(email_regex, email):
            self.ui.label.setText("Invalid Email!")
            self.ui.label.setStyleSheet("color: red;")

        elif not re.match(pass_regex, password):
            self.ui.textBrowser.setHtml( "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Swis721 Blk BT\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; color:#ff0000;\">Valid password Contains:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; color:#ff0000;\">- At least 6 charachters</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; color:#ff0000;\">- At least 1 upper case and 1 lower case alphabet</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; color:#ff0000;\">- At least 1 number</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; color:#ff0000;\">- Only &quot;.&quot; or &quot;_&quot; (optional)</span></p></body></html>")
            self.ui.label.setText("Please Enter A Password!")
            self.ui.label.setStyleSheet("color: red;")

        elif username in usernames:
            self.ui.label.setText("Username has been taken before!")
            self.ui.label.setStyleSheet("color: red;")

        elif balance != "":
            try:
                balance = int(balance)
                balance_check = True
            except:
                self.ui.label.setText("Invalid Balance!")
                self.ui.label.setStyleSheet("color: red;")

        if balance_check:
            is_registered=True
            add_user(name, username,email,password,profile,is_registered, balance)
            self.user = get_user_by_email(email, username)
            self.open_interface_page()


    def login(self):
        user_email = self.ui.NameLogin.text()
        password = self.ui.passwordLogin.text()
        user = get_user_by_email(user_email, user_email)
        if user_email =="":
                self.ui.label_14.setText("Please Enter Your Username or Email!")
                self.ui.label_14.setStyleSheet("color: red;")
        elif password == "":
            self.ui.label_14.setText("Please Enter Your Password!")
            self.ui.label_14.setStyleSheet("color: red;")            
        elif not user:
            self.ui.label_14.setText("User Not Found!")
            self.ui.label_14.setStyleSheet("color: red;")
        else:
            if user[4] != password:
                self.ui.label_14.setText("Password Is Incorrect!")
                self.ui.label_14.setStyleSheet("color: red;")
            else:
                self.ui.label_14.setText("")
                self.user = user
                self.open_interface_page()



    
class MainWindow(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self)
        self.ui = InterfacePageUI()
        self.ui.setupUi(self)
        self.user = user
        self.group = None


        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################

        ########################################################################

        self.show()
        set_user(self.ui, self.user)

        #CenterMenu Expanding
        self.ui.InfoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.InfoBtn.clicked.connect(lambda: self.ui.label_2.setText("Information"))
        self.ui.DebtsBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.DebtsBtn.clicked.connect(lambda: self.ui.label_2.setText("Debts"))

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

        self.ui.LogOutBtn_3.clicked.connect(self.logout)
        self.ui.LogOutProfileBtn.clicked.connect(self.logout)
        name_edited = True
        self.ui.EditProfileBtn.clicked.connect(lambda: toggle_edit_mode_NameProfile(self.ui, name_edited, self.ui.NameProfile.text()))

        balance_edited = True
        self.ui.BalanceEditBtn.clicked.connect(lambda: toggle_edit_Balance(self.ui, balance_edited, self.ui.BalanceProfile.text()))

        self.ui.FinalAddRecurrentExpenseBtn.clicked.connect(lambda: add_recurrent(self.ui, self.user))

        self.ui.FinalAddGrpBtn.clicked.connect(lambda: create_group(self.ui, self.user))
        self.ui.GroupIcon.clicked.connect(lambda: show_all_existing_groups(self.ui, self.user))

        self.ui.ShareSplit.clicked.connect(lambda: add_shares(self.ui, "share", "add_expense"))
        self.ui.PercentageSplit.clicked.connect(lambda: add_shares(self.ui, "percentage", "add_expense"))
        self.ui.radioButton_7.clicked.connect(lambda: add_shares(self.ui, "equally", "add_expense"))

        self.ui.share.clicked.connect(lambda: add_shares(self.ui, "share", "add_group"))
        self.ui.percentage.clicked.connect(lambda: add_shares(self.ui, "percentage", "add_group"))
        self.ui.Equal.clicked.connect(lambda: add_shares(self.ui, "equally", "add_group"))
        
        
    

        
    
    def change_Btn_name(btn):
        btn.setObjectName("GrpBtn")
    
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
