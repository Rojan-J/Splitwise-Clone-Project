class Users:
    def __init__(self, name, email_adress):
        self.name = name
        self.email = email_adress
        self.balance = 0

    def add_balance(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"User({self.name}, Balance: {self.balance})"

