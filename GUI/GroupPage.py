from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QFileDialog , QTableWidgetItem


import sys
import os
import json

sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Models"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Core"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database/transaction import"))


# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database"))
# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Models"))
# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Core"))
# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Utils"))
# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database\transaction import"))


from db_operations import *
from groups import *
import sqlite3
from graph import *
from debt_simplification import *
from currency_conversion_all_currencies import *
from group_transaction_import import import_from_excel



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
        group_grp = Groups(group_name, group_owner, debts = dict(), members = [], expenses = [])
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
    ui.ExpensesTable.setRowCount(0)
    header = ui.ExpensesTable.horizontalHeader()
    header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
    for expense in expenses:
        row_position = ui.ExpensesTable.rowCount()
        ui.ExpensesTable.insertRow(row_position)
        var_to_add = [expense[1], expense[4],str(expense[6]), expense[5], expense[8], expense[7], expense[10], expense[9]]
        for col, value in enumerate(var_to_add):
            ui.ExpensesTable.setItem(row_position, col, QtWidgets.QTableWidgetItem(value))



    safe_disconnect(ui.AddExpensesBtn, lambda: add_expense_page(ui, grp))
    safe_disconnect(ui.DebtGraphBtn, lambda: show_graph(grp, ui))
    safe_disconnect(ui.closeGraphBtn, lambda: clear_graph(ui))
    safe_disconnect(ui.ExpenseGraphBtn, lambda: show_expenses_graph(grp, ui))

    # Reconnect buttons for the new group
    ui.AddExpensesBtn.clicked.connect(lambda: add_expense_page(ui, grp))
    ui.DebtGraphBtn.clicked.connect(lambda: show_graph(grp, ui))
    ui.closeGraphBtn.clicked.connect(lambda: clear_graph(ui))
    ui.ExpenseGraphBtn.clicked.connect(lambda: show_expenses_graph(grp, ui))
    
    ui.AddExpensesBtn.clicked.connect(lambda: add_expense_page(ui, grp))
    ui.DebtGraphBtn.clicked.connect(lambda: show_graph(grp, ui))
    ui.closeGraphBtn.clicked.connect(lambda: clear_graph(ui))
    ui.ExpenseGraphBtn.clicked.connect(lambda: show_expenses_graph(grp, ui))


def upload_group_excel(ui,user):
    file_path, _ = QFileDialog.getOpenFileName(
        None, "Select Excel File", "", "Excel Files (*.xlsx *.xls)"
    )
    
    if not file_path:
        ui.GExcelLabel.setText("No file selected.")
        ui.GExcelLabel.setStyleSheet("color: red;")
        return

    ui.uploaded_file_path = file_path
    ui.GExcelLabel.setText("Excel uploaded successfully!")
    ui.GExcelLabel.setStyleSheet("color: green;")



    if ui.uploaded_file_path:
        try:
            import_from_excel(ui.uploaded_file_path)  
            ui.GExcelLabel.setText("Transactions imported successfully!")
            ui.GExcelLabel.setStyleSheet("color: green;")
            print("finish importing fro excel")
            show_all_existing_groups(ui, user)
            
        except ValueError as ve:
            ui.GExcelLabel.setText(f"Import failed: {str(ve)}")
            ui.GExcelLabel.setStyleSheet("color: red;")
        except Exception as e:
            ui.GExcelLabel.setText(f"Unexpected error: {str(e)}")
            ui.GExcelLabel.setStyleSheet("color: red;")



def create_group(ui, user):
    default_shares = None
    default_prop_j = None
    default_shares_j = None
    split="equally"
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
        if split == "share":
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
    error  = 0 
    widgets = [ui.GrpNameLabel, ui.NoMembersLabel, ui.GrpMembersLabel, ui.DefaultSplitLabel]
    print([group_name, group_no, members, split])
    for widget, data in enumerate([group_name, group_no, members, split]):
        if data == "" or data == [] or data == 0:
            widgets[widget].setStyleSheet("color: red;")
            ui.ErrorLabel.setText("Fill out all inforamtion!")
            ui.ErrorLabel.setStyleSheet("color : red;")
            error = 1

        else:
            error =0
            widgets[widget].setStyleSheet("color: white;")
            ui.ErrorLabel.setText("")
    if error == 0:
        if group_no != "" and group_no != len(members):
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
        group.add_members(member, split, default_shares_j, default_prop_j)
    connection.commit()
    connection.close()



