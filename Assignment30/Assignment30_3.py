"""
Docstring for Assignment30.Program_3

Please follow below rules while designing automation script as  
• Accept input through command line or through file. 
• Display any message in log file instead of console. 
• For separate task define separate function. 
• For robustness handle every expected exception. 
• Perform validations before taking any action. 
• Create user defined modules to store the functionality. 



Question: Q3) Display File Line by Line
Input: 
Demo.txt
Problem Statement: 
Write a program which accepts a file name from the user and displays the contents of the file line by line on the 
screen.
Expected Output: 
Display each line of Demo.txt one by one.

"""

import os

def count_lines_in_file(file_name):
    if os.path.exists(file_name):
        file = open(file_name, 'r')
        lines = file.readlines()
        file.close()
        return len(lines)
    else:
        print(f"The file '{file_name}' does not exist.")
        return 0
    
def display_file_contents(file_name):
    if (os.path.exists(file_name) == True):
        contents = open(file_name, 'r')
        print(contents.read())
        contents.close()
    else:
        print(f"The file '{file_name}' does not exist.")

def main():
    file_name = input("Enter the file name to count lines: ")
    line_count = count_lines_in_file(file_name)
    if line_count > 0:
        print(f"Total number of lines in '{file_name}': {line_count}")
        print("-"*30)
        display_file_contents(file_name)
        print("-"*30)
    else:
        print("No lines counted as file is empty or does not exist.")

if __name__ == "__main__":
    main()
