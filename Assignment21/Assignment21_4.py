"""
Docstring for Assignment21.Program_4

Question 4: Design a Python application that creates two threads.
• Thread 1 should compute the sum of elements from a list.
• Thread 2 should compute the product of elements from the same list.
• Return the results to the main thread and display them.
"""

import threading
from functools import reduce

def user_defined_list():
    number_of_elements = int(input("Enter the number of elements in the list: "))
    numbers = []
    for i in range(number_of_elements):
        num = int(input(f"Enter element {i + 1}: "))
        numbers.append(num)
    return numbers

sum_of_elements = lambda x, y: x + y
product_of_elements = lambda x, y: x * y

results = {}

def compute_sum(numbers):
    results['sum'] = reduce(sum_of_elements, numbers)

def compute_product(numbers):
    results['product'] = reduce(product_of_elements, numbers)

def main():
    numbers = user_defined_list()

    add_thread = threading.Thread(target=compute_sum, args=(numbers,))
    multiply_thread = threading.Thread(target=compute_product, args=(numbers,))

    add_thread.start()
    multiply_thread.start()

    add_thread.join()
    multiply_thread.join()

    print("Sum of elements:", results['sum'])
    print("Product of elements:", results['product'])

if __name__ == "__main__":
    main()