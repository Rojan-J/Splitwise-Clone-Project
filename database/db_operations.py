import sqlite3

def get_connection():
    connection=sqlite3.connect("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database.db")

    connection.execute("PRAGMA foreign_keys=ON")  #enable foreign key support
    
    return connection

def add_user(name, username,email,password_hash,profile=0, is_registered=True, balance=0, temp = False):
    connection=get_connection()
    cursor=connection.cursor()
    
    cursor.execute('''
        INSERT INTO users (name, username, email, password_hash, is_registered, profile, balance, temp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, username, email, password_hash, is_registered, profile, balance, temp))
    
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

def add_friends(friendship_id, user_name, friends_name, friend_email,  default_split = "equally", default_shares_j = None, default_proportions_j = None):
    connection = get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        INSERT INTO user_friends (friendship_id, username, friend_name, friend_email, default_split, default_shares, default_proportions) 
        VALUES (?, ?, ?,?, ?, ?, ?)
    ''', (friendship_id, user_name, friends_name,friend_email, default_split, default_shares_j, default_proportions_j, ))
    connection.commit()
    connection.close()

def get_friend_expenses_by_friendship_id(friendship_id):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM friend_expenses WHERE friendship_id = ?
    ''', (friendship_id, ))
    
    #fetch the first matching row
    expenses=cursor.fetchall()
    connection.close()
    return expenses



def get_all_groups():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM groups')
    groups = cursor.fetchall()
    connection.close()
    return groups

def add_user_to_group(user_id,username, group_id, groupname):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO user_group (user_id,username, group_id, groupname)
        VALUES (?, ?, ?, ?)
    ''', (user_id,username, group_id, groupname))
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
    
    
    
def add_expanse(group_id, groupname, payername, contributers, amount, category, date, description=None, split_type = "equally", proportions = None, shares = None):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO group_expenses (group_id,groupname, payername, contributers, amount, category, date, description, split_type, proportions, shares)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (group_id, groupname, payername, contributers, amount, category, date, description, split_type, proportions, shares))
    connection.commit()
    connection.close()
    

#to add a single user's contribution to an expense    
def add_contribution(expense_id, total_expense, username,amount_contributed, groupname, split_proportion=None, share=None, for_what = "groups"):
    connection = get_connection()
    cursor = connection.cursor()
    
    cursor.execute('''
            INSERT INTO expense_user (expense_id, total_expense,  username, amount_contributed, split_proportion, for_what, name)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (expense_id, total_expense, username, amount_contributed,split_proportion, for_what, groupname))

    connection.commit()
    connection.close()

def get_groups_by_username(username):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM user_group WHERE username = ?
    ''', (username, ))
    
    #fetch the first matching row
    groups=cursor.fetchall()
    connection.close()
    return groups

def get_group_expenses_by_group_id(group_id):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM group_expenses WHERE group_id = ?
    ''', (group_id, ))
    
    #fetch the first matching row
    expenses=cursor.fetchall()
    connection.close()
    return expenses
    
    
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


def get_recurrent_expense_by_username(username):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM recurrent_expenses WHERE username = ?
    ''', (username, ))
    
    #fetch the first matching row
    recurrent=cursor.fetchall()
    connection.close()
    return recurrent

def get_expenses_of_grp_by_grp_id(group_id):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM group_expenses WHERE group_id = ?
    ''', (group_id, ))
    
    #fetch the first matching row
    expenses=cursor.fetchall()
    connection.close()
    return expenses

def get_expenses_of_friend_by_friendship_id(friendship_id):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM friend_expenses WHERE friendship_id = ?
    ''', (friendship_id, ))
    
    #fetch the first matching row
    expenses=cursor.fetchall()
    connection.close()
    return expenses

def get_default_split(group_id, group_name):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM user_group WHERE group_id = ? AND group_name = ?
    ''', (group_id,  group_name))
    
    #fetch the first matching row
    defaults=cursor.fetchone()
    connection.close()
    return defaults

def get_default_split_friend(frienship_id, friend_name):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM user_friends WHERE friendship_id = ? AND friend_name = ?
    ''', (frienship_id,  friend_name))
    
    #fetch the first matching row
    defaults=cursor.fetchone()
    connection.close()
    return defaults



def get_friends_by_username(username):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM user_friends WHERE username = ?
    ''', (username, ))
    
    #fetch the first matching row
    friends=cursor.fetchall()
    connection.close()
    return friends

def get_friends_profile_by_friendship_id(friendship_id):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT friend_profile FROM friends WHERE friendship_id = ?
    ''', (friendship_id, ))
    
    #fetch the first matching row
    friend =cursor.fetchone()
    connection.close()
    return friend