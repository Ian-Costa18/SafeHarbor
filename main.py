from devicefinder import findDevices
from lockunlock import lockDevice, unlockDevice

first_time = True

while True:

    if first_time:
        hwid = findDevices()[0]
        baseline_hwid = hwid
        first_time = False
        for i in baseline_hwid:
            print(f"Found device '{i}'")

    else:
        hwid, names = findDevices()
        new_hwid = []
        
        if hwid != baseline_hwid:
            for device in hwid:
                if device not in baseline_hwid:
                    new_hwid.append(device)
                    lock(device)

            

    
