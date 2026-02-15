"""
Docstring for Assignment32.Program_4

Question: 4. Design automation script which accept directory name and delete all duplicate files from that 
directory. Write names of duplicate files from that directory into log file named as Log.txt. 
Log.txt file should be created into current directory. Display execution time required for the 
script. 
Usage : DirectoryDusplicateRemoval.py “Demo” 
Demo is name of directory.

"""

import sys
import os
import hashlib
import time

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
                start_time = time.time()
                file_hashes = {}
                for file in files:
                    file_path = os.path.join(foldername, file)
                    with open(file_path, 'rb') as f:
                        file_date = f.read()
                        file_hash = hashlib.md5(file_date).hexdigest()
                        if file_hash in file_hashes:
                            with open('Log_duplicate.txt', 'a') as log_file:
                                log_file.write(f'Duplicate file found: {file_path} is a duplicate of {file_hashes[file_hash]}\n')
                            
                        else:
                            file_hashes[file_hash] = file_path

                    for file_hash, file_path in file_hashes.items():
                        with open('Log_duplicate.txt', 'a') as log_file:
                            log_file.write(f'Unique file: {file_path}\n')
                            
                        if file_hash in file_hashes:
                            try:
                                with open('Log_duplicate.txt', 'a') as log_file:
                                    log_file.write(f'Deleting duplicate file: {file_path}\n')
                                    os.remove(file_path)
                                    print(f'{file_path} has been deleted.')
                                    end_time = time.time()
                                    print(f"Execution time: {end_time - start_time:.2f} seconds")
                            except Exception as e:
                                print(f'Error deleting {file_path}: {e}')
                               

            

if __name__ == "__main__":
    main()