import os
import sys
import time
import subprocess
from datetime import datetime
from pathlib import Path

def get_adb_output(command: str) -> str:
    """Safely executes an ADB command and returns the output."""
    try:
        # Use subprocess.check_output for better error handling than getoutput
        return subprocess.check_output(f"adb shell {command}", 
                                       shell=True, 
                                       stderr=subprocess.STDOUT, 
                                       universal_newlines=True).strip()
    except subprocess.CalledProcessError as e:
        return f"Error executing {command}: {e.output}"

def run_memory_monitor(duration_sec: int, interval_sec: int = 60):
    """
    Monitors Android memory usage with precision timing and organized logging.
    """
    # 1. Setup directory using Pathlib for cross-platform compatibility
    today_folder = Path.cwd() / datetime.now().strftime("%Y%m%d")
    today_folder.mkdir(exist_ok=True)

    # 2. Setup file name
    start_ts = datetime.now().strftime("%H%M%S")
    result_file = today_folder / f"{start_ts}_Memory_Full_Report.txt"

    print(f"[INFO] Logging to: {result_file}")
    print(f"[INFO] Duration: {duration_sec}s | Interval: {interval_sec}s")
    print("-" * 50)

    start_time = time.time()
    end_time = start_time + duration_sec
    next_check = start_time

    try:
        with open(result_file, mode='a', encoding="utf-8") as f:
            while time.time() < end_time:
                current_time = time.time()
                
                # Check if it's time for the next sample
                if current_time >= next_check:
                    elapsed = int(current_time - start_time)
                    
                    # Fetching data
                    device_date = get_adb_output("date")
                    proc_meminfo = get_adb_output("cat /proc/meminfo")
                    dumpsys_mem = get_adb_output("dumpsys meminfo")

                    # Extract MemAvailable efficiently
                    mem_available = "N/A"
                    for line in proc_meminfo.splitlines():
                        if "MemAvailable" in line:
                            mem_available = line.strip()
                            break

                    # Logging to file
                    log_header = f"\n{'='*20} [{elapsed:5d}s] {device_date} {'='*20}\n"
                    f.write(log_header)
                    f.write(f"Summary: {mem_available}\n\n")
                    f.write("--- /proc/meminfo ---\n" + proc_meminfo + "\n\n")
                    f.write("--- dumpsys meminfo ---\n" + dumpsys_mem + "\n")
                    
                    # Ensure data is written to disk
                    f.flush()

                    print(f"[{elapsed:5d}s] Recorded: {mem_available}")

                    # Calculate next tick (prevents time drift)
                    next_check += interval_sec
                
                # Dynamic sleep to save CPU, but responsive enough for the next check
                time.sleep(0.5)

    except IOError as e:
        print(f"[ERROR] File writing failed: {e}")

def main():
    """Entry point for the script with CLI argument parsing."""
    if len(sys.argv) < 2 or sys.argv[1] in ["?", "-h", "--help"]:
        print(f"Usage:   python {sys.argv[0]} [Duration(s)] [Interval(s)]")
        print(f"Example: python {sys.argv[0]} 3600 60")
        return

    try:
        duration = int(sys.argv[1])
        # Default interval to 60 if not provided
        interval = int(sys.argv[2]) if len(sys.argv) > 2 else 60
        
        run_memory_monitor(duration, interval)
        print("\n[INFO] Monitoring finished successfully.")
    except ValueError:
        print("[ERROR] Please provide integers for duration and interval.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] Aborted by user.")
        sys.exit(0)