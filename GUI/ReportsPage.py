from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import re
import sys
import os
import json
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
#sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database"))


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

    monthly_report = cal_month_expenses(username)
    ui.label_27.setText(f"Total expenses in this month: {monthly_report}")

    ui.ReportBtn.clicked.connect(lambda: show_report(username, ui))

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


def get_expenses_report_group_by(username, group_by, start_date = None, end_date = None):
        
        grouped_expenses={}
        connection=get_connection()
        cursor=connection.cursor()
        

        if start_date and end_date:
            cursor.execute("""
            SELECT name, SUM(amount_contributed)
            FROM expense_user
            WHERE username = ? AND for_what= ? AND date BETWEEN ? AND ?
            GROUP BY name
        """, (username, group_by, start_date, end_date, ))
        
            expense_by_group=cursor.fetchall()
            
            for group, total_amount in expense_by_group:
                grouped_expenses[group] = total_amount
        
        else:
            cursor.execute("""
                SELECT name, SUM(amount_contributed)
                FROM expense_user
                WHERE username = ? AND for_what=  ?  
                GROUP BY name
            """, (username, group_by, ))
            
            expense_by_group=cursor.fetchall()
            
            for group, total_amount in expense_by_group:
                grouped_expenses[group] = total_amount
        
        
        connection.close()
        return grouped_expenses


def get_expenses_by_category_report(username, start_date =None, end_date= None):
        
    category_expenses={}
    connection=get_connection()
    cursor=connection.cursor()
    
    if start_date and end_date:
        cursor.execute("""
            SELECT category, SUM(amount_contributed)
            FROM expense_user
            WHERE username = ? AND date BETWEEN ? AND ?
            GROUP BY category
        """, (username, start_date, end_date, ))
        
        expense_by_category=cursor.fetchall()

        for category, total_amount in expense_by_category:
            category_expenses[category] = total_amount

    else:
        cursor.execute("""
            SELECT category, SUM(amount_contributed)
            FROM expense_user
            WHERE username = ?
            GROUP BY category
        """, (username,))
        
        expense_by_category=cursor.fetchall()
        
        for category, total_amount in expense_by_category:
            category_expenses[category] = total_amount
    
    
    connection.close()
    return category_expenses


def clear_dates(ui):
    layout = ui.frame_39.layout()
    while layout.count():
        item = layout.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        widget.deleteLater()

def add_custom_time_duration(ui):
    ui.frame_40 = QtWidgets.QFrame(ui.frame_39)
    ui.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
    ui.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
    ui.frame_40.setObjectName("frame_40")
    ui.horizontalLayout_48 = QtWidgets.QHBoxLayout(ui.frame_40)
    ui.horizontalLayout_48.setSpacing(30)
    ui.horizontalLayout_48.setObjectName("horizontalLayout_48")
    ui.label_33 = QtWidgets.QLabel(ui.frame_40)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(ui.label_33.sizePolicy().hasHeightForWidth())
    ui.label_33.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setFamily("Swis721 Blk BT")
    font.setPointSize(10)
    ui.label_33.setFont(font)
    ui.label_33.setObjectName("label_33")
    ui.label_33.setText("From:")
    ui.horizontalLayout_48.addWidget(ui.label_33, 0, QtCore.Qt.AlignHCenter)
    ui.label_34 = QtWidgets.QLabel(ui.frame_40)
    font = QtGui.QFont()
    font.setFamily("Swis721 Blk BT")
    font.setPointSize(10)
    ui.label_34.setFont(font)
    ui.label_34.setObjectName("label_34")
    ui.label_34.setText("To:")
    ui.horizontalLayout_48.addWidget(ui.label_34, 0, QtCore.Qt.AlignHCenter)
    ui.verticalLayout_69.addWidget(ui.frame_40)
    ui.frame_41 = QtWidgets.QFrame(ui.frame_39)
    ui.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
    ui.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
    ui.frame_41.setObjectName("frame_41")
    ui.horizontalLayout_49 = QtWidgets.QHBoxLayout(ui.frame_41)
    ui.horizontalLayout_49.setSpacing(30)
    ui.horizontalLayout_49.setObjectName("horizontalLayout_49")
    ui.dateEdit = QtWidgets.QDateEdit(ui.frame_41)
    font = QtGui.QFont()
    font.setFamily("Swis721 BlkEx BT")
    font.setPointSize(10)
    font.setBold(False)
    font.setUnderline(False)
    font.setWeight(50)
    ui.dateEdit.setFont(font)
    ui.dateEdit.setObjectName("dateEdit")
    ui.horizontalLayout_49.addWidget(ui.dateEdit, 0, QtCore.Qt.AlignHCenter)
    ui.dateEdit_2 = QtWidgets.QDateEdit(ui.frame_41)
    font = QtGui.QFont()
    font.setFamily("Swis721 BlkEx BT")
    font.setPointSize(10)
    font.setBold(False)
    font.setWeight(50)
    ui.dateEdit_2.setFont(font)
    ui.dateEdit_2.setObjectName("dateEdit_2")
    ui.horizontalLayout_49.addWidget(ui.dateEdit_2, 0, QtCore.Qt.AlignHCenter)
    ui.verticalLayout_69.addWidget(ui.frame_41)
    ui.verticalLayout_68.addWidget(ui.frame_39)


