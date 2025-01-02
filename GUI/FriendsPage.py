from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date

import sys
import os
import json
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Models"))
from db_operations import *
from friends import *
import sqlite3
from groups import *

def show_all_existing_friends(ui, user):
    friends = get_friends_by_username(user[2])
    friendsbtn = dict()
    FriendsBox = dict()
    FriendsFriends = dict()
    while ui.verticalLayout_87.count():
        item = ui.verticalLayout_87.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        if widget:
            widget.deleteLater()
    for  friend in friends:        
        friendship_id, friend_name, friend_email = friend[0], friend[2], friend[3]
        connection=get_connection()
        cursor=connection.cursor()
        friend_friend = Friends(user[2], friend_name, friend_email)
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
        icon22.addPixmap(QtGui.QPixmap(":/images/219969.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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


        ui.verticalLayout_87.addWidget(ui.FriendsFrame)


    for friend, btn in friendsbtn.items():
        btn.clicked.connect(lambda _, f= friend: specific_friend_page(ui, f))



def specific_friend_page(ui, friend: Friends):
    pass