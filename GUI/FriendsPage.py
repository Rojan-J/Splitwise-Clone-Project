from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import re
import sys
import os
import json
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Models"))

#sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database"))
#sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Models"))


from db_operations import *
from friends import *
import sqlite3
from friends import *

def show_all_existing_friends(ui, user):
    friends = get_friends_by_username(user[2])
    friendsbtn = dict()
    FriendsBox = dict()
    FriendsFriends = dict()
    while ui.verticalLayout_55.count():
        item = ui.verticalLayout_55.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        if widget:
            widget.deleteLater()
    for  friend in friends:        
        friendship_id, friend_name, friend_email = friend[0], friend[2], friend[3]
        friend_profile = get_friends_profile_by_friendship_id(friendship_id)[0]
        friend_friend = Friends(user[2], friend_name, friend_email, friend_profile)
        FriendsFriends[friend_name] = friend_friend

        ui.FriendsFrame = QtWidgets.QFrame(ui.frame_63)
        ui.FriendsFrame.setEnabled(True)
        ui.FriendsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ui.FriendsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        ui.FriendsFrame.setObjectName(f"{friend_name}Frame")
        ui.horizontalLayout_32 = QtWidgets.QHBoxLayout(ui.FriendsFrame)
        ui.horizontalLayout_32.setObjectName("horizontalLayout_32")
        ui.FriendsFrame.setStyleSheet("*{\n"
"    background-color: #2c313c;\n"
"    border-radius: 10px\n"
"}")

        ui.ProfileFriend = QtWidgets.QPushButton(ui.FriendsFrame)
        ui.ProfileFriend.setText("")
        icon22 = QtGui.QIcon()
        if friend_profile == 0:
            icon22.addPixmap(QtGui.QPixmap(":/images/219969.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        else:            
            icon22.addPixmap(QtGui.QPixmap(":/images/219986.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.ProfileFriend.setIcon(icon22)
        ui.ProfileFriend.setIconSize(QtCore.QSize(80, 80))
        ui.ProfileFriend.setObjectName(f"ProfileFriend{friend_name}")
        ui.horizontalLayout_32.addWidget(ui.ProfileFriend, 0, QtCore.Qt.AlignLeft)

        ui.frame_17 = QtWidgets.QFrame(ui.FriendsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.frame_17.sizePolicy().hasHeightForWidth())
        ui.frame_17.setSizePolicy(sizePolicy)
        ui.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ui.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        ui.frame_17.setObjectName(f"frame{friend_name}")
        ui.verticalLayout_21 = QtWidgets.QVBoxLayout(ui.frame_17)
        ui.verticalLayout_21.setObjectName("verticalLayout_21")

        ui.label_8 = QtWidgets.QLabel(ui.frame_17)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(18)
        ui.label_8.setFont(font)
        ui.label_8.setObjectName("label_8")
        ui.label_8.setText(f"Name: {friend_name}")
        ui.verticalLayout_21.addWidget(ui.label_8)

        ui.label_16 = QtWidgets.QLabel(ui.frame_17)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(13)
        ui.label_16.setFont(font)
        ui.label_16.setObjectName("label_16")
        ui.label_16.setText(f"Net Balance: {friend_friend.get_total_expenses_of_friend()[0]}")
        ui.verticalLayout_21.addWidget(ui.label_16)

        ui.FriendBtn = QtWidgets.QPushButton(ui.frame_17)
        ui.FriendBtn.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/icons2/icons2/log-in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.FriendBtn.setIcon(icon23)
        ui.FriendBtn.setIconSize(QtCore.QSize(32, 32))
        ui.FriendBtn.setObjectName(f"{friend_name}")
        ui.verticalLayout_21.addWidget(ui.FriendBtn, 0, QtCore.Qt.AlignRight)
        ui.horizontalLayout_32.addWidget(ui.frame_17)
        friendsbtn[friend_friend] = ui.FriendBtn


        ui.verticalLayout_55.addWidget(ui.FriendsFrame)


    for friend, btn in friendsbtn.items():
        btn.clicked.connect(lambda _, f= friend: specific_friend_page(ui, f, user[2]))



def specific_friend_page(ui, friend: Friends, username):
    ui.mainPages.setCurrentWidget(ui.FriendPage)
    ui.FriendName.setText(friend.friend_name)
    profile = friend.friend_profile
    icon22 = QtGui.QIcon()
    if profile == 0:
        icon22.addPixmap(QtGui.QPixmap(":/images/219969.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    else:
        icon22.addPixmap(QtGui.QPixmap(":/images/219986.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)    
    expenses = get_expenses_of_friend_by_friendship_id(friend.friendship_id)
    ui.TableOfExpenses.setRowCount(0)
    header = ui.TableOfExpenses.horizontalHeader()
    header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    for expense in expenses:
        print(expense)
        row_position = ui.TableOfExpenses.rowCount()
        ui.TableOfExpenses.insertRow(row_position)
        var_to_add = [expense[1], expense[3],str(expense[5]), expense[4], expense[7], expense[6], expense[9], expense[8]]
        for col, value in enumerate(var_to_add):
            ui.TableOfExpenses.setItem(row_position, col, QtWidgets.QTableWidgetItem(value))
    
    ui.AddFriendExpenseBtn.clicked.connect(lambda: add_expense_page_friend(ui, friend, username))
    ui.AddFriendBtn_2.clicked.connect(lambda: edit_friend(ui, friend, username ))

def add_expense_page_friend(ui, friend: Friends, username, recover= True):
    if recover:
        ui.MeCh.setText(f"{username}")
        ui.FrCh.setText(f"{friend.friend_name}")
        layout = ui.scrollAreaWidgetContents_21.layout()
        # Iterate through the layout's items
        while layout.count():
            item = layout.takeAt(0)  # Remove the first item in the layout
            widget = item.widget()
            widget.deleteLater()


    ui.FinalAddFriendExpenseBtn.clicked.connect(lambda: add_friend_expense(ui, friend, username))

def create_friend(ui, user):
    default_shares = None
    default_prop_j = None
    default_shares_j = None
    split="equally"
    percent_total = True
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    friend_profile = 0



    
    friend_name = ui.NameInput.text()
    friend_email = ui.EmailInput.text()
    if ui.MaleProfileBtn.isChecked():
        friend_profile = 1
    else:
        friend_profile = 0

    layout = ui.split_frame.layout()
    print(layout)
    count = layout.count()
    for SplitBtnNo in range(count):
        Split = layout.itemAt(SplitBtnNo).widget()
        print(Split)
        if isinstance(Split, QtWidgets.QRadioButton) and Split.isChecked():
            split = Split.text()
    if split != "equally":
        default_shares = get_shares_friend(ui, "add_friend")
        if split == "share":
            default_shares_j = json.dumps(default_shares)
            default_prop_j = None
        else:
            default_prop_j = json.dumps(default_shares)
            default_shares_j = None
    
    if split == "percentage":
        if sum(default_shares.values()) != 100:
            percent_total = False
    print([friend_name, friend_email, re.match(email_regex, friend_email), split, percent_total, friend_profile])
    if friend_name != ""  and friend_email != "" and re.match(email_regex, friend_email) and split !=""  and percent_total:
        print("Yes")
        add_friend_to_dataset(friend_name, friend_email, user, split, default_shares_j, default_prop_j, friend_profile)
        ui.GrpNameInput.setText("")
        ui.NoMembersInput.setValue(0)
        ui.GrpMembersInput.setText("")
        for SplitBtnNo in range(count):
            Split = layout.itemAt(SplitBtnNo).widget()
            if isinstance(Split, QtWidgets.QRadioButton) and Split.isChecked():
                Split.setChecked(False)
        add_shares_friend(ui, "equally", friend_name, user[2], "add_friend")
        
        ui.rightMenuContainer.collapseMenu()
        show_all_existing_friends(ui, user)
    error  = 0 
    widgets = [ui.NameLabel, ui.EmailLabel]
    print([friend_name, friend_email])
    for widget, data in enumerate([friend_name, friend_email]):
        if data == "" :
            widgets[widget].setStyleSheet("color: red;")
            ui.ErrorLabel3.setText("Fill out all inforamtion!")
            ui.ErrorLabel3.setStyleSheet("color : red;")
            error = 1

        else:
            error =0
            widgets[widget].setStyleSheet("color: white;")
            ui.ErrorLabel.setText("")
    if error == 0:
    
        if split == "percentage":
            if not percent_total:
                ui.ErrorLabel3.setText("Enter correct percentages!")
                ui.ErrorLabel3.setStyleSheet("color : red;")
                ui.label.setStyleSheet("color: red;")
            else:
                ui.ErrorLabel3.setText("")
                ui.ErrorLabel3.setStyleSheet("color : white;")
                ui.label.setStyleSheet("color: white;")

def add_friend_to_dataset(friend_name, friend_email, user, split, default_shares_j, default_prop_j, friend_profile):
    print(friend_profile)
    friend = Friends(user[2], friend_name, friend_email, friend_profile)
    friend.add_friend(user[2], user[3], split , default_shares_j, default_prop_j)


def get_shares_friend(ui, page):
    shares = dict()
    if page=="add_friend": layout = ui.scrollAreaWidgetContents_11.layout()
    elif page=="add_expense": layout  = ui.scrollAreaWidgetContents_21.layout()
    elif page == "edit_friend": layout = ui.scrollAreaWidgetContents_17.layout()
    i= 1
    while i < layout.count():
        label_item = layout.itemAt(i)
        share_item = layout.itemAt(i + 1)
        label_widget = label_item.widget()
        share_widget = share_item.widget()
        label = label_widget.text()
        share = share_widget.value()
        shares[label] = share
        i += 2

    return shares

def add_shares_friend(ui, split_type, friendname, username, page):
    if page=="add_friend": 
        layout = ui.scrollAreaWidgetContents_11.layout()
        scroll = ui.scrollAreaWidgetContents_11
    elif page == "add_expense" :  
        layout = ui.scrollAreaWidgetContents_21.layout()
        scroll = ui.scrollAreaWidgetContents_21
    elif page == "edit_friend":
        layout = ui.scrollAreaWidgetContents_17.layout()
        scroll = ui.scrollAreaWidgetContents_17
    while layout.count():
        item = layout.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        widget.deleteLater()
    if split_type != "equally":
        contributers=[friendname, username]
        ui.label = QtWidgets.QLabel(scroll)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        ui.label.setFont(font)
        ui.label.setObjectName("label")
        layout.addWidget(ui.label)
        ui.label.setText(f"{split_type}s:")
        for contributer in contributers:
            ui.label_9 = QtWidgets.QLabel(scroll)
            ui.label_9.setObjectName("label_9")
            layout.addWidget(ui.label_9)
            ui.label_9.setText(contributer)
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            font.setPointSize(8)
            ui.label_9.setFont(font)
            ui.spinBox = QtWidgets.QSpinBox(scroll)
            ui.spinBox.setObjectName("spinBox")
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            font.setPointSize(8)
            ui.spinBox.setFont(font)
            ui.spinBox.setValue(0)
            layout.addWidget(ui.spinBox)


def isfloat(value):
    try:
        float(value)  
        return True
    except:  
        return False
    
def add_friend_expense(ui, friend, username):

    category = ""
    label = ui.FriendExpenseLabelInput.text()
    amount = ui.AmountInputFr.text()
    selected_date = ui.DateInputFr.selectedDate().toString("yyyy-dd-MM")
    print(selected_date)
    payer = ui.PayerInputFr.text()
    description = ui.DiscriptionInputFr.toPlainText()
    split_type = "default split"
    default = False
    error_def_perc = False

    contributers = []
    ui.MeCh.setText(f"{username}")
    ui.FrCh.setText(f"{friend.friend_name}")
    if ui.MeCh.isChecked():
        contributers.append(username)
    if ui.FrCh.isChecked():
        contributers.append(friend.friend_name)



    for categoryBtnNo in range(6):
        categoryBtn = ui.gridLayout_13.itemAt(categoryBtnNo).widget()
        if categoryBtn.isChecked():
              category = categoryBtn.text()
    if category == "":
         category = "etc."


    for SplitTypeNo in range(4):
        SplitTypeBtn = ui.verticalLayout_56.itemAt(SplitTypeNo).widget()
        if SplitTypeBtn.isChecked():
            split_type = SplitTypeBtn.text()

    if split_type == "share" or split_type == "percentage":
            shares = get_shares_friend(ui, "add_expense")


    if split_type == "default split":
        default = True
        defaults = get_default_split_friend(friend.friendship_id, friend.friend_name)
        default_split = defaults[-3]
        default_shares = defaults[-2]
        default_proportions = defaults[-1]
        if default_shares:
            default_shares = json.loads(default_shares)
        if  default_proportions:
            default_proportions = json.loads(default_proportions)
        split_type = default_split
        if split_type == "share":
            shares = dict()
            for contributer in contributers:
                shares[contributer] = default_shares[contributer]
        elif split_type == "percentage":
            shares = default_proportions
    
        
    def total_perc(split_type):
        if split_type == "percentage":
            if  default == False:
                shares = get_shares_friend(ui, "add_expense")
            else:
                shares = default_proportions
            if sum(shares.values()) != 100:
                return False
        return True
        


    widgets = [ui.FrienndExpenseLabel, ui.AmountLabelFr, ui.PayerLabelFr, ui.ContributersLabelFr]

    error = 0
    
    for widget, data in enumerate([label, amount, payer, contributers]):
        if data == "" or data == [] or not data:
            widgets[widget].setStyleSheet("color: red;")
            ui.ErrorLabelFrEx.setText("Fill out all required inforamtion!")
            ui.ErrorLabelFrEx.setStyleSheet("color : red;")
            error = 1
    

        else:
            widgets[widget].setStyleSheet("color: white;")
            ui.ErrorLabelFrEx.setText("")
            error = 0

    if payer not in [friend.friend_name, username]:
        widgets[1].setStyleSheet("color: red;")
        widgets[2].setStyleSheet("color: red;")
        if error == 0:
            ui.ErrorLabelFrEx.setText("Payer is not accepted!")
            ui.ErrorLabelFrEx.setStyleSheet("color : red;")
            error = 2

    else:
        error = 0
        widgets[1].setStyleSheet("color: white;")
        widgets[2].setStyleSheet("color: white;")
        ui.ErrorLabelFrEx.setText("")

    
    
    if split_type == "percentage" and default == False:
        if not total_perc(split_type):
            ui.label.setStyleSheet("color: red;")
            if error == 0:
                ui.ErrorLabelFrEx.setText("Enter correct percentages!")
                ui.ErrorLabelFrEx.setStyleSheet("color : red;")
                
                error =3
        else:
            ui.ErrorLabelFrEx.setText("")
            ui.ErrorLabelFrEx.setStyleSheet("color : white;")
            ui.label.setStyleSheet("color: white;")
            error = 0
    
    if default == True and split_type == "percentage":
        if len(contributers) != 2:
            error_def_perc = True
            ui.SplitLabelFrFr.setStyleSheet("color: red;")
            if error == 0:
                ui.ErrorLabelFrEx.setText("Your default split is percentage based; This mode of split is applicable only when both are contributed!")
                ui.ErrorLabelFrEx.setStyleSheet("color : red;")

            

    if error_def_perc == False and label != "" and amount != "" and selected_date != "" and isfloat(amount) and contributers != [] and payer != ""  and payer in [friend.friend_name, username] and total_perc(split_type):

        ui.FrienndExpenseLabel.setStyleSheet("color: white;")
        ui.AmountLabelFr.setStyleSheet("color: white;")
        ui.PayerLabelFr.setStyleSheet("color: white;")
        ui.ContributersLabelFr.setStyleSheet("color: white;")
        ui.SplitLabelFr.setStyleSheet("color: white;")
        ui.ErrorLabelFrEx.setText("")
        ui.ErrorLabelFrEx.setStyleSheet("color : white;")
        if split_type == "share":
            shares = shares
            friend.add_expenses(label, amount, payer, contributers, selected_date, category,description, split_type, shares=shares)
        elif split_type == "percentage":
            proportions = shares
            friend.add_expenses(label, amount, payer, contributers, selected_date, category,description, split_type, proportions=proportions)
        else:
            friend.add_expenses(label,amount, payer, contributers, selected_date, category,description, split_type)
        
        if default == True : split_title =f"default ({split_type})"
        else: split_title = split_type
        var_to_add = [label, payer, str(amount),",".join(contributers), selected_date, category, split_title, description]
        row_position = ui.TableOfExpenses.rowCount()
        ui.TableOfExpenses.insertRow(row_position)
        for col, value in enumerate(var_to_add):
            ui.TableOfExpenses.setItem(row_position, col, QtWidgets.QTableWidgetItem(value))

        ui.FriendExpenseLabelInput.setText("")
        ui.AmountInputFr.setText("")
        ui.PayerInputFr.setText("")
        ui.DiscriptionInputFr.setText("")
        split_type = "equally"
        add_shares_friend(ui, split_type, friend.friend_name, username, "add_expense")
        for SplitTypeNo in range(4):
            ui.verticalLayout_56.itemAt(SplitTypeNo).widget().setChecked(False)
        layout = ui.scrollAreaWidgetContents_14.layout()
        for i in range(layout.count()):
            layout.itemAt(i).widget().setChecked(False)
        for categoryBtnNo in range(6):
            ui.gridLayout_13.itemAt(categoryBtnNo).widget().setChecked(False)
        ui.GrpTotalExpense.setText(f"Total Expense: {friend.get_total_expenses_of_friend()[0]}")
        
        ui.rightMenuContainer.collapseMenu()



def edit_friend(ui, friend, username):
    default_shares_j = None
    default_prop_j = None

    percent_total = True
    if ui.MaleProfileBtn_2.isChecked():
        friend_profile = 1
    elif ui.LadyProfileBtn_2.isChecked():
        friend_profile = 0
    layout = ui.split_frame_2.layout()
    count = layout.count()
    for SplitBtnNo in range(count):
        Split = layout.itemAt(SplitBtnNo).widget()
        print(Split)
        if isinstance(Split, QtWidgets.QRadioButton) and Split.isChecked():
            split = Split.text()
    if split != "equally":
        default_shares = get_shares_friend(ui, "edit_friend")
        if split == "share":
            default_shares_j = json.dumps(default_shares)
            default_prop_j = None
        else:
            default_prop_j = json.dumps(default_shares)
            default_shares_j = None
    
    if split == "percentage":
        if sum(default_shares.values()) != 100:
            percent_total = False

    if  split !=""  and percent_total:
        print("Yes")
        edit_friend_database(friend.friendship_id, friend_profile, split, default_shares_j, default_prop_j)
        for SplitBtnNo in range(count):
            Split = layout.itemAt(SplitBtnNo).widget()
            if isinstance(Split, QtWidgets.QRadioButton) and Split.isChecked():
                Split.setChecked(False)
        add_shares_friend(ui, "equally", friend.friend_name, username, "edit_friend")
        
        ui.rightMenuContainer.collapseMenu()
        specific_friend_page(ui, friend, username)
    
    
    if split == "percentage":
        if not percent_total:
            ui.ErrorLabel3_2.setText("Enter correct percentages!")
            ui.ErrorLabel3_2.setStyleSheet("color : red;")
            ui.label.setStyleSheet("color: red;")
        else:
            ui.ErrorLabel3_2.setText("")
            ui.ErrorLabel3_2.setStyleSheet("color : white;")
            ui.label.setStyleSheet("color: white;")