def split_amount(ui,amount_input):
    parts=amount_input.split()
    
    if len(parts)==1:
        
        amount=float(parts[0])
        currency="IRR"
    
    elif len(parts)==2:
        amount=float(parts[0])
        currency=parts[1].upper()
        
    else:
        ui.ErrorLabel2.setText("Invalid input format for expense!")
        ui.ErrorLabel2.setStyleSheet("color : red;")
        
    return amount,currency

        

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


    try:
        ui.FinalAddExpenseBtn.clicked.disconnect()
    except TypeError:
        pass  # No connection to disconnect


    ui.FinalAddExpenseBtn.clicked.connect(lambda _, g=group: add_group_expense(ui, g))
    return
    



def add_group_expense(ui, main_group: Groups):
    
    from currency_conversion_all_currencies import convert_to_IRR
    print(" Add called, mambers are: " , main_group.members, main_group.debts)
    category = ""
    label = ui.GrpExpenseLabelInput.text()
    print(label)
    amount_input = ui.AmountInput.text()
    selected_date = ui.calendarWidget.selectedDate().toString("yyyy-dd-MM")
    payer = ui.PayerInput.text()
    description = ui.DiscriptionInput.toPlainText()
    split_type = "default split"
    default = False
    error_def_perc = False

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

    
    try:
        amount,currency=split_amount(ui,amount_input)
        if currency=="IRR":
            IRR_amount=amount
        else:
            IRR_amount=convert_to_IRR(amount,date=selected_date,from_c=currency)
        
    except Exception as e:
        ui.ErrorLabel2.setText(f"Error: {str(e)}")
        ui.ErrorLabel2.setStyleSheet("color: red;")
        



    if split_type == "share" or split_type == "percentage":
            shares = get_shares(ui, "add_expense")
            print("COUNT", ui.verticalLayout_25.count())

    if split_type == "default split":
        default = True
        defaults = get_default_split(main_group.group_id, main_group.group_name)
        default_split = defaults[-3]
        default_shares = defaults[-2]
        default_proportions = defaults[-1]
        if default_shares:
            default_shares = json.loads(default_shares)
        if  default_proportions:
            default_proportions = json.loads(default_proportions)
        split_type = default_split
        if split_type == "share":
            shares = dict()
            for contributer in contributers:
                shares[contributer] = default_shares[contributer]
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
        


    widgets = [ui.GrpExpenseLabelLabel, ui.AmountLabel, ui.PayerLabel, ui.ContributersLabel]

    error = 0    
    for widget, data in enumerate([label, amount_input , payer, contributers]):
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

    
    
    if split_type == "percentage" and default == False:
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
    
    if default == True and split_type == "percentage":
        if len(contributers) != len(main_group.members):
            error_def_perc = True
            ui.SplitLabel.setStyleSheet("color: red;")
            if error == 0:
                ui.ErrorLabel2.setText("Your default split is percentage based; This mode of split is applicable only when all of the members are contributed!")
                ui.ErrorLabel2.setStyleSheet("color : red;")

            

    if error_def_perc == False and label != "" and amount_input != "" and selected_date != "" and isfloat(amount) and contributers != [] and payer != ""  and payer in main_group.members and total_perc(split_type):
        ui.SplitLabel.setStyleSheet("color: white;")
        ui.ErrorLabel2.setText("")
        ui.ErrorLabel2.setStyleSheet("color : white;")
        if split_type == "share":
            shares = shares
            main_group.add_expenses(label, IRR_amount, payer, contributers, selected_date, category,description, split_type, shares=shares)
        elif split_type == "percentage":
            proportions = shares
            main_group.add_expenses(label, IRR_amount, payer, contributers, selected_date, category,description, split_type, proportions=proportions)
        else:
            main_group.add_expenses(label,IRR_amount, payer, contributers, selected_date, category,description, split_type)
        
        if default == True : split_title =f"default ({split_type})"
        else: split_title = split_type
        var_to_add = [label, payer, str(IRR_amount),",".join(contributers), selected_date, category, split_title, description]
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
    return



    

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



#R

