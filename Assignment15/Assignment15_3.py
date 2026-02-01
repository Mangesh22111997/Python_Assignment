"""
Docstring for Assignment15.Program_3

Question 3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd 
numbers.

"""

odd_list = lambda list_of_numbers: list(filter(lambda x: x % 2 == 1, list_of_numbers))

def main():
    numbers = [11, 12, 13, 14, 15, 16, 20, 30, 40, 50]
    print('Original list: ', numbers)
    odd_numbers = odd_list(numbers)
    print('List of odd numbers: ', odd_numbers)

if __name__ == "__main__":
    main()