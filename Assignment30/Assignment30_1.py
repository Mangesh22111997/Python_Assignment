"""
Please follow below rules while designing automation script as  
• Accept input through command line or through file. 
• Display any message in log file instead of console. 
• For separate task define separate function. 
• For robustness handle every expected exception. 
• Perform validations before taking any action. 
• Create user defined modules to store the functionality. 


Docstring for Assignment30.Program_1

Question: Q1) Count Lines in a File
Problem Statement: 
Write a program which accepts a file name from the user and counts how many lines are present in the file.
Input: 
Demo.txt
Expected Output: 
Total number of lines in Demo.txt.

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
    
def main():
    file_name = input("Enter the file name to count lines: ")
    line_count = count_lines_in_file(file_name)
    if line_count > 0:
        print(f"Total number of lines in '{file_name}': {line_count}")
    else:
        print("No lines counted as file is empty or does not exist.")

if __name__ == "__main__":
    main()
