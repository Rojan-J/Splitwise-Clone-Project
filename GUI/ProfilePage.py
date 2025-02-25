from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os

from datetime import datetime
# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database"))

sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))


from db_operations import *
from db_operations import get_user_by_email


def set_user(ui, username):
    user = get_user_by_email(username, username)
    ui.NameProfile.setText(user[1])
    ui.UsernameProfile.setText(user[2])
    ui.EmailProfile.setText(user[3])
    ui.BalanceProfile.setText(str(user[-2]))
    if user[-3] == 0:
        profile = QtGui.QIcon(":/images/3135823.png")
        ui.PicProfile.setIcon(profile)

    else:
        profile = QtGui.QIcon(":/images/Layer 1.png")
        ui.PicProfile.setIcon(profile)
        ui.PicProfile.setIconSize(QtCore.QSize(90, 90))
    
    header = ui.tableWidget_2.horizontalHeader()
    header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    recurrents = get_recurrent_expense_by_username(user[2])
    ui.tableWidget_2.setRowCount(0)
    for expense in recurrents:
        row_position = ui.tableWidget_2.rowCount()
        ui.tableWidget_2.insertRow(row_position)
        var_to_add = [expense[2], str(expense[-3]), expense[4], expense[-4], expense[-2]]
        for col, value in enumerate(var_to_add):
            ui.tableWidget_2.setItem(row_position, col, QtWidgets.QTableWidgetItem(value))

    notifications =  get_user_notifications(username)
    if not notifications:
        
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons2/icons2/bell.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.NotificationBtn.setIcon(icon7)
        ui.NotificationBtn.setIconSize(QtCore.QSize(24, 24))
    else:
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons2/icons2/inbox.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.NotificationBtn.setIcon(icon7)
        ui.NotificationBtn.setIconSize(QtCore.QSize(24, 24))




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

def isfloat(value):
    try:
        float(value)  
        return True
    except:  
        return False

def add_recurrent(ui, user):
    category = ""
    username = user[2]
    user_id = user[0]
    label = ui.LabelInput.text()
    amount = ui.AmountRExpenseInput.text()
    days = []
    for day in range(31):
        dayCheck = ui.gridLayout_16.itemAt(day).widget()
        if dayCheck.isChecked():
            days.append(dayCheck.text())
    days = ",".join(days)
    for categoryBtnNo in range(6):
        categoryBtn = ui.gridLayout_17.itemAt(categoryBtnNo).widget()
        if categoryBtn.isChecked():
              category = categoryBtn.text()
    if category == "":
         category = "etc."
    if label != "" and amount != "" and days != "" and isfloat(amount) :
        add_recurrent_expense(username, user_id, label, amount, days, category)
        var_to_add = [label, str(amount), days, str(datetime.now().month), category]
        row_position = ui.tableWidget_2.rowCount()
        ui.tableWidget_2.insertRow(row_position)
        for col, value in enumerate(var_to_add):
            print(col, value)
            ui.tableWidget_2.setItem(row_position, col, QtWidgets.QTableWidgetItem(value))

        ui.LabelInput.setText("")
        ui.AmountRExpenseInput.setText("")
        for day in range(31):
            ui.gridLayout_16.itemAt(day).widget().setChecked(False)
        
        for categoryBtnNo in range(6):
            ui.gridLayout_17.itemAt(categoryBtnNo).widget().setChecked(False)

        ui.rightMenuContainer.collapseMenu()
    widgets = [ui.LabelLabel, ui.AmountRExpenseLabel, ui.DaysLabel, ui.CategoryLabel_5]
    for widget, data in enumerate([label, amount, days, category]):
        if data == "":
            widgets[widget].setStyleSheet("color: red;")
        else:
            widgets[widget].setStyleSheet("color: white;")
    if not isfloat(amount):
        widgets[1].setStyleSheet("color: red;")
    else:
        widgets[1].setStyleSheet("color: white;")



def process_recurring_expenses(username):
    connection = get_connection()
    cursor = connection.cursor()
    
    # Get today's day
    today_day = datetime.now().day
    
    # Fetch all recurring expenses
    cursor.execute("SELECT label, expense_id, amount, category, days_of_month, month, paid FROM recurrent_expenses WHERE username=  ?", (username, ))
    recurring_expenses = cursor.fetchall()
    current_year = datetime.now().year
    current_month = datetime.now().month
    if recurring_expenses:
        month = recurring_expenses[0][-2]
        if month != current_month:
            update_month_of_recurrent()
    
    
    cursor.execute("SELECT label, expense_id, amount, category, days_of_month, month, paid FROM recurrent_expenses WHERE username=  ?", (username, ))
    recurring_expenses = cursor.fetchall()

    for expense in recurring_expenses:
        label, expense_id, amount, category, days_of_month, month, paid = expense
        days_list = [int(day) for day in days_of_month.split(",")]

        cursor.execute("SELECT * FROM simplified_debts WHERE id=  ?", (expense_id, ))
        duplicated_expense = cursor.fetchall()
        print("PAID", paid)
        



        if paid == "Not Paid!" :
            
            # Check if today is a recurring day
            if today_day in days_list and not duplicated_expense:
                # Insert expense into the debts or expenses table
                cursor.execute("""
                    INSERT INTO simplified_debts (for_what, id, name, debtor_name, amount)
                    VALUES ("recurrent", ?, ?, ?, ?)
                """, (expense_id, label, username, amount))
                

                # Combine year, month, and day to create a complete date
                complete_date = datetime(current_year, current_month, today_day)

                cursor.execute("""
                    INSERT INTO expense_user (total_expense, username, amount_contributed, split_proportion, for_what, name, date, category)
                    VALUES (?, ?, ?, ?, "recurrent", ?, ?, ?) 
                """, (amount, username, amount, 1, label, complete_date, category, ))
    
    connection.commit()
    connection.close()





#def draw_recurrent_table(ui, user)