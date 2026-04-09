'''
Please follow below rules while designing automation script as
• Accept input through command line or through file.
• Display any message in log file instead of console.
• For separate task define separate function.
• For robustness handle every expected exception.
• Perform validations before taking any action.
• Create user defined modules to store the functionality.

Please add below features in our project named as Platform Surveillance
System
1. Add Thread Monitoring Feature
For each running process, display:
• Process Name
• PID
• Number of Threads created by that process
Requirement
Store information in log file along with timestamp.

2. Add Open Files Monitoring Feature
For each process, display:
• Number of files opened by the process
Requirement
• Count open file descriptors using system/library calls
• Handle permission errors properly
• Mention “Access Denied” in log if required

3. Add Actual Memory Allocation Feature
Display real memory usage of each process:
• RSS (Resident Set Size – actual RAM used)
• VMS (Virtual Memory)
• Memory Percentage
Requirement
Show:
• Top 10 memory consuming processes

4. Add Periodic Email Reporting Feature
Automatically send system report through email at regular intervals.
Email must contain:
• Log file attachment
• Summary of:
◦ Total processes
◦ Top CPU usage processes
◦ Top Memory usage processes
◦ Top Thread count processes
◦ Top Open file processes
Usage
PlatformSurveillance.py "MarvellousLogs" "receiver@gmail.com" 10
Where:
• MarvellousLogs → log folder
• receiver@gmail.com → receiver mail
• 10 → interval in minutes
'''

import sys
import os
import psutil
import time
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# ============================================================================
# FUNCTION 1: THREAD MONITORING
# ============================================================================
def thread_monitoring(log_file):
    """
    MONITORS: All running processes and their thread counts
    
    LOGS: Process Name, PID, Thread Count with timestamp
    HANDLES: NoSuchProcess and AccessDenied exceptions
    """
    try:
        with open(log_file, 'a') as log:
            log.write("\n" + "="*80 + "\n")
            log.write(f"[FUNCTION: thread_monitoring] - {datetime.datetime.now()}\n")
            log.write("="*80 + "\n")
            log.write(f"{'Process Name':<30} {'PID':<10} {'Thread Count':<15}\n")
            log.write("-"*55 + "\n")
            
            thread_count = 0
            for proc in psutil.process_iter(['name', 'pid', 'num_threads']):
                try:
                    log.write(f"{proc.info['name']:<30} {proc.info['pid']:<10} {proc.info['num_threads']:<15}\n")
                    thread_count += 1
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            
            log.write("-"*55 + "\n")
            log.write(f"Total processes: {thread_count} | Status: SUCCESS\n")
            log.write("="*80 + "\n\n")
    except Exception as e:
        with open(log_file, 'a') as log:
            log.write(f"ERROR in thread_monitoring: {str(e)}\n")


# ============================================================================
# FUNCTION 2: OPEN FILES MONITORING  
# ============================================================================
def open_files_monitoring(log_file):
    """
    MONITORS: Open file descriptors per process
    
    LOGS: Process Name, PID, Open Files count
    HANDLES: AccessDenied with explicit logging
    """
    try:
        with open(log_file, 'a') as log:
            log.write("\n" + "="*80 + "\n")
            log.write(f"[FUNCTION: open_files_monitoring] - {datetime.datetime.now()}\n")
            log.write("="*80 + "\n")
            log.write(f"{'Process Name':<30} {'PID':<10} {'Open Files':<15}\n")
            log.write("-"*55 + "\n")
            
            process_count = 0
            denied_count = 0
            for proc in psutil.process_iter(['name', 'pid']):
                try:
                    open_files = proc.open_files()
                    log.write(f"{proc.info['name']:<30} {proc.info['pid']:<10} {len(open_files):<15}\n")
                    process_count += 1
                except psutil.AccessDenied:
                    log.write(f"{proc.info['name']:<30} {proc.info['pid']:<10} {'Access Denied':<15}\n")
                    denied_count += 1
                except (psutil.NoSuchProcess, Exception):
                    continue
            
            log.write("-"*55 + "\n")
            log.write(f"Total: {process_count} | Access Denied: {denied_count} | Status: SUCCESS\n")
            log.write("="*80 + "\n\n")
    except Exception as e:
        with open(log_file, 'a') as log:
            log.write(f"ERROR in open_files_monitoring: {str(e)}\n")

