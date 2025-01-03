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
    user = get_user_by_email (username, username)
    all_expenses = total_expenses_of_user(username)
    ui.label_24.setText(f"Total Expenses: {cal_total_expense(all_expenses)}")
    group_expenses = total_expenses_of(all_expenses, "group")
    ui.label_25.setText(f"Total Expenses in groups: {group_expenses}")
    friend_expenses = total_expenses_of(all_expenses, "friend")
    ui.label_26.setText(f"Total expenses with friends: {friend_expenses}")

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

