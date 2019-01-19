import subprocess
import re

def findDevices() :

    devices_str = subprocess.check_output([".\\devcon", "find", "*USB*"]).decode("utf-8")
    
    regex = r": .*"

    devices_re = re.findall(regex, devices_str)

    devices_lst = []

    for string in devices_re:
        # Removes /r at the end of string
        r = len(string)-1
        # Removes ': ' at the begining of string
        devices_lst.append(string[2:r])

    return devices_lst

print(findDevices())

