from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date

import sys
import os
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Models"))
from db_operations import *
from groups import *
import sqlite3

def show_all_existing_groups(ui, user, grpbtns):
    groups = get_groups_by_username(user[2])
    grpbtns = dict()
    GroupsBox = dict()
    GroupGroups = dict()
    while ui.verticalLayout_20.count():
        item = ui.verticalLayout_20.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        if widget:
            widget.deleteLater()
    for  group in groups:
        
        group_id, group_name = group[2:]
        connection=get_connection()
        cursor=connection.cursor()
        cursor.execute("SELECT group_owner FROM groups WHERE group_name = ? and group_id = ?", (group_name, group_id, ))
        group_owners = cursor.fetchone()
        group_owner = group_owners[0]
        group_grp = Groups(group_name, group_owner)
        GroupGroups[group_name] = group_grp

        ui.GrpFrame = QtWidgets.QFrame(ui.GroupsGrid)
        ui.GrpFrame.setEnabled(True)
        ui.GrpFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ui.GrpFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        ui.GrpFrame.setObjectName(f"{group_name}Frame")
        ui.verticalLayout_100 = QtWidgets.QVBoxLayout(ui.GrpFrame)
        ui.verticalLayout_100.setObjectName("verticalLayout_100")

        ui.namelabel = QtWidgets.QLabel(ui.GrpFrame)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(18)
        ui.namelabel.setFont(font)
        ui.namelabel.setObjectName("namelabel")
        ui.namelabel.setText(f"{group_name}")
        ui.verticalLayout_100.addWidget(ui.namelabel)

        ui.expenselabel = QtWidgets.QLabel(ui.GrpFrame)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(13)
        ui.expenselabel.setFont(font)
        ui.expenselabel.setObjectName("expenselabel")
        ui.expenselabel.setText(f"Total expense: {group_grp.get_total_expenses_of_group()[0]}")
        ui.verticalLayout_100.addWidget(ui.expenselabel)

        ui.GrpBtn = QtWidgets.QPushButton(ui.GrpFrame)
        ui.GrpBtn.setText("")
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/icons2/icons2/log-in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ui.GrpBtn.setIcon(icon23)
        ui.GrpBtn.setIconSize(QtCore.QSize(32, 32))
        ui.GrpBtn.setObjectName(f"{group_name}")
        ui.verticalLayout_100.addWidget(ui.GrpBtn, 0, QtCore.Qt.AlignRight)
        grpbtns[group_grp] = ui.GrpBtn

        ui.verticalLayout_20.addWidget(ui.GrpFrame)

    for group, btn in grpbtns.items():
        btn.clicked.connect(lambda _, g=group: specific_group_page(ui, g))




def specific_group_page(ui,grp : Groups):
    ui.mainPages.setCurrentWidget(ui.GrpPage)
    ui.GrpName.setText(grp.group_name)
    ui.grp_owner.setText(f"Owner: {grp.group_owner}")
    ui.GrpTotalExpense.setText(f"Total Expense: {grp.get_total_expenses_of_group()[0]}")
    expenses = get_expenses_of_grp_by_grp_id(grp.group_id)
    print(grp.members)

    header = ui.ExpensesTable.horizontalHeader()
    header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    for expense in expenses:
        row_position = ui.ExpensesTable.rowCount()
        ui.ExpensesTable.insertRow(row_position)
        var_to_add = [str(expense[5]), expense[3], expense[4], str(expense[7]), expense[6], expense[9], expense[8]]
        for col, value in enumerate(var_to_add):
            ui.ExpensesTable.setItem(row_position, col, QtWidgets.QTableWidgetItem(value))
    
    ui.AddExpensesBtn.clicked.connect(lambda: add_expense_page(ui, grp))

def create_group(ui, user):
    connection=get_connection()
    cursor=connection.cursor()
    
    
    group_name = ui.GrpNameInput.text()
    group_no = ui.NoMembersInput.value()
    members = ui.GrpMembersInput.toPlainText().split("\n")
    for SplitBtnNo in range(11):
        Split = ui.verticalLayout_30.itemAt(SplitBtnNo).widget()
        if isinstance(Split, QtWidgets.QRadioButton) and Split.isChecked():
            split = Split.text()


    group = Groups(group_name, user[2], split)
    cursor.execute("SELECT group_id FROM groups WHERE group_name = ? and group_owner = ?", (group_name, user[2], ))
    new_group = cursor.fetchone()
    cursor.execute("INSERT INTO user_group (user_id, username, group_id, group_name) VALUES (?, ?, ?, ?)", (user[0], user[2], new_group[0], group_name))    
    for member in members:
        group.add_members(member)
    connection.commit()
    connection.close()   

