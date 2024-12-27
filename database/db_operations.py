import sqlite3

def get_connection():
    return sqlite3.connect("database.db")

def add_user(username,email,password_hash, is_registered=True):
    connection=get_connection()
    cursor=connection.cursor()
    
    cursor.execute('''
        INSERT INTO users (username, email, password_hash, is_registered)
        VALUES (?, ?, ?, ?)
    ''', (username, email, password_hash, is_registered))
    
    connection.commit()
    connection.close()
    
    
def get_user_by_email (email):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE email = ?
    ''', (email,))
    
    #fetch the first matching row
    user=cursor.fetchone()
    connection.close()
    return user


def add_group(group_name):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        INSERT INTO groups (group_name)
        VALUES (?)
    ''', (group_name,))
    connection.commit()
    connection.close()
    
    
def get_all_groups():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM groups')
    groups = cursor.fetchall()
    connection.close()
    return groups

def add_user_to_group(user_id,group_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO user_group (user_id, group_id)
        VALUES (?, ?)
    ''', (user_id, group_id))
    connection.commit()
    connection.close()
    
def add_temp_user_tto_group(temp_user_id, group_id, temp_member_name, temp_member_email):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO user_group (temp_user_id, group_id, temp_memmber_name, temp_member_email)
        VALUES (?, ?, ?, ?)
    ''', (temp_user_id, group_id, temp_member_name, temp_member_email))
    connection.commit()
    connection.close()
    
    
    
def add_expanse(group_id,payer_id,amount,category,date,description=None):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO expenses (group_id, payer_id, amount, category, date, description)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (group_id, payer_id, amount, category, date, description))
    connection.commit()
    connection.close()
    
    
def add_contribution(expense_id,user_id,amount_contributed):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO expense_user (expense_id, user_id, amount_contributed)
        VALUES (?, ?, ?)
    ''', (expense_id, user_id, amount_contributed))
    connection.commit()
    connection.close()
    
    
def add_debt(debtor_id,creditor_id,amount):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO debts (debtor_id, creditor_id, amount)
        VALUES (?, ?, ?)
    ''', (debtor_id, creditor_id, amount))
    connection.commit()
    connection.close()
    

def update_debt_status(debt_id,status):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE debts SET status = ? WHERE debt_id = ?
    ''', (status, debt_id))
    connection.commit()
    connection.close()
    
    