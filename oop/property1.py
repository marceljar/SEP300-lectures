class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        print(f"Balance fetched through getter")
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        print(f"Balance set to: {amount} via setter")
        self.__balance = amount

checkings = Account(100)
print(checkings.balance)   # looks like a variable access

checkings.balance = 200    # looks like an assignment
print(checkings.balance)   # looks like a variable access
