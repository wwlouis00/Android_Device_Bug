import os
import time
import subprocess
from datetime import datetime

def main():
    # 在當前目錄建立檔案
    base_dir = os.getcwd()
    result_file = os.path.join(base_dir, "MemTest.txt")

    print(f"[INFO] 紀錄檔案：{result_file}")

    for i in range(12):  # 跑 12 次
        header = f"=============<{i+1}>=============\n"
        print(header.strip())

        # 用 append 模式一次寫入 header
        with open(result_file, "a", encoding="utf-8") as f:
            f.write(header)

        # 直接抓 adb 輸出
        meminfo = subprocess.getoutput("adb shell cat /proc/meminfo")

        # 寫入檔案
        with open(result_file, "a", encoding="utf-8") as f:
            f.write(meminfo + "\n\n")

        # 每次間隔 1 小時
        if i < 11:  # 最後一次不需要 sleep
            time.sleep(3600)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] 使用者中斷程式。")
