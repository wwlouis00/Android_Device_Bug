import threading
import subprocess
import os
from datetime import datetime

# 建立時間戳路徑
def get_log_path():
    base_dir = os.getcwd()  # 使用當前路徑
    # 用日期建立資料夾
    folder_name = datetime.now().strftime("%Y%m%d")
    folder_path = os.path.join(base_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # 檔案名稱：時分秒.log
    file_name = datetime.now().strftime("%H%M%S") + ".log"
    return os.path.join(folder_path, file_name)

# adb logcat 執行
def run_logcat():
    log_path = get_log_path()
    print(f"開始記錄 log 到：{log_path}")
    with open(log_path, "w", encoding="utf-8") as f:
        process = subprocess.Popen(["adb", "logcat"], stdout=f, stderr=subprocess.STDOUT)
        process.wait()  # 這會卡住直到 adb logcat 停止

# 測試函數
def fun_timer():
    print("Hello Timer!")

if __name__ == "__main__":
    # 5 秒後開始 logcat
    t1 = threading.Timer(5, run_logcat)
    t1.start()

    # 1 秒後印出一次 Hello Timer
    t2 = threading.Timer(1, fun_timer)
    t2.start()

    # 10 秒後再印一次 Hello Timer
    t3 = threading.Timer(10, fun_timer)
    t3.start()
