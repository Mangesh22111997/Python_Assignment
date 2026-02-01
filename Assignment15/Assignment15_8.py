"""
Docstring for Assignment15.Program_8

Question 8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers 
divisible by both 3 and 5.

"""

divisible_by_3_5 = lambda x: x%3 == 0 and x%5 == 0

def main():
    numbers = [10, 15, 23, 30, 45, 60, 77, 90, 100, 120]
    result = list(filter(divisible_by_3_5, numbers))
    print("Numbers divisible by both 3 and 5 are:", result)

if __name__ == "__main__":
    main()