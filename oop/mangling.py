class Account:
    def __init__(self, amount):
        self.__balance = amount

    def display(self):
        return self.__balance
    
    def change_balance(self, new_balance):
        self.__balance = new_balance

checkings = Account(100)
print(checkings.display())
checkings.change_balance(150)
print(checkings.display())

# print(checkings.__balance) # error due to name mangling
print(checkings._Account__balance) # works, but discouraged
checkings._Account__balance = 200  # works, but discouraged
print(checkings._Account__balance) # works, but discouraged
