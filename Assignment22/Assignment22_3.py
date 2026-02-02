"""
Docstring for Assignment22.Program_3

Question:3: Write a Python program to implement a class named Arithmetic with the following 
characteristics:
• The class should contain two instance variables: Value1 and Value2.
• Define a constructor (__init__) that initializes all instance variables to 0.
• Implement the following instance methods:
◦ Accept() – accepts values for Value1 and Value2 from the user.
◦ Addition() – returns the addition of Value1 and Value2.
◦ Subtraction() – returns the subtraction of Value1 and Value2.
◦ Multiplication() – returns the multiplication of Value1 and Value2.
◦ Division() – returns the division of Value1 and Value2 (handle division by zero 
properly).
• Create multiple objects of the Arithmetic class and invoke all the instance methods.

"""

class Arithmetic:
    def __init__(self):
        self.Value1 = 0  # Instance variable
        self.Value2 = 0  # Instance variable

    def Accept(self):
        self.Value1 = int(input("Enter the first value (Value1): "))
        self.Value2 = int(input("Enter the second value (Value2): "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Error: Division by zero is not allowed."
        

obj1 = Arithmetic()
obj2 = Arithmetic()
obj3 = Arithmetic()

obj1.Accept()
print(f"Addition: {obj1.Addition()}")
print(f"Subtraction: {obj1.Subtraction()}")
print(f"Multiplication: {obj1.Multiplication()}")
print(f"Division: {obj1.Division()}")

obj2.Accept()
print(f"Addition: {obj2.Addition()}")
print(f"Subtraction: {obj2.Subtraction()}")
print(f"Multiplication: {obj2.Multiplication()}")
print(f"Division: {obj2.Division()}")

obj3.Accept()
print(f"Addition: {obj3.Addition()}")
print(f"Subtraction: {obj3.Subtraction()}")
print(f"Multiplication: {obj3.Multiplication()}")
