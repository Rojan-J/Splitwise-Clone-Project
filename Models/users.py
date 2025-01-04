import sqlite3

class Users:
    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
        self.balance = 0
        self.user_id=None
        
        #fetch user data from database if email is provided
        if email:
            self.load_from_database(email)

    def load_from_database(self,email):
        connection=sqlite3.connect("database.db")
        cursor=connection.cursor()
        #find a row where the email matches the email address passed to the Users object
        cursor.execute("SELECT user_id, username, email, balance FROM users WHERE email = ?", (email,))
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
    
    
