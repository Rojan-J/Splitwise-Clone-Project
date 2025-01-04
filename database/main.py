from db_setup import initialize_database
from db_operations import add_user, get_user_by_email, add_group, get_all_groups


def main():
    initialize_database()

    #test the database
    add_user("Rojan", "rojan@gmail.com", "rojanj")
    add_user("Niloo", "niloofar@gmail.com", "niloot")
    add_group("food")

    user = get_user_by_email("rojan@gmail.com")
    print("Retrieved User:", user)

    groups = get_all_groups()
    print("Groups:", groups)
    

if __name__ == "__main__":
    main()
    
