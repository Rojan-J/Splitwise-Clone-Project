import sqlite3
import json
from datetime import date

from users import Users


import sys
import os
# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database"))
# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Utils\currency_conversion"))
# sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Core"))


sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Utils/currency_conversion"))
sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/Core"))

from debt_simplification import *

from db_operations import *

from currency_conversion_all_currencies import convert_to_IRR


class Groups:
    def __init__(self, group_name, group_owner, split = "equally", expenses = [], members = [], debts = dict(),default_shares=None, default_proportions=None):
        self.group_name = group_name
        self.group_id = None
        self.members = members
        self.expenses = expenses
        self.debts = debts
        self.simplified_debts = self.debts.copy()
        self.group_owner = group_owner
        
        self.split_type = split
        self.default_shares = default_shares if default_shares is not None else {}
        self.default_proportions = default_proportions if default_proportions is not None else {}
        
        self.load_from_database()
    

        
    def load_from_database(self):
        self.members= []
        connection=get_connection()
        cursor=connection.cursor()
        
        cursor.execute("SELECT group_id FROM groups WHERE group_name = ? and group_owner = ?", (self.group_name, self.group_owner, ))
        group = cursor.fetchone()
        print("LoadName", self.group_name)
        
        #check if group exists and fetch members of the group
        if group:
            self.group_id =group[0]
            cursor.execute("""
                SELECT u.username
                FROM users u
                JOIN user_group ug ON u.username = ug.username
                WHERE ug.group_name = ? 
            """, (self.group_name,))
            members = cursor.fetchall()
            
            for member in members:
                self.members.append(member[0])  #name=key, email=value
            
            print("LoadMembers", self.members)
            print("LoadId", self.group_id)
            
            all_expenses  =get_group_expenses_by_group_id(self.group_id)
            for expense in all_expenses:
                self.expenses.append([expense[1],expense[5], expense[3], expense[4], expense[7], expense[6], expense[8], expense[9], expense[10], expense[11]])
            print()

            all_debts = get_groups_debts_by_group_id(self.group_id)
            print(all_debts, "all_debts")
            for debt in all_debts:
                debtor = debt[2]
                creditor = debt[3]
                amount = debt[4]
                if (debtor, creditor) not in self.debts:
                    self.debts[(debtor, creditor)]= {"capacity": amount}
                else:
                    self.debts[(debtor, creditor)]["capacity"] += amount


        else:
            cursor.execute("INSERT INTO groups (group_name, group_owner) VALUES (?, ?)", (self.group_name, self.group_owner, ))
            
            self.group_id = cursor.lastrowid
            print(f"Group '{self.group_name}' created with group_id: {self.group_id}")
        connection.commit()
        connection.close()
        print(self.debts, "Still in load")  
        return

        
        
     

    def add_members(self, username, split, default_shares_j, default_prop_j):
        if username not in self.members:
            self.members.append(username)
            
            connection=get_connection()
            cursor=connection.cursor()
            
            # check if user already exists
            user = get_user_by_email (username, username)
            if user:
                user_id = user[0]
            else:
                add_user(username, username, "Defaultmail@mail.com", "DefaultPass0", 0, True, 0, True)
                cursor.execute("SELECT user_id FROM users WHERE username = ?", (username, ))
                user = cursor.fetchone()
                user_id = user[0]
            
            #add member to the group
            print_table_columns("user_group")
            cursor.execute("INSERT INTO user_group (user_id, username, group_id, group_name, default_split, default_shares, default_proportions) VALUES (?, ?, ?, ?, ?, ?, ?)", (user_id, username, self.group_id, self.group_name, split, default_shares_j, default_prop_j))
            connection.commit()
            connection.close()    
        return
            

    def add_expenses(self,label, expense, payer, contributors, expense_date = date.today(), category="etc.",description=None, split_type="equally", proportions=None, shares=None, currency = "IRR"):
        print(self.debts, "before_add")
        #contributors is a list of users represented by their ids who are sharing the expense
        #contributions is a list that hold each contributor's share
        #contributor represents the user's id who contributed
        #contribution represents the amount that the contributor has paid
                
        connection = get_connection()
        cursor = connection.cursor()

        
        #check if expenses are added correctly:
        print(f"Adding expense: group_id={self.group_id}, payer_id={payer}, amount={expense}, category={category}, date={expense_date}, shares={shares}, proportions={proportions}")

        json_shares = json.dumps(shares)
        json_proportions = json.dumps(proportions)

        # add expense
        cursor.execute("""
            INSERT INTO group_expenses (label, group_id,groupname, payername, contributers, amount, category, date, description, split_type, proportions, shares, currency) 
            VALUES (?, ?, ?, ?, ?, ?,?,?,?, ?, ?, ?, ?)
        """, (label, self.group_id, self.group_name, payer, ",".join(contributors), expense, category, str(expense_date), description , split_type, json_proportions, json_shares, currency))
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
                raise ValueError(f"Invalid split_type:{split_type}")
            total_share=sum(shares.values())
            contributions=[(contributor,float(expense)*(share/total_share))for contributor, share in shares.items()]
        
            
        else:
            raise ValueError(f"Invalid split_type:{split_type}")
        

            
        for contributor,contribution in contributions:
            if split_type == "share":
                share = f"{split_type} :{shares[contributor]}"

            elif split_type == "equally":
                share = "equal split"
            
            else:
                share = f"{split_type} :{proportions[contributor]}"
            proportion=contribution/float(expense)
                
            cursor.execute("""
                INSERT INTO expense_user (expense_id, total_expense,  username, amount_contributed, split_proportion, for_what, name, share, date, category)
                VALUES (?, ?, ?,?,?, "group", ?, ?, ?, ?)
            """, (expense_id, expense, contributor, contribution, proportion, self.group_name, share, expense_date, category))

        connection.commit()
        connection.close()
        print(self.debts, "before_cal_debts")     
        self.cal_debts(contributions, payer)
        print("Before Simplification: ", self.group_name, self.debts)
        debt_simplification = Debtsimplification(self)
        debt_simplification.creating_simplified_graph()
        update_group_debts(self.group_id, self.group_name)

        for (debtor, creditor), debt in self.simplified_debts.items():
            debt = debt["capacity"]
            if debtor != creditor:
                add_simplified_debt(self.group_id, self.group_name, debtor, creditor, debt)
        
        return

        
    def get_expenses_by_category(self):
        
        category_expenses={}
        connection=get_connection()
        cursor=connection.cursor()
        
        print(f"Retrieving expenses for group_id={self.group_id} and categorizing them.")
       
        cursor.execute("""
            SELECT category, SUM(amount)
            FROM group_expenses
            WHERE group_id = ? or groupname = ?
            GROUP BY category
        """, (self.group_id, self.group_name,))
        
        expense_by_category=cursor.fetchall()
        print("Expenses retrieved:", expense_by_category)
        
        for category, total_amount in expense_by_category:
            category_expenses[category] = total_amount
        
        
        connection.close()
        return category_expenses
    
    def get_total_expenses_of_group(self):

        connection=get_connection()
        cursor=connection.cursor()
        
        print(f"Retrieving expenses for group_id={self.group_id} and categorizing them.")
       
        cursor.execute("""
            SELECT SUM(amount)
            FROM group_expenses
            WHERE group_id = ? AND groupname = ?
        """, (self.group_id, self.group_name,))
        
        total_expenses=cursor.fetchone()
        
        
        connection.close()
        return total_expenses
        

    def cal_debts(self,contributions,payer):

        for contributor ,contribution in contributions:
            if contributor != payer:
                if (contributor, payer) not in self.debts:
                    self.debts[(contributor, payer)]= {"capacity": contribution}
                else:
                    self.debts[(contributor, payer)]["capacity"] += contribution

                add_debt(self.group_id, contributor,payer,contribution)
                
        print(self.debts, "In cal_debts")
        return
                
                
    def settle_debt(self,debtor,creditor,amount):
        if(debtor,creditor) not in self.debts:     #check if debtor owes to creditor
            return
        
        current_debt=self.debts[(debtor,creditor)]
        if amount>current_debt["capacity"]-current_debt["flow"]:
            print("Error: Amount exceeds the debt")
            
        current_debt["flow"]+=amount
        
        if current_debt["flow"]>=current_debt["capacity"]:
            self.debts.pop((debtor,creditor))
        return

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
    return


    
            


