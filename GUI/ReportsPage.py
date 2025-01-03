from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import re
import sys
import os
import json
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))

import matplotlib.pyplot as plt
from db_operations import *



def show_total_expenses(username, ui):
    all_expenses = total_expenses_of_user(username)
    ui.label_24.setText(f"Total Expenses: {cal_total_expense(all_expenses)}")
    group_expenses = total_expenses_of(all_expenses, "group")
    ui.label_25.setText(f"Total Expenses in groups: {group_expenses}")
    friend_expenses = total_expenses_of(all_expenses, "friend")
    ui.label_26.setText(f"Total expenses with friends: {friend_expenses}")

    all_owes = total_user_owes(username)
    all_owed = total_user_owed(username)

    owes  =cal_total_owes(all_owes)
    owed = cal_total_owes(all_owed)

    ui.label_28.setText(f"How much you owe: {owes} R ")
    ui.label_29.setText(f"How much you are owed: {owed} R")

def total_expenses_of(expenses, type):
    total_expense = 0
    for expense in expenses:
        if expense[5] == type:
            total_expense += expense[3]
    return total_expense

def cal_total_expense(expenses):
    total_expense = 0
    for expense in expenses:
        total_expense += expense[3]
    return total_expense

def cal_total_owes(owes):
    total_owes = 0
    for owe in owes:
        total_owes += owe[-2]
    return total_owes