def get_group_expenses(group_id):
    
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""
            SELECT expense_id, label
            FROM group_expenses
            WHERE group_id = ?
        """, (group_id,))
        expenses = cursor.fetchall()
        print(f"Debug: Group ID being passed: {group_id}")

        print(f"Fetched expenses for group {group_id}: {expenses}")
        
        return expenses
    except sqlite3.Error as e:
        print(f"Database Error: {str(e)}")
        return []
    finally:
        if 'connection' in locals() and connection:
            connection.close()
    
    
    return


def add_new_member_to_group(ui):
    
    group = take_group(ui)
        
    if group is None:
        ui.ErrorAddMember.setText("Group not found!")
        ui.ErrorAddMember.setStyleSheet("color: red;")
        return
    
    new_member_name=ui.NewMemberInput.text().strip()
    
    if not new_member_name: #if the user didnt type anything
        ui.NewMemberLabel.setStyleSheet("color:red;")
        ui.ErrorAddMember.setText("Please enter a valid member name")
        ui.ErrorAddMember.setStyleSheet("color: red;")
        return
    
    
    if new_member_name in group.members:
        ui.NewMemberLabel.setStyleSheet("color: red;")
        ui.ErrorAddMember.setText("Member already exists in the group!")
        ui.ErrorAddMember.setStyleSheet("color: red;")
        return
    
    
    try:
        
        # Ensure layout exists
        if not ui.scrollAreaWidgetContents_19.layout():
            expense_layout = QtWidgets.QVBoxLayout(ui.scrollAreaWidgetContents_19)
            ui.scrollAreaWidgetContents_19.setLayout(expense_layout)
        else:
            expense_layout = ui.scrollAreaWidgetContents_19.layout()

        # Clear previous widgets
        while expense_layout.count():
            item = expense_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        print(f"Debug: Group ID being used hereeeee: {group.group_id}")
        
        existing_expenses=get_group_expenses(group.group_id)
        expense_layout=ui.scrollAreaWidgetContents_19.layout()
        
        for expense_id,label in existing_expenses:
            checkbox = QtWidgets.QCheckBox(ui.scrollAreaWidgetContents_19)
            checkbox.setObjectName(f"expense_{expense_id}")
            checkbox.setText(label)
            expense_layout.addWidget(checkbox)
        
        if not hasattr(group, 'split_type'):
            group.split_type = "equally"  
        if not hasattr(group, 'default_shares'):
            group.default_shares = {}  
        if not hasattr(group, 'default_proportions'):
            group.default_proportions = {} 
            
        ui.FinalAddMemberBtn.clicked.connect(lambda: save_new_member_with_expenses(ui, group, new_member_name))

            
            
        connection=get_connection()
        cursor=connection.cursor()
        
        cursor.execute("""
            INSERT INTO user_group (group_id, group_name, username, default_split, default_shares, default_proportions)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (group.group_id, group.group_name, new_member_name, group.split_type, json.dumps(group.default_shares), json.dumps(group.default_proportions)))
        
        connection.commit()
        
        connection.commit()
        group.add_members(new_member_name, group.split_type, json.dumps(group.default_shares), json.dumps(group.default_proportions))
        
        
        members_layout = ui.scrollAreaWidgetContents_7.layout()
        ui.checkBox_2 = QtWidgets.QCheckBox(ui.scrollAreaWidgetContents_7)
        ui.checkBox_2.setObjectName(new_member_name)
        ui.checkBox_2.setText(new_member_name)
        members_layout.addWidget(ui.checkBox_2)
        
        

    except sqlite3.Error as e:
        ui.ErrorAddMember.setText(f"Database Error: {str(e)}")
        ui.ErrorAddMember.setStyleSheet("color: red;")
    finally:
        connection.close()
 
 

