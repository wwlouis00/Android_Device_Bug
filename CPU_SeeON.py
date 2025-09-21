import os
import datetime
import subprocess

def create_test_directory(base_dir="CPU_Usage_Test"):
    abs_path = os.path.join(os.path.abspath('.'), base_dir)
    try:
        os.makedirs(abs_path, exist_ok=True)
    except Exception as e:
        print(f"Error! Could not create directory: {abs_path}\n{e}")
        return None
    return abs_path

def get_log_filename(directory):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M')
    return os.path.join(directory, f"CPU_SeeON_{timestamp}.txt")

def run_cpu_test(log_path):
    cmd = ['adb', 'shell', 'cpu_usage']
    try:
        with open(log_path, 'w', encoding='utf-8') as logfile:
            subprocess.run(cmd, stdout=logfile, stderr=subprocess.STDOUT, check=True)
        print(f"[Path] {log_path}\n")
        print("CPU usage test completed.")
    except Exception as e:
        print(f"Error during CPU usage test: {e}")

def main():
    test_dir = create_test_directory()
    if not test_dir:
        return
    log_file = get_log_filename(test_dir)
    run_cpu_test(log_file)
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()