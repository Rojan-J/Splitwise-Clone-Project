import sqlite3

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
            

    def add_expenses(self, expense, payer, contributors):
        self.expenses.append([expense, payer, contributors])
        
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        # add expense
        cursor.execute("""
            INSERT INTO expenses (group_id, payer_id, amount, category, date) 
            VALUES (?, ?, ?, ?, date('now'))
        """, (self.group_id, payer, expense, "General"))
        expense_id = cursor.lastrowid

        for contributor in contributors:
            cursor.execute("""
                INSERT INTO expense_user (expense_id, user_id, amount_contributed)
                VALUES (?, ?, ?)
            """, (expense_id, contributor, expense / len(contributors)))

        connection.commit()
        connection.close()     
        
        self.cal_debts()

    def cal_debts(self):
        expense = self.expenses[-1]
        portion = expense[0]/len(expense[2])
        for contributer in expense[2]:
            if (contributer, expense[1]) not in self.debts.keys():
                self.debts[(contributer, expense[1])]= {"capacity": portion, "flow": 0}
            else:
                self.debts[(contributer, expense[1])]["capacity"] += portion






#test the database/ user, group connection

def main():
    group = Groups("Food")
    group.add_members("Rojan", "rojan@gmail.com")
    group.add_members("Niloo", "niloo@gmail.com.com")


    user = Users(email="rojan@gmail.com")
    print(user)

    group.add_expenses(100, user.user_id, [user.user_id,2])  # Rojan pays for all


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


