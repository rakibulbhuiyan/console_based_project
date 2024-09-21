from Bank import Bank
from Admin import Admin
from Customer import Customer


def create_account(bank):
    print("\n--- Create an Account ---")
    print("1. Create Customer Account")
    print("2. Create Admin Account")
    print("3. Back")
    account_choice = int(input("Enter your choice: "))
    
    if account_choice==1:
        name     = input('Enter your name: ') 
        email    = input('Enter your email: ')  
        password = input('Enter your password: ') 
        customer = Customer(name,email,password)
        bank.register_user(customer)
        customer.create_account()
        print('customer account create successfully')
    if account_choice==2:
        name     = input('Enter your name: ') 
        email    = input('Enter your email: ') 
        password = input('Enter your password: ') 
        admin    = Admin(name,email,password)
        bank.register_user(admin)
        admin.create_account()
        print('admin account create successfully')
    if account_choice==3:
        pass
        print("Invalid choise. please try again")


def login(bank):

    while True:
        print("\n--- Login ---")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Back")
        login_choice = int(input("Enter your choice: "))

        if login_choice==1:
            email    = input("enter admin email: ")
            password = input("enter admin password: ")
            admin    = admin.get_user_by_email(email)
            if admin and admin.authenticate(email,password):
                print("login successfully")
                admin_menu(bank)
                break
            else:
                print("Invalid email or password.")
        elif login_choice == 2:
            email    = input("enter customer email: ")
            password = input("enter customer password: ")
            customer = customer.get_user_by_email(email)
            if customer and customer.authenticate(email,password):
                print(f"Customer {customer.name} logged in successfully.")
                customer_menu(bank)
                break
            else:
                print("Invalid email or password.")
        elif login_choice==3:
            break
        else:
            print("Invalid choice. try again")

def admin_menu(bank):
    print("\n--- Admin Menu ---")
    print("1. Create Account ")
    print("2. check total balance")
    print("3. checlk total loan amount ")
    print("4. toggle loan feature (on/off)")
    print("5. Logout")
    
    choice = int(input("Enter your choice: "))
    if choice==1:
        create_account(bank)
    elif choice==2:
        total_amount=bank.get_total_balance()
        print(f"Total Bank Balance: {total_amount} Taka")
    elif choice==3:
        total_loan_amount=bank.get_total_loan_balance()
        print(f"Total Bank Balance: {total_loan_amount} Taka")
    elif choice == 4:
            loan_feature_enabled = input("Enable or Disable Loan Feature (y/n): ")
            if loan_feature_enabled.lower() == 'y':
                bank.enable_loan_feature()
                print("Loan Feature Enabled.")
            else:
                bank.disable_loan_feature()
                print("Loan Feature Disabled.")
    elif choice==5:
        print("admin logged out.")
        break
    else:
        print("Invalid choice. please try again.")

def customer_menu(customer,bank):
    while True:
        print("\n--- Customer Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer Money")
        print("5. Take Loan")
        print("6. View Transaction History")
        print("7. Logout")
        choice = int(input("Enter your choice: "))





def main():
    bank=Bank()
    while True:
        print("\n--- Banking Management System ---")
        print("1. Create an Account")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice ==1:
            create_account(bank)
        elif choice ==2:
            login(bank)
        elif choice ==3:
            break
        else:
            print("Invalid choice ,please try again")




if __name__ == "__main__":
    main()