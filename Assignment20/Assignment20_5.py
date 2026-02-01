"""
Docstring for Assignment20.Program_5

Question: 5: Design a Python application that creates two threads named Thread1 and Thread2.
• Thread1 should display numbers from 1 to 50.
• Thread2 should display numbers from 50 to 1 in reverse order.
• Ensure that:
◦ Thread2 starts execution only after Thread1 has completed.
• Use appropriate thread synchronization
"""

import threading

def display_numbers_1_to_50():
    for i in range(1, 51):
        print(i)

def display_numbers_50_to_1():
    for i in range(50, 0, -1):
        print(i)

if __name__ == "__main__":
    thread1 = threading.Thread(target=display_numbers_1_to_50)
    thread2 = threading.Thread(target=display_numbers_50_to_1)

    thread1.start()
    thread1.join()  # Ensure thread2 starts only after thread1 completes

    thread2.start()
    thread2.join()