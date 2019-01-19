import subprocess
import re

def findDevices() :

    devices_str = subprocess.check_output([".\\devcon", "find", "*USB*"]).decode("utf-8")
    
    regex = r": .*"

    devices_re = re.findall(regex, devices_str)

    devices_lst = devices_str.split("\n")

    device_ids, device_names = [],[]

    for i in devices_lst:
        device_ids.append(i[:i.find(':')].strip())

    for string in devices_re:
        # Removes /r at the end of string
        r = len(string)-1
        # Removes ': ' at the begining of string
        device_names.append(string[2:r])

    return device_ids, device_names

