"""
Docstring for Assignment15.Program_6

Question 6. Write a lambda function using reduce() which accepts a list of numbers and returns the minimum 
element.

"""


from functools import reduce


min_number = lambda a,b: a if a<b else b

def main():
    num_list = [22,23,45,67,78,90]
    minimum_number = reduce(min_number, num_list)
    print("The minimum number in the list is:", minimum_number)

if __name__ == "__main__":
    main()