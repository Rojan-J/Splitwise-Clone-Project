import sqlite3

def check_table_schema():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()
    
    # Check the schema of the users table
    cursor.execute("PRAGMA table_info(users);")
    schema = cursor.fetchall()
    connection.close()
    
    # Print the schema
    print("Schema of users table:")
    for column in schema:
        print(column)
        
    

if __name__ == "__main__":
    check_table_schema()


