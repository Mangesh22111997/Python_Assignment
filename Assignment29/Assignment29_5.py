"""
Docstring for Assignment29.Program_5

Question: Q5) Frequency of a String in File
Problem Statement: 
Write a program which accepts a file name and one string from the user and returns the frequency (count of 
occurrences) of that string in the file.
Input: 
Demo.txt Marvellous
Expected Output: 
Count how many times "Marvellous" appears in Demo.txt.

"""

import os
import sys

def check_file_exists(file_name):
    return os.path.exists(file_name)

def display_file_contents(file_name):
    if (os.path.exists(file_name) == True):
        contents = open(file_name, 'r')
        print(contents.read())
        contents.close()
    else:
        print(f"The file '{file_name}' does not exist.")

def copy_file_contents(source_file, dest_file="Demo.txt"):
    if not os.path.exists(source_file):
        print(f"The source file '{source_file}' does not exist.")
        return

    with open(source_file, 'r') as src:
        with open(dest_file, 'a') as dst:
            dst.write(src.read())
    
    print(f"Contents copied from '{source_file}' to '{dest_file}' successfully.")

def frequency_of_string_in_file(file_name='Demo.txt', search_string=''):
    if not os.path.exists(file_name):
        print(f"The file '{file_name}' does not exist.")
        return 0

    count = 0
    with open(file_name, 'r') as file:
        for word in file:
            count = count + word.count(search_string)
    
    return count

def main():
    # Accept command-line arguments
    if len(sys.argv) == 3:
        file_name = sys.argv[1]
        search_string = sys.argv[2]
    elif len(sys.argv) == 2:
        file_name = sys.argv[1]
        search_string = input("Enter the string to search for: ")
    else:
        file_name = input("Enter the file name to check: ")
        search_string = input("Enter the string to search for: ")
    
    if check_file_exists(file_name):
        print(f"The file '{file_name}' exists in the current directory.")
    else:
        print(f"The file '{file_name}' does not exist in the current directory.")

    display_file_contents(file_name)

    count = frequency_of_string_in_file(file_name, search_string)
    print(f"The string '{search_string}' appears {count} times in the file '{file_name}'.")

    


if __name__ == "__main__":
    main() 
