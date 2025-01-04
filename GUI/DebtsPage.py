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


def show_all_debts(username, ui):
    all_debts = total_user_owes(username)
    debts_radio_buttons = dict()
    for debt in all_debts:
        ui.widget_23 = QtWidgets.QWidget(ui.scrollAreaWidgetContents_35)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ui.widget_23.sizePolicy().hasHeightForWidth())
        ui.widget_23.setSizePolicy(sizePolicy)
        ui.widget_23.setObjectName("widget_23")
        ui.verticalLayout_176 = QtWidgets.QVBoxLayout(ui.widget_23)
        ui.verticalLayout_176.setObjectName("verticalLayout_176")
        ui.label_85 = QtWidgets.QLabel(ui.widget_23)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(11)
        ui.label_85.setFont(font)
        ui.label_85.setObjectName("label_85")
        ui.verticalLayout_176.addWidget(ui.label_85, 0, QtCore.Qt.AlignLeft)
        ui.frame_109 = QtWidgets.QFrame(ui.widget_23)
        ui.frame_109.setFrameShape(QtWidgets.QFrame.StyledPanel)
        ui.frame_109.setFrameShadow(QtWidgets.QFrame.Raised)
        ui.frame_109.setObjectName("frame_109")
        ui.verticalLayout_177 = QtWidgets.QVBoxLayout(ui.frame_109)
        ui.verticalLayout_177.setObjectName("verticalLayout_177")
        ui.radioButton_49 = QtWidgets.QRadioButton(ui.frame_109)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        ui.radioButton_49.setFont(font)
        ui.radioButton_49.setObjectName("radioButton_49")
        ui.verticalLayout_177.addWidget(ui.radioButton_49)
        ui.radioButton_50 = QtWidgets.QRadioButton(ui.frame_109)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        ui.radioButton_50.setFont(font)
        ui.radioButton_50.setObjectName("radioButton_50")
        ui.verticalLayout_177.addWidget(ui.radioButton_50)
        ui.radioButton_51 = QtWidgets.QRadioButton(ui.frame_109)
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        ui.radioButton_51.setFont(font)
        ui.radioButton_51.setObjectName("radioButton_51")
        ui.verticalLayout_177.addWidget(ui.radioButton_51)
        ui.verticalLayout_176.addWidget(ui.frame_109, 0, QtCore.Qt.AlignHCenter)
        ui.verticalLayout_175.addWidget(ui.widget_23)
        ui.label_85.setText(f"you owe {debt[-3]} {[debt[-2]]} R")
        ui.radioButton_49.setText("Pay from this account")
        ui.radioButton_50.setText("Paid by cash")
        debts_radio_buttons[debt[0]] = [ui.radioButton_49, ui.radioButton_50]