def save_new_member_with_expenses(ui,group,new_member_name):
    selected_expenses=[]
    layout = ui.scrollAreaWidgetContents_19.layout()
    
    for i in range(layout.count()):
        checkbox = layout.itemAt(i).widget()
        if checkbox.isChecked():
            expense_id = int(checkbox.objectName().replace("expense_", ""))
            expense_label = checkbox.text()
            selected_expenses.append(expense_id)  # Extract expense ID

    try:
        connection = get_connection()
        cursor = connection.cursor()


        cursor.execute("""
            INSERT INTO user_group (group_id, group_name, username, default_split, default_shares, default_proportions)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (group.group_id, group.group_name, new_member_name, group.split_type, 
              json.dumps(group.default_shares), json.dumps(group.default_proportions)))

        cursor.execute("SELECT user_id FROM users WHERE username = ?", (new_member_name,))
        user_id = cursor.fetchone()[0]

        for expense_id in selected_expenses:
            cursor.execute("""
                INSERT INTO expense_user (expense_id, username, amount_contributed, split_proportion, for_what, name, share)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (expense_id, new_member_name, 0, 0, "group", group.group_name, "equal_split"))

        connection.commit()

    
        group.add_members(new_member_name, group.split_type, json.dumps(group.default_shares), json.dumps(group.default_proportions))
        ui.NewMemberLabel.setStyleSheet("color: green;")
        ui.ErrorAddMember.setText(f"Member {new_member_name} added successfully!")
        ui.ErrorAddMember.setStyleSheet("color: green;")

    except sqlite3.Error as e:
        ui.ErrorLabel3.setText(f"Database error: {e}")
        ui.ErrorLabel3.setStyleSheet("color: red;")
        
        
def show_graph(group, ui):
    layout = ui.scrollAreaWidgetContents_23.layout()
    while layout.count():
        item = layout.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        widget.deleteLater()
    graph = Graph(group)
    graph.plot_graph()
    ui.graph = QtWidgets.QLabel(ui.scrollAreaWidgetContents_23)
    pixmap = QtGui.QPixmap("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Core/graph_plot.png")
    ui.graph.setPixmap(pixmap)
    ui.graph.setScaledContents(True)  # Scale the image to fit the frame

    # Set a layout for the frame and add the label
    layout.setContentsMargins(0, 0, 0, 0)  # Optional: Remove margins
    layout.addWidget(ui.graph)
    font = QtGui.QFont()
    font.setFamily("Swis721 Blk BT")
    font.setPointSize(10)
    font.setBold(False)
    font.setWeight(50)
    
    ui.pushButton.setText("Simplify the graph")
    ui.pushButton.setFont(font)
    layout_2 = ui.scrollAreaWidgetContents_6.layout()
    while layout_2.count():
        item = layout_2.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        widget.deleteLater()
    for (debtor, creditor), debt in group.debts.items():
        debt = debt["capacity"]
        ui.weight = QtWidgets.QLabel(ui.scrollAreaWidgetContents_6)
        ui.weight.setText(f"{debtor} owes {creditor} {debt} R")
        ui.weight.setFont(font)
        ui.weight.setObjectName(f"{(debtor, creditor)}")
        layout_2.addWidget(ui.weight)
    ui.pushButton.clicked.connect(lambda: show_simplified_graph(group, ui))

def show_simplified_graph(group: Groups, ui):
    debt_simplification = Debtsimplification(group)
    debt_simplification.creating_simplified_graph()
    layout = ui.scrollAreaWidgetContents_23.layout()
    while layout.count():
        item = layout.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        widget.deleteLater()
    ui.GraphTitle.setText("Simplified Graph")
    ui.graph = QtWidgets.QLabel(ui.scrollAreaWidgetContents_23)
    pixmap = QtGui.QPixmap("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Core/graph_plot.png")
    ui.graph.setPixmap(pixmap)
    ui.graph.setScaledContents(True)  # Scale the image to fit the frame

    # Set a layout for the frame and add the label
    layout.setContentsMargins(0, 0, 0, 0)  # Optional: Remove margins
    layout.addWidget(ui.graph)
    font = QtGui.QFont()
    font.setFamily("Swis721 Blk BT")
    font.setPointSize(10)
    font.setBold(False)
    font.setWeight(50)
    
    ui.pushButton.setText("")
    ui.pushButton.setFont(font)
    layout_2 = ui.scrollAreaWidgetContents_6.layout()
    while layout_2.count():
        item = layout_2.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        widget.deleteLater()
    for (debtor, creditor), debt in group.simplified_debts.items():
        if debtor != creditor:
            debt = debt["capacity"]
            ui.weight = QtWidgets.QLabel(ui.scrollAreaWidgetContents_6)
            ui.weight.setText(f"{debtor} owes {creditor} {debt} R")
            ui.weight.setFont(font)
            ui.weight.setObjectName(f"{(debtor, creditor)}")
            layout_2.addWidget(ui.weight)

    update_group_debts(group.group_id, group.group_name)

    for (debtor, creditor), debt in group.simplified_debts.items():
        debt = debt["capacity"]
        if debtor != creditor:
            add_simplified_debt(group.group_id, group.group_name, debtor, creditor, debt)

    specific_group_page(ui,group)
    

