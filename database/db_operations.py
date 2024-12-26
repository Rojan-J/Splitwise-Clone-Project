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


    
    