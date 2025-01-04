import sqlite3

def check_table_schema():
    # Open the connection first
    connection = sqlite3.connect("database.db")  # Replace with the actual path if needed
    cursor = connection.cursor()
    
    # Check the schema of the users table
    cursor.execute("PRAGMA table_info(users);")
    schema = cursor.fetchall()

    # Print the schema
    print("Schema of users table:")
    for column in schema:
        print(column)
    
    # Close the connection after all operations
    connection.close()

if __name__ == "__main__":
    check_table_schema()
