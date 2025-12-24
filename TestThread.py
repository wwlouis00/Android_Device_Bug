import threading
import subprocess
import time
import sys
from datetime import datetime
from pathlib import Path

class LogcatManager:
    """Class to manage ADB logcat lifecycle and file logging."""
    
    def __init__(self):
        self.process = None
        self.log_path = self._prepare_path()

    def _prepare_path(self):
        """Creates directory and returns unique log file path."""
        # Use Pathlib for better path management
        log_dir = Path.cwd() / datetime.now().strftime("%Y%m%d")
        log_dir.mkdir(parents=True, exist_ok=True)
        
        file_name = datetime.now().strftime("%H%M%S_Logcat.log")
        return log_dir / file_name

    def start_logging(self):
        """Starts adb logcat as a subprocess."""
        print(f"[INFO] Initializing Logcat: {self.log_path}")
        
        # Optional: Clear the device log buffer before starting
        # subprocess.run(["adb", "logcat", "-c"])

        try:
            # Open file with 'with' logic is handled by Popen's stdout parameter
            log_file = open(self.log_path, "w", encoding="utf-8")
            
            # Use Popen to run as a non-blocking background task
            self.process = subprocess.Popen(
                ["adb", "logcat", "-v", "time"],  # Add '-v time' for better debug context
                stdout=log_file,
                stderr=subprocess.STDOUT
            )
            print("[INFO] Logcat is running in the background...")
        except FileNotFoundError:
            print("[ERROR] ADB not found. Ensure Android SDK is in your PATH.")
        except Exception as e:
            print(f"[ERROR] Failed to start logcat: {e}")

    def stop_logging(self):
        """Gracefully stops the logcat process."""
        if self.process:
            print(f"\n[INFO] Stopping Logcat...")
            self.process.terminate()  # Sends SIGTERM
            self.process.wait()
            print("[INFO] Logcat stopped.")

def fun_timer(message="Hello Timer!"):
    """Standard task function."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

if __name__ == "__main__":
    logger = LogcatManager()

    # 1. Schedule Hello Timer (after 1s)
    threading.Timer(1, fun_timer, args=["Initial Task - Hello!"]).start()

    # 2. Schedule Logcat start (after 5s)
    # Using lambda to call the method without blocking
    log_timer = threading.Timer(5, logger.start_logging)
    log_timer.start()

    # 3. Schedule another task (after 10s)
    threading.Timer(10, fun_timer, args=["Delayed Task - Logging check"]).start()

    try:
        # Keep the main thread alive while timers run
        # In a real test, this might be your main testing logic
        while threading.active_count() > 1:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] User interrupted.")
    finally:
        # Crucial: Ensure the background logcat process is killed
        logger.stop_logging()
        print("[INFO] Program exited.")