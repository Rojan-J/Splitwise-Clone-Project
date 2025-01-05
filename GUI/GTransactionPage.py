from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QFileDialog , QTableWidgetItem
from datetime import date
import matplotlib.pyplot as plt
import pandas as pd


import sys
import os
import json

sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Models"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Core"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Utils"))


# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database"))
# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Models"))
# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Core"))
# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Utils"))



from db_operations import *
from groups import *
import sqlite3
from graph import *
from debt_simplification import *
from currency_conversion_all_currencies import *
from group_transaction_import import import_from_excel


#this is for adding new groups


def setup_Gtransaction_page(ui):
    ui.GExcelLabel.setText("No file uploaded yet")
    ui.GExcelLabel.setStyleSheet("color: red;")
    
    ui.GExcelTable.setColumnCount(0)
    ui.GExcelTable.setRowCount(0)
    ui.GExcelTable.setHorizontalHeaderLabels([])

    ui.UploadButton.clicked.connect(lambda: upload_excel(ui))
    ui.ProcessButton.clicked.connect(lambda: process_excel(ui))
    
    
    
def upload_excel(ui):
    
    file_path, _ = QFileDialog.getOpenFileName(
        None, "Select Excel File", "", "Excel Files (*.xlsx *.xls)"
    )
    
    if not file_path:
        ui.GExcelLabel.setText("No file selected.")
        ui.GExcelLabel.setStyleSheet("color: red;")
        return

    try:
        data = pd.read_excel(file_path)
        ui.GExcelTable.setRowCount(len(data))
        ui.GExcelTable.setColumnCount(len(data.columns))
        ui.GExcelTable.setHorizontalHeaderLabels(data.columns.tolist())
        
        for i, row in data.iterrows():
            for j, value in enumerate(row):
                ui.GExcelTable.setItem(i, j, QTableWidgetItem(str(value)))
                
                
        ui.GExcelLabel.setText("Excel uploaded successfully!")
        ui.GExcelLabel.setStyleSheet("color: green;")
        ui.uploaded_file_path = file_path 
        
    except Exception as e:
        ui.GExcelLabel.setText(f"Error reading Excel: {str(e)}")
        ui.GExcelLabel.setStyleSheet("color: red;")

        
        
def process_excel(ui):
    
    if not hasattr(ui, 'uploaded_file_path') or not ui.uploaded_file_path:
        ui.GExcelLabel.setText("Please upload an Excel file first.")
        ui.GExcelLabel.setStyleSheet("color: red;")
        return
    
    try:
        import_from_excel(ui.uploaded_file_path)  
        ui.GExcelLabel.setText("Transactions imported successfully!")
        ui.GExcelLabel.setStyleSheet("color: green;")
    except ValueError as ve:
        ui.GExcelLabel.setText(f"Import failed: {str(ve)}")
        ui.GExcelLabel.setStyleSheet("color: red;")
    except Exception as e:
        ui.GExcelLabel.setText(f"Unexpected error: {str(e)}")
        ui.GExcelLabel.setStyleSheet("color: red;")
                
                
        
    

    