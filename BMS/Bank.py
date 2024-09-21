class Bank:
    def __init__(self):
        self.users=[]
        self.total_loan_amount=0
        self.loan_feature_enabled= True
    
    def register_user(self,user):
        self.users.append(user)

    def get_user_by_email(self,email):
        for user in self.users:
            if user.email == email:
                return user
        return None
    
    def get_total_balance(self):
        total_balance=sum( user.check_balance() for user in self.users)
        return total_balance
        
    def get_total_loan_amount(self):
        return self.total_loan_amount

    def enable_loan_feature(self):
        self.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.loan_feature_enabled = False