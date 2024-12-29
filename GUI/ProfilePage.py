from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
from db_operations import *

def set_user(ui, user):
    ui.NameProfile.setText(user[1])
    ui.UsernameProfile.setText(user[2])
    ui.EmailProfile.setText(user[3])
    ui.BalanceProfile.setText(str(user[-1]))
    print(user[-2] == 0)
    if user[-2] == 0:
        profile = QtGui.QIcon(":/images/3135823.png")
        ui.PicProfile.setIcon(profile)

    else:
        profile = QtGui.QIcon(":/images/Layer 1.png")
        ui.PicProfile.setIcon(profile)
        ui.PicProfile.setIconSize(QtCore.QSize(90, 90))

def toggle_edit_mode_NameProfile(ui, edited, name):
        
        if edited:
            ui.NameProfile.deleteLater()
            ui.horizontalLayout_51.removeWidget(ui.NameProfile)
            ui.NameLineEdit = QtWidgets.QLineEdit(ui.ProfileContainer)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(ui.NameLineEdit.sizePolicy().hasHeightForWidth())
            ui.NameLineEdit.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            font.setPointSize(20)
            ui.NameLineEdit.setFont(font)
            ui.NameLineEdit.setObjectName("NameLineEdit")
            ui.horizontalLayout_51.addWidget(ui.NameLineEdit)
            ui.NameLineEdit.setText(name)
            ui.EditProfileBtn.deleteLater()
            ui.EditProfileBtn = QtWidgets.QPushButton(ui.ProfileContainer)
            ui.EditProfileBtn.setText("")
            icon17 = QtGui.QIcon()
            icon17.addPixmap(QtGui.QPixmap("icons2/check-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            ui.EditProfileBtn.setIcon(icon17)
            ui.EditProfileBtn.setIconSize(QtCore.QSize(32, 32))
            ui.EditProfileBtn.setObjectName("EditProfileBtn")
            ui.horizontalLayout_51.addWidget(ui.EditProfileBtn)
            edited = False
            ui.EditProfileBtn.clicked.connect(lambda: toggle_edit_mode_NameProfile(ui, edited, name))

        else:
            user_name = ui.UsernameProfile.text()
            new_name = ui.NameLineEdit.text()
            name = " ".join(new_name.split()) if new_name.strip() else name  # Avoid empty names
            update_name(user_name, name)
            ui.NameLineEdit.deleteLater()
            ui.NameProfile = QtWidgets.QLabel(ui.ProfileContainer)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(ui.NameProfile.sizePolicy().hasHeightForWidth())
            ui.NameProfile.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            font.setPointSize(20)
            ui.NameProfile.setFont(font)
            ui.NameProfile.setObjectName("NameProfile")
            ui.horizontalLayout_51.addWidget(ui.NameProfile)
            ui.NameProfile.setText(name)
            # Switch back to display mode
            ui.NameProfile.setText(name)
            ui.EditProfileBtn.deleteLater()
            ui.EditProfileBtn = QtWidgets.QPushButton(ui.ProfileContainer)
            ui.EditProfileBtn.setText("")
            icon17 = QtGui.QIcon()
            icon17.addPixmap(QtGui.QPixmap("icons2/edit-3.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            ui.EditProfileBtn.setIcon(icon17)
            ui.EditProfileBtn.setIconSize(QtCore.QSize(32, 32))
            ui.EditProfileBtn.setObjectName("EditProfileBtn")
            ui.horizontalLayout_51.addWidget(ui.EditProfileBtn)


            edited = True
            ui.EditProfileBtn.clicked.connect(lambda: toggle_edit_mode_NameProfile(ui, edited, name))


def toggle_edit_Balance(ui, edited, balance):
        
        if edited:
            ui.BalanceProfile.deleteLater()
            ui.BalanceLineEdit = QtWidgets.QLineEdit(ui.frame_52)
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            font.setPointSize(11)
            ui.BalanceLineEdit.setFont(font)
            ui.BalanceLineEdit.setObjectName("BalanceLineEdit")
            ui.verticalLayout_90.addWidget(ui.BalanceLineEdit)
            ui.BalanceLineEdit.setText(balance)

            ui.BalanceEditBtn.deleteLater()
            ui.BalanceEditBtn = QtWidgets.QPushButton(ui.ProfileeInformations)
            ui.BalanceEditBtn.setText("")
            icon18 = QtGui.QIcon()
            icon18.addPixmap(QtGui.QPixmap("icons2/check-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            ui.BalanceEditBtn.setIcon(icon18)
            ui.BalanceEditBtn.setIconSize(QtCore.QSize(20, 20))
            ui.BalanceEditBtn.setObjectName("BalanceEditBtn")
            ui.gridLayout_15.addWidget(ui.BalanceEditBtn, 2, 2, 1, 1)
            edited = False
            ui.BalanceEditBtn.clicked.connect(lambda: toggle_edit_Balance(ui, edited, balance))

        else:
            user_name = ui.UsernameProfile.text()
            balance_check = False
            new_balance = ui.BalanceLineEdit.text()
            if new_balance != "":
                try:
                    new_balance = float(new_balance)
                    balance_check = True
                except:
                    balance_check = False
                balance = new_balance if balance_check else balance

            update_balance(user_name, float(balance))
            ui.BalanceLineEdit.deleteLater()
            ui.BalanceProfile = QtWidgets.QLabel(ui.frame_52)
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            font.setPointSize(11)
            ui.BalanceProfile.setFont(font)
            ui.BalanceProfile.setObjectName("BalanceProfile")
            ui.verticalLayout_90.addWidget(ui.BalanceProfile)
            ui.BalanceProfile.setText(str(balance))
            # Switch back to display mode
            ui.BalanceProfile.setText(str(balance))

            ui.BalanceEditBtn.deleteLater()
            ui.BalanceEditBtn = QtWidgets.QPushButton(ui.ProfileeInformations)
            ui.BalanceEditBtn.setText("")
            icon18 = QtGui.QIcon()
            icon18.addPixmap(QtGui.QPixmap("icons2/edit-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            ui.BalanceEditBtn.setIcon(icon18)
            ui.BalanceEditBtn.setIconSize(QtCore.QSize(20, 20))
            ui.BalanceEditBtn.setObjectName("BalanceEditBtn")
            ui.gridLayout_15.addWidget(ui.BalanceEditBtn, 2, 2, 1, 1)


            edited = True
            ui.BalanceEditBtn.clicked.connect(lambda: toggle_edit_Balance(ui, edited, balance))


def add_recurrent(ui, user):
    username = user[2]
    user_id = user[0]
    label = ui.LabelInput.text()
    amount = ui.AmountRExpenseInput.text()
    days = []
    for day in range(31):
        dayCheck = ui.gridLayout_16.itemAt(day)
        if dayCheck.isChecked():
            days.append(dayCheck.text())
    days = ",".join(days)
    for categoryBtnNo in range(6):
        categoryBtn = ui.gridLayout_17.itemAt(categoryBtnNo)
        if categoryBtn.isChecked():
              category = categoryBtn.text()
    print(username, user_id, label, amount, days, category)