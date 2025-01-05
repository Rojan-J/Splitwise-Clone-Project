import sqlite3

def get_connection():
    # connection=sqlite3.connect("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database.db")
    connection=sqlite3.connect(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database.db")

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
    
# def get_user_by_email (email, username):
#     connection=get_connection()
#     cursor=connection.cursor()
#     cursor.execute('''
#         SELECT * FROM users WHERE email = ? or username = ?
#     ''', (email,username, ))

def get_user_by_email(email, username):
    try:
        # Debugging output
        print(f"Debugging `get_user_by_email`: email={email}, type={type(email)}, username={username}, type={type(username)}")
        
        # Ensure parameters are strings
        email = str(email) if email is not None else ""
        username = str(username) if username is not None else ""

        # Establish connection and execute query
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''
            SELECT * FROM users WHERE email = ? OR username = ?
        ''', (email, username))
        
        # Fetch the first matching row
        user = cursor.fetchone()
        print(f"Query result: {user}")
        return user

    except sqlite3.InterfaceError as e:
        print(f"SQLite InterfaceError: {e}")
    except Exception as e:
        print(f"Error in `get_user_by_email`: {e}")
    finally:
        if 'connection' in locals() and connection:
            connection.close()
    
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
      
    
def add_debt(group_id, debtor_id,creditor_id,amount):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO debts (group_id, debtor_name, creditor_name, amount)
        VALUES (?, ?, ?, ?)
    ''', (group_id, debtor_id, creditor_id, amount))
    connection.commit()
    connection.close()

def add_friend_debt(friendship_id, debtor_id,creditor_id,amount):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO friend_debts (friendship_id, debtor_name, creditor_name, amount)
        VALUES (?, ?, ?, ?)
    ''', (friendship_id, debtor_id, creditor_id, amount))
    connection.commit()
    connection.close()

def add_simplified_debt(group_id, group_name, debtor_name,creditor_name,amount):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO simplified_debts (id, name, debtor_name, creditor_name, amount, for_what)
        VALUES (?, ?, ?, ?, ?, "group")
    ''', (group_id, group_name, debtor_name, creditor_name, amount))
    connection.commit()
    connection.close()

def add_simplified_debt_friend(group_id, group_name, debtor_name,creditor_name,amount):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO simplified_debts (id, name, debtor_name, creditor_name, amount, for_what)
        VALUES (?, ?, ?, ?, ?, "friend")
    ''', (group_id, group_name, debtor_name, creditor_name, amount))
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
        UPDATE simplified_debts SET status = ? WHERE debt_id = ?
    ''', (status, debt_id))
    connection.commit()
    connection.close()

def update_group_debts(group_id, group_name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute ('''
        DELETE FROM simplified_debts
        WHERE id = ? and name = ?;
    ''', (group_id, group_name, ))
    connection.commit()
    connection.close()

def update_friend_debts(friendship_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute ('''
        DELETE FROM simplified_debts
        WHERE id = ?;
    ''', (friendship_id, ))
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

def get_balance(username):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT balance FROM users WHERE username = ?
    ''', (username, ))
    
    #fetch the first matching row
    balance=cursor.fetchall()
    connection.close()
    return balance[0]



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

def edit_friend_database(friendship_id, friend_profile, default_split, default_share, default_prop):
    print("Profile is:", friend_profile)
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        UPDATE friends
        SET friend_profile = ?
        WHERE friendship_id = ?;
    ''', (friend_profile, friendship_id, ))

    cursor.execute('''
        UPDATE user_friends
        SET default_split = ?, default_shares = ? , default_proportions = ?
        WHERE friendship_id = ?;
    ''', (default_split, default_share, default_prop, friendship_id, ))
    
    connection.commit()
    connection.close()


def get_groups_debts_by_group_id(group_id):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM debts WHERE group_id = ?
    ''', (group_id, ))
    
    #fetch the first matching row
    debts=cursor.fetchall()
    connection.close()
    return debts


def get_friend_debts_by_group_id(friendship_id):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM friend_debts WHERE friendship_id = ?
    ''', (friendship_id, ))
    
    #fetch the first matching row
    debts=cursor.fetchall()
    connection.close()
    return debts

def total_expenses_of_user(username):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM expense_user WHERE username = ?
    ''', (username, ))
    
    #fetch the first matching row
    expenses=cursor.fetchall()
    connection.close()
    return expenses

def total_user_owes(username):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM simplified_debts WHERE debtor_name = ? and (status = ? or status= ?)
    ''', (username,  "pending", "Not Paid!", ))

    owes=cursor.fetchall()
    connection.close()
    return owes

def total_user_owed(username):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM simplified_debts WHERE creditor_name = ? and (status = ? or status= ?)
    ''', (username, "pending", "Not Paid!",  ))
    
    #fetch the first matching row
    owes=cursor.fetchall()
    connection.close()
    return owes

def get_debt_creditor(debt_id):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT creditor_name FROM simplified_debts WHERE debt_id = ?
    ''', (debt_id, ))
    
    #fetch the first matching row
    creditor=cursor.fetchone()
    connection.close()
    return creditor[0]

def get_temp_creditor(username):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE username = ?
    ''', (username, ))
    
    #fetch the first matching row
    temp=cursor.fetchone()
    connection.close()
    return temp[-1]


def add_notification(username, sender, debt_id, amount):
    connection=get_connection()
    cursor=connection.cursor()
    
    cursor.execute('''
        INSERT INTO user_notification (username, debt_id, sender, amount)
        VALUES (?, ?, ?, ?)
    ''', (username,debt_id, sender, amount))
    
    connection.commit()
    connection.close()


def get_user_notifications(username):
    connection=get_connection()
    cursor=connection.cursor()
    cursor.execute('''
        SELECT * FROM user_notification WHERE username = ? and checked = ?
    ''', (username, 0))
    
    #fetch the first matching row
    messages =cursor.fetchall()
    connection.close()
    return messages

def update_notification_status(username):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE user_notification SET check = ? WHERE username = ?
    ''', (1, username, ))
    connection.commit()
    connection.close()