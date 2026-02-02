"""
Docstring for Assignment22.Program_1

Question:1: Write a Python program to implement a class named Demo with the following 
specifications:
• The class should contain two instance variables: no1 and no2.
• The class should contain one class variable named Value.
• Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
• Implement two instance methods:
◦ Fun() – displays the values of instance variables no1 and no2.
◦ Gun() – displays the values of instance variables no1 and no2.
Create two objects of the Demo class as follows:

Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)
Call the instance methods in the given sequence: 

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()
"""

class Demo:
    Value = 0  # Class variable

    def __init__(self, No1, No2):
        self.no1 = No1  # Instance variable
        self.no2 = No2  # Instance variable

    def Fun(self):
        print('Inside Fun method')
        print('Value of no1: ', self.no1)
        print('Value of no2: ', self.no2)

    def Gun(self):
        print('Inside Gun method')
        print('Value of no1: ', self.no1)
        print('Value of no2: ', self.no2)

Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)


Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()

