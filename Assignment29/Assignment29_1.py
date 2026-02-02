"""
Docstring for Assignment29.Program_1

Question: Q1) Check File Exists in Current Directory
Problem Statement: 
Write a program which accepts a file name from the user and checks whether that file exists in the current 
directory or not.
Input: 
Demo.txt
Expected Output: 
Display whether Demo.txt exists or not.

"""
import os

def check_file_exists(file_name):
    return os.path.exists(file_name)

def main():
    file_name = input("Enter the file name to check: ")
    if check_file_exists(file_name):
        print(f"The file '{file_name}' exists in the current directory.")
    else:
        print(f"The file '{file_name}' does not exist in the current directory.")


if __name__ == "__main__":
    main()
