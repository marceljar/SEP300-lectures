from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass   # Every payment method must implement this


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using credit card.")

class DebitCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using debit card.")

class ETransfer(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using e-transfer.")

class FakeCard(PaymentMethod):
    def display(self):
        print(f"My balance is ${self.balance}.")

# abstractObject = PaymentMethod() # error
# abstractObject = FakeCard() # error 

choice = input("Choose a payment method (C for credit, \
                D for debit, or E for e-transfer: ")
if choice == 'C':
    method = CreditCard()
elif choice == 'D':
    method = DebitCard()
elif choice == 'E':
    method = ETransfer()
else:
    print(" Invalid payment method")

method.pay(100)