def get_dates(ui):
    start_date = ui.dateEdit.date().toString("yyyy-dd-MM")
    end_date = ui.dateEdit_2.date().toString("yyyy-dd-MM")
    error_date = False

    if start_date > end_date:
        error_date = True

    return error_date, start_date, end_date


def cal_month_expenses(username):
    # Connect to your database
    connection = get_connection()
    cursor = connection.cursor()

    # Get current year and month
    current_year = datetime.now().year
    current_month = datetime.now().month

    # SQL query to sum the amount column for the current month and year
    cursor.execute( """
        SELECT SUM(amount_contributed)
        FROM expense_user
        WHERE substr(date, 1, 4) = ? AND substr(date, 9, 2) = ? AND username= ?
    """, (str(current_year), f"{current_month:02d}", username, ))

    total_amount = cursor.fetchone()[0]
    if total_amount is None:
        total_amount = 0
    
    connection.close()
    return total_amount

def show_report(username, ui):
    category_expenses = dict()
    group_expenses = dict()
    friend_expenses = dict()
    if ui.MonthlyReportBtn.isChecked():
        error_date, start_date, end_date = get_dates(ui)
        if not error_date:
            ui.ErrorLabelCustomTime.setText("")
            if ui.CategoryReportBtn.isChecked():
                category_expenses = get_expenses_by_category_report(username, start_date, end_date)

            elif ui.GrpReportBtn.isChecked():
                group_expenses = get_expenses_report_group_by(username, "group", start_date, end_date)

            elif ui.FriendReportBtn.isChecked():
                friend_expenses = get_expenses_report_group_by(username, "friend", start_date, end_date)
        else:
            ui.ErrorLabelCustomTime.setText("Enter correct time duration!")
            ui.ErrorLabelCustomTime.setStyleSheet("color: red;")
    elif ui.TotalReportBtn.isChecked():
        if ui.CategoryReportBtn.isChecked():
            category_expenses = get_expenses_by_category_report(username)

        elif ui.GrpReportBtn.isChecked():
            group_expenses = get_expenses_report_group_by(username, "group")

        elif ui.FriendReportBtn.isChecked():
            friend_expenses = get_expenses_report_group_by(username, "friend")

    if category_expenses:
        categories = list(category_expenses.keys())
        amounts = list(category_expenses.values())

        legend  = [f"{label} ({size :.1f} R)" for label, size in zip(categories, amounts)]



        def autopct_amount(pct, values):
            total = sum(values)
            amount = int(round(pct * total / 100.0))
            return f"{amount} R"
        # Create the pie chart
        plt.figure(figsize=(8, 6))  # Set figure size
        plt.pie(
            amounts, 
            startangle=90,      
            colors=plt.cm.Paired.colors,  
        )
        plt.legend(legend, title="Categories", loc="lower center", bbox_to_anchor=(1, 0.5))
        

        png_path = "C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Core/graph_pie_plot.png"
        #png_path = r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Core\graph_pie_plot.png"


        
        # Save as PNG
        plt.savefig(png_path)

        layout = ui.scrollAreaWidgetContents_25.layout()
        while layout.count():
            item = layout.takeAt(0)  # Get the first item
            widget = item.widget()  # Get the widget
            widget.deleteLater()
        
        ui.graph = QtWidgets.QLabel(ui.scrollAreaWidgetContents_25)
        pixmap = QtGui.QPixmap(png_path)
        ui.graph.setPixmap(pixmap)
        ui.graph.setScaledContents(True)  # Scale the image to fit the frame

        # Set a layout for the frame and add the label
        layout.setContentsMargins(0, 0, 0, 0)  # Optional: Remove margins
        layout.addWidget(ui.graph)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        
        ui.pushButton.setText("")
        ui.label_35.setText("Expenses Distribution in each category")
        ui.label_35.setFont(font)

    
    elif group_expenses or friend_expenses:
        if group_expenses:
            groupby_expense = group_expenses
            x_title = "Groups"
            png_path = "C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Core/graph_group_by_plot_group.png"
            #png_path = r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Core\graph_group_by_plot_group.png"
        elif friend_expenses:
            groupby_expense = friend_expenses
            x_title = "Friends"
            png_path = "C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Core/graph_group_by_plot_friend.png"
            #png_path = r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Core\graph_group_by_plot_friend.png"

        categories = list(groupby_expense.keys())
        amounts = list(groupby_expense.values())


        plt.figure(figsize=(8, 6)) 
        plt.bar(categories, amounts, color='skyblue')

        plt.xlabel(x_title)
        plt.ylabel('Amount')

        for i, amount in enumerate(amounts):
            plt.text(i, amount + 5, str(amount), ha='center', va='bottom')

        
        
        # Save as PNG
        plt.savefig(png_path)

        layout = ui.scrollAreaWidgetContents_25.layout()
        while layout.count():
            item = layout.takeAt(0)  # Get the first item
            widget = item.widget()  # Get the widget
            widget.deleteLater()
        
        ui.graph = QtWidgets.QLabel(ui.scrollAreaWidgetContents_25)
        pixmap = QtGui.QPixmap(png_path)
        ui.graph.setPixmap(pixmap)
        ui.graph.setScaledContents(True)  # Scale the image to fit the frame

        # Set a layout for the frame and add the label
        layout.setContentsMargins(0, 0, 0, 0)  # Optional: Remove margins
        layout.addWidget(ui.graph)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        
        ui.pushButton.setText("")
        ui.label_35.setText(f"Expenses Distribution in each {x_title}")
        ui.label_35.setFont(font)

        