def add_expense_page(ui, group, recover = True):
    print("CALLED")
    if recover:
        print("CAlled")
        layout = ui.scrollAreaWidgetContents_7.layout()
        # Iterate through the layout's items
        while layout.count():
            item = layout.takeAt(0)  # Remove the first item in the layout
            widget = item.widget()
            widget.deleteLater()

        for member in group.members:
            ui.checkBox_2 = QtWidgets.QCheckBox(ui.scrollAreaWidgetContents_7)
            ui.checkBox_2.setObjectName(member)
            ui.checkBox_2.setText(member)
            ui.verticalLayout_23.addWidget(ui.checkBox_2)

        layout = ui.scrollAreaWidgetContents_9.layout()
        # Iterate through the layout's items
        while layout.count():
            item = layout.takeAt(0)  # Remove the first item in the layout
            widget = item.widget()
            widget.deleteLater()


    ui.FinalAddExpenseBtn.clicked.connect(lambda: add_group_expense(ui, group))
    



def add_group_expense(ui, main_group):
    print("YES")
    category = ""
    label = ui.GrpExpenseLabelInput.text()
    amount = ui.AmountInput.text()
    selected_date = ui.calendarWidget.selectedDate()
    payer = ui.PayerInput.text()
    description = ui.DiscriptionInput.toPlainText()
    split_type = "equally"

    contributers = get_contributers(ui)

    print(contributers)

    for categoryBtnNo in range(6):
        categoryBtn = ui.gridLayout_2.itemAt(categoryBtnNo).widget()
        if categoryBtn.isChecked():
              category = categoryBtn.text()
    if category == "":
         category = "etc."

    print(category)

    for SplitTypeNo in range(4):
        SplitTypeBtn = ui.verticalLayout_22.itemAt(SplitTypeNo).widget()
        if SplitTypeBtn.isChecked():
            split_type = SplitTypeBtn.text()

    print(split_type)
    print(label, amount, selected_date, contributers, payer)
    print(label == "" , amount == "" , selected_date == "" , isfloat(amount), contributers == [] , payer != "")

    if label != "" and amount != "" and selected_date != "" and isfloat(amount) and contributers != [] and payer != "" :
        if split_type == "share":
            
            shares = get_shares(ui)
            print(shares)
            main_group.add_expenses(amount, payer, contributers, selected_date, category,description, split_type, shares=shares)
        elif split_type == "percentage":
            proportions = get_shares(ui)
            main_group.add_expenses(amount, payer, contributers, selected_date, category,description, split_type, proportions=proportions)
        else:
            main_group.add_expenses(amount, payer, contributers, selected_date, category,description, split_type)
        var_to_add = [str(amount), payer,",".join(contributers), selected_date.toString(), category, split_type, description]
        row_position = ui.ExpensesTable.rowCount()
        ui.ExpensesTable.insertRow(row_position)
        for col, value in enumerate(var_to_add):
            ui.ExpensesTable.setItem(row_position, col, QtWidgets.QTableWidgetItem(value))

def add_shares(ui, split_type, group):
    contributers= get_contributers(ui)
    ui.label = QtWidgets.QLabel(ui.scrollAreaWidgetContents_9)
    font = QtGui.QFont()
    font.setFamily("Swis721 Blk BT")
    font.setPointSize(10)
    ui.label.setFont(font)
    ui.label.setObjectName("label")
    ui.verticalLayout_25.addWidget(ui.label)
    ui.label.setText(f"{split_type}s:")
    for contributer in contributers:
        ui.label_9 = QtWidgets.QLabel(ui.scrollAreaWidgetContents_9)
        ui.label_9.setObjectName("label_9")
        ui.verticalLayout_25.addWidget(ui.label_9)
        ui.label_9.setText(contributer)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(8)
        ui.label_9.setFont(font)
        ui.spinBox = QtWidgets.QSpinBox(ui.scrollAreaWidgetContents_9)
        ui.spinBox.setObjectName("spinBox")
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(8)
        ui.spinBox.setFont(font)
        ui.verticalLayout_25.addWidget(ui.spinBox)

def isfloat(value):
    try:
        float(value)  
        return True
    except:  
        return False
    
def get_contributers(ui):
    contributers = []
    layout = ui.scrollAreaWidgetContents_7.layout()
    for i in range(layout.count()):
        item = layout.itemAt(i)  # Remove the first item in the layout
        widget = item.widget()
        if widget.isChecked():
            contributer = widget.text()
            contributers.append(contributer)
    return contributers

def get_shares(ui):
    shares = dict()
    layout = ui.scrollAreaWidgetContents_9.layout()
    i= 1
    while i != layout.count():
        label_item = layout.itemAt(i)
        share_item = layout.itemAt(i + 1)
        label_widget = label_item.widget()
        share_widget = share_item.widget()
        label = label_widget.text()
        share = share_widget.value()
        shares[label] = share
        i += 2
    return shares

def take_group(ui):
    group = Groups(ui.GrpName.text(), ui.grp_owner.text())
    return group

