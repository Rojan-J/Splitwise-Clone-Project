from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date

import sys
import os
import json
#sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database"))


#sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Models"))
sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Models"))
#sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Core"))
sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Core"))


from db_operations import *
from groups import *
import sqlite3
from graph import *




def perform_search(ui):
    
    date_input = ui.SearchDateInput.selectedDate().toString("yyyy-MM-dd") if ui.SearchDateInput.selectedDate() else None
    label_input = ui.ExpenseLabelInput.text().strip()
    user_input = ui.UserExpenseInput.text().strip()
    
    if not date_input and not label_input and not user_input:
        ui.DateSearchLabel.setText("Please provide at least one search criterion.")
        ui.DateSearchLabel.setStyleSheet("color: red;")
        return
    
    
    ui.DateSearchLabel.setText("")
    
    query = "SELECT expense_id, date, label, amount, username FROM expenses WHERE 1=1"
    params = []
    
    
    #adding search conditions
    if date_input:
        query += " AND date = ?"
        params.append(date_input)

    if label_input:
        query += " AND label LIKE ?"
        params.append(f"%{label_input}%")

    if user_input:
        query += " AND username LIKE ?"
        params.append(f"%{user_input}%")

    try:
        connection=get_connection()
        cursor=connection.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        
        ui.SearchResultTable.setRowCount(0)


        #display data
        for row_idx, row_data in enumerate(results):
            ui.SearchResultTable.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                ui.SearchResultTable.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        if not results:
            ui.DateSearchLabel.setText("No results found.")
            ui.DateSearchLabel.setStyleSheet("color: orange;")
        else:
            ui.DateSearchLabel.setText("Results updated.")
            ui.DateSearchLabel.setStyleSheet("color: green;")

    except sqlite3.Error as e:
        ui.DateSearchLabel.setText(f"Database error: {e}")
        ui.DateSearchLabel.setStyleSheet("color: red;")  


# def navigate_to_expense_details(ui):
#     #get the selected row
#     selected_row = ui.SearchResultTable.currentRow()
    
#     if selected_row == -1:
#         ui.DateSearchLabel.setText("Please select a result to view details.")
#         ui.DateSearchLabel.setStyleSheet("color: red;")
#         return
    
#     expense_id_item = ui.SearchResultTable.item(selected_row, 0)
    
#     if not expense_id_item:
#         ui.DateSearchLabel.setText("Invalid selection.")
#         ui.DateSearchLabel.setStyleSheet("color: red;")
#         return

#     expense_id = int(expense_id_item.text())
    
    # try:
        
    #     connection = get_connection()
    #     cursor = connection.cursor()

    #     cursor.execute("SELECT * FROM expenses WHERE expense_id = ?", (expense_id,))
    #     expense_details = cursor.fetchone()

        