"""
Docstring for Assignment15.Program_1

Question 1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of 
each number.

"""

square_list = lambda list_of_numbers: list(map(lambda x: x**2, list_of_numbers))

def main():
    numbers = [10,20,30,40,50]
    print('Original list: ', numbers)
    squared_numbers = square_list(numbers)
    print('List of squares: ', squared_numbers)

if __name__ == "__main__":
    main()