def clear_graph(ui):
    layout = ui.scrollAreaWidgetContents_23.layout()
    while layout.count():
        item = layout.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        widget.deleteLater()

    layout_2 = ui.scrollAreaWidgetContents_6.layout()
    while layout_2.count():
        item = layout_2.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        widget.deleteLater()
    ui.GraphTitle.setText("")


def show_expenses_graph(group, ui):
    all_expenses = group.get_expenses_by_category()
    categories = list(all_expenses.keys())
    amounts = list(all_expenses.values())


    def autopct_amount(pct, values):
        total = sum(values)
        amount = int(round(pct * total / 100.0))
        return f"{amount} R"
    # Create the pie chart
    plt.figure(figsize=(8, 6))  # Set figure size
    plt.pie(
        amounts, 
        labels=categories, 
        autopct=lambda pct: autopct_amount(pct, amounts),  
        startangle=90,      
        colors=plt.cm.Paired.colors,  
    )

    # Add a 
    plt.title("Expense Distribution")

    png_path = "C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Core/graph_pie_plot.png"
    
    #png_path = r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Core\graph_pie_plot.png"

    
    # Save as PNG
    plt.savefig(png_path)

    layout = ui.scrollAreaWidgetContents_23.layout()
    while layout.count():
        item = layout.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        widget.deleteLater()
    
    ui.graph = QtWidgets.QLabel(ui.scrollAreaWidgetContents_23)
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
    ui.GraphTitle.setText("Expenses in each category")
    ui.GraphTitle.setFont(font)

    layout_2 = ui.scrollAreaWidgetContents_6.layout()
    while layout_2.count():
        item = layout_2.takeAt(0)  # Get the first item
        widget = item.widget()  # Get the widget
        widget.deleteLater()



def safe_disconnect(button, handler):
    try:
        button.clicked.disconnect(handler)
    except TypeError:
        pass  # No previous connection, safe to ignore
    
    
    
    

def view_all_groups():
    # Connect to the database
    connection = sqlite3.connect(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database.db")  # Use your actual database path
    cursor = connection.cursor()
    
    # Query to fetch all groups
    cursor.execute("SELECT * FROM groups")
    
    # Fetch all results
    groups = cursor.fetchall()
    
    # Print all groups
    if groups:
        print("Groups in the database:")
        for group in groups:
            print(group)  # Print each group record
    else:
        print("No groups found in the database.")
    
    # Close the connection
    connection.close()

# Call the function to view all groups
#view_all_groups()

import sqlite3

def view_user_groups():
    # Connect to the database
    connection = sqlite3.connect(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database.db")  # Use your actual database path
    cursor = connection.cursor()
    
    # Query to fetch all user-group associations
    cursor.execute("SELECT * FROM user_group")
    
    # Fetch all results
    user_groups = cursor.fetchall()
    
    # Print all user-group associations
    if user_groups:
        print("User-Group Associations:")
        for user_group in user_groups:
            print(user_group)  # Print each user-group record
    else:
        print("No user-group associations found in the database.")
    
    # Close the connection
    connection.close()

# Call the function to view user-group associations
#view_user_groups()



def group_expenses():
    # Connect to the database
    connection = sqlite3.connect(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database.db")  # Use your actual database path
    cursor = connection.cursor()
    
    # Query to fetch all user-group associations
    cursor.execute("SELECT * FROM group_expenses")
    
    # Fetch all results
    group_expense = cursor.fetchall()
    
    # Print all user-group associations
    if group_expense:
        print("group_expenses Associations:")
        for user_group in group_expense:
            print(user_group)  # Print each user-group record
    else:
        print("No group_expenses associations found in the database.")
    
    # Close the connection
    connection.close()

# Call the function to view user-group associations
#group_expenses()