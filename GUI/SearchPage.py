
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QFileDialog , QTableWidgetItem


import sys
import os
import json

import sqlite3
sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database"))
from db_operations import *




def perform_search(ui):
    # Get the user inputs
    label_input = ui.ExpenseLabelInput_2.text().strip()
    user_input = ui.UserExpenseInput_2.text().strip()
    date_input = ui.SearchDateInput_2.selectedDate().toString("yyyy-MM-dd") if ui.SearchDateInput_2.selectedDate() else None

    # Validate input: at least one search criterion must be provided
    if not label_input and not user_input and not date_input:
        ui.DateSearchLabel_2.setText("Please provide at least one search criterion.")
        ui.DateSearchLabel_2.setStyleSheet("color: red;")
        return

    ui.DateSearchLabel_2.setText("")  # Clear the label before showing results

    # Build the query for both tables
    query = '''
        SELECT expense_id, label, payername, contributers, amount, category, date, description, split_type, proportions, shares, currency 
        FROM friend_expenses WHERE 1=1
    '''
    query_params = []

    # Append conditions based on user input
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
    # Execute the query on the database
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query, query_params)

        results = cursor.fetchall()
        ui.SearchResultTable_2.setRowCount(0)  # Clear previous results

        ui.SearchResultTable_2.setColumnCount(12)
        
        # Set the headers for the table
        ui.SearchResultTable_2.setHorizontalHeaderLabels([
            "Expense ID", "Label", "Payer Name", "Contributors", "Amount", "Category", "Date", "Description", 
            "Split Type", "Proportions", "Shares", "Currency"
        ])
        
        # Display results in the table with white background color
        for row_idx, row_data in enumerate(results):
            ui.SearchResultTable_2.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(col_data))
                item.setBackground(QtGui.QColor("white"))  # Set the background color of the item to white
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
