"""
Docstring for Assignment15.Program_2

Question 2. Write a lambda function using filter() which accepts a list of numbers and returns a list of even 
numbers.

"""

even_list = lambda list_of_numbers: list(filter(lambda x: x % 2 == 0, list_of_numbers))

def main():
    numbers = [11, 12, 13, 14, 15, 16, 20, 30, 40, 50]
    print('Original list: ', numbers)
    even_numbers = even_list(numbers)
    print('List of even numbers: ', even_numbers)

if __name__ == "__main__":
    main()