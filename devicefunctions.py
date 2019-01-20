""" A module holding 3 functions
find_devices: A scanner for device ID's
lock_device: Runs a .bat file that locks out devices
unlock_device: Opposite of lock_device
"""
import subprocess
import re

# All names have been commented out since they weren't being used

def find_devices():
    """ Finds currently plugged in USB devices
    Returns a list of device ID's
    """

    devices_str = subprocess.check_output(["devcon", "find", "*USB*"]).decode("utf-8")
    # Use regex to find device names
    regex = r": .*"
    devices_re = re.findall(regex, devices_str)
    devices_lst = devices_str.split("\n")
    device_ids, device_names = [], []

    # Find device IDs in devices_lst, delete last 2 entries (found message and new line)
    for index, i in enumerate(devices_lst):
        if index != len(devices_lst)-2:
            device_ids.append(i[:i.find(':')].strip())

    # Find device names in devices_re
    for string in devices_re:
        # Removes /r at the end of string
        r_remove = len(string)-1
        # Removes ': ' at the begining of string
        device_names.append(string[2:r_remove])

    # Delete devices we cannot lock
    for index, device in enumerate(device_ids):
        if "VID" in device or "ROOT":
            if "CH000001" not in device:
                del device_ids[index]

    return device_ids

def lock_device(device_id):
    """ Runs locker.bat with device_id
    Returns a string
    """

    print(f"Locking {device_id}")

    # Get useable device_id
    device_id = '"' + device_id.split('&')[0] + '"'

    # Open locker.bat
    locker = subprocess.Popen(["locker.bat ", device_id], stdout=subprocess.PIPE)

    return locker.stdout


def unlock_device(device_id):
    """ Runs unlocker.bat with device_id
    Returns a string
    """

    print(f"Unlocking {device_id}")

    # Get useable device_id
    device_id = '"' + device_id.split('&')[0] + '"'

    # Open unlocker.bat
    unlocker = subprocess.Popen(["unlocker.bat ", device_id], stdout=subprocess.PIPE)

    return unlocker.stdout
