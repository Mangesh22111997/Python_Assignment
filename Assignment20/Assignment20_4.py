"""
Docstring for Assignment20.Program_4

4: Design a Python application that creates three threads named Small, Capital, and 
Digits.
• All threads should accept a string as input.
• The Small thread should count and display the number of lowercase characters.
• The Capital thread should count and display the number of uppercase characters.
• The Digits thread should count and display the number of numeric digits.
• Each thread must also display:
◦ Thread ID
◦ Thread Name
"""

import threading
import os

def small_char_count(string):
    count = 0
    for i in string:
        if i.islower():
            count += 1
    print('Count of small characters:', count)
    main_pid = os.getpid()
    main_tid = threading.get_ident()
    print(f"Main thread in process PID: {main_pid}, Thread ID: {main_tid}")

def capital_char_count(string):
    count = 0
    for i in string:
        if i.isupper():
            count += 1
    print('Count of capital characters:', count)
    main_pid = os.getpid()
    main_tid = threading.get_ident()
    print(f"Main thread in process PID: {main_pid}, Thread ID: {main_tid}")

def digit_count(string):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    print('Count of digits:', count)
    main_pid = os.getpid()
    main_tid = threading.get_ident()
    print(f"Main thread in process PID: {main_pid}, Thread ID: {main_tid}")

def main():
    input_string = input('Enter a string: ')

    small_thread = threading.Thread(target=small_char_count, args=(input_string,), name='SmallThread')
    capital_thread = threading.Thread(target=capital_char_count, args=(input_string,), name='CapitalThread') 
    digit_thread = threading.Thread(target=digit_count, args=(input_string,), name='DigitThread')

    print('Thread ID and Name:')

    small_thread.start()
    capital_thread.start()
    digit_thread.start()

    small_thread.join()
    capital_thread.join()
    digit_thread.join()

if __name__ == "__main__":
    main()  
        

