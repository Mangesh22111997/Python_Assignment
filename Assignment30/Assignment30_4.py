"""
Docstring for Assignment30.Program_4

Please follow below rules while designing automation script as  
• Accept input through command line or through file. 
• Display any message in log file instead of console. 
• For separate task define separate function. 
• For robustness handle every expected exception. 
• Perform validations before taking any action. 
• Create user defined modules to store the functionality. 



Question: Q4) Copy File Contents into Another File
Problem Statement: 
Write a program which accepts two file names from the user.
• First file is an existing file
• Second file is a new file
Copy all contents from the first file into the second file.
Input: 
ABC.txt Demo.txt
Expected Output: 
Contents of ABC.txt copied into Demo.txt.

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

def copy_file_contents(source_file, dest_file):
    if not os.path.exists(source_file):
        print(f"The source file '{source_file}' does not exist.")
        return
    else:
        source_file_content = open(source_file, 'r')
        content = source_file_content.read()
        source_file_content.close()
        
        dest_file_content = open(dest_file, 'a')
        dest_file_content.write(content)
        dest_file_content.close()
        
        print(f"Contents copied from '{source_file}' to '{dest_file}' successfully.")


def main():
    source_file = input("Enter the source file name: ")
    dest_file = input("Enter the destination file name: ")

    line_count = count_lines_in_file(source_file)
    if line_count > 0:
        print(f"Total number of lines in '{source_file}': {line_count}")
        print("-"*30)
        display_file_contents(source_file)
        print("-"*30)
        copy_file_contents(source_file, dest_file)
    else:
        print("No lines counted as file is empty or does not exist.")

    copy_file_contents(source_file, dest_file)

if __name__ == "__main__":
    main()

    
