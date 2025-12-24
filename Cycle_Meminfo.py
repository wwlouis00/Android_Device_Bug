import subprocess
import time
from datetime import datetime

# Define the ADB command as a list for better security and performance
ADB_CMD = ["adb", "shell", "grep", "-e", "MemAvailable", "-e", "MemFree", "/proc/meminfo"]

def monitor_memory(rounds=3600, interval=1):
    """
    Monitors memory usage and logs it to both console and a file.
    """
    # Create a unique filename with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"MemMonitor_{timestamp}.txt"
    
    print(f"[INFO] Monitoring started. Saving to {log_filename}")
    
    try:
        with open(log_filename, "a", encoding="utf-8") as f:
            for i in range(1, rounds + 1):
                # Get current time for each record
                current_time = datetime.now().strftime("%H:%M:%S")
                header = f"ROUND {i} | {current_time} ==================\n"
                
                # Execute command and capture output
                try:
                    # Using subprocess.check_output is more robust than os.system
                    output = subprocess.check_output(ADB_CMD, universal_newlines=True)
                except subprocess.CalledProcessError:
                    output = "Error: Failed to fetch memory info. (Device disconnected?)\n"

                # Print to console
                print(header + output)
                
                # Write to file
                f.write(header + output + "\n")
                f.flush()  # Ensure data is written to disk immediately
                
                # Wait for the next round
                if i < rounds:
                    time.sleep(interval)

    except KeyboardInterrupt:
        print("\n[INFO] Monitoring stopped by user.")

if __name__ == "__main__":
    # You can easily change rounds and interval here
    monitor_memory(rounds=3600, interval=1)