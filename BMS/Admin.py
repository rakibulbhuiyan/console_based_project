from User import User


class Admin(User):
    def create_account(self):
        print(f"Admin {self.name} with email {self.email} has created an account.")
    
    def deposit(self,amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount} Taka as an Admin.")
    
    def withdraw(self,amount):
        print("admin cannot withdraw money.")
    
    def check_balance(self):
        return self.balance
    
    def transfer(self, recipient, amount):
        print("Admin cannot transfer money.")

    def take_loan(self, amount):
        print("Admin cannot take a loan.")
