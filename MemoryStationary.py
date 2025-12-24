import os
import time
import subprocess
from datetime import datetime
from pathlib import Path

def get_mem_available():
    """Fetches MemAvailable from the connected Android device."""
    try:
        # Using grep directly in adb shell
        cmd = ["adb", "shell", "grep", "-e", "MemAvailable", "/proc/meminfo"]
        result = subprocess.check_output(cmd, universal_newlines=True, stderr=subprocess.STDOUT)
        return result.strip()
    except subprocess.CalledProcessError:
        return "Error: Could not reach device or fetch memory info."

def main():
    # 1. Setup paths and directories
    test_time_str = datetime.now().strftime('%Y%m%d_%H%M')
    base_path = Path.cwd() / "MemOverall_Test"
    
    try:
        base_path.mkdir(exist_ok=True)
    except Exception as e:
        print(f"Critical Error: Could not create directory {base_path}. {e}")
        return

    log_file = base_path / f"MemStationary_{test_time_str}.txt"
    print(f"[Path] {log_file}\n")

    # 2. Define testing schedule (Minutes from start)
    # The gaps between these are: 0, 1, 1, 1, 2, 5 minutes
    intervals = [0, 1, 2, 3, 5, 10]
    last_checkpoint = 0

    # 3. Execution Loop
    for minute in intervals:
        # Calculate sleep time based on the difference from the last checkpoint
        sleep_duration = (minute - last_checkpoint) * 60
        if sleep_duration > 0:
            print(f"[Waiting] Sleeping for {minute - last_checkpoint} minute(s)...")
            time.sleep(sleep_duration)

        # Prepare log entry
        timestamp = datetime.now().strftime('%H:%M:%S')
        label = "Origin" if minute == 0 else f"{minute} Minute"
        mem_info = get_mem_available()
        
        entry = f"【{label}】 @ {timestamp}\n{mem_info}\n\n"
        
        # Write to console and file
        print(f"[Logging] {label}")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(entry)
        
        last_checkpoint = minute

    print("\nTest Completed.")
    input("Press Enter to exit...") # Cross-platform alternative to PAUSE

if __name__ == "__main__":
    main()