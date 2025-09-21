import subprocess
import time

def run_cmd(cmd, echo=True):
    """Run a shell command and print its output."""
    if echo:
        print(f"[CMD] {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8')
        if result.stdout:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")

def main():
    # Enable developer mode on Android device
    run_cmd("adb shell setprop persist.horus.rddevmode 1")

    # Prompt user to close CU or SteamVR before starting the test
    print("[Close CU or SteamVR to Start Test]")
    run_cmd("TASKKILL /IM vrmonitor.exe")
    input("[Press Enter to start the test after CU and SteamVR are closed]\n")

    # Get root access on Android device
    run_cmd("adb root")

    # Push SteamVR.url file to /storage directory on Android device
    print("[PUSH ITEM]")
    run_cmd(r'adb push "C:\Users\PQT2\Desktop\SteamVR.url" /storage')

    # List files in /storage directory on Android device
    print("[LIST ITEM]")
    run_cmd("adb shell ls /storage")

    time.sleep(1)

    # Pull SteamVR.url file from Android device to local D:\Tools folder
    print("[PULL ITEM]")
    run_cmd(r'adb pull /storage/SteamVR.url D:\Tools')
    run_cmd(r'Start D:\Tools')

    print("[PLEASE CHECK ITEM FROM FOLDER]\n")
    time.sleep(10)

    # Delete SteamVR.url file from local and Android device
    print("[DELETE ITEM]")
    run_cmd(r'del D:\Tools\SteamVR.url')
    run_cmd("adb shell rm /storage/SteamVR.url")

    # List files again in /storage directory on Android device
    print("[LIST ITEM]")
    run_cmd("adb shell ls /storage")

    input("[Press Enter to execute ADB REBOOT]\n")
    run_cmd("adb reboot")

    # Search and run ViveConsole.exe if exists
    result = subprocess.run('where /R "c:\\Program Files (x86)" ViveConsole.exe', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    exe_path = result.stdout.strip()
    if exe_path:
        run_cmd(f'"{exe_path}"')
    else:
        print("ViveConsole.exe not found.")

if __name__ == "__main__":
    main()