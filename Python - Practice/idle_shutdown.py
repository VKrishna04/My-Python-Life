import os
import time
import ctypes
import logging
from datetime import datetime

# Windows API Constants
MONITOR_ON = 1
MONITOR_OFF = 2
MONITOR_STANDBY = 3


class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def setup_logging():
    logging.basicConfig(
        filename="screen_monitor.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
    )


def get_idle_time():
    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(LASTINPUTINFO)
    if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii)):
        millis = ctypes.windll.kernel32.GetTickCount() - lii.dwTime
        return millis / 1000
    return 0


def is_monitor_on():
    try:
        # GetMonitorState function from user32.dll
        monitor_state = ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, -1)
        return monitor_state == MONITOR_ON
    except:
        return True


def monitor_idle_time(threshold_seconds):
    setup_logging()
    start_time = time.time()
    logging.info(f"Monitoring started with threshold: {threshold_seconds} seconds")

    while True:
        clear_screen()
        idle_time = get_idle_time()
        elapsed_time = time.time() - start_time

        print(f"Monitoring System Status:")
        print(f"------------------------")
        print(f"Elapsed Time: {elapsed_time:.2f} seconds")
        print(f"Idle Time: {idle_time:.2f} seconds")
        print(f"Threshold: {threshold_seconds} seconds")
        print(f"------------------------")

        # Check monitor state
        if not is_monitor_on():
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\nMonitor turned off at {timestamp}")
            logging.info(f"Monitor turned off at {timestamp}")
            break

        time.sleep(0.5)  # Update twice per second


if __name__ == "__main__":
    THRESHOLD_SECONDS = 60  # Set idle time threshold in seconds
    try:
        monitor_idle_time(THRESHOLD_SECONDS)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user")
        logging.info("Monitoring stopped by user")
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        logging.error(f"Error occurred: {str(e)}")
