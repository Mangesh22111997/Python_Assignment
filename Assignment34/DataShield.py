"""
Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.
Please add below features in our project named as Marvellous Data Shield
System

1. Logging System
• Create a Logs/ folder
• Store:
◦ Backup start time
◦ Files copied
◦ Zip file name
◦ Errors (if any)

2. Email Notification
• Send an email after backup completion
• Attach:
◦ Log file
◦ Zip file name

3. Restore Feature
• Add a command:
python Script.py --restore ZipFileName Destination
• Extract backup to given directory

4. Exclude Files / Folders
• Ignore:
◦ .tmp, .log, .exe
◦ or user-defined extensions

5. Backup History Tracker
• Maintain a file:
◦ Date
◦ Number of files
◦ Zip size
• Display history using:
python Script.py --history

"""

import os 
import shutil
import zipfile
import json
import datetime
import hashlib
import time
import sys
from pathlib import Path


# ============================================================================
# CONFIGURATION
# ============================================================================

LOGS_FOLDER = "Logs"
HISTORY_FILE = "backup_history.json"
BACKUP_FOLDER = "Backups"
CHECKSUMS_FILE = "file_checksums.json"
EXCLUDE_EXTENSIONS = ['.tmp', '.log', '.exe', '.lnk', '.bak']
BACKUP_INTERVAL = 60  # Backup interval in seconds (60 = 1 minute)


# ============================================================================
# FUNCTION 1: LOGGING SYSTEM
# ============================================================================

def create_log_file():
    """Create a new log file with timestamp for current backup session."""
    if not os.path.exists(LOGS_FOLDER):
        os.makedirs(LOGS_FOLDER)
        print(f"✓ Created Logs folder: {LOGS_FOLDER}")
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(LOGS_FOLDER, f"backup_{timestamp}.log")
    
    # Write log header
    with open(log_file, 'w') as f:
        f.write("="*80 + "\n")
        f.write("MARVELLOUS DATA SHIELD SYSTEM - BACKUP LOG\n")
        f.write("="*80 + "\n")
        f.write(f"Backup Start Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*80 + "\n\n")
    
    return log_file


def log_to_file(log_file, message):
    """Write message to log file with timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    with open(log_file, 'a') as f:
        f.write(log_entry + "\n")


# ============================================================================
# FUNCTION: CHECKSUM CALCULATION
# ============================================================================

def calculate_file_checksum(file_path):
    """Calculate MD5 checksum of a file."""
    try:
        md5 = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b''):
                md5.update(chunk)
        return md5.hexdigest()
    except Exception as e:
        return None


def load_checksums():
    """Load previously stored file checksums."""
    if os.path.exists(CHECKSUMS_FILE):
        try:
            with open(CHECKSUMS_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}


def save_checksums(checksums):
    """Save file checksums to file."""
    try:
        with open(CHECKSUMS_FILE, 'w') as f:
            json.dump(checksums, f, indent=2)
    except Exception as e:
        print(f"⚠ Error saving checksums: {str(e)}")


def get_all_files(source_directory):
    """Recursively get all files from directory using os.walk, excluding filtered files."""
    files_dict = {}
    
    try:
        for root, dirs, files in os.walk(source_directory):
            for file in files:
                file_path = os.path.join(root, file)
                
                if should_exclude_file(file_path):
                    continue
                
                relative_path = os.path.relpath(file_path, source_directory)
                files_dict[relative_path] = file_path
        
        return files_dict
    except Exception as e:
        print(f"⚠ Error walking directory: {str(e)}")
        return {}


# ============================================================================
# FUNCTION 2: BACKUP CREATION
# ============================================================================

def should_exclude_file(file_path):
    """Check if file should be excluded from backup."""
    file_ext = os.path.splitext(file_path)[1].lower()
    return file_ext in EXCLUDE_EXTENSIONS


def create_backup(source_directory, log_file):
    """
    Create backup of NEW/MODIFIED files detected by checksum.
    Logs: Files copied, zip file name, errors if any.
    
    Returns: (zip_file_path, file_count, total_size, changed_files_count)
    """
    try:
        print(f"\n[FUNCTION: create_backup] Starting backup...")
        log_to_file(log_file, "[FUNCTION: create_backup] Backup process started")
        
        # Validate source
        if not os.path.isdir(source_directory):
            error_msg = f"ERROR: Source directory not found: {source_directory}"
            print(f"✗ {error_msg}")
            log_to_file(log_file, error_msg)
            return None, 0, 0, 0
        
        print(f"  Source: {os.path.abspath(source_directory)}")
        log_to_file(log_file, f"Source Directory: {os.path.abspath(source_directory)}")
        
        # Create backup folder
        if not os.path.exists(BACKUP_FOLDER):
            os.makedirs(BACKUP_FOLDER)
        
        # Load previous checksums
        print(f"\n[READING FILE SYSTEM]")
        print(f"  Scanning with os.walk()...")
        old_checksums = load_checksums()
        current_files = get_all_files(source_directory)
        new_checksums = {}
        
        print(f"  Total files found: {len(current_files)}")
        print(f"  Previous checksums: {len(old_checksums)}\n")
        
        log_to_file(log_file, f"Total files in source: {len(current_files)}")
        log_to_file(log_file, f"Previous checksums recorded: {len(old_checksums)}")
        
        # Find new/modified files
        files_to_backup = []
        changed_count = 0
        new_count = 0
        
        print(f"[CHECKSUM VERIFICATION]")
        print(f"  Checking file changes...\n")
        log_to_file(log_file, "Checking file changes using checksums...")
        
        for relative_path, full_path in current_files.items():
            try:
                current_checksum = calculate_file_checksum(full_path)
                new_checksums[relative_path] = current_checksum
                
                old_checksum = old_checksums.get(relative_path, None)
                
                # File is new or modified
                if old_checksum != current_checksum:
                    files_to_backup.append(full_path)
                    
                    if old_checksum is None:
                        print(f"  [NEW FILE] {relative_path}")
                        log_to_file(log_file, f"[NEW FILE] {relative_path}")
                        new_count += 1
                    else:
                        print(f"  [MODIFIED] {relative_path}")
                        log_to_file(log_file, f"[MODIFIED] {relative_path}")
                        changed_count += 1
                
            except Exception as e:
                print(f"  [ERROR] {relative_path}: {str(e)}")
                log_to_file(log_file, f"[ERROR] {relative_path}: {str(e)}")
        
        print(f"\n[BACKUP SUMMARY]")
        print(f"  New files: {new_count}")
        print(f"  Modified files: {changed_count}")
        print(f"  Total to backup: {len(files_to_backup)}\n")
        
        log_to_file(log_file, f"New files detected: {new_count}")
        log_to_file(log_file, f"Modified files detected: {changed_count}")
        
        file_count = len(files_to_backup)
        
        # If no changes, skip backup
        if file_count == 0:
            print("  ✓ No changes detected - skipping backup")
            log_to_file(log_file, "No file changes detected - backup skipped")
            save_checksums(new_checksums)
            return None, 0, 0, 0
        
        # Calculate total size
        total_size = sum(os.path.getsize(f) for f in files_to_backup)
        print(f"  Total size: {total_size / (1024*1024):.2f} MB\n")
        log_to_file(log_file, f"Total backup size: {total_size / (1024*1024):.2f} MB")
        
        # Create backup folder
        if not os.path.exists(BACKUP_FOLDER):
            os.makedirs(BACKUP_FOLDER)
        
        # Create zip file with only changed files
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_{os.path.basename(source_directory)}_{timestamp}"
        zip_file_path = os.path.join(BACKUP_FOLDER, f"{backup_name}.zip")
        
        print(f"[CREATING ZIP FILE]")
        print(f"  File: {os.path.basename(zip_file_path)}\n")
        log_to_file(log_file, f"Creating zip file: {zip_file_path}")
        
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for idx, file_path in enumerate(files_to_backup, 1):
                arcname = os.path.relpath(file_path, source_directory)
                zipf.write(file_path, arcname)
                
                if idx % 10 == 0 or idx == file_count:
                    print(f"  Progress: {idx}/{file_count} files added")
                    log_to_file(log_file, f"Progress: {idx}/{file_count} files added")
        
        # Get zip size
        zip_size = os.path.getsize(zip_file_path)
        compression = (1 - zip_size/total_size)*100 if total_size > 0 else 0
        
        print(f"\n[ZIP CREATION COMPLETE]")
        print(f"  Zip file: {zip_file_path}")
        print(f"  Zip size: {zip_size / (1024*1024):.2f} MB")
        print(f"  Compression: {compression:.1f}%\n")
        
        log_to_file(log_file, f"Zip file name: {os.path.basename(zip_file_path)}")
        log_to_file(log_file, f"Zip file size: {zip_size / (1024*1024):.2f} MB")
        log_to_file(log_file, f"Compression ratio: {compression:.1f}%")
        
        # Update checksums for next run
        save_checksums(new_checksums)
        log_to_file(log_file, "Checksums updated for next backup cycle")
        
        return zip_file_path, file_count, zip_size, (new_count + changed_count)
        
    except Exception as e:
        error_msg = f"ERROR in create_backup: {str(e)}"
        print(f"✗ {error_msg}")
        log_to_file(log_file, error_msg)
        return None, 0, 0, 0


def send_backup_email(receiver_email, sender_email, app_password, log_file, zip_file, log_content):
    """
    Email notification feature - to be implemented.
    """
    pass


# ============================================================================
# FUNCTION 4: RESTORE FEATURE
# ============================================================================

def restore_backup(zip_file_path, destination_directory, log_file):
    """
    Restore backup from zip file to destination directory.
    Command: python DataShield.py --restore ZipFileName Destination
    """
    try:
        print(f"\n[FUNCTION: restore_backup] Starting restore...")
        log_to_file(log_file, "[FUNCTION: restore_backup] Restore process started")
        
        # Validate zip file
        if not os.path.isfile(zip_file_path):
            error_msg = f"ERROR: Zip file not found: {zip_file_path}"
            print(f"✗ {error_msg}")
            log_to_file(log_file, error_msg)
            return False
        
        if not zipfile.is_zipfile(zip_file_path):
            error_msg = f"ERROR: Invalid zip file: {zip_file_path}"
            print(f"✗ {error_msg}")
            log_to_file(log_file, error_msg)
            return False
        
        # Create destination if needed
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
            print(f"  Created destination: {destination_directory}")
            log_to_file(log_file, f"Created destination directory: {destination_directory}")
        
        print(f"  Zip file: {zip_file_path}")
        print(f"  Destination: {destination_directory}\n")
        log_to_file(log_file, f"Restoring from: {zip_file_path}")
        log_to_file(log_file, f"Destination: {destination_directory}")
        
        # Extract files
        with zipfile.ZipFile(zip_file_path, 'r') as zipf:
            file_list = zipf.namelist()
            file_count = len(file_list)
            
            print(f"[EXTRACTING FILES]")
            print(f"  Total files: {file_count}\n")
            log_to_file(log_file, f"Files to extract: {file_count}")
            
            for idx, file_name in enumerate(file_list, 1):
                zipf.extract(file_name, destination_directory)
                
                if idx % 10 == 0 or idx == file_count:
                    print(f"  Progress: {idx}/{file_count} files extracted")
                    log_to_file(log_file, f"Progress: {idx}/{file_count} files extracted")
        
        print(f"\n✓ Restore completed successfully!")
        print(f"  Files restored: {file_count}\n")
        log_to_file(log_file, f"Restore completed - {file_count} files extracted")
        return True
        
    except Exception as e:
        error_msg = f"ERROR in restore_backup: {str(e)}"
        print(f"✗ {error_msg}")
        log_to_file(log_file, error_msg)
        return False


# ============================================================================
# FUNCTION 5: BACKUP HISTORY TRACKER
# ============================================================================

def add_to_history(backup_zip, file_count, zip_size):
    """Add backup entry to history file with date, file count, and zip size."""
    try:
        if not os.path.exists(BACKUP_FOLDER):
            os.makedirs(BACKUP_FOLDER)
        
        # Load existing history
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, 'r') as f:
                history = json.load(f)
        else:
            history = []
        
        # Add new entry
        entry = {
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "backup_file": os.path.basename(backup_zip),
            "file_count": file_count,
            "zip_size_mb": round(zip_size / (1024*1024), 2),
            "full_path": os.path.abspath(backup_zip)
        }
        
        history.append(entry)
        
        # Save updated history
        with open(HISTORY_FILE, 'w') as f:
            json.dump(history, f, indent=2)
        
        print("[BACKUP HISTORY UPDATED]")
        print(f"  Total backups recorded: {len(history)}")
        
    except Exception as e:
        print(f"⚠ History update failed: {str(e)}")


def display_backup_history():
    """Display all backup history (python DataShield.py --history)."""
    if not os.path.exists(HISTORY_FILE):
        print("\n" + "="*80)
        print("MARVELLOUS DATA SHIELD - BACKUP HISTORY")
        print("="*80)
        print("\nNo backups found yet.\n")
        return
    
    with open(HISTORY_FILE, 'r') as f:
        history = json.load(f)
    
    print("\n" + "="*80)
    print("MARVELLOUS DATA SHIELD - BACKUP HISTORY")
    print("="*80)
    print(f"\n{'#':<3} {'Date':<20} {'Backup File':<35} {'Files':<8} {'Size (MB)':<12}")
    print("-"*80)
    
    for idx, entry in enumerate(history, 1):
        date = entry.get('date', 'N/A')
        backup_file = entry.get('backup_file', 'N/A')
        file_count = entry.get('file_count', 0)
        zip_size = entry.get('zip_size_mb', 0)
        
        print(f"{idx:<3} {date:<20} {backup_file:<35} {file_count:<8} {zip_size:<12.2f}")
    
    print("-"*80)
    print(f"Total Backups: {len(history)}\n")


# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    """Main orchestration function for Data Shield System."""
    try:
        print("\n" + "="*80)
        print("MARVELLOUS DATA SHIELD SYSTEM")
        print("="*80)
        
        # Handle --history request
        if len(sys.argv) > 1 and sys.argv[1] == "--history":
            display_backup_history()
            return
        
        # Handle --restore request
        if len(sys.argv) > 1 and sys.argv[1] == "--restore":
            if len(sys.argv) < 4:
                print("\nUsage: python DataShield.py --restore <backup_zip> <destination>")
                return
            
            zip_file = sys.argv[2]
            destination = sys.argv[3]
            
            log_file = create_log_file()
            print(f"\n[RESTORE MODE]")
            success = restore_backup(zip_file, destination, log_file)
            
            if success:
                print(f"Log file: {log_file}")
            else:
                print(f"ERROR! Check log: {log_file}")
            
            return
        
        # Handle backup mode
        if len(sys.argv) < 2:
            print("\n[USAGE]")
            print("Backup (single):     python DataShield.py <source_directory>")
            print("Backup (continuous): python DataShield.py <source_directory> --monitor")
            print("Restore:             python DataShield.py --restore <backup_zip> <destination>")
            print("History:             python DataShield.py --history\n")
            return
        
        source_dir = sys.argv[1]
        
        # Validate source directory
        if not os.path.isdir(source_dir):
            print(f"\n✗ ERROR: Source directory not found: {source_dir}\n")
            return
        
        # Check if continuous monitoring mode
        continuous_mode = len(sys.argv) > 2 and sys.argv[2] == "--monitor"
        
        if continuous_mode:
            print(f"\n[CONTINUOUS BACKUP MODE]")
            print(f"  Source: {os.path.abspath(source_dir)}")
            print(f"  Interval: {BACKUP_INTERVAL} seconds")
            print(f"  Press Ctrl+C to stop\n")
            
            cycle = 0
            while True:
                cycle += 1
                timestamp_start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"\n{'='*80}")
                print(f"BACKUP CYCLE #{cycle} - Started at {timestamp_start}")
                print(f"{'='*80}")
                
                log_file = create_log_file()
                
                # Create backup
                result = create_backup(source_dir, log_file)
                
                if result[0] is None:
                    print(f"⚠ No changes detected - waiting for next cycle...")
                else:
                    zip_path, file_count, zip_size, changed_count = result
                    add_to_history(zip_path, file_count, zip_size)
                    
                    # Complete summary
                    print("\n" + "="*80)
                    print("✓ BACKUP CYCLE COMPLETED")
                    print("="*80)
                    print(f"  Files backed up: {file_count}")
                    print(f"  Backup size: {zip_size / (1024*1024):.2f} MB")
                    print(f"  Log file: {log_file}")
                    print("="*80)
                
                # Wait for next cycle
                print(f"\n[WAITING FOR NEXT CYCLE]")
                print(f"  Next backup in {BACKUP_INTERVAL} seconds...")
                print(f"  Press Ctrl+C to stop\n")
                
                try:
                    time.sleep(BACKUP_INTERVAL)
                except KeyboardInterrupt:
                    print("\n\n✓ Backup system stopped.")
                    return
        
        else:
            # Single backup mode
            print(f"\n[SINGLE BACKUP MODE]")
            print(f"  Source: {os.path.abspath(source_dir)}\n")
            
            log_file = create_log_file()
            
            # Create backup
            result = create_backup(source_dir, log_file)
            
            if result[0] is None:
                print(f"✗ No changes detected or backup failed")
                return
            
            zip_path, file_count, zip_size, changed_count = result
            add_to_history(zip_path, file_count, zip_size)
            
            # Final summary
            print("="*80)
            print("✓ BACKUP COMPLETED SUCCESSFULLY")
            print("="*80)
            print(f"  Source:   {os.path.abspath(source_dir)}")
            print(f"  Backup:   {zip_path}")
            print(f"  Files:    {file_count}")
            print(f"  Size:     {zip_size / (1024*1024):.2f} MB")
            print(f"  Log:      {log_file}")
            print("="*80 + "\n")
        
    except KeyboardInterrupt:
        print("\n\n✓ Backup system stopped.")
    except Exception as e:
        print(f"\n✗ FATAL ERROR: {str(e)}\n")


if __name__ == "__main__":
    main()