"""
Docstring for Assignment15.Program_9

Question 9. Write a lambda function using reduce() which accepts a list of numbers and returns the product of all 
elements.

"""
from functools import reduce

product = lambda a,b: a*b

def main():
    numbers = [1,2,3,4,5]
    product_of_elements = reduce(product, numbers)
    print("The product of all elements in the list is:", product_of_elements)

if __name__ == "__main__":
    main()