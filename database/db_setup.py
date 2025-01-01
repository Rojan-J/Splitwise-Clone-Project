import sqlite3

def initialize_database():
    connection=sqlite3.connect("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database.db")  #create database file

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
            name TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            is_registered BOOLEAN DEFAULT TRUE,
            profile INTEGER DEFAULT 0,
            balance REAL DEFAULT 0,
            temp BOOLEAN DEFAULT FALSE
 
        )
    ''')
    #unregistered users could have is_registered=FALSE

    # Create groups table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS groups (
            group_id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name TEXT NOT NULL,
            group_owner TEXT NOT NULL
        )
    ''')

    # Create user-group relationship table 
    #primart key is to ensure that a user can only belong to a particular group once
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_group (
            user_id INTEGER,
            username TEXT NOT NULL,
            group_id INTEGER ,
            group_name TEXT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            
            PRIMARY KEY(user_id, group_id)

        )
    ''')
     # Create expenses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS group_expenses (
            expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_id INTEGER,
            groupname TEXT NOT NULL,
            payername INTEGER,
            contributers TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL DEFAULT 'etc.',  -- Added category column,
            date TEXT NOT NULL,
            description TEXT,
            split_type TEXT DEFAULT 'equally',
            proportions TEXT,
            shares TEXT,
            currency TEXT DEFAULT 'IRR',
            FOREIGN KEY(group_id) REFERENCES groups(group_id)

        )
    ''')

    # Create expense-user relationship table (for tracking contributions)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expense_user (
            expense_id INTEGER,
            total_expense REAL NOT NULL,
            username TEXT NOT NULL,
            amount_contributed REAL NOT NULL,
            split_proportion REAL,  -- Add this column,
            for_what TEXT NOT NULL,
            name TEXT NOT NULL,
            share REAL,  -- Share for share-based splits,
            FOREIGN KEY(expense_id) REFERENCES group_expenses(expense_id),
            FOREIGN KEY(username) REFERENCES users(username)
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

    #Create Recurrnt Expenses for user

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recurrent_expenses (
            username TEXT NOT NULL,
            user_id INTEGER,
            label TEXT NOT NULL,
            expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
            days_of_month TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            paid TEXT NOT NULL DEFAULT 'Paid',
            FOREIGN KEY(username) REFERENCES users(username),
            FOREIGN KEY(user_id) REFERENCES users(user_id)
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