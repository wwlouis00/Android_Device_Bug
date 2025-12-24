import os
import time
import datetime
import subprocess
from pathlib import Path

def run_adb_cmd(cmd):
    """Executes an ADB command and returns the stripped output."""
    try:
        # Use subprocess.check_output for more reliable result capturing
        result = subprocess.check_output(f'adb shell "{cmd}"', shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output.strip()}"

def get_panel_status():
    """Gets panel status and extracts the relevant state indicator."""
    raw_output = run_adb_cmd("su 0 dp panelstatus")
    
    # Improved parsing: 
    # If you know the specific word (e.g., '0x01' or 'ON'), 
    # it's safer to look for that rather than hardcoding index 53:57.
    # Here we fallback to slicing but add a safety check.
    if len(raw_output) > 57:
        return raw_output[53:57].strip()
    return raw_output[-10:].strip() # Fallback to last 10 chars if output is short

def main():
    # 1. Setup Directory using Pathlib (Modern approach)
    log_dir = Path("Display")
    log_dir.mkdir(exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    record_file = log_dir / f"OnOffTest_{timestamp}.txt"

    # 2. User Input with basic validation
    try:
        total_rounds = int(input("Enter number of On/Off cycles (3s interval): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    print(f"[INFO] Logging to: {record_file}")

    # 3. Test Loop
    with open(record_file, "a", encoding="utf-8") as f:
        for i in range(1, total_rounds + 1):
            print(f"\n--- Round {i} ---")
            f.write(f"ROUND {i}\n")

            # Sequence: ON then OFF
            for action in ["displayon", "displayoff"]:
                # Execute command
                run_adb_cmd(f"su 0 dp {action}")
                
                # Verify status
                status = get_panel_status()
                state_label = action.replace("display", "").upper() # "ON" or "OFF"
                
                log_entry = f"{state_label:<4}: {status}"
                print(log_entry)
                f.write(log_entry + "\n")
                
                # Interval between actions
                if not (i == total_rounds and action == "displayoff"):
                    time.sleep(3)
            
            f.write("\n") # Add newline after each round for readability

    print("\n[INFO] Test completed.")
    os.system("pause")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] Process interrupted by user.")