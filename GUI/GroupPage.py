from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date

import sys
import os
import json
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Models"))
from db_operations import *
from groups import *
import sqlite3

def show_all_existing_groups(ui, user):
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
        
        group_id, group_name = group[2:4]
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
        ui.GrpFrame.setStyleSheet("*{\n"
"    background-color: #2c313c;\n"
"    border-radius: 10px\n"
"}")

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
    header = ui.ExpensesTable.horizontalHeader()
    header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    for expense in expenses:
        row_position = ui.ExpensesTable.rowCount()
        ui.ExpensesTable.insertRow(row_position)
        var_to_add = [expense[1], expense[4],str(expense[6]), expense[5], expense[8], expense[7], expense[10], expense[9]]
        for col, value in enumerate(var_to_add):
            ui.ExpensesTable.setItem(row_position, col, QtWidgets.QTableWidgetItem(value))
    
    ui.AddExpensesBtn.clicked.connect(lambda: add_expense_page(ui, grp))

def create_group(ui, user):
    default_shares = None
    default_prop_j = None
    default_shares_j = None
    split=""
    percent_total = True

    
    
    group_name = ui.GrpNameInput.text()
    group_no = ui.NoMembersInput.value()
    members = get_members(ui)
    if members == [""]: members = [] 
    for SplitBtnNo in range(11):
        Split = ui.verticalLayout_30.itemAt(SplitBtnNo).widget()
        if isinstance(Split, QtWidgets.QRadioButton) and Split.isChecked():
            split = Split.text()
    if split != "equally":
        default_shares = get_shares(ui, "add_group")
        if split == "shares":
            default_shares_j = json.dumps(default_shares)
            default_prop_j = None
        else:
            default_prop_j = json.dumps(default_shares)
            default_shares_j = None
    
    if split == "percentage":
        if sum(default_shares.values()) != 100:
            percent_total = False
    if group_name != "" and group_no != 0 and members != [] and split !="" and int(group_no) == len(members) and percent_total:
        add_group_to_dataset(group_name, user, members, split, default_shares_j, default_prop_j)
        ui.GrpNameInput.setText("")
        ui.NoMembersInput.setValue(0)
        ui.GrpMembersInput.setText("")
        for SplitBtnNo in range(11):
            Split = ui.verticalLayout_30.itemAt(SplitBtnNo).widget()
            if isinstance(Split, QtWidgets.QRadioButton) and Split.isChecked():
                Split.setChecked(False)
        add_shares(ui, "equally", "add_group")
        
        ui.rightMenuContainer.collapseMenu()
        show_all_existing_groups(ui, user)
    widgets = [ui.GrpNameLabel, ui.NoMembersLabel, ui.GrpMembersLabel, ui.DefaultSplitLabel]
    for widget, data in enumerate([group_name, group_no, members, split]):
        if data == "" or data == [""] or not data:
            widgets[widget].setStyleSheet("color: red;")
            ui.ErrorLabel.setText("Fill out all inforamtion!")
            ui.ErrorLabel.setStyleSheet("color : red;")

        else:
            widgets[widget].setStyleSheet("color: white;")
            ui.ErrorLabel.setText("")

    if group_no != "" and group_no != len(members):
        print(group_no, members, len(members), len(members) == group_no)
        widgets[1].setStyleSheet("color: red;")
        widgets[2].setStyleSheet("color: red;")
        ui.ErrorLabel.setText("Number of Members does't match the list of their user name!")
        ui.ErrorLabel.setStyleSheet("color : red;")

    else:
        widgets[1].setStyleSheet("color: white;")
        widgets[2].setStyleSheet("color: white;")
        ui.ErrorLabel.setText("")
    
    if split == "percentage":
        if not percent_total:
            ui.ErrorLabel.setText("Enter correct percentages!")
            ui.ErrorLabel.setStyleSheet("color : red;")
            ui.label.setStyleSheet("color: red;")
        else:
            ui.ErrorLabel.setText("")
            ui.ErrorLabel.setStyleSheet("color : white;")
            ui.label.setStyleSheet("color: white;")


