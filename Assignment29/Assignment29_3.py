"""
Docstring for Assignment29.Program_3

Question: Q3) Copy File Contents into a New File (Command Line)
Input (Command Line): 
ABC.txt
Problem Statement: 
Write a program which accepts an existing file name through command line arguments, creates a new file 
named Demo.txt, and copies all contents from the given file into Demo.txt.
Expected Output: 
Create Demo.txt and copy contents of ABC.txt into Demo.txt

"""

import os

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

def main():
    file_name = input("Enter the file name to check: ")
    if check_file_exists(file_name):
        print(f"The file '{file_name}' exists in the current directory.")
    else:
        print(f"The file '{file_name}' does not exist in the current directory.")

    display_file_contents(file_name)

    copy_file_contents(file_name)


if __name__ == "__main__":
    main()