"""
Docstring for Assignment15.Program_4

Question 4. Write a lambda function using reduce() which accepts a list of numbers and returns the addition of 
all elements.

"""

from functools import reduce

Add = lambda x, y: x + y

def main():
    numbers = [1, 2, 3, 4, 5]
    addition = reduce(Add, numbers)
    print("The addition of all elements in the list is:", addition)

if __name__ == "__main__":
    main()