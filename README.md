# Android Debug Tool

This project introduces commonly used debugging tools on the Android platform, helping developers analyze, debug applications, and monitor device or emulator status. Below are the main tools and their usage:

## 1. Android Debug Bridge (ADB)

ADB is a powerful command-line tool for communicating with Android devices connected to your development machine. Common uses include installing/uninstalling apps, file transfer, debugging, and testing.

**Common Commands:**
```bash
# List connected devices
adb devices

# Install APK file
adb install path/to/your_app.apk

# Uninstall specified app
adb uninstall com.example.your_app
```

## 2. Logcat

Logcat is Android’s logging tool for capturing and viewing application and system logs. It helps track errors and analyze behaviors.

**Common Commands:**
```bash
# View all log output
adb logcat

# Filter logs by tag
adb logcat -s TAG_NAME
```

## 3. Android Profiler

Android Profiler provides a graphical interface to analyze app performance and behavior, including CPU, memory, and network metrics.

**Usage Steps:**
1. Open your project in Android Studio.
2. Click the Android Profiler panel at the bottom.
3. Select the metrics to monitor (CPU, memory, network).
4. Run your app and observe real-time performance data.

## 4. Hierarchy Viewer

Hierarchy Viewer is a visual tool for inspecting and analyzing the UI structure of Android applications, helping optimize interface design and debugging.

**Usage Steps:**
1. Open your project in Android Studio.
2. Select the layout XML file you want to inspect.
3. Click the Hierarchy Viewer panel.
4. Check the layout hierarchy and component properties.

---

For more details, please refer to the [official Android documentation](https://developer.android.com/studio/debug).