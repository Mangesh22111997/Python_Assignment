"""
Docstring for Assignment31.Program_1

Please follow below rules while designing automation script as  
• Accept input through command line or through file. 
• Display any message in log file instead of console. 
• For separate task define separate function. 
• For robustness handle every expected exception. 
• Perform validations before taking any action. 
• Create user defined modules to store the functionality. 



Question: 1.Design automation script which accept directory name and file extension from user. Display all 
files with that extension. 
Usage : DirectoryFileSearch.py “Demo” “.txt” 
Demo is name of directory and .txt is the extension that we want to search.

"""
import os

def DirectoryFileSearch(directory, extension):
    if not os.path.isdir(directory):
        print(f'The directory: {directory} does not exist.')
        return
    
    else:
        for foldername, subfoler, file in os.walk(directory):
            for file in file:
                if file.endswith(extension):
                    print(f'{file} is found in {foldername}')
                    print(f'Full (Relative) path of the file is: {os.path.join(foldername, file)}')
                    print(f'Full (Absolute) path of the file is: {os.path.abspath(os.path.join(foldername, file))}')

                # else:
                #     print(f'{file} is not found in {foldername}')
    

def main():
    directory = input("Enter the directory name: ")
    extension = input("Enter the file extension: ")

    DirectoryFileSearch("Demo", ".txt")

if __name__ == "__main__":
    main()
