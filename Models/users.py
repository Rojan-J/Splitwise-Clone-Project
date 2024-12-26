import sqlite3

class Users:
    def __init__(self, name, email_adress):
        self.name = name
        self.email = email_adress
        self.balance = 0
        self.user_id=None
        
        #fetch user data from database if email is provided
        if email_adress:
            self.load_from_database()

    def load_from_database(self):
        connection=sqlite3.connect("database.db")
        cursor=connection.cursor()
        #find a row where the email matches the email address passed to the Users object
        cursor.execute("SELECT user_id, username, email, balance FROM users WHERE email = ?", (self.email,))
        #retrive the first row
        result = cursor.fetchone()

        #if row is found:
        if result:
            self.user_id, self.name, self.email, self.balance = result
        
        connection.close()
        
    def add_balance(self, amount):
        self.balance += amount

        #update database
        connection=sqlite3.connect("database.db")
        cursor=connection.cursor()
        cursor.execute("UPDATE users SET balance = ? WHERE user_id = ?", (self.balance, self.user_id))
        connection.commit()
        connection.close()


    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"User({self.name}, Balance: {self.balance})"