import sys
import os
sys.path.append(os.path.abspath(r"C:\Users\LENOVO\OneDrive\Documents\GitHub\Splitwise-Clone-Project\database"))

#sys.path.append(os.path.abspath("C:/Users/niloo/Term7/AP/Project/Splitwise-Clone-Project/database"))



from db_setup import initialize_database
from db_operations import add_user, get_user_by_email, add_group, get_all_groups


def main():
    initialize_database()
    

if __name__ == "__main__":
    main()
    
