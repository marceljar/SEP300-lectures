class Account:
    def __init__(self, amount):
        self._balance = amount

    def display(self):
        return self._balance
    
    def change_balance(self, new_balance):
        self._balance = new_balance

checkings = Account(100)
print(checkings.display())
checkings.change_balance(150)
print(checkings.display())

print(checkings._balance) # works, but discouraged
checkings._balance = 200  # works, but discouraged
print(checkings._balance) 
