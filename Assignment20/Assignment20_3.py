"""
Docstring for Assignment20.Program_3

Question:3: Design a Python application that creates two threads named EvenList and OddList.
• Both threads should accept a list of integers as input.
• The EvenList thread should:
◦ Extract all even elements from the list.
◦ Calculate and display their sum.
• The OddList thread should:
◦ Extract all odd elements from the list.
◦ Calculate and display their sum.
• Threads should run concurrently
"""

import threading

def EvenList(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    even_sum = sum(even_numbers)
    print(f"Even numbers: {even_numbers}")
    print(f"Sum of even numbers: {even_sum}")

def OddList(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    odd_sum = sum(odd_numbers)
    print(f"Odd numbers: {odd_numbers}")
    print(f"Sum of odd numbers: {odd_sum}")

def main():
    number_of_elements = int(input("Enter the number of elements in the list: "))
    numbers = []
    for i in range(number_of_elements):
        num = int(input(f"Enter element {i + 1}: "))
        numbers.append(num)

    even_thread = threading.Thread(target=EvenList, args=(numbers,))
    odd_thread = threading.Thread(target=OddList, args=(numbers,))

    even_thread.start()
    odd_thread.start()          

    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()