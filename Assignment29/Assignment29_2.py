"""
Docstring for Assignment29.Program_2

Question: Q2) Display File Contents
Problem Statement: 
Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the 
console.
Input: 
Demo.txt
Expected Output: 
Display contents of Demo.txt on console.

"""
import os

def display_file_contents(file_name):
    if (os.path.exists(file_name) == True):
        contents = open(file_name, 'r')
        print(contents.read())
        contents.close()

       
    else:
        print(f"The file '{file_name}' does not exist.")

def main():
    file_name = input("Enter the file name to display its contents: ")
    display_file_contents(file_name)

if __name__ == "__main__":
    main()