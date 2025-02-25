from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
import matplotlib.pyplot as plt

import sys
import os
import json

# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Utils\currency_conversion"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Utils/currency_conversion"))

from currency_conversion_all_currencies import convert_to_IRR

#Gui objects: LineEdit to get the expense: AmountCurrencyInput - lineEdit to get the currency:Currency - pushbotton: ConvertCurrencyBtn -Label to show the result= ConversionResult


def convert_currency(ui):
    
    try:
        
        amount_input=ui.AmountCurrencyInput.text()
        currency_input=ui.CurrencyInput.text()
        

        if not amount_input or not currency_input:
            ui.ConversionResult.setText("Amount and currency cannot be empty")
            ui.ConversionResult.setStyleSheet("color : red;")
            return
        
        try:
            amount=float(amount_input)
        except ValueError:
            ui.ConversionResult.setText("Invalid format for amount. Please enter a valid number")
            ui.ConversionResult.setStyleSheet("color : red;")
            return
            
        currency=currency_input.strip().upper()    
        
        if not currency.isalpha():
            ui.ConversionResult.setText("Invalid currency format. Please enter a valid currency")
            ui.ConversionResult.setStyleSheet("color : red;")
            return
            
        
        converted_amount=convert_to_IRR(amount,from_c=currency)
        
        ui.ConversionResult.setText(f"Converted Amount: {converted_amount:.2f} IRR")
        ui.ConversionResult.setStyleSheet("color: green;")
        
    except Exception as e:
        ui.ConversionResult.setText(f"Error: {str(e)}")
        ui.ConversionResult.setStyleSheet("color:red;")
        
    
    