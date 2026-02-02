"""
Docstring for Assignment23.Program_3

Question: 3: Write a Python program to implement a class named Numbers with the following 
specifications:
• The class should contain one instance variable:
◦ Value
• Define a constructor (__init__) that accepts a number from the user and initializes Value.
• Implement the following instance methods:
◦ ChkPrime() – returns True if the number is prime, otherwise returns False
◦ ChkPerfect() – returns True if the number is perfect, otherwise returns False
◦ Factors() – displays all factors of the number
◦ SumFactors() – returns the sum of all factors 
(You may use this method as a helper in ChkPerfect() if required)
• Create multiple objects and call all methods.

"""

from functools import reduce


class Numbers:
    def __init__(self, Value):
        self.Value = Value  # Instance variable for the number

    def ChkPrime(self):
        if self.Value <= 1:
            return False  # Numbers <= 1 are not prime

        # Loop through numbers from 2 to n-1
        for i in range(2, self.Value):
            if self.Value % i == 0:  # Check divisibility
                return False

        # if no divisor found then its a Prime Number
        return True
    
    def Factors(self):
        factors = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors.append(i)
        print(f"Factors of {self.Value}: {factors}")
        return factors
    
    def SumFactors(self):
        sum_of_factors = 0
        factors_list = self.Factors()  # Get the list of factors
        sum_of_factors = reduce(lambda x, y: x + y, factors_list)  # Sum them up

        return sum_of_factors
    
    def ChkPerfect(self):
        sum_of_factors = self.SumFactors() - self.Value  # Exclude the number itself
        if sum_of_factors == self.Value:
            return True
        else:
            return False
    

obj1 = Numbers(6)
print(f"Is {obj1.Value} Prime? {obj1.ChkPrime()}")
print(f"Factors of {obj1.Value}: ", end="")
obj1.Factors()
print(f"Sum of Factors of {obj1.Value}: {obj1.SumFactors()}")
print(f"Is {obj1.Value} Perfect? {obj1.ChkPerfect()}")


