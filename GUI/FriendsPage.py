from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import re
import sys
import os
import json
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Models"))
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
        btn.clicked.connect(lambda _, f= friend: specific_friend_page(ui, f))



def specific_friend_page(ui, friend: Friends):
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
    
    ui.AddExpensesBtn.clicked.connect(lambda: add_expense_page_friend(ui, friend))

def add_expense_page_friend(ui, friend: Friends):
    pass

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
        default_shares = get_shares_friend(ui)
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
        add_shares_friend(ui, "equally", friend_name, user[2])
        
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


def get_shares_friend(ui):
    shares = dict()
    layout = ui.scrollAreaWidgetContents_11.layout()
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

def add_shares_friend(ui, split_type, friendname, username):
    layout = ui.scrollAreaWidgetContents_11.layout()
    while layout.count():
        item = layout.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        widget.deleteLater()
    if split_type != "equally":
        contributers=[friendname, username]
        ui.label = QtWidgets.QLabel(ui.scrollAreaWidgetContents_11)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        ui.label.setFont(font)
        ui.label.setObjectName("label")
        ui.verticalLayout_29.addWidget(ui.label)
        ui.label.setText(f"{split_type}s:")
        for contributer in contributers:
            ui.label_9 = QtWidgets.QLabel(ui.scrollAreaWidgetContents_11)
            ui.label_9.setObjectName("label_9")
            ui.verticalLayout_29.addWidget(ui.label_9)
            ui.label_9.setText(contributer)
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            font.setPointSize(8)
            ui.label_9.setFont(font)
            ui.spinBox = QtWidgets.QSpinBox(ui.scrollAreaWidgetContents_11)
            ui.spinBox.setObjectName("spinBox")
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            font.setPointSize(8)
            ui.spinBox.setFont(font)
            ui.spinBox.setValue(0)
            ui.verticalLayout_29.addWidget(ui.spinBox)


def isfloat(value):
    try:
        float(value)  
        return True
    except:  
        return False
    
