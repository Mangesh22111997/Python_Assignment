"""
Docstring for Assignment30.Program_2

Please follow below rules while designing automation script as  
• Accept input through command line or through file. 
• Display any message in log file instead of console. 
• For separate task define separate function. 
• For robustness handle every expected exception. 
• Perform validations before taking any action. 
• Create user defined modules to store the functionality. 



Question: Q2) Count Words in a File
Problem Statement: 
Write a program which accepts a file name from the user and counts the total number of words in that file.
Input: 
Demo.txt
Expected Output: 
Total number of words in Demo.txt.

"""

import os

def count_words_in_file(file_name):
    if os.path.exists(file_name):
        file = open(file_name, 'r')
        content = file.read()
        words = content.split()
        file.close()
        return len(words)
    else:
        print(f"The file '{file_name}' does not exist.")
        return 0
    
def main():
    file_name = input("Enter the file name to count words: ")
    line_count = count_words_in_file(file_name)
    if line_count > 0:
        print(f"Total number of lines in '{file_name}': {line_count}")
    else:
        print("No lines counted as file is empty or does not exist.")

if __name__ == "__main__":
    main()
