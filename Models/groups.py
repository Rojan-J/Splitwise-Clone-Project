
    
from users import Users
class Groups:
    def __init__(self, group_name):
        self.group_name = group_name
        self.members = dict()
        self.expenses = []
        self.debts =dict()

    def add_members(self, name, email):
        if name not in self.members:
            self.members[name] = email

    def add_expenses(self, expense, payer, contributers):
        self.expenses.append([expense, payer, contributers])
        self.cal_debts()

    def cal_debts(self):
        expense = self.expenses[-1]
        portion = expense[0]/len(expense[2])
        for contributer in expense[2]:
            if (contributer, expense[1]) not in self.debts.keys():
                self.debts[(contributer, expense[1])]= {"capacity": portion}
            else:
                self.debts[(contributer, expense[1])]["capacity"] += portion


