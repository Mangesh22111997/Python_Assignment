"""
Docstring for Assignment30.Program_5

Please follow below rules while designing automation script as  
• Accept input through command line or through file. 
• Display any message in log file instead of console. 
• For separate task define separate function. 
• For robustness handle every expected exception. 
• Perform validations before taking any action. 
• Create user defined modules to store the functionality. 



Question: Q5) Search a Word in File
Problem Statement: 
Write a program which accepts a file name and a word from the user and checks whether that word is present in 
the file or not.
Input: 
Demo.txt Marvellous
Expected Output: 
Display whether the word Marvellous is found in Demo.txt or not.

"""

import os

def search_word_in_file(file_name , search_word):
    if not os.path.exists(file_name):
        print(f"The file '{file_name}' does not exist.")
        return False

    file_content = open(file_name, 'r')
    file_content = file_content.read()

    if search_word in file_content:
        return True
    
    return False

def main():
    file_name = input("Enter the file name: ")
    search_word = input("Enter the word to search for: ")

    found = search_word_in_file(file_name, search_word)

    if found:
        print(f"The word '{search_word}' is found in the file '{file_name}'.")
    else:
        print(f"The word '{search_word}' is NOT found in the file '{file_name}'.")

if __name__ == "__main__":
    main()  