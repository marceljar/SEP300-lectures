from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, amount):
        self.balance = amount

    @abstractmethod
    def pay(self, amount):
        pass   

class CreditCard(PaymentMethod):
    def pay(self, amount):
        self.balance -= amount
        print(f"Paid ${amount} using credit card.")

class DebitCard(PaymentMethod):
    def pay(self, amount):
        self.balance -= amount
        print(f"Paid ${amount} using debit card.")

class ETransfer(PaymentMethod):
    def pay(self, amount):
        self.balance -= amount
        print(f"Paid ${amount} using e-transfer.")

def read_balance(method):
    print(f"Current balance is {method.balance}")

payment_methods = [CreditCard(100), DebitCard(100), \
                   ETransfer(100) ]

for method in payment_methods:
    method.pay(20)

for method in payment_methods:
    read_balance(method)
