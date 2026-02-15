"""
Docstring for Assignment32.Program_1

Question: 1.Design automation script which accept directory name and display checksum of all files. 
Usage : DirectoryChecksum.py “Demo” 
Demo is name of directory.

"""
import sys
import os
import hashlib


def main():
    if len(sys.argv) != 2:
        print("Usage: DirectoryChecksum.py <directory_name>")
        return
    
    else:
        directory_name = sys.argv[1]
        if not os.path.exists(directory_name):
            print(f'The directory: {directory_name} does not exist.')
            return
        
        else:
            for foldername, subfolder, files in os.walk(directory_name):
                for file in files:
                    file_path = os.path.join(foldername, file)
                    try:
                        with open(file_path, 'rb') as f:
                            file_data = f.read()
                            checksum = hashlib.md5(file_data).hexdigest()
                            print(f'File: {file_path} Checksum: {checksum}')
                    except Exception as e:
                        print(f'Error processing file {file_path}: {e}')

if __name__ == "__main__":
    main()