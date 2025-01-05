import pandas as pd
import sqlite3
import sys
import os
from datetime import datetime
from sqlite3 import IntegrityError


sys.path.append(os.path.abspath("C:/Users/LENOVO/OneDrive/Documents/Github/Splitwise-Clone-Project/database"))
sys.path.append(os.path.abspath("C:/Users/LENOVO/OneDrive/Documents/Github/Splitwise-Clone-Project/Utils"))


from currency_conveyrsion_all_currencies import convert_to_IRR
from db_operations import *

def update_friends_transactions(username,file_path):
    data=pd.read_excel(file_path)
    
    required_columns = [
        "friend_name", "amount", "payer_name", "split_type", "category", 
        "date", "description", "percentage", "share", "currency"
    ]
    
    if not all(column in data.columns for column in required_columns):
        raise ValueError("The Excel file is missing required columns.")

    connection = sqlite3.connect("C:/Users/LENOVO/OneDrive/Documents/Github/Splitwise-Clone-Project/database/database.db")
    cursor = connection.cursor()
    for _, row in data.iterrows():
        friend_name = row["friend_name"]
        payer_name = row["payer_name"]
        amount = row["amount"]
        split_type = row["split_type"]
        category = row["category"]
        date = row["date"]
        description = row.get("description", None)
        percentage = row["percentage"] if "percentage" in row else None
        share = row["share"] if "share" in row else None
        currency = row["currency"] if "currency" in row else "IRR"
        
        if isinstance(date, float):
            date = pd.to_datetime(date, unit="D", origin="1900-01-01").strftime("%Y-%d-%m")
            
        cursor.execute("SELECT friendship_id FROM friends WHERE (username = ? AND friend_name = ?) OR (username = ? AND friend_name = ?)", (username, friend_name, friend_name, username))
        friendship = cursor.fetchone()
        
        if not friendship:
            cursor.execute(
                "INSERT INTO friends (username, friend_name, friend_email, friend_profile) VALUES (?, ?, ?, ?)",
                (username, friend_name, f"{friend_name}@example.com", "")
            )
            connection.commit()
            friendship_id = cursor.lastrowid
            print(f"Added new friend: {friend_name} with friendship_id {friendship_id}.")
        else:
            friendship_id = friendship[0]
            
            
        cursor.execute('''
            SELECT 1 
            FROM friend_expenses 
            WHERE friendship_id = ? AND payername = ? AND amount = ? AND category = ? 
                  AND date = ? AND description = ? AND split_type = ?
        ''', (friendship_id, payer_name, amount, category, date, description, split_type))

        if cursor.fetchone():
            print(f"Duplicate transaction found for friend {friend_name}. Skipping entry.")
            continue


        if currency != "IRR":
            amount = convert_to_IRR(amount, date=date, from_c=currency)
            print(f"Converted amount {row['amount']} {currency} to {amount} IRR.")


        cursor.execute('''
            INSERT INTO friend_expenses (friendship_id, payername, amount, category, date, description, split_type, proportions, shares, currency) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (friendship_id, payer_name, amount, category, date, description, split_type, str(percentage), str(share), currency))
        expense_id = cursor.lastrowid
        print(f"Inserted expense with ID {expense_id} for friend {friend_name}.")


        contributors=[username, friend_name]
        
        
        if split_type == "equally":
            amount_per_user = amount / len(contributors)
            for contributor in contributors:
                cursor.execute('''
                    INSERT INTO expense_user (expense_id, total_expense, username, amount_contributed, split_proportion, for_what, name)
                    VALUES (?, ?, ?, ?, ?, "friend", ?)
                ''', (expense_id, amount, contributor, amount_per_user, amount_per_user / amount, friend_name))
            print("Expense split equally.")

        elif split_type == "percentage":
            if not percentage or len(percentage) != len(contributors):
                raise ValueError("Percentage values must match the number of contributors.")
            for i, contributor in enumerate(contributors):
                amount_contributed = amount * (percentage[i] / 100)
                cursor.execute('''
                    INSERT INTO expense_user (expense_id, total_expense, username, amount_contributed, split_proportion, for_what, name)
                    VALUES (?, ?, ?, ?, ?, "friend", ?)
                ''', (expense_id, amount, contributor, amount_contributed, amount_contributed / amount, friend_name))
            print("Expense split by percentage.")

        elif split_type == "share":
            if not share or len(share) != len(contributors):
                raise ValueError("Share values must match the number of contributors.")
            total_share = sum(share.values())
            for contributor in contributors:
                amount_contributed = amount * (share[contributor] / total_share)
                cursor.execute('''
                    INSERT INTO expense_user (expense_id, total_expense, username, amount_contributed, split_proportion, for_what, name)
                    VALUES (?, ?, ?, ?, ?, "friend", ?)
                ''', (expense_id, amount, contributor, amount_contributed, amount_contributed / amount, friend_name))
            print("Expense split by share.")


  
            
    connection.commit()
    connection.close()
    print("Friends transactions updated successfully.")
