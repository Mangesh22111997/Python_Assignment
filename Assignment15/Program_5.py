"""
Docstring for Assignment15.Program_5

Question 5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum 
element.

"""

from functools import reduce


max_number = lambda a,b: a if a>b else b

def main():
    num_list = [22,23,45,67,78,90]
    maximum_number = reduce(max_number, num_list)
    print("The maximum number in the list is:", maximum_number)

if __name__ == "__main__":
    main()