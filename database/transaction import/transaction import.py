import openpyxl
import pandas as pd
from datetime import datetime
from sqlite3 import IntegrityError #to catch specififc errors in data
from db_operations import get_connection
from currency_conversion(all_currencies) import convert_to_IRR


def import_from_excel(file_path):
    data=pd.read_excel(file_path)
    
    required_col=["group_name","members","payer_id","amount","category","date","description","split_type","percentage","share","currency"]
    
    if not all (column in data.columns for column in required_col):
        raise ValueError("The Excel file is missing required columns.")
    
    connection=get_connection()
    cursor=connection.cursor()
    
    row_count=0
    
    for _, row in data.iterrows():
        group_name=row["group_name"]
        members=row["members"].split(",")
        payer_id=row["payer_id"]
        amount=row["amount"]
        category=row["category"]
        date=row["date"]
        description=row.get("description", None)
        split_type=row["split_type"]
        percentage=row["percentage"]
        share=row["share"]
        currency = row["currency"] if "currency" in row else "IRR"
        
        
        #convert the data format if necessary
        if isinstance(date,float):
            date=pd.to_datetime(date,unit="D",origin="1900-01-01").strftime("%Y=%m-%d")
       
       
        #check or creat all imports
        
        #group
        cursor.execute('SELECT group_id FROM groups WHERE group_name = ?', (group_name,))
        group = cursor.fetchone()
        
        if not group: #if it has'nt been created yet
            cursor.execute('INSERT INTO groups (group_name) VALUES (?)', (group_name,))
            connection.commit()
            group_id = cursor.lastrowid
        else:
            group_id = group[0]
            
                
        #friends
        #NOTE: work more on the non-user friends inf. in database
        
        for member in members:
            cursor.execute('SELECT user_id FROM users WHERE username = ?', (member,))
            user=cursor.fetchone()
            
            if not user: #if that friend doesnt have an account, add them with just a username
                cursor.execute('INSERT INTO users (username) VALUES (?)', (member,))
                connection.commit()
                user_id=cursor.lastrowid
                    
            else:
                user_id=user[0]
                
            cursor.execute('SELECT 1 FROM user_group WHERE group_id = ? AND user_id = ?', (group_id, user_id))
                
            if not cursor.fetchone():  #add friend to the group if not already a member
                    cursor.execute('INSERT INTO user_group (user_id, username, group_id, group_name) VALUES (?, ?, ?, ?)', (user_id, member, group_id, group_name))
                    connection.commit()
                    
                    
        if currency != "IRR":
                amount = convert_to_IRR(amount, date=date, from_c=currency)
                
        #insert the expenses:
        cursor.execute('''
                INSERT INTO group_expenses (group_id, groupname, payername, contributers, amount, category, date, description, split_type, proportions, shares, currency) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (group_id, group_name, payer_id, ",".join(members), amount, category, date, description, split_type, percentage, share, currency))
        
        expense_id = cursor.lastrowid
        
        #split expenses
        if split_type == "equally":
            amount_per_user = amount / len(members)
            for member in members:
                cursor.execute('''
                    INSERT INTO expense_user (expense_id, total_expense, username, amount_contributed, split_proportion, for_what, name)
                    VALUES (?, ?, ?, ?, ?, "group", ?)
                ''', (expense_id, amount, member, amount_per_user, amount_per_user / amount, group_name))
       
        elif split_type == "percentage":
            if not isinstance(percentage, list) or len(percentage) != len(members):
                raise ValueError("Percentage values must be provided as a list with the same length as the number of members.")
            for i, member in enumerate(members):
                amount_contributed = amount * (percentage[i] / 100)
                cursor.execute('''
                    INSERT INTO expense_user (expense_id, total_expense, username, amount_contributed, split_proportion, for_what, name)
                    VALUES (?, ?, ?, ?, ?, "group", ?)
                ''', (expense_id, amount, member, amount_contributed, amount_contributed / amount, group_name))
       
        elif split_type == "share":
            total_share = sum(share.values())
            for member, member_share in share.items():
                amount_contributed = amount * (member_share / total_share)
                cursor.execute('''
                    INSERT INTO expense_user (expense_id, total_expense, username, amount_contributed, split_proportion, for_what, name)
                    VALUES (?, ?, ?, ?, ?, "group", ?)
                ''', (expense_id, amount, member, amount_contributed, amount_contributed / amount, group_name))

        
        #members structure is needed/ i would add these part after changinf the db for friends
        
        
        row_count+=1
        
    connection.commit()
    connection.close()
    

