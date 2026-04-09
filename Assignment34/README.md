# MARVELLOUS DATA SHIELD SYSTEM
## Advanced Backup & Restore Solution with Checksum-Based Change Detection

---

## **SYSTEM OVERVIEW**

DataShield.py is a comprehensive automated backup system that:
- ✓ Monitors folders/files using `os.walk()`
- ✓ Detects changes using MD5 checksums
- ✓ Backs up only NEW and MODIFIED files
- ✓ Runs at frequent intervals automatically
- ✓ Maintains complete backup history with metadata
- ✓ Supports restore from backups
- ✓ Logs all activities with timestamps

---

## **KEY FEATURES**

### 1. **Checksum-Based Change Detection**
- Every file's MD5 checksum is calculated and stored
- Only files with changed checksums are backed up
- Reduces backup size and time significantly
- Checksums stored in `file_checksums.json`

### 2. **Automatic Backup at Intervals**
- System runs continuously with configurable time intervals
- Default: 60 seconds between backup cycles
- Each cycle:
  - Scans all files using os.walk()
  - Compares checksums against previous run
  - Creates incremental backup zip with only changed files
  - Updates backup history
  - Displays detailed progress

### 3. **File Exclusion**
- Automatically skips: `.tmp`, `.log`, `.exe`, `.lnk`, `.bak`
- Configurable via `EXCLUDE_EXTENSIONS` variable
- Excluded files logged for transparency

### 4. **Comprehensive Logging**
- Creates timestamped log files in `Logs/` folder
- Logs contain:
  - Backup start time
  - Files scanned (new, modified, excluded)
  - File counts and sizes
  - Compression ratio
  - All errors with timestamps

### 5. **Backup History Tracker**
- JSON-based history file: `backup_history.json`
- Records for each backup:
  - Date and time
  - Backup zip filename
  - Number of files backed up
  - Zip file size in MB
  - Full path to backup

### 6. **Restore Feature**
- Extract any backup to specified destination
- Command: `python DataShield.py --restore <zip_file> <destination>`
- Validates zip integrity before extraction
- Logs all restore operations

### 7. **Email Notification** (stub - `pass` for future implementation)
- Function ready for email feature
- Will send completion notifications when implemented

---

## **USAGE GUIDE**

### **Command-Line Usage:**

```bash
# Single backup (one-time)
python DataShield.py <source_directory>

# Continuous automatic backups at intervals
python DataShield.py <source_directory> --monitor
  (Press Ctrl+C to stop)

# Restore from backup
python DataShield.py --restore <backup_zip_file> <destination_folder>

# View backup history
python DataShield.py --history

# Show usage help
python DataShield.py
```

### **Examples:**

```bash
# Backup TestData once
python DataShield.py TestData

# Continuous monitoring of TestData (backs up every 60 seconds)
python DataShield.py TestData --monitor

# Restore backup_TestData_20260405_022317.zip to RecoveredData folder
python DataShield.py --restore backup_TestData_20260405_022317.zip RecoveredData

# Show all backup history
python DataShield.py --history
```

---

## **SYSTEM FILES & FOLDERS**

```
Assignment34/
├── DataShield.py              # Main script
├── file_checksums.json        # Stores file checksums for change detection
├── backup_history.json        # History of all backups (date, count, size)
├── Logs/                      # Log files for each backup cycle
│   ├── backup_20260405_022317.log
│   ├── backup_20260405_022335.log
│   └── ...
├── Backups/                   # Zip files of backups
│   ├── backup_TestData_20260405_022317.zip
│   ├── backup_TestData_20260405_022335.zip
│   └── ...
└── TestData/                  # Example source folder
    ├── file1.txt
    └── file2.txt
```

---

## **HOW CHECKSUM DETECTION WORKS**

### First Backup Cycle:
```
Files scanned: file1.txt, file2.txt
Previous checksums recorded: 0
Action: All files are NEW → Back them up
Result: Both files placed in zip
Store checksums: file1.txt=abc123, file2.txt=def456
```

### Second Backup Cycle (file1.txt modified):
```
Files scanned: file1.txt (checksum=xyz789), file2.txt (checksum=def456)
Previous checksums: file1.txt=abc123, file2.txt=def456
Comparison:
  • file1.txt: abc123 ≠ xyz789 → MODIFIED ✓
  • file2.txt: def456 = def456 → UNCHANGED (skip)
Action: Only file1.txt is backed up
Result: Smaller backup size, faster backup
Update checksums: file1.txt=xyz789, file2.txt=def456
```

