import sqlite3
from datetime import date

from users import Users

class Groups:
    def __init__(self, group_name):
        self.group_name = group_name
        self.group_id=None
        self.members = dict()
        self.expenses = []
        self.debts =dict()
        
        self.load_from_database()
        
    def load_from_database(self):
        connection=sqlite3.connect("database.db")
        cursor=connection.cursor()
        
        cursor.execute("SELECT group_id FROM groups WHERE group_name = ?", (self.group_name,))
        group = cursor.fetchone()
        
        #check if group exists and fetch members of the group
        if group:
            self.group_id = group[0]

        else:
            cursor.execute("INSERT INTO groups (group_name) VALUES (?)", (self.group_name,))
            self.group_id = cursor.lastrowid
            print(f"Group '{self.group_name}' created with group_id: {self.group_id}")

            
        cursor.execute("""
            SELECT u.user_id, u.username, u.email 
            FROM users u
            JOIN user_group ug ON u.user_id = ug.user_id
            WHERE ug.group_id = ?
        """, (self.group_id,))
        members = cursor.fetchall()
        
        for member in members:
            self.members[member[1]] = member[2]  #name=key, email=value
        
        connection.close()

        
        
        

    def add_members(self, name, email):
        if name not in self.members:
            self.members[name] = email
            
            connection=sqlite3.connect("database.db")
            cursor=connection.cursor()
            
            # check if user already exists
            cursor.execute("SELECT user_id FROM users WHERE email = ?", (email,))
            user = cursor.fetchone()

            if user:
                user_id = user[0]
            else:
                cursor.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)", 
               (name, email, "placeholder_hash"))
                user_id = cursor.lastrowid
            
            #add member to the group
            cursor.execute("INSERT INTO user_group (user_id, group_id) VALUES (?, ?)", (user_id, self.group_id))
            connection.commit()
            connection.close()    
            

    def add_expenses(self, expense, payer, contributors, category="General", split_type="equally", proportions=None):
        
        #contributors is a list of users represented by their ids who are sharing the expense
        #contributions is a list that hold each contributor's share
        #contributor represents the user's id who contributed
        #contribution represents the amount that the contributor has paid
        
        self.expenses.append([expense, payer, contributors,category])
        
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        #check if expenses are added correctly:
        print(f"Adding expense: group_id={self.group_id}, payer_id={payer}, amount={expense}, category={category}, date={date.today()}")

        # add expense
        cursor.execute("""
            INSERT INTO expenses (group_id, payer_id, amount, category, date) 
            VALUES (?, ?, ?, ?, date('now'))
        """, (self.group_id, payer, expense, category))
        expense_id = cursor.lastrowid

        print(f"Expense added with ID: {expense_id}")
        
        contributions=[]
        if split_type=="equally":
            amount_per_user=expense/len(contributors)
            contributions=[(contributor, amount_per_user) for contributor in contributors]
            
        elif split_type=="percentage":
            if not proportions or len(proportions)!=len(contributors):
                raise ValueError("proportionss must match the number of contributors for expense split.")
            
            contributions=[(contributor,expense*(percentage)) for contributor, percentage in zip(contributors, proportions)]
            
        for contributor,contribution in contributions:
            cursor.execute("""
                INSERT INTO expense_user (expense_id, user_id, amount_contributed)
                VALUES (?, ?, ?)
            """, (expense_id, contributor, contribution))

        connection.commit()
        connection.close()     
        
        self.cal_debts(contributions,payer)
        
    def get_expenses_by_category(self):
        
        category_expenses={}
        connection=sqlite3.connect("database.db")
        cursor=connection.cursor()
        
        print(f"Retrieving expenses for group_id={self.group_id} and categorizing them.")
       
        cursor.execute("""
            SELECT category, SUM(amount)
            FROM expenses
            WHERE group_id = ?
            GROUP BY category
        """, (self.group_id,))
        
        expense_by_category=cursor.fetchall()
        print("Expenses retrieved:", expense_by_category)
        
        for category, total_amount in expense_by_category:
            category_expenses[category] = total_amount
        
        
        connection.close()
        return category_expenses
        

    def cal_debts(self,contributions,payer):
        # expense = self.expenses[-1]
        # portion = expense[0]/len(expense[2])
        for contributor ,contribution in contributions:
            if (contributor, payer) not in self.debts:
                self.debts[(contributor, payer)]= {"capacity": contribution, "flow": 0}
            else:
                self.debts[(contributor, payer)]["capacity"] += contribution
                
                
                
    def settle_debt(self,debtor,creditor,amount):
        if(debtor,creditor) not in self.debts:     #check if debtor owes to creditor
            return
        
        current_debt=self.debts[(debtor,creditor)]
        if amount>current_debt["capacity"]-current_debt["flow"]:
            print("Error: Amount exceeds the debt")
            
        current_debt["flow"]+=amount
        
        if current_debt["flow"]>=current_debt["capacity"]:
            self.debts.pop((debtor,creditor))           
            
        
            


reset_expenses_for_testing = True


def clear_expenses(group_id):
    if not reset_expenses_for_testing:
        print("test mode is off- skipping clearing expenses")
        return
    
    connection=sqlite3.connect("database.db")
    cursor=connection.cursor()
    
    cursor.execute("DELETE FROM expense_user WHERE expense_id IN (SELECT expense_id FROM expenses WHERE group_id = ?)", (group_id,))
    cursor.execute("DELETE FROM expenses WHERE group_id = ?", (group_id,))
    
    connection.commit()
    connection.close()
    print(f"Cleared expenses for group_id={group_id}.")

#test the database/ user, group connection

def main():
    group = Groups("Food")
    
    clear_expenses(group.group_id)
    group.add_members("Rojan", "rojan@gmail.com")
    group.add_members("Niloo", "niloo@gmail.com.com")


    user = Users(email="rojan@gmail.com")
    print(user)

    group.add_expenses(100, user.user_id, [user.user_id,2], category="Food",split_type="percentage",proportions=[60,40])  # Rojan pays for all

    expense_report=group.get_expenses_by_category()
    print("expense by category:")
    print("Expenses by category:")
    category_expenses = group.get_expenses_by_category()
    
    if category_expenses:
        for category, total_amount in category_expenses.items():
            print(f"  {category}: {total_amount}")
    else:
        print("No expenses by category found.")

# def update_balance(user_id, new_balance):
#     connection = sqlite3.connect("database.db")
#     cursor = connection.cursor()

#     # Update the balance for the given user
#     cursor.execute("UPDATE users SET balance = ? WHERE user_id = ?", (new_balance, user_id))

#     connection.commit()
#     connection.close()

# # Example usage: update Rojan's balance to 50
# update_balance(1, 50.0)

if __name__ == "__main__":
    main()


