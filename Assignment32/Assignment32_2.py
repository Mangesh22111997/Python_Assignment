"""
Docstring for Assignment32.Program_2

Question: 2. Design automation script which accept directory name and write names of duplicate files from 
that directory into log file named as Log.txt. Log.txt file should be created into current 
directory. 
Usage : DirectoryDusplicate.py “Demo” 
Demo is name of directory.

"""

import sys
import os
import hashlib

def main():
    if len(sys.argv) != 2:
        print("Usage: DirectoryDuplicate.py <directory_name>")
        return
    
    else:
        if not os.path.exists(sys.argv[1]):
            print(f'The directory: {sys.argv[1]} does not exist.')
            return
        
        else:
            directory_name = sys.argv[1]

            for foldername, subfolder, files in os.walk(directory_name):
                file_hashes = {}
                for file in files:
                    file_path = os.path.join(foldername, file)
                    with open(file_path, 'rb') as f:
                        file_date = f.read()
                        file_hash = hashlib.md5(file_date).hexdigest()
                        if file_hash in file_hashes:
                            with open('Log.txt', 'a') as log_file:
                                log_file.write(f'Duplicate file found: {file_path} is a duplicate of {file_hashes[file_hash]}\n')
                        else:
                            file_hashes[file_hash] = file_path

if __name__ == "__main__":
    main()