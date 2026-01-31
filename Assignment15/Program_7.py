"""
Docstring for Assignment15.Program_7

Question 7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings 
having length greater than 5.

"""

strings = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grapefruit"]

result = list(filter(lambda s: len(s) > 5, strings))

print("Strings with length greater than 5:", result)