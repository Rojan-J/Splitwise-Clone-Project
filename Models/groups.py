
    
from users import Users
class Groups:
    def __init__(self, group_name):
        self.group_name = group_name
        self.members = []
        self.expenses = []
        self.debts = []

    def add_members(self, name, email):
        if Users(name, email) not in self.members:
            self.members.append(Users(name, email))

    def add_expenses(self, expense, payer, contributers):
        self.expenses.append([expense, payer, contributers])

    def cal_debts(self):
        for expense in self.expenses:
            portion = expense[0]/len(expense[2])
            for contributer in expense[2]:
                self.debts.append((contributer, expense[1], portion))
