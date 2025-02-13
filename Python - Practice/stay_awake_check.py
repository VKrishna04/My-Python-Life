import os
import subprocess
import psutil  # Install with `pip install psutil`


def get_display_timeout():
    """
    Retrieves the display timeout value from the current power settings.
    Returns the timeout in minutes, or 0 if display timeout is disabled.
    """
    print("Checking native display timeout settings...")
    try:
        # Fetch display timeout using powercfg
        result = subprocess.check_output(
            "powercfg /q SCHEME_CURRENT SUB_VIDEO VIDEOIDLE", shell=True, text=True
        )

        for line in result.splitlines():
            if "VIDEOIDLE" in line and "Power Setting Index" in line:
                timeout_value = int(line.split()[-1])
                if timeout_value == 0x0 or timeout_value == 0xFFFFFFFF:
                    print(
                        "Display timeout is disabled (screen will stay on indefinitely)."
                    )
                    return 0
                else:
                    print(f"Native display timeout is set to {timeout_value} seconds.")
                    return timeout_value // 60  # Convert to minutes

    except Exception as e:
        print(f"Error retrieving display timeout: {e}")
    return -1


def check_awake_tools():
    """
    Checks for known screen-awake tools like PowerToys Awake, Caffeine, or similar.
    Returns True if any such tools are detected.
    """
    print("\nChecking for tools like PowerToys Awake or similar...")
    awake_tools = ["PowerToys.Awake", "Caffeine", "KeepAwake", "NoSleep"]
    found = False

    # Iterate through all running processes
    for process in psutil.process_iter(["name"]):
        try:
            process_name = process.info["name"]
            for tool in awake_tools:
                if tool.lower() in process_name.lower():
                    print(f"Tool detected: {process_name}")
                    found = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if not found:
        print("No known awake tools detected.")
    return found


def check_system_awake_requests():
    """
    Checks system-wide requests to keep the display awake using `powercfg /requests`.
    Returns True if there are active requests preventing sleep.
    """
    print("\nChecking system requests preventing sleep...")
    try:
        result = subprocess.check_output("powercfg /requests", shell=True, text=True)
        print("Power requests summary:\n", result.strip())

        if "None." in result:
            print("No active system requests preventing sleep detected.")
            return False
        else:
            print("System requests are preventing sleep.")
            return True
    except Exception as e:
        print(f"Error checking system requests: {e}")
    return False


def decide_screen_timeout():
    """
    Combines all checks to decide when the screen will timeout.
    """
    print("\n----- Final Screen Timeout Analysis -----\n")

    # Check display timeout setting
    display_timeout = get_display_timeout()

    # Check for awake tools
    awake_tools_running = check_awake_tools()

    # Check for system requests preventing sleep
    system_awake_requests = check_system_awake_requests()

    # Final decision logic
    if system_awake_requests:
        print(
            "\nConclusion: Active system requests are preventing the screen from sleeping."
        )
    elif awake_tools_running:
        print(
            "\nConclusion: An awake tool is running. The screen will stay on indefinitely."
        )
    elif display_timeout == 0:
        print(
            "\nConclusion: Display timeout is disabled. The screen will stay on indefinitely."
        )
    elif display_timeout > 0:
        print(
            f"\nConclusion: The screen will timeout in {display_timeout} minutes as per native settings."
        )
    else:
        print(
            "\nConclusion: Unable to determine the screen timeout. Please check power settings manually."
        )


if __name__ == "__main__":
    print("Analyzing system settings, tools, and power configurations...\n")
    decide_screen_timeout()