# ============================================================================
# FUNCTION 3: MEMORY ALLOCATION MONITORING
# ============================================================================
def memory_allocation_monitoring(log_file):
    """
    MONITORS: Memory usage for all processes - shows TOP 10
    
    LOGS: Process Name, PID, RSS (MB), VMS (MB), Memory %
    HANDLES: NoSuchProcess and AccessDenied gracefully
    """
    try:
        with open(log_file, 'a') as log:
            log.write("\n" + "="*80 + "\n")
            log.write(f"[FUNCTION: memory_allocation_monitoring] - {datetime.datetime.now()}\n")
            log.write("="*80 + "\n")
            log.write("TOP 10 MEMORY-CONSUMING PROCESSES\n")
            log.write(f"{'Rank':<5} {'Process Name':<25} {'PID':<10} {'RSS (MB)':<12} {'VMS (MB)':<12} {'Memory %':<10}\n")
            log.write("-"*80 + "\n")
            
            processes = []
            for proc in psutil.process_iter(['name', 'pid', 'memory_info', 'memory_percent']):
                try:
                    mem_info = proc.info['memory_info']
                    rss_mb = mem_info.rss / (1024 * 1024)
                    vms_mb = mem_info.vms / (1024 * 1024)
                    mem_percent = proc.info['memory_percent']
                    processes.append((proc.info['name'], proc.info['pid'], rss_mb, vms_mb, mem_percent))
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
            
            # Sort by RSS and get top 10
            top_processes = sorted(processes, key=lambda x: x[2], reverse=True)[:10]
            for idx, proc in enumerate(top_processes, 1):
                log.write(f"{idx:<5} {proc[0]:<25} {proc[1]:<10} {proc[2]:<12.2f} {proc[3]:<12.2f} {proc[4]:<10.2f}\n")
            
            log.write("-"*80 + "\n")
            log.write(f"Total processes scanned: {len(set([p[0] for p in processes]))} | Status: SUCCESS\n")
            log.write("="*80 + "\n\n")
    except Exception as e:
        with open(log_file, 'a') as log:
            log.write(f"ERROR in memory_allocation_monitoring: {str(e)}\n")

# ============================================================================
# FUNCTION 4: EMAIL REPORTING WITH ATTACHMENT
# ============================================================================
def send_email_report(log_file, receiver_email, sender_email, app_password):
    """
    SENDS: Monitoring report via Gmail SMTP with log file attached
    
    PARAMETERS:
        log_file         - Log file path to attach
        receiver_email   - Recipient email
        sender_email     - Gmail sender address  
        app_password     - Gmail App Password (NOT regular password)
    
    SETUP: Enable 2FA on Gmail and generate app password from:
           https://myaccount.google.com/apppasswords
    
    RETURNS: True if successful, False otherwise
    """
    try:
        with open(log_file, 'a') as log:
            log.write("\n" + "="*80 + "\n")
            log.write(f"[FUNCTION: send_email_report] - {datetime.datetime.now()}\n")
            log.write("="*80 + "\n")
            log.write(f"To: {receiver_email} | From: {sender_email}\n")
            
            # Validate credentials
            if not sender_email or not app_password or sender_email == "your_email@gmail.com":
                log.write("⚠ SKIPPED: Email credentials not configured\n")
                log.write("="*80 + "\n\n")
                return False
            
            try:
                # Create email
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = f"System Report - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                
                # Email body
                body_text = f"""\nPlatform Surveillance System Report
Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

MONITORING SUMMARY:
✓ Thread Monitoring       - Tracked process threads
✓ Open Files Monitoring   - File descriptor analysis  
✓ Memory Allocation       - Top 10 memory processes
✓ Email Report            - Delivered via SMTP

See attached log file for detailed results.

---
Marvellous Infosystems\n"""
                
                msg.attach(MIMEText(body_text, 'plain'))
                
                # Attach log file
                if os.path.exists(log_file):
                    with open(log_file, 'rb') as attachment:
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(attachment.read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(log_file)}')
                        msg.attach(part)
                    log.write(f"✓ Log file attached ({os.path.getsize(log_file)} bytes)\n")
                
                # Send via Gmail SMTP
                log.write("Connecting to Gmail SMTP...\n")
                smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                smtp.login(sender_email, app_password)
                smtp.send_message(msg)
                smtp.quit()
                
                log.write(f"✓ Email sent successfully to {receiver_email}\n")
                log.write("Status: SUCCESS\n")
                log.write("="*80 + "\n\n")
                return True
                
            except smtplib.SMTPAuthenticationError:
                log.write("✗ FAILED: Invalid email or app password\n")
                log.write("="*80 + "\n\n")
                return False
            except smtplib.SMTPException as e:
                log.write(f"✗ FAILED: SMTP Error - {str(e)}\n")
                log.write("="*80 + "\n\n")
                return False
                
    except Exception as e:
        with open(log_file, 'a') as log:
            log.write(f"✗ ERROR in send_email_report: {str(e)}\n")
        return False



