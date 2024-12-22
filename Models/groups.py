
    
from users import Users
class Groups:
    def __init__(self, group_name):
        self.group_name = group_name
        self.members = []
        self.expenses = []

    def add_members(self, name, email):
        if Users(name, email) not in self.members:
            self.members.append(Users(name, email))

    def add_expenses(self, expense):
        self.expenses.append(expense)

    def calculate_balances(self):
        pass