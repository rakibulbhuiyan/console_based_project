from abc import abstractmethod,ABC

class User(ABC):

    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
        self.balance=0
        self.transaction_history=[]
    
    @abstractmethod
    def create_account(self):
        pass
    
    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass
    
    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def transfer(self,recipient,amount):
        pass

    @abstractmethod
    def take_loan(self,amount):
        pass
    
    def get_transaction_history(self):
        return self.transaction_history
    
    @abstractmethod
    def authenticate(self,email,password):
        return self.email==email and  self.password==password
