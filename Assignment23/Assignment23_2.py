"""
Docstring for Assignment23.Program_2

Question: 2:  Write a Python program to implement a class named BankAccount with the following 
requirements:
• The class should contain two instance variables:
◦ Name (Account holder name)
◦ Amount (Account balance)
• The class should contain one class variable:
◦ ROI (Rate of Interest), initialized to 10.5
• Define a constructor (__init__) that accepts Name and initial Amount.
• Implement the following instance methods:
◦ Display() – displays account holder name and current balance
◦ Deposit() – accepts an amount from the user and adds it to balance
◦ Withdraw() – accepts an amount from the user and subtracts it from balance 
(Ensure withdrawal is allowed only if sufficient balance exists)
◦ CalculateInterest() – calculates and returns interest using formula: 
Interest = (Amount * ROI) / 100
• Create multiple objects and demonstrate all methods.
"""

class BankAccount:
    ROI = 10.5 # Class variable for Rate of Interest

    def __init__(self, Name, Amount):
        self.Name = Name  # Instance variable for account holder name
        self.Amount = Amount  # Instance variable for account balance

    def Display(self):
        print(f"Account Holder: {self.Name}, Current Balance: {self.Amount}")

    def Deposit(self):
        deposit_amount = float(input("Enter amount to deposit: "))
        self.Amount = self.Amount + deposit_amount
        print(f"Deposited: {deposit_amount}. New Balance: {self.Amount}")

    def Withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= self.Amount:
            self.Amount = self.Amount - withdraw_amount
            print(f"Withdrew: {withdraw_amount}. New Balance: {self.Amount}")
        else:
            print("Insufficient balance for withdrawal.")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest
    

obj1 = BankAccount("Alice", 1000)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
interest1 = obj1.CalculateInterest()
print(f"Interest for {obj1.Name}: {interest1}")

obj2 = BankAccount("Bob", 2000)
obj2.Display()
obj2.Deposit()
obj2.Withdraw()
interest2 = obj2.CalculateInterest()
print(f"Interest for {obj2.Name}: {interest2}")

obj3 = BankAccount("Charlie", 1500)
obj3.Display()
obj3.Deposit()
obj3.Withdraw()
interest3 = obj3.CalculateInterest()
print(f"Interest for {obj3.Name}: {interest3}")