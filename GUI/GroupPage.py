from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date

import sys
import os
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Models"))
from db_operations import *
from groups import *

def show_all_existing_groups(ui, user):
    groups = get_groups_by_username(user[2])
    for group in groups:
        group_id, group_name = group[2:]

def create_group(ui, user):
    group_name = ui.GrpNameInput.text()
    group_no = ui.NoMembersInput.value()
    members = ui.GrpMembersInput.toPlainText().split("\n")
    for SplitBtnNo in range(11):
        Split = ui.verticalLayout_30.itemAt(SplitBtnNo).widget()
        if isinstance(Split, QtWidgets.QRadioButton) and Split.isChecked():
            split = Split.text()


    group = Groups(group_name, user[2], split)
    for member in members:
        group.add_members(member)



