import os
import re
import subprocess
import sys
import time
from datetime import datetime


def get_meminfo(duration_sec: int, interval_sec: int = 60):
    """
    每隔 interval_sec 秒，抓取一次 adb meminfo，直到 duration_sec 秒結束
    """
    # 建立以日期為名的資料夾
    base_dir = os.getcwd()
    folder_name = datetime.now().strftime("%Y%m%d")
    folder_path = os.path.join(base_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # 檔案名稱 (開始時間)
    result_file = os.path.join(folder_path, datetime.now().strftime("%H%M%S") + "_MemAvailable_usage.txt")

    print(f"[INFO] 紀錄檔案: {result_file}")
    print(f"[INFO] 總執行時間: {duration_sec} 秒，每 {interval_sec} 秒紀錄一次")

    start_time = time.time()

    while time.time() - start_time < duration_sec:
        elapsed = int(time.time() - start_time)

        if elapsed % interval_sec == 0:
            ts = subprocess.getoutput('adb shell date')
            check_mem = subprocess.getoutput('adb shell cat /proc/meminfo')
            dumpsys_mem = subprocess.getoutput('adb shell "dumpsys meminfo"')

            with open(result_file, mode='a', encoding="utf-8") as f:
                f.write("=" * 40 + "\n")
                f.write(f"[TimeStamp] {ts}\n\n")
                f.write(check_mem + "\n\n")
                f.write(dumpsys_mem + "\n\n")

            # 找出 MemAvailable
            mem_available = ""
            for line in check_mem.splitlines():
                if "MemAvailable" in line:
                    mem_available = line.strip()
                    break

            if mem_available:
                print(f"[{elapsed:5d}s] {mem_available}")

        time.sleep(1)


if __name__ == "__main__":
    try:
        if len(sys.argv) == 2 and sys.argv[1] != "?":
            test_time = int(sys.argv[1])
            get_meminfo(test_time)
        else:
            print("使用方式:\n    python " + sys.argv[0] + " [測試時間 (秒)]")
            print("例如:\n    python " + sys.argv[0] + " 600   # 紀錄 10 分鐘")
    except KeyboardInterrupt:
        print("\n[INFO] 使用者中斷程式。")
