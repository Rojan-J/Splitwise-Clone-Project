import sqlite3

def initialize_database():
    connection=sqlite3.connect("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database.db")  #create database file
    # connection=sqlite3.connect(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database.db")

    

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
            group_id INTEGER,
            group_name TEXT NOT NULL,
            default_split TEXT DEFAULT 'equally',
            default_shares TEXT,
            default_proportions TEXT,
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            
            PRIMARY KEY(user_id, group_id)

        )
    ''')
     # Create expenses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS group_expenses (
            expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
            label TEXT NOT NULL,
            group_id INTEGER,
            groupname TEXT NOT NULL,
            payername TEXT NOT NULL,
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
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            share REAL,  -- Share for share-based splits,
            FOREIGN KEY(username) REFERENCES users(username)
        )
    ''')


    # Create debt table (tracking debts between users)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS debts (
            debt_id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_id INTEGER,
            debtor_name INTEGER,
            creditor_name INTEGER,
            amount REAL NOT NULL,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY(debtor_name) REFERENCES users(username),
            FOREIGN KEY(creditor_name) REFERENCES users(username)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS simplified_debts (
            debt_id INTEGER PRIMARY KEY AUTOINCREMENT,
            for_what TEXT NOT NULL,
            id Integer TEXT NOT NULL,
            name TEXT NOT NULL, 
            debtor_name TEXT NOT NULL, 
            creditor_name TEXT,
            amount REAL NOT NULL,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY(debtor_name) REFERENCES users(username),
            FOREIGN KEY(creditor_name) REFERENCES users(username)
                   

        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS friend_debts (
            debt_id INTEGER PRIMARY KEY AUTOINCREMENT,
            friendship_id INTEGER,
            debtor_name TEXT NOT NULL,
            creditor_name TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT DEFAULT 'pending',
            FOREIGN KEY(debtor_name) REFERENCES users(username),
            FOREIGN KEY(creditor_name) REFERENCES users(username)
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
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS friends (
            friendship_id INTEGER PRIMARY KEY AUTOINCREMENT,
            friend_name TEXT NOT NULL,
            friend_email TEXT NOT NULL,
            username TEXT NOT NULL,
            friend_profile INTEGER,

            FOREIGN KEY(username) REFERENCES users(username)    
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_friends (
            friendship_id INTEGER,
            username TEXT NOT NULL,
            friend_name TEXT NOT NULL,
            friend_email TEXT NOT NULL,
            default_split TEXT DEFAULT 'equally',
            default_shares TEXT,
            default_proportions TEXT,
            FOREIGN KEY(username) REFERENCES users(username),
            FOREIGN KEY(friendship_id) REFERENCES friends(friendship_id)  
        )
    ''')


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS friend_expenses (
            expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
            label TEXT NOT NULL,
            friendship_id INTEGER,
            payername TEXT NOT NULL,
            contributers TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL DEFAULT 'etc.',  -- Added category column,
            date TEXT NOT NULL,
            description TEXT,
            split_type TEXT DEFAULT 'equally',
            proportions TEXT,
            shares TEXT,
            currency TEXT DEFAULT 'IRR',
            FOREIGN KEY(friendship_id) REFERENCES friends(friendship_id)

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