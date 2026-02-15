"""
Docstring for Assignment31.Program_2

Please follow below rules while designing automation script as  
• Accept input through command line or through file. 
• Display any message in log file instead of console. 
• For separate task define separate function. 
• For robustness handle every expected exception. 
• Perform validations before taking any action. 
• Create user defined modules to store the functionality. 



Question: 2. Design automation script which accept directory name and two file extensions from user. 
Rename all files with first file extension with the second file extenntion. 
Usage : DirectoryRename.py “Demo” “.txt” “.doc” 
Demo is name of directory and .txt is the extension that we want to search and rename 
with .doc. 
After execution this script each .txt file gets renamed as .doc.

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

    
def DirectoryRename(directory, old_extension, new_extension):
    DirectoryFileSearch(directory, old_extension)

    for foldername, subfolder, file in os.walk(directory):
        for file in file:
            if file.endswith(old_extension):
                old_file_path = os.path.join(foldername, file)
                new_file_name = file.replace(old_extension, new_extension)
                new_file_path = os.path.join(foldername, new_file_name)

                try:
                    os.rename(old_file_path, new_file_path)
                    print(f'{old_file_path} has been renamed to {new_file_path}')
                except Exception as e:
                    print(f'Error renaming {old_file_path}: {e}')
def main():
    directory = input("Enter the directory name: ")
    old_extension = input("Enter the old file extension: ")
    new_extension = input("Enter the new file extension: ")

    DirectoryRename(directory, old_extension, new_extension)

if __name__ == "__main__":
    main()
