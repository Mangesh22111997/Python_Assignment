"""
Docstring for Assignment20.Program_1

Question: 1: Design a Python application that creates two separate threads named Even and Odd.
• The Even thread should display the first 10 even numbers.
• The Odd thread should display the first 10 odd numbers.
• Both threads should execute independently using the threading module.
• Ensure proper thread creation and execution.

"""

import threading

def print_even_numbers():
    for i in range(0, 20, 2):
        print(f"Even: {i}")

def print_odd_numbers():
    for i in range(1, 20, 2):
        print(f"Odd: {i}")

if __name__ == "__main__":
    even_thread = threading.Thread(target=print_even_numbers)
    odd_thread = threading.Thread(target=print_odd_numbers)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()