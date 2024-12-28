import sqlite3

def initialize_database():
    connection=sqlite3.connect("database.db")  #create database file

    cursor=connection.cursor()  # to interact with the database
    
    # Drop tables if they already exist
    cursor.execute("DROP TABLE IF EXISTS debts;")
    cursor.execute("DROP TABLE IF EXISTS expense_user;")
    cursor.execute("DROP TABLE IF EXISTS expenses;")
    cursor.execute("DROP TABLE IF EXISTS user_group;")
    cursor.execute("DROP TABLE IF EXISTS groups;")
    cursor.execute("DROP TABLE IF EXISTS users;")
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            is_registered BOOLEAN DEFAULT TRUE,
            balance REAL DEFAULT 0     
        )
    ''')
    #unregistered users could have is_registered=FALSE

    # Create groups table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS groups (
            group_id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT NOT NULL
        )
    ''')

    # Create user-group relationship table 
    #primart key is to ensure that a user can only belong to a particular group once
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_group (
            user_id INTEGER,
            temp_user_id INTEGER,
            group_id INTEGER,
            temp_memmber_name TEXT,
            temp_member_email TEXT,
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            FOREIGN KEY(group_id) REFERENCES groups(group_id),
            PRIMARY KEY(user_id, group_id),
            UNIQUE(temp_user_id, group_id)  
        )
    ''')

    # Create expenses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_id INTEGER,
            payer_id INTEGER,
            amount REAL NOT NULL,
            category TEXT NOT NULL DEFAULT 'General',  -- Added category column,
            date TEXT NOT NULL,
            description TEXT,
            FOREIGN KEY(group_id) REFERENCES groups(group_id),
            FOREIGN KEY(payer_id) REFERENCES users(user_id)
        )
    ''')


    # Create expense-user relationship table (for tracking contributions)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expense_user (
            expense_id INTEGER,
            user_id INTEGER,
            temp_user_id INTEGER,
            amount_contributed REAL NOT NULL,
            split_proportion REAL,  -- Add this column,
            FOREIGN KEY(expense_id) REFERENCES expenses(expense_id),
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            PRIMARY KEY(expense_id, user_id),
            UNIQUE(temp_user_id, expense_id)
        )
    ''')


    # Create debt table (tracking debts between users)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS debts (
            debt_id INTEGER PRIMARY KEY AUTOINCREMENT,
            debtor_id INTEGER,
            creditor_id INTEGER,
            temp_debtor_id INTEGER,
            temp_creditor_id INTEGER,
            amount REAL NOT NULL,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY(debtor_id) REFERENCES users(user_id),
            FOREIGN KEY(creditor_id) REFERENCES users(user_id),
            UNIQUE(temp_debtor_id, temp_creditor_id)
        )
    ''')




    connection.commit()


    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        print(f"\nTable: {table[0]}")
        cursor.execute(f"SELECT * FROM {table[0]}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            
    connection.close()

initialize_database()