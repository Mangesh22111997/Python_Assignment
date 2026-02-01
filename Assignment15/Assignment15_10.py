"""
Docstring for Assignment15.Program_10

Question 10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even 
numbers

"""

even_number = lambda x: x % 2 == 0

def main():
    numbers = [10, 15, 22, 33, 42, 55, 60, 77, 80, 91]
    ever_numbers_list = list(filter(even_number, numbers))
    count_of_even_numbers = len(ever_numbers_list)
    print("Count of even numbers in the list is:", count_of_even_numbers)

if __name__ == "__main__":
    main()