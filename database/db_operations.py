import sqlite3

def get_connection():
    connection=sqlite3.connect("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database.db")

    connection.execute("PRAGMA foreign_keys=ON")  #enable foreign key support
    
    return connection

def add_user(name, username,email,password_hash,profile=0, is_registered=True, balance=0):
    connection=get_connection()
    cursor=connection.cursor()
    
    cursor.execute('''
        INSERT INTO users (name, username, email, password_hash, is_registered, profile, balance)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, username, email, password_hash, is_registered, profile, balance))
    
    connection.commit()
    connection.close()
    
def get_user_by_email (email, username):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE email = ? or username = ?
    ''', (email,username, ))
    
    #fetch the first matching row
    user=cursor.fetchone()
    connection.close()
    return user

def get_all_usernames():
    all_usernames = []

    connection=get_connection()
    cursor=connection.cursor()

    # Execute the query to fetch all usernames
    cursor.execute('SELECT username FROM users;')
    usernames = cursor.fetchall()

    for username in usernames:
        all_usernames.append(username[0])
    
    connection.close()
    return all_usernames


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
    
def add_temp_user_to_group(temp_user_id, group_id, temp_member_name, temp_member_email):
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
    

#to add a single user's contribution to an expense    
def add_contribution(expense_id,user_id,amount_contributed, split_proportion=None, share=None):
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
            INSERT INTO expense_user (expense_id, user_id, amount_contributed, split_proportion, share)
            VALUES (?, ?, ?, ?, ?)
        ''', (expense_id, user_id, amount_contributed, split_proportion, share))

    connection.commit()
    connection.close()
    
    
#to add contributions for multiple users based on their percentage shares 
def add_percentage_contributions(expense_id,user_contributions):
    connection=get_connection()
    cursor=connection.cursor()
    
    cursor.execute('''
        SELECT amount FROM expenses WHERE expense_id = ?
    ''', (expense_id,))
    expense = cursor.fetchone()
    
    total_amount = expense[0]
    
    total_percentage = sum(percentage for _, percentage in user_contributions)
    if total_percentage != 1.0:
        raise ValueError("Total percentage must sum up to 100% (1.0).")

    for user_id, percentage in user_contributions:
        amount_contributed = total_amount * percentage
        cursor.execute('''
            INSERT INTO expense_user (expense_id, user_id, amount_contributed, split_proportion)
            VALUES (?, ?, ?, ?)
        ''', (expense_id, user_id, amount_contributed, percentage))
    
    connection.commit()
    connection.close()
    
    
def add_share_contributions(expense_id, user_contributions):
    connection=get_connection()
    cursor=connection.cursor()
        
    cursor.execute('''
        SELECT amount FROM expenses WHERE expense_id = ?
    ''', (expense_id,))
    expense = cursor.fetchone()  
      
    total_amount = expense[0]
    total_shares = sum(share for _, share in user_contributions)
    
    for user_id, share in user_contributions:
        amount_contributed = (share / total_shares) * total_amount
        cursor.execute('''
            INSERT INTO expense_user (expense_id, user_id, amount_contributed, share)
            VALUES (?, ?, ?, ?)
        ''', (expense_id, user_id, amount_contributed, share))
    
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

def add_recurrent_expense(username, user_id, label, amount, days, category, paid = "Paid"):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO recurrent_expenses (username, user_id, label, days_of_month, amount, category, paid)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (username, user_id, label, days, amount, category, paid))
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

def update_name(user_name, new_name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE users SET name = ? WHERE username = ?
    ''', (new_name, user_name))
    connection.commit()
    connection.close()

    

def update_balance(user_name, balance):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE users SET balance = ? WHERE username = ?
    ''', (balance, user_name))
    connection.commit()
    connection.close()
    