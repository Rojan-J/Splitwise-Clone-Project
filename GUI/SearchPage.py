
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QFileDialog , QTableWidgetItem


import sys
import os
import json

import sqlite3
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database"))
from db_operations import *




def perform_search(ui):
    label_input = ui.ExpenseLabelInput_2.text().strip()
    user_input = ui.UserExpenseInput_2.text().strip()
    date_input = ui.SearchDateInput_2.selectedDate().toString("yyyy-dd-MM") if ui.SearchDateInput_2.selectedDate() else None

    if not label_input and not user_input and not date_input:
        ui.DateSearchLabel_2.setText("Please provide at least one search criterion.")
        ui.DateSearchLabel_2.setStyleSheet("color: red;")
        return

    ui.DateSearchLabel_2.setText("")  

    query = '''
        SELECT expense_id, label, payername, contributers, amount, category, date, description, split_type, proportions, shares, currency 
        FROM friend_expenses WHERE 1=1
    '''
    query_params = []

    if label_input:
        query += " AND label LIKE ?"
        query_params.append(f"%{label_input}%")

    if user_input:
        query += " AND payername LIKE ?"
        query_params.append(f"%{user_input}%")

    if date_input:
        query += " AND date = ?"
        query_params.append(date_input)

    query += " UNION ALL "  

    query += '''
        SELECT expense_id, label, payername, contributers, amount, category, date, description, split_type, proportions, shares, currency 
        FROM group_expenses WHERE 1=1
    '''
   
    if label_input:
        query += " AND label LIKE ?"
        query_params.append(f"%{label_input}%")

    if user_input:
        query += " AND payername LIKE ?"
        query_params.append(f"%{user_input}%")

    if date_input:
        query += " AND date = ?"
        query_params.append(date_input)

    print(f"Query: {query}")
    print(f"Parameters: {query_params}")
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, query_params)

        results = cursor.fetchall()
        ui.SearchResultTable_2.setRowCount(0)
        header = ui.SearchResultTable_2.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        ui.SearchResultTable_2.setColumnCount(12)
        
        ui.SearchResultTable_2.setHorizontalHeaderLabels([
            "Expense ID", "Label", "Payer Name", "Contributors", "Amount", "Category", "Date", "Description", 
            "Split Type", "Proportions", "Shares", "Currency"
        ])
        
    
        for row_idx, row_data in enumerate(results):
            ui.SearchResultTable_2.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(col_data))
                item.setBackground(QtGui.QColor("white"))  
                ui.SearchResultTable_2.setItem(row_idx, col_idx, item)
                
        if not results:
            ui.DateSearchLabel_2.setText("No results found.")
            ui.DateSearchLabel_2.setStyleSheet("color: orange;")
        else:
            ui.DateSearchLabel_2.setText("Results updated.")
            ui.DateSearchLabel_2.setStyleSheet("color: green;")

    except sqlite3.Error as e:
        ui.DateSearchLabel_2.setText(f"Database error: {e}")
        ui.DateSearchLabel_2.setStyleSheet("color: red;")
