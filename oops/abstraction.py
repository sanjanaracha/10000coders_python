# Create an abstract class 'UPIPayment' with methods pay(amount) using the abc module to define the abstract method.
# Create subclasses: PhonePe, GooglePay, Paytm that inherit from UPIPayment.
# Implement the pay() method in each subclass to deduct the balance and print a payment message, hiding implementation details.
# Implement a check_balance() method in each subclass to show the remaining balance.
# Assign initial balances to each app (PhonePe: 5000, GooglePay: 3000, Paytm: 4000).
# Create objects of each subclass and call their methods to demonstrate payment and balance check functionalities.
# Ensure the abstract class 'UPIPayment' is not instantiated directly, following the principles of abstraction.
# The output should display the payment details, such as "Paid ■1000 using PhonePe", after a payment is made.


from abc import ABC,abstractmethod
class UPIPayment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def check_balance(self):
        pass

class PhonePe(UPIPayment):
    def __init__(self):
        self.balance=5000
    def pay(self,amount):
        self.balance-=amount
        print(f"paid {amount} using PhonePe")
    def check_balance(self):
        print(self.balance)

class GooglePay(UPIPayment):
    def __init__(self):
        self.balance=3000
    def pay(self,amount):
        self.balance-=amount
        print(f"paid {amount} using PhonePe")
    def check_balance(self):
        print(self.balance)

class Paytm(UPIPayment):

    def __init__(self):
        self.balance=4000
    def pay(self,amount):
        self.balance-=amount
        print(f"paid {amount} using PhonePe")
    def check_balance(self):
        print(self.balance)
c=input("select a payment type phonepe,googlepay,paytm:").lower()
amount=int(input("enter money:"))
if c=="phonepe":
    p=PhonePe()
    p.pay(amount)
    p.check_balance()
elif c=="googlepay":
    g=GooglePay()
    g.pay(amount)
    g.check_balance()
elif c=="paytm":
    pay=Paytm()
    pay.pay(amount)
    pay.check_balance()
else:
    print("enter correct payment method")