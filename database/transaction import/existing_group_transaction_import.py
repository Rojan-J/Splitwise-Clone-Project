import openpyxl
import pandas as pd
from datetime import datetime
from sqlite3 import IntegrityError #to catch specififc errors in data
import sys
import os
#sys.path.append(os.path.abspath("C:/Users/LENOVO/OneDrive/Documents/Github/Splitwise-Clone-Project/database"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))

from db_operations import *

# sys.path.append(os.path.abspath("C:/Users/LENOVO/OneDrive/Documents/GitHub/Splitwise-Clone-Project/Utils/currency_conversion"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project//Utils/currency_conversion"))
from currency_conversion_all_currencies import convert_to_IRR

def update_existing_group(group_name,file_path):
    data=pd.read_excel(file_path)
    required_col=["group_name","members","payer_id","amount","category","date","description","split_type","percentage","share","currency"]
    
    if not all(column in data.columns for column in required_col):
        raise ValueError("The Excel file is missing required columns.")
    
    # connection = sqlite3.connect("C:/Users/LENOVO/OneDrive/Documents/Github/Splitwise-Clone-Project/database/database.db")
    connection = sqlite3.connect("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database/database.db")

    cursor=connection.cursor()
    
    #check if the group exists:
    cursor.execute('SELECT group_id FROM groups WHERE group_name = ?', (group_name,))
    group = cursor.fetchone()
    
    if not group:
        raise ValueError(f"Group '{group_name}' does not exist in the database.")
    
    group_id=group[0]
    row_count=0
    
    for _, row in data.iterrows():
        #check if the group name in the excel matches the provided group name
        excel_group_name=row["group_name"]
        
        if excel_group_name!=group_name:
            raise ValueError(f"Excel file contains data for a different group: {excel_group_name}. Expected group: {group_name}.")
        

        members = row["members"].split(",")
        payer_id = row["payer_id"]
        amount = row["amount"]
        category = row["category"]
        date = row["date"]
        description = row.get("description", None)
        split_type = row["split_type"]
        percentage = row["percentage"]
        share = row["share"]
        currency = row["currency"] if "currency" in row else "IRR"
        
        if isinstance(date, float):
            date = pd.to_datetime(date, unit="D", origin="1900-01-01").strftime("%Y-%d-%m")

        #check if an identical expense is alredy added to the group
        cursor.execute('''
            SELECT 1 
            FROM group_expenses 
            WHERE group_id = ? AND groupname = ? AND payername = ? AND contributers = ? AND amount = ? AND category = ? 
                  AND date = ? AND description = ? AND split_type = ? AND proportions = ? AND shares = ? 
        ''', (group_id, group_name, payer_id, ",".join(members), amount, category, date, description, split_type, percentage, share))

        if cursor.fetchone():  

            print(f"Duplicate expense found. Skipping entry for {description or 'Unnamed Expense'} on {date}.")
            continue

        #check if members exist and add them to the group if not
        for member in members:
            cursor.execute('SELECT user_id FROM users WHERE username = ?', (member,))
            user = cursor.fetchone()
            
            if not user: #if that friend doesnt have an account, add them with just a username
                cursor.execute('INSERT INTO users (username, name, email, password_hash) VALUES (?,?,?,?)', (member,member,f"{member}@gmail.com",""))
                connection.commit()
                user_id=cursor.lastrowid
                print(f"Created new user: {member} (ID: {user_id})")    
            else:
                user_id=user[0]
                
            cursor.execute('SELECT 1 FROM user_group WHERE group_id = ? AND user_id = ?', (group_id, user_id))
                
            if not cursor.fetchone():  #add friend to the group if not already a member
                    cursor.execute('INSERT INTO user_group (user_id, username, group_id, group_name) VALUES (?, ?, ?, ?)', (user_id, member, group_id, group_name))
                    connection.commit()
                    print(f"Added user {member} to group {group_name}.")
        
        if currency != "IRR":
                amount = convert_to_IRR(amount, date=date, from_c=currency)
                print(f"Converted amount {row['amount']} {currency} to {amount} IRR.")
        #insert the expenses:
        cursor.execute('''
                INSERT INTO group_expenses (label,group_id, groupname, payername, contributers, amount, category, date, description, split_type, proportions, shares, currency) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
            ''', (row.get("label","Expense"), group_id, group_name, payer_id, ",".join(members), amount, category, date, description, split_type, percentage, share, currency))
        
        expense_id = cursor.lastrowid
        print(f"Inserted expense (ID: {expense_id}) for group {group_name}.")
        
        #split expenses
        if split_type == "equally":
            amount_per_user = amount / len(members)
            for member in members:
                cursor.execute('''
                    INSERT INTO expense_user (expense_id, total_expense, username, amount_contributed, split_proportion, for_what, name)
                    VALUES (?, ?, ?, ?, ?, "group", ?)
                ''', (expense_id, amount, member, amount_per_user, amount_per_user / amount, group_name))
       
            print("Split equally among members.")
       
        elif split_type == "percentage":
            if not isinstance(percentage, list) or len(percentage) != len(members):
                raise ValueError("Percentage values must be provided as a list with the same length as the number of members.")
            for i, member in enumerate(members):
                amount_contributed = amount * (percentage[i] / 100)
                cursor.execute('''
                    INSERT INTO expense_user (expense_id, total_expense, username, amount_contributed, split_proportion, for_what, name)
                    VALUES (?, ?, ?, ?, ?, "group", ?)
                ''', (expense_id, amount, member, amount_contributed, amount_contributed / amount, group_name))
            print("Split by percentage.")
            
        elif split_type == "share":
            total_share = sum(share.values())
            for member, member_share in share.items():
                amount_contributed = amount * (member_share / total_share)
                cursor.execute('''
                    INSERT INTO expense_user (expense_id, total_expense, username, amount_contributed, split_proportion, for_what, name)
                    VALUES (?, ?, ?, ?, ?, "group", ?)
                ''', (expense_id, amount, member, amount_contributed, amount_contributed / amount, group_name))
            print("Split by share.")
            
            
            
            
        row_count+=1
    
    connection.commit()
    connection.close()
    
    
#update_existing_group("Test_group1", "C:/Users/LENOVO/OneDrive/Documents/Github/Splitwise-Clone-Project/database/transaction import/TestExcel_GroupUpdate.xlsx")
    
            
    