def add_group_to_dataset(group_name, user, members, split, default_shares_j, default_prop_j):
    connection=get_connection()
    cursor=connection.cursor()
    group = Groups(group_name, user[2], split)
    cursor.execute("SELECT group_id FROM groups WHERE group_name = ? and group_owner = ?", (group_name, user[2], ))
    connection.commit()
    new_group = cursor.fetchone()
    cursor.execute("INSERT INTO user_group (user_id, username, group_id, group_name, default_split, default_shares, default_proportions) VALUES (?, ?, ?, ?, ?, ?, ?)", (user[0], user[2], new_group[0], group_name, split, default_shares_j, default_prop_j)) 
    connection.commit()   
    for member in members:
        if member == user[2]:
            continue
        group.add_members(member)
    connection.commit()
    connection.close()

    

def add_expense_page(ui, group, recover = True):
    if recover:
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
    category = ""
    label = ui.GrpExpenseLabelInput.text()
    print(label)
    amount = ui.AmountInput.text()
    selected_date = ui.calendarWidget.selectedDate().toString("yyyy-dd-mm")
    payer = ui.PayerInput.text()
    description = ui.DiscriptionInput.toPlainText()
    split_type = "equally"
    default = False

    contributers = get_contributers(ui)



    for categoryBtnNo in range(6):
        categoryBtn = ui.gridLayout_2.itemAt(categoryBtnNo).widget()
        if categoryBtn.isChecked():
              category = categoryBtn.text()
    if category == "":
         category = "etc."


    for SplitTypeNo in range(4):
        SplitTypeBtn = ui.verticalLayout_22.itemAt(SplitTypeNo).widget()
        if SplitTypeBtn.isChecked():
            split_type = SplitTypeBtn.text()

    if split_type == "share" or split_type == "percentage":
            shares = get_shares(ui, "add_expense")
            print("COUNT", ui.verticalLayout_25.count())

    if split_type == "default split":
        default = True
        defaults = get_default_split(main_group.group_id, main_group.group_name)
        default_split = defaults[-3]
        default_shares = defaults[-1]
        default_proportions = defaults[-2]
        if default_shares:
            default_shares = json.loads(default_shares)
        if  default_proportions:
            default_proportions = json.loads(default_proportions)
        split_type = default_split
        if split_type == "share":
            shares = default_shares
        elif split_type == "percentage":
            shares = default_proportions
    
        
    def total_perc(split_type):
        if split_type == "percentage":
            if  default == False:
                shares = get_shares(ui, "add_expense")
            else:
                shares = default_proportions
            if sum(shares.values()) != 100:
                print("No")
                print(shares.values())
                return False
        return True
        

    if label != "" and amount != "" and selected_date != "" and isfloat(amount) and contributers != [] and payer != ""  and payer in main_group.members and total_perc(split_type):
        if split_type == "share":
            shares = shares
            main_group.add_expenses(label, amount, payer, contributers, selected_date, category,description, split_type, shares=shares)
        elif split_type == "percentage":
            proportions = shares
            main_group.add_expenses(label, amount, payer, contributers, selected_date, category,description, split_type, proportions=proportions)
        else:
            main_group.add_expenses(label,amount, payer, contributers, selected_date, category,description, split_type)
        var_to_add = [label, payer, str(amount),",".join(contributers), selected_date, category, split_type, description]
        row_position = ui.ExpensesTable.rowCount()
        ui.ExpensesTable.insertRow(row_position)
        for col, value in enumerate(var_to_add):
            ui.ExpensesTable.setItem(row_position, col, QtWidgets.QTableWidgetItem(value))

        ui.GrpExpenseLabelInput.setText("")
        ui.AmountInput.setText("")
        ui.PayerInput.setText("")
        ui.DiscriptionInput.setText("")
        split_type = "equally"
        add_shares(ui, split_type, "add_expense")
        for SplitTypeNo in range(4):
            ui.verticalLayout_22.itemAt(SplitTypeNo).widget().setChecked(False)
        layout = ui.scrollAreaWidgetContents_7.layout()
        for i in range(layout.count()):
            layout.itemAt(i).widget().setChecked(False)
        for categoryBtnNo in range(6):
            ui.gridLayout_2.itemAt(categoryBtnNo).widget().setChecked(False)
        ui.GrpTotalExpense.setText(f"Total Expense: {main_group.get_total_expenses_of_group()[0]}")
        
        ui.rightMenuContainer.collapseMenu()
        


    widgets = [ui.GrpExpenseLabelLabel, ui.AmountLabel, ui.PayerLabel, ui.ContributersLabel]

    error = 0
    print([label, amount, payer, contributers], amount == "")
    
    for widget, data in enumerate([label, amount, payer, contributers]):
        if data == "" or data == [] or not data:
            widgets[widget].setStyleSheet("color: red;")
            ui.ErrorLabel2.setText("Fill out all required inforamtion!")
            ui.ErrorLabel2.setStyleSheet("color : red;")
            error = 1
    

        else:
            widgets[widget].setStyleSheet("color: white;")
            ui.ErrorLabel2.setText("")
            error = 0

    if payer not in main_group.members:
        widgets[1].setStyleSheet("color: red;")
        widgets[2].setStyleSheet("color: red;")
        if error == 0:
            ui.ErrorLabel2.setText("Payer is not in the group!")
            ui.ErrorLabel2.setStyleSheet("color : red;")
            error = 2

    else:
        error = 0
        widgets[1].setStyleSheet("color: white;")
        widgets[2].setStyleSheet("color: white;")
        ui.ErrorLabel2.setText("")

    
    
    if split_type == "percentage":
        if not total_perc(split_type):
            ui.label.setStyleSheet("color: red;")
            if error == 0:
                ui.ErrorLabel2.setText("Enter correct percentages!")
                ui.ErrorLabel2.setStyleSheet("color : red;")
                
                error =3
        else:
            ui.ErrorLabel2.setText("")
            ui.ErrorLabel2.setStyleSheet("color : white;")
            ui.label.setStyleSheet("color: white;")
            error = 0


    

def add_shares(ui, split_type, page):
    if page=="add_expense":
        layout = ui.scrollAreaWidgetContents_9.layout()
        print(layout == ui.verticalLayout_25)
    else:
        layout = ui.scrollAreaWidgetContents_10.layout()
        print(layout == ui.verticalLayout_27)
    while layout.count():
        item = layout.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        widget.deleteLater()
    if split_type != "equally":
        if page=="add_expense":
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
                ui.spinBox.setValue(0)
                ui.verticalLayout_25.addWidget(ui.spinBox)
        if page =="add_group":
            members = get_members(ui)
            ui.label = QtWidgets.QLabel(ui.scrollAreaWidgetContents_10)
            font = QtGui.QFont()
            font.setFamily("Swis721 Blk BT")
            font.setPointSize(10)
            ui.label.setFont(font)
            ui.label.setObjectName("label")
            ui.verticalLayout_27.addWidget(ui.label)
            ui.label.setText(f"{split_type}s:")
            for member in members:
                ui.label_9 = QtWidgets.QLabel(ui.scrollAreaWidgetContents_10)
                ui.label_9.setObjectName("label_9")
                ui.verticalLayout_27.addWidget(ui.label_9)
                ui.label_9.setText(member)
                font = QtGui.QFont()
                font.setFamily("Swis721 Blk BT")
                font.setPointSize(8)
                ui.label_9.setFont(font)
                ui.spinBox = QtWidgets.QSpinBox(ui.scrollAreaWidgetContents_10)
                ui.spinBox.setObjectName("spinBox")
                font = QtGui.QFont()
                font.setFamily("Swis721 Blk BT")
                font.setPointSize(8)
                ui.spinBox.setFont(font)
                ui.spinBox.setValue(0)
                ui.verticalLayout_27.addWidget(ui.spinBox)

        print(layout.count())


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

def get_members(ui):
    members = ui.GrpMembersInput.toPlainText().split("\n")
    if members == [""]: members =[]
    return members


def get_shares(ui, page):
    shares = dict()
    if page == "add_expense":
        layout = ui.scrollAreaWidgetContents_9.layout()
    elif page == "add_group":
        layout = ui.scrollAreaWidgetContents_10.layout()
    
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

    print(shares)
    return shares

def take_group(ui):
    group = Groups(ui.GrpName.text(), ui.grp_owner.text())
    return group

