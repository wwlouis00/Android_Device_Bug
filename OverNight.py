import os
import time
import subprocess
from datetime import datetime

def get_meminfo():
    """Fetches memory info from the device via adb."""
    try:
        # Using subprocess.check_output for better error handling
        output = subprocess.check_output(["adb", "shell", "cat", "/proc/meminfo"], 
                                         universal_newlines=True, 
                                         stderr=subprocess.STDOUT)
        return output
    except subprocess.CalledProcessError as e:
        return f"[ERROR] Failed to fetch meminfo: {e.output}"
    except FileNotFoundError:
        return "[ERROR] ADB command not found. Please ensure ADB is installed and in PATH."

def main():
    # Configuration
    total_iterations = 12
    interval_seconds = 3600  # 1 hour
    base_dir = os.getcwd()
    result_file = os.path.join(base_dir, "MemTest.txt")

    print(f"[INFO] Logging to: {result_file}")
    print(f"[INFO] Monitoring started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Open file in append mode once per iteration or use a single context manager
    for i in range(total_iterations):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        header = f"============= <Iteration {i+1}> | {current_time} =============\n"
        
        print(f"[INFO] Progress: {i+1}/{total_iterations} - Logging data...")

        # Fetch data
        mem_data = get_meminfo()

        # Write to file
        try:
            with open(result_file, "a", encoding="utf-8") as f:
                f.write(header)
                f.write(mem_data)
                f.write("\n\n")
        except IOError as e:
            print(f"[ERROR] Could not write to file: {e}")

        # Wait for the next cycle, except after the last iteration
        if i < total_iterations - 1:
            print(f"[INFO] Sleeping for {interval_seconds} seconds...")
            time.sleep(interval_seconds)

    print(f"[INFO] Monitoring completed successfully at {datetime.now()}.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] Program interrupted by user.")