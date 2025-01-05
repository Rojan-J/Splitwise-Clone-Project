from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import re
import sys
import os
import json
# sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))


sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database"))

import matplotlib.pyplot as plt
from db_operations import *


def show_all_debts(username, ui):
    all_debts = total_user_owes(username)
    print(all_debts, "ALL DEBTS ARE")
    debts_radio_buttons = dict()
    layout =  ui.widget_23.layout()
    while layout.count():
        item = layout.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        if widget:
            widget.deleteLater()
    for debt in all_debts:
        ui.widget_23 = QtWidgets.QWidget(ui.scrollAreaWidgetContents_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.widget_23.sizePolicy().hasHeightForWidth())
        ui.widget_23.setSizePolicy(sizePolicy)
        ui.widget_23.setObjectName(f"debt to {debt[-3]}")
        ui.verticalLayout_176 = QtWidgets.QVBoxLayout(ui.widget_23)
        ui.verticalLayout_176.setObjectName("verticalLayout_176")
        ui.label_85 = QtWidgets.QLabel(ui.widget_23)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(11)
        ui.label_85.setFont(font)
        ui.label_85.setObjectName("label_85")
        ui.verticalLayout_176.addWidget(ui.label_85, 0, QtCore.Qt.AlignCenter)
        ui.frame_109 = QtWidgets.QFrame(ui.widget_23)
        ui.frame_109.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ui.frame_109.setFrameShadow(QtWidgets.QFrame.Raised)
        ui.frame_109.setObjectName("frame_109")
        ui.verticalLayout_177 = QtWidgets.QVBoxLayout(ui.frame_109)
        ui.verticalLayout_177.setObjectName("verticalLayout_177")
        ui.label_85.setText(f"you owe {debt[-3]} {debt[-2]} R")
        if debt[-1] == "Not Paid!":
            ui.radioButton_49 = QtWidgets.QRadioButton(ui.frame_109)
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            ui.radioButton_49.setFont(font)
            ui.radioButton_49.setObjectName(f"payed_online{debt[-3]}")
            ui.verticalLayout_177.addWidget(ui.radioButton_49)
            ui.radioButton_50 = QtWidgets.QRadioButton(ui.frame_109)
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            ui.radioButton_50.setFont(font)
            ui.radioButton_50.setObjectName(f"payed_cash{debt[-3]}")
            ui.verticalLayout_177.addWidget(ui.radioButton_50)
            ui.verticalLayout_176.addWidget(ui.frame_109, 0, QtCore.Qt.AlignHCenter)
            ui.verticalLayout_175.addWidget(ui.widget_23)
            ui.radioButton_49.setText("Pay from this account")
            ui.radioButton_50.setText("Paid by cash")
            debts_radio_buttons[(debt[0], debt[-2], debt[-3])] = [ui.radioButton_49, ui.radioButton_50, ui.widget_23]
        
        elif debt[-1] =="pending":
            layout = ui.widget_23.layout()
            ui.CashPaidLabel = QtWidgets.QLabel(ui.widget_23)
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            font.setPointSize(10)
            ui.CashPaidLabel.setFont(font)
            ui.CashPaidLabel.setObjectName("CashPaidLabel")
            layout.addWidget(ui.CashPaidLabel)
            ui.CashPaidLabel.setText("Pending")

    for debt, btn in debts_radio_buttons.items():
        btn[1].clicked.connect(lambda _, b=btn, d= debt: pay_cash(ui,b, d))
        btn[0].clicked.connect(lambda _, b=btn, d =debt: pay_online(ui, b, d, username))



def pay_cash(ui, btn, debt_id):
    debt_id = debt_id[0]
    layout = btn[2].layout()
    if btn[1]:
        layout.removeWidget(btn[1])
        btn[1].deleteLater()
        btn[1] = None

    if btn[0]:
        layout.removeWidget(btn[0])
        btn[0].deleteLater()
        btn[0] = None

    ui.CashPaidLabel = QtWidgets.QLabel(btn[2])
    font = QtGui.QFont()
    font.setFamily("Swis721 Blk BT")
    font.setPointSize(10)
    ui.CashPaidLabel.setFont(font)
    ui.CashPaidLabel.setObjectName("CashPaidLabel")
    layout.addWidget(ui.CashPaidLabel)
    ui.CashPaidLabel.setText("Paid by cash!")
    update_debt_status(debt_id,"Paid")


def pay_online(ui, btn, debt, username):
    debt_id, debt_amount, creditor = debt
    layout = btn[2].layout()
    if btn[1]:
        layout.removeWidget(btn[1])
        btn[1].deleteLater()
        btn[1] = None

    if btn[0]:
        layout.removeWidget(btn[0])
        btn[0].deleteLater()
        btn[0] = None

    temporary = get_temp_creditor(creditor)

    if temporary == 1:

        ui.CashPaidLabel = QtWidgets.QLabel(btn[2])
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        ui.CashPaidLabel.setFont(font)
        ui.CashPaidLabel.setObjectName("CashPaidLabel")
        layout.addWidget(ui.CashPaidLabel)
        
        current_balance = get_balance(username)[0]
        print("Cur_bal is" , current_balance)
        new_balance = current_balance - debt_amount
        if new_balance >= 0:
            update_debt_status(debt_id,"Paid")
            update_balance(username, new_balance)
            ui.CashPaidLabel.setText("Paid Online!")
        else:
            ui.CashPaidLabel.setText("You don't have enough Money!")

    elif temporary == 0:
        ui.CashPaidLabel = QtWidgets.QLabel(btn[2])
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(10)
        ui.CashPaidLabel.setFont(font)
        ui.CashPaidLabel.setObjectName("CashPaidLabel")
        layout.addWidget(ui.CashPaidLabel)
        ui.CashPaidLabel.setText("Pending")
        current_balance = get_balance(username)[0]
        new_balance = current_balance - debt_amount
        if new_balance >= 0:
            update_balance(username, new_balance)
            add_notification(creditor, username, debt_id, debt_amount)
            update_debt_status(debt_id,"pending")
        else:
            ui.CashPaidLabel.setText("You don't have enough Money!")




    



