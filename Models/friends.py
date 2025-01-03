import sqlite3
import json
from datetime import date

from users import Users



import sys
import os
# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database"))
# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Utils\currency_conversion"))


sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Utils/currency_conversion"))
from db_operations import *

from currency_conversion_all_currencies import convert_to_IRR


class Friends:
    def __init__(self, username, friend_name, friends_email, friend_profile,  split = "equally", expenses = [], debts = dict()):
        print("'profile is", friend_profile)
        self.friend_name = friend_name
        self.friendship_id = None
        self.expenses = expenses
        self.debts = debts
        self.friend_email = friends_email
        self.friend_profile = friend_profile
        self.load_from_database(username)
        print(self.friend_name, self.friend_profile)


        
    def load_from_database(self, username):
        connection=get_connection()
        cursor=connection.cursor()
        
        cursor.execute("SELECT * FROM friends WHERE (friend_name = ? and username = ?) or (friend_name = ? and username = ?)", (self.friend_name, username, username, self.friend_name))
        friend = cursor.fetchone()
        print(friend)
        #check if group exists and fetch members of the group
        if friend:
            self.friendship_id = friend[0]
            self.friend_profile = friend[-1]
            
            all_expenses = get_friend_expenses_by_friendship_id(self.friendship_id)
            for expense in all_expenses:
                self.expenses.append([expense[1],expense[5], expense[3], expense[4], expense[7], expense[6], expense[8], expense[9], expense[10], expense[11]])

        else:
            cursor.execute("INSERT INTO friends (username, friend_name, friend_email, friend_profile) VALUES (?, ?, ?, ?)", (username, self.friend_name, self.friend_email, self.friend_profile, ))
            
            self.friendship_id = cursor.lastrowid
            print(f"friend '{self.friend_name}' created with friendship_id: {self.friendship_id}")
        connection.commit()
        connection.close()

        
        
        

    def add_friend(self, username, user_email, split = "equally", default_shares_j = None, default_proportions_j = None):
        add_friends(self.friendship_id, username, self.friend_name, self.friend_email, split, default_shares_j, default_proportions_j)
        connection=get_connection()
        cursor=connection.cursor()
        
        # check if user already exists
        friend = get_user_by_email (self.friend_email, self.friend_name)
        if friend:
            friend_id = friend[0]
        else:
            add_user(self.friend_name, self.friend_name, self.friend_email, "DefaultPass0", 0, True, 0, True)
            cursor.execute("SELECT user_id FROM users WHERE username = ?", (self.friend_name, ))
            friend = cursor.fetchone()
            friend_id = friend[0]

        
        #add member to the group
        add_friends(self.friendship_id, self.friend_name, username, user_email, split, default_shares_j, default_proportions_j)
        connection.commit()
        connection.close()    
            

    def add_expenses(self,label, expense, payer, contributors, expense_date = date.today(), category="etc.",description=None, split_type="equally", proportions=None, shares=None, currency = "IRR"):
        
        #contributors is a list of users represented by their ids who are sharing the expense
        #contributions is a list that hold each contributor's share
        #contributor represents the user's id who contributed
        #contribution represents the amount that the contributor has paid
                
        connection = get_connection()
        cursor = connection.cursor()

        
        #check if expenses are added correctly:
        print(f"Adding expense: friendship_id={self.friendship_id}, payer={payer}, amount={expense}, category={category}, date={expense_date}, shares={shares}, proportions={proportions}")

        json_shares = json.dumps(shares)
        json_proportions = json.dumps(proportions)

        # add expense
        cursor.execute("""
            INSERT INTO friend_expenses (label, friendship_id, payername, contributers, amount, category, date, description, split_type, proportions, shares, currency) 
            VALUES (?, ?, ?, ?, ?,?,?,?, ?, ?, ?, ?)
        """, (label, self.friendship_id, payer, ",".join(contributors), expense, category, str(expense_date), description , split_type, json_proportions, json_shares, currency))
        expense_id = cursor.lastrowid

        print(f"Expense added with ID: {expense_id}")
        
        contributions=[]
        if split_type=="equally":
            amount_per_user=float(expense)/len(contributors)
            contributions=[(contributor, amount_per_user) for contributor in contributors]
            
        elif split_type=="percentage":
            
            contributions=[(contributor,float(expense)*(percentage)) for contributor, percentage in proportions.items()]
            print(contributions)
            
        elif split_type=="share":
            if not shares or len(shares)!=len(contributors):
                total_share=sum(shares.values())
                contributions=[(contributor,float(expense)*(share/total_share))for contributor, share in shares.items()]
            
            
        else:
            raise ValueError(f"Invalid split_type:{split_type}")
        
        print(contributions)
            
        for contributor,contribution in contributions:
            if split_type == "share":
                share = f"{split_type} :{shares[contributor]}"

            elif split_type == "equally":
                share = "equal split"
            
            else:
                share = f"{split_type} :{proportions[contributor]}"
            proportion=contribution/float(expense)

            cursor.execute("SELECT friend_name FROM user_friends WHERE username = ?", (contributor, ))
            friend_name = cursor.fetchone()[0]
                
            cursor.execute("""
                INSERT INTO expense_user (expense_id, total_expense,  username, amount_contributed, split_proportion, for_what, name, share)
                VALUES (?, ?, ?,?,?, "friend", ?, ?)
            """, (expense_id, expense, contributor, contribution, proportion, friend_name, share))

        connection.commit()
        connection.close()     
        

        
    def get_expenses_by_category(self):
        
        category_expenses={}
        connection=get_connection()
        cursor=connection.cursor()
        
        print(f"Retrieving expenses for friendship_id={self.friendship_id} and categorizing them.")
       
        cursor.execute("""
            SELECT category, SUM(amount)
            FROM friend_expenses
            WHERE friendship_id = ?
            GROUP BY category
        """, (self.friendship_id,))
        
        expense_by_category=cursor.fetchall()
        print("Expenses retrieved:", expense_by_category)
        
        for category, total_amount in expense_by_category:
            category_expenses[category] = total_amount
        
        
        connection.close()
        return category_expenses
    
    def get_total_expenses_of_friend(self):

        connection=get_connection()
        cursor=connection.cursor()
        
        print(f"Retrieving expenses for friendship_id={self.friendship_id} and categorizing them.")
       
        cursor.execute("""
            SELECT SUM(amount)
            FROM friend_expenses
            WHERE friendship_id = ?
        """, (self.friendship_id, ))
        
        total_expenses=cursor.fetchone()
        
        
        connection.close()
        return total_expenses
        

    def cal_debts(self,contributions,payer):

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

def print_table_columns(table_name):
    connection = get_connection()
    cursor = connection.cursor()
    
    # Query the table's metadata
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    
    print(f"Columns in the table '{table_name}':")
    for column in columns:
        print(f"Column Name: {column[1]}, Data Type: {column[2]}")
    
    connection.close()

