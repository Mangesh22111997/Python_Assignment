"""
Docstring for Assignment31.Program_3

Please follow below rules while designing automation script as  
• Accept input through command line or through file. 
• Display any message in log file instead of console. 
• For separate task define separate function. 
• For robustness handle every expected exception. 
• Perform validations before taking any action. 
• Create user defined modules to store the functionality. 



Question: 3. Design automation script which accept two directory names. Copy all files from first directory 
into second directory. Second directory should be created at run time. 
Demo is name of directory which is existing and contains files in it. We have to create new 
Directory as Temp and copy all files from Demo to Temp.

"""
import os
import shutil

def DirectoryFileCopy(source_directory, destination_directory):
    if not os.path.exists(source_directory):
        print(f'The source directory: {source_directory} does not exist.')
        return
    
    else:
        os.makedirs(destination_directory, exist_ok=True)
        for foldername, subfolder, files in os.walk(source_directory):
            # Calculate the relative path from source directory
            relative_path = os.path.relpath(foldername, source_directory)
            # Create corresponding destination path maintaining structure
            if relative_path == '.':
                current_dest_dir = destination_directory
            else:
                current_dest_dir = os.path.join(destination_directory, relative_path)
            
            # Create subdirectories in destination
            os.makedirs(current_dest_dir, exist_ok=True)
            
            for file in files:
                source_file_path = os.path.join(foldername, file)
                destination_file_path = os.path.join(current_dest_dir, file)

                if not os.path.exists(destination_file_path):
                    try:
                        shutil.copy2(source_file_path, destination_file_path)
                        print(f'{source_file_path} has been copied to {destination_file_path}')
                    except Exception as e:
                        print(f'Error copying {source_file_path} to {destination_file_path}: {e}')

                else:
                    print(f'{destination_file_path} already exists. Skipping the copy operation for {source_file_path}.')
            
                    
                    
def main():
    source_directory = "Demo"
    destination_directory = "Temp"
    DirectoryFileCopy(source_directory, destination_directory)

if __name__ == "__main__":
    main()