### Third Backup Cycle (no changes):
```
Files scanned: file1.txt (checksum=xyz789), file2.txt (checksum=def456)
Previous checksums: file1.txt=xyz789, file2.txt=def456
Comparison:
  • file1.txt: xyz789 = xyz789 → UNCHANGED ✓
  • file2.txt: def456 = def456 → UNCHANGED ✓
Action: No changes detected → Skip backup
Result: No backup zip created this cycle
```

---

## **CONFIGURATION**

Edit these variables in `DataShield.py` to customize:

```python
BACKUP_INTERVAL = 60              # Seconds between automatic backup cycles
EXCLUDE_EXTENSIONS = [            # File extensions to skip
    '.tmp', '.log', '.exe', 
    '.lnk', '.bak'
]
LOGS_FOLDER = "Logs"              # Where logs are stored
BACKUP_FOLDER = "Backups"         # Where zip files are stored
HISTORY_FILE = "backup_history.json"  # History filename
CHECKSUMS_FILE = "file_checksums.json" # Checksums database
```

---

## **TESTED FUNCTIONALITY**

✅ **Checksum Calculation**: MD5-based file change detection working
✅ **os.walk() Scanning**: Recursive directory traversal implemented
✅ **New File Detection**: Detects files with no previous checksum
✅ **Modified File Detection**: Detects files with different checksums
✅ **Incremental Backup**: Only changed files added to zip
✅ **History Tracking**: JSON-based backup metadata storage
✅ **History Display**: Formatted table view with all backup details
✅ **Restore Feature**: Zip extraction with validation
✅ **File Exclusion**: Extensions filtered automatically
✅ **Comprehensive Logging**: Timestamped logs with detailed information

---

## **OUTPUT EXAMPLE**

### Single Backup Run:
```
================================================================================
MARVELLOUS DATA SHIELD SYSTEM
================================================================================

[SINGLE BACKUP MODE]
  Source: G:\Mangesh\Python\Python_Assignments\Assignment34\TestData

[FUNCTION: create_backup] Starting backup...
  Source: G:\Mangesh\Python\Python_Assignments\Assignment34\TestData

[READING FILE SYSTEM]
  Scanning with os.walk()...
  Total files found: 2
  Previous checksums: 0

[CHECKSUM VERIFICATION]
  Checking file changes...

  [NEW FILE] file1.txt
  [NEW FILE] file2.txt

[BACKUP SUMMARY]
  New files: 2
  Modified files: 0
  Total to backup: 2

  Total size: 0.00 MB

[CREATING ZIP FILE]
  File: backup_TestData_20260405_022317.zip
  Progress: 2/2 files added

[ZIP CREATION COMPLETE]
  Zip file: Backups\backup_TestData_20260405_022317.zip
  Zip size: 0.00 MB
  Compression: -229.5%

[BACKUP HISTORY UPDATED]
  Total backups recorded: 1

================================================================================
✓ BACKUP COMPLETED SUCCESSFULLY
================================================================================
  Source:   G:\Mangesh\Python\Python_Assignments\Assignment34\TestData
  Backup:   Backups\backup_TestData_20260405_022317.zip
  Files:    2
  Size:     0.00 MB
  Log:      Logs\backup_20260405_022317.log
================================================================================
```

### Backup History Display:
```
================================================================================
MARVELLOUS DATA SHIELD - BACKUP HISTORY
================================================================================

#   Date                 Backup File                         Files    Size (MB)
--------------------------------------------------------------------------------
1   2026-04-05 02:23:17  backup_TestData_20260405_022317.zip 2        0.00
2   2026-04-05 02:23:35  backup_TestData_20260405_022335.zip 1        0.00
--------------------------------------------------------------------------------
Total Backups: 2
```

---

## **CONTINUOUS MONITORING MODE (--monitor)**

When running with `--monitor` flag:
- System enters infinite loop
- Each cycle:
  1. Creates new log file with timestamp
  2. Scans all files using os.walk()
  3. Compares checksums with previous run
  4. Creates incremental backup if changes found
  5. Updates history and checksums
  6. Sleeps for BACKUP_INTERVAL seconds
  7. Repeats from step 1

Example: `python DataShield.py MyData --monitor`
- Will continuously monitor MyData folder
- Backs up every 60 seconds (or when interval changes)
- Press Ctrl+C to gracefully stop

---

## **FUTURE ENHANCEMENTS**

- Email notifications (function stub ready)
- CSV export of history
- Backup encryption
- Differential backup options
- Automatic cleanup of old backups
- Cloud storage integration

---

## **NOTES**

- All backup zip files stored in `Backups/` folder
- All logs stored in `Logs/` folder with `YYYYMMDD_HHMMSS` timestamps
- History always appends to `backup_history.json` (never deleted)
- Checksums file updates after each backup cycle
- System is production-ready with error handling throughout

---

**End of Documentation**
