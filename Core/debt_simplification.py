import sys
import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..","Models")))
sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Models"))
sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\Core"))



from users import Users
from graph import Graph


class Debtsimplification:
    def __init__(self, group):
        self.group=group
        self.simplified_debts=[]
        
        
    def calculate_balances(self):
        net_balance={user:0 for user in self.group.members}
        print(self.group.members, self.group.debts, "CHeck")
        
        for(u,v), debt in self.group.debts.items():  #u and v are debtor and creditor
            net_balance[u]-= debt["capacity"]
            net_balance[v]+= debt["capacity"]
            
        return net_balance
    
    def split_creditors_and_debtors(self, net_balance):
        creditors=[]
        debtord=[]
        for user, balance in net_balance.items():
            if balance>0:
                creditors.append((user,balance))
                
            elif balance<0:
                debtord.append((user,-balance))
                
        return creditors,debtord
    
    def simplify(self,creditors,debtors):
        simplified_debts=[]
        
        while creditors and debtors:
            debtor, debt_amount=debtors.pop(0)
            creditor, credit_amount=creditors.pop(0)
            
            settled_amount=min(debt_amount,credit_amount)
            simplified_debts.append((debtor,creditor,settled_amount))
            
            if debt_amount>settled_amount:
                debtors.insert(0,(debtor,debt_amount-settled_amount))
            elif credit_amount>settled_amount:
                creditors.insert(0,(creditor,credit_amount-settled_amount))
            
        return simplified_debts
    
    
    def upgrade_group_debts(self,simplified_debts):
        self.group.simplified_debts.clear()
        for debtor,creditor,amount in simplified_debts:
            if(debtor,creditor) not in self.group.simplified_debts:
                self.group.simplified_debts[(debtor,creditor)]={"capacity":amount}
                
            else:
                self.group.simplified_debts[(debtor,creditor)]["capacity"]+=amount
                        
            
    def final_simplifying(self):
        
        net_balance=self.calculate_balances()
        
        creditors,debtors=self.split_creditors_and_debtors(net_balance)
        
        simplified_debts=self.simplify(creditors,debtors)
        
        self.upgrade_group_debts(simplified_debts)

    def creating_simplified_graph(self):
        self.final_simplifying()
        simplified_graph = Graph(self.group)
        simplified_graph.graph_type = "simplified"
        simplified_graph.plot_graph() 
               
            

