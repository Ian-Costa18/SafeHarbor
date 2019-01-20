from devicefunctions import findDevices, lockDevice, unlockDevice
from smsmessagingnogui import run

def main():
    """ Main file for *PROGRAM NAME HERE*
    Detects if a new USB device gets plugged in, disables it and then sends an SMS
    """

    first_time = True
    locked_devices = []
    smscheck = 0

    while True:
        hwid = findDevices()

        # Setup first time variables
        if first_time:
            baseline_hwid = hwid
            first_time = False
            print("\n".join(baseline_hwid))

        else:
            # Check if there's new device id's
            lock_device = []
            lockcheck = 0
            if hwid != baseline_hwid:
                smsclient = None
                for device in hwid:
                    # If there is a new device, lock it
                    if device not in baseline_hwid:
                        lock_device.append(device)
                        while device not in baseline_hwid and lockcheck <= 15:
                            lockcheck += 1
                            lockDevice(device)
                            try:
                                lock_device.remove(device)
                            except ValueError:
                                continue
                        baseline_hwid.append(device)

                if lock_device == [] and smscheck == 0:
                    smsclient = run()
                    smscheck = 1


if __name__ == "__main__":
    main()
                        
    
