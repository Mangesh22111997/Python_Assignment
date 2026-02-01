"""
Docstring for Assignment21.Program_2

Question: 2: Design a Python application that creates two threads.
• Thread 1 should calculate and display the maximum element from an list.
• Thread 2 should calculate and display the minimum element from the same list.
• The list should be accepted from the user.
"""

import threading


def user_defined_list():
    number_of_elements = int(input("Enter the number of elements in the list: "))
    numbers = []
    for i in range(number_of_elements):
        num = int(input(f"Enter element {i + 1}: "))
        numbers.append(num)
    return numbers

def max_number(n):
    num_max = n[0]

    for i in n:
        if i > num_max:
            num_max = i

    print(f"Maximum number in the list: {num_max}")      
   
def min_number(n):
    num_min = n[0]

    for i in n:
        if i < num_min:
            num_min = i

    print(f"Minimum number in the list: {num_min}")   


def main():
    numbers = user_defined_list()

    max_thread = threading.Thread(target=max_number, args=(numbers,))
    min_thread = threading.Thread(target=min_number, args=(numbers,))

    max_thread.start()
    min_thread.start()


if __name__ == "__main__":
    main()