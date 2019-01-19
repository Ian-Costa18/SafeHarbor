import subprocess
import re

def findDevices() :

    devices_str = subprocess.check_output([".\\devcon", "find", "*USB*"]).decode("utf-8")
    
    regex = r": .*"

    devices_re = re.findall(regex, devices_str)

    devices_lst = devices_str.split("\n")

    device_ids, device_names = [],[]

    # Find device IDs in devices_lst, delete last 2 entries (found message and new line)
    for index, i in enumerate(devices_lst):
        if index != len(devices_lst)-2:
            device_ids.append(i[:i.find(':')].strip())

    # Find device names in devices_re
    for string in devices_re:
        # Removes /r at the end of string
        r = len(string)-1
        # Removes ': ' at the begining of string
        device_names.append(string[2:r])

    return device_ids, device_names

