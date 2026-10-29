# Bank Account Class
# Create a class BankAccount
# It should have:
# account_holder
# balance
# 
# Methods:
# deposit(amount)
# withdraw(amount)
# display_balance()
# 
# Test by depositing and withdrawing money

class BankAccount:
    def __init__(self, account_holder,__balance):
        self.account_holder = account_holder
        self.__balance = __balance

    def withdraw(self,amount_to_be_withdrawn):
        self.__balance = self.__balance - amount_to_be_withdrawn
        return self.__balance

    def deposit(self,amount_to_be_deposited):
        self.__balance = self.__balance + amount_to_be_deposited
        return self.__balance

    def display_balance(self):
        print(f"Your Current Balance is: {self.__balance}")

    def displayinfo(self):
        print(f"Account Holder Name: {self.account_holder}")
        print(f"Currect Balance: {self.__balance}")

p1 = BankAccount("Anand",120)

p1.displayinfo()

print(f"Your remaining balance after withdraw is: {p1.withdraw(10)}")

print(f"Your total balance balance after adding is: {p1.deposit(500)}")

p1.display_balance()

