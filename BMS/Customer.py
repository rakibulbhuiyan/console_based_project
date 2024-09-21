from User import User

class Customer(User):

    def create_customer(self):
        print(f"Customer {self.name} with {self.email} has created an account")
    
    def deposit(self,amount):
        self.balance +=amount
        self.transection_history.appen(f"Deposit {amount} Taka")
    
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance -=amount
            self.transaction_history.append(f"Withdraw {amount} Taka")
            return True
        else:
            print("Insufficient balance. Cannot withdraw.")
            return False
    
    def check_balance(self):
        return self.balance

    def take_loan(self,amount):
        if amount <= 2*self.balance:
            self.balance +=amount
            self.transaction_history.append(f"Took a loan of {amount} Taka")
            return True
        else:
            print("Loan amount exceeds twice your balance.")
            return False


    
