import openpyxl
import pandas as pd
from datetime import datetime
from sqlite3 import IntegrityError #to catch specififc errors in data
from db_operations import get_connection


def import_from_excel(file_path):
    data=pd.read_excel(file_path)
    
    required_col=["group_name","members","payer_id","amount","category","date","description","split_type","percentage","share"]
    
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
        #i would add this part after I changed the friends structure table in database
        
        
        #split expenses
        
        #members structure is needed/ i would add these part after changinf the db for friends
        
        
        row_count+=1
        
    connection.commit()
    connection.close()
    

