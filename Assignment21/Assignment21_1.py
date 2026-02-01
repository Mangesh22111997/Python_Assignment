"""
Docstring for Assignment21.Program_1

Question:1: Design a Python application that creates two threads named Prime and NonPrime.
• Both threads should accept a list of integers.
• The Prime thread should display all prime numbers from the list.
• The NonPrime thread should display all non-prime numbers from the list.

"""
import threading


def user_defined_list():
    number_of_elements = int(input("Enter the number of elements in the list: "))
    numbers = []
    for i in range(number_of_elements):
        num = int(input(f"Enter element {i + 1}: "))
        numbers.append(num)
    return numbers

def isPrime(n):
    if n <= 1:
        return False

    # Check divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True
                            
def main():
    numbers = user_defined_list()

    def print_prime_numbers():
        print("Prime numbers in the list:")
        for num in numbers:
            if isPrime(num):
                print(num)

    def print_non_prime_numbers():
        print("Non-prime numbers in the list:")
        for num in numbers:
            if not isPrime(num):
                print(num)

    prime_thread = threading.Thread(target=print_prime_numbers)
    non_prime_thread = threading.Thread(target=print_non_prime_numbers)

    prime_thread.start()
    non_prime_thread.start()

    prime_thread.join()
    non_prime_thread.join()

if __name__ == "__main__":
    main()