class Account():
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance        
        
    def deposit(self, amount):

        self.balance = self.balance + amount
        print(f'Added {amount} to the balance')
        
    def withdraw(self,amount):
       
        if amount <= self.balance:
            self.balance = self.balance - amount
            print (f'Withdrawl approved')
        else:
            print(f'You do not have enough funds!')
            
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'