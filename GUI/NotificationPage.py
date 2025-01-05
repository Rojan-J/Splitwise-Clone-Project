from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import re
import sys
import os
import json
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))

#sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database"))

import matplotlib.pyplot as plt
from db_operations import *


def show_all_notifications(user, ui):
    layout = ui.scrollAreaWidgetContents_26.layout()
    while layout.count():
        item = layout.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        if widget:
            widget.deleteLater()
    notifications = get_user_notifications(user)
    print(notifications)
    notification_btns = dict()
    for notif in notifications:
        debtor, debt_id, amount = notif[2:5]
        notification_message = f"Did {debtor} payed you {amount} R?"
        ui.widget_notification = QtWidgets.QWidget(ui.scrollAreaWidgetContents_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.widget_notification.sizePolicy().hasHeightForWidth())
        ui.widget_notification.setSizePolicy(sizePolicy)
        ui.widget_notification.setObjectName(f"verification of {debt_id}")
        ui.verticalLayout_800 = QtWidgets.QVBoxLayout(ui.widget_notification)
        ui.verticalLayout_800.setObjectName("verticalLayout_800")
        ui.label_verification = QtWidgets.QLabel(ui.widget_notification)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(11)
        ui.label_verification.setFont(font)
        ui.label_verification.setObjectName("label_verification")
        ui.verticalLayout_800.addWidget(ui.label_verification, 0, QtCore.Qt.AlignCenter)
        ui.frame_900 = QtWidgets.QFrame(ui.widget_notification)
        ui.frame_900.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ui.frame_900.setFrameShadow(QtWidgets.QFrame.Raised)
        ui.frame_900.setObjectName("frame_900")
        ui.verticalLayout_801 = QtWidgets.QVBoxLayout(ui.frame_900)
        ui.verticalLayout_801.setObjectName("verticalLayout_801")
        ui.Verified_Payment = QtWidgets.QPushButton(ui.frame_900)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        ui.Verified_Payment.setFont(font)
        ui.Verified_Payment.setObjectName(f"verification button of {debt_id}")
        ui.verticalLayout_801.addWidget(ui.Verified_Payment)
        ui.UnverifiedBtn = QtWidgets.QPushButton(ui.frame_900)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        ui.UnverifiedBtn.setFont(font)
        ui.UnverifiedBtn.setObjectName(f"unverification button of {debt_id}")
        ui.verticalLayout_801.addWidget(ui.UnverifiedBtn)
        ui.verticalLayout_800.addWidget(ui.frame_900, 0, QtCore.Qt.AlignHCenter)
        layout = ui.scrollAreaWidgetContents_26.layout()
        layout.addWidget(ui.widget_notification)
        ui.label_verification.setText(notification_message)
        ui.Verified_Payment.setText("Verify")
        ui.UnverifiedBtn.setText("Deny")
        notification_btns[(debt_id, debtor, amount)] = [ui.Verified_Payment, ui.UnverifiedBtn, ui.frame_900, ui.label_verification]

    for debt, btn in notification_btns.items():
        btn[0].clicked.connect(lambda _, b=btn, d= debt: verified_payment(ui, b, d, user))
        btn[1].clicked.connect(lambda _, b=btn, d =debt: unverified_payment(ui, b, d, user))


def verified_payment(ui, btn, debt, username):
    debt_id, debtor, amount = debt
    Verified_btn, Unverified_btn, btns_frame, message = btn
    layout = btns_frame.layout()
    while layout.count():
        item = layout.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        if widget:
            widget.deleteLater()

    message.setText("Verified")

    update_debt_status(debt_id,"Paid")
    current_balance = get_balance(username)[0]
    new_balance = current_balance + amount

    update_balance(username, new_balance)
    update_notification_status(username)

    

def unverified_payment(ui, btn, debt, user):
    debt_id, debtor, amount = debt
    Verified_btn, Unverified_btn, btns_frame, message = btn
    layout = btns_frame.layout()
    while layout.count():
        item = layout.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        if widget:
            widget.deleteLater()

    message.setText("Denied")


    update_debt_status(debt_id,"Not Paid!")
    current_balance = get_balance(debtor)[0]
    new_balance = current_balance + amount

    update_balance(debtor, new_balance)
    update_notification_status(username)


        

