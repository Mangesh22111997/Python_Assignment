"""
Docstring for Assignment20.Program_2

Question: 2: Design a Python application that creates two threads named EvenFactor and 
OddFactor.
• Both threads should accept one integer number as a parameter.
• The EvenFactor thread should:
    ◦ Identify all even factors of the given number.
    ◦ Calculate and display the sum of even factors.
• The OddFactor thread should:
    ◦ Identify all odd factors of the given number.
    ◦ Calculate and display the sum of odd factors.
• After both threads complete execution, the main thread should display the message: 
“Exit from main”
"""

import threading

def even_factors_and_sum(number):
    even_factors = [i for i in range(1, number + 1) if number % i == 0 and i % 2 == 0]
    even_sum = sum(even_factors)
    print(f"Even factors of {number}: {even_factors}")
    print(f"Sum of even factors: {even_sum}")

def odd_factors_and_sum(number):
    odd_factors = [i for i in range(1, number + 1) if number % i == 0 and i % 2 != 0]
    odd_sum = sum(odd_factors)
    print(f"Odd factors of {number}: {odd_factors}")
    print(f"Sum of odd factors: {odd_sum}")

if __name__ == "__main__":
    number = int(input("Enter an integer number: "))

    even_thread = threading.Thread(target=even_factors_and_sum, args=(number,))
    odd_thread = threading.Thread(target=odd_factors_and_sum, args=(number,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

    print("Exit from main")

