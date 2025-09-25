import os
import time
import datetime
import subprocess

def get_panel_status():
    """取得 panelstatus 結果 (只取中間 4 個字元)"""
    text = subprocess.getoutput(r'adb shell "su 0 dp panelstatus"')
    return text[53:57].strip()

def log_to_file(filepath, content):
    """寫入檔案"""
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(content + "\n")

def main():
    # 建立輸出資料夾
    base_dir = os.path.abspath(".")
    log_dir = os.path.join(base_dir, "Display")
    os.makedirs(log_dir, exist_ok=True)

    # 紀錄檔案名稱
    the_time = datetime.datetime.now().strftime("%Y%m%d_%H%M")
    record_file = os.path.join(log_dir, f"OnOffTest_{the_time}.txt")

    # 輸入測試次數
    rounds = int(input("請輸入執行 Display On/Off 的次數 (每 3 秒一個動作): "))

    for i in range(rounds):
        print(f"< {i+1} ROUND >")

        # Display ON
        subprocess.run(r'adb shell "su 0 dp displayon"', shell=True)
        status_on = get_panel_status()
        log_to_file(record_file, f"ROUND {i+1}")
        log_to_file(record_file, f"ON  : {status_on}")
        print(f"ON  : {status_on}")
        time.sleep(3)

        # Display OFF
        subprocess.run(r'adb shell "su 0 dp displayoff"', shell=True)
        status_off = get_panel_status()
        log_to_file(record_file, f"OFF : {status_off}\n")
        print(f"OFF : {status_off}")
        time.sleep(3)

    print("執行結束")
    os.system("pause")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[INFO] 使用者中斷程式。")