# ============================================================================
# MAIN FUNCTION - ORCHESTRATES ENTIRE SYSTEM
# ============================================================================
def main():
    """
    ORCHESTRATES: Complete surveillance system with monitoring & email
    
    FLOW:
        1. Validates command-line arguments
        2. Creates log folder and initializes log file
        3. Runs monitoring functions at intervals
        4. Sends periodic email reports
        5. Handles interruptions gracefully
    """
    try:
        # Validate arguments
        if len(sys.argv) != 4:
            print("=" * 80)
            print("PLATFORM SURVEILLANCE SYSTEM - EMAIL REFERENCE VERSION")
            print("=" * 80)
            print("\nUsage: python Platform_Surveillance_System_Email.py <folder> <email> <interval>")
            print("Example: python Platform_Surveillance_System_Email.py MarvellousLogs user@gmail.com 10\n")
            print("Arguments:")
            print("  folder    - Log folder path")
            print("  email     - Recipient email")
            print("  interval  - Minutes between cycles\n")
            print("NOTE: This is a REFERENCE version with email capability")
            print("=" * 80)
            return
        
        log_folder = sys.argv[1]
        receiver_email = sys.argv[2]
        
        try:
            interval_minutes = int(sys.argv[3])
            if interval_minutes <= 0:
                print("ERROR: Interval must be positive integer")
                return
        except ValueError:
            print("ERROR: Interval must be valid integer")
            return
        
        # ===== EMAIL CONFIGURATION (EDIT BELOW) =====
        sender_email = "your_email@gmail.com"      # CONFIGURE: Your Gmail
        app_password = "your_app_password_here"    # CONFIGURE: Gmail app password
        
        # Instructions to get Gmail App Password:
        # 1. Enable 2-Step Verification on Google Account
        # 2. Visit: https://myaccount.google.com/apppasswords
        # 3. Select "Mail" and "Windows" (or "Other")
        # 4. Copy the 16-character password
        
        # Create log folder
        if not os.path.exists(log_folder):
            try:
                os.makedirs(log_folder)
                print(f"✓ Created folder: {log_folder}")
            except Exception as e:
                print(f"✗ Error creating folder: {str(e)}")
                return
        
        # Initialize log file
        log_filename = f"PlatformSurveillance_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        log_file = os.path.join(log_folder, log_filename)
        
        print("\n" + "="*80)
        print("PLATFORM SURVEILLANCE SYSTEM - STARTED")
        print("="*80)
        print(f"Log Folder:      {log_folder}")
        print(f"Log File:        {log_file}")
        print(f"Receiver:        {receiver_email}")
        print(f"Interval:        {interval_minutes} minute(s)")
        print(f"Email Enabled:   {'YES ✓' if sender_email != 'your_email@gmail.com' else 'NO (configure credentials)'}")
        print("="*80 + "\n")
        
        # Write log header
        with open(log_file, 'w') as log:
            log.write("="*80 + "\n")
            log.write("PLATFORM SURVEILLANCE SYSTEM - LOG FILE\n")
            log.write("="*80 + "\n")
            log.write(f"Start Time: {datetime.datetime.now()}\n")
            log.write(f"Log Folder: {log_folder}\n")
            log.write(f"Receiver:   {receiver_email}\n")
            log.write(f"Interval:   {interval_minutes} minute(s)\n")
            log.write("="*80 + "\n\n")
        
        cycle = 0
        
        # ===== MAIN MONITORING LOOP =====
        while True:
            cycle += 1
            try:
                # Cycle header
                with open(log_file, 'a') as log:
                    log.write(f"\n{'*'*80}\n")
                    log.write(f"CYCLE #{cycle} - {datetime.datetime.now()}\n")
                    log.write(f"{'*'*80}\n\n")
                
                # Run monitoring functions
                thread_monitoring(log_file)
                open_files_monitoring(log_file)
                memory_allocation_monitoring(log_file)
                
                # Send email if configured
                if sender_email != "your_email@gmail.com":
                    send_email_report(log_file, receiver_email, sender_email, app_password)
                else:
                    with open(log_file, 'a') as log:
                        log.write("\n" + "="*80 + "\n")
                        log.write("[FUNCTION: send_email_report] - SKIPPED\n")
                        log.write("Reason: Email credentials not configured\n")
                        log.write("Action: Set sender_email and app_password in main()\n")
                        log.write("="*80 + "\n\n")
                
                # Cycle completion
                with open(log_file, 'a') as log:
                    log.write(f"Cycle #{cycle} completed. Next in {interval_minutes} minute(s)...\n")
                
                time.sleep(interval_minutes * 60)
                
            except KeyboardInterrupt:
                with open(log_file, 'a') as log:
                    log.write(f"\nMonitoring stopped at {datetime.datetime.now()}\n")
                    log.write("="*80 + "\n")
                print(f"\n✓ Stopped. See {log_file}")
                break
            except Exception as e:
                with open(log_file, 'a') as log:
                    log.write(f"\nCycle #{cycle} Error: {str(e)}\nContinuing...\n")
    
    except Exception as e:
        print(f"✗ FATAL ERROR: {str(e)}")


# ============================================================================
# ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    main()
