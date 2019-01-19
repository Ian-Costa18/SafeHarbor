from devicefunctions import findDevices, lockDevice, unlockDevice
from smsclient import App, startclient
from time import sleep

def main():
    """ Main file for *PROGRAM NAME HERE*
    Detects if a new USB device gets plugged in, disables it and then sends an SMS
    """

    first_time = True
    locked_devices = []

    while True:
        hwid = findDevices()

        # Setup first time variables
        if first_time:
            baseline_hwid = hwid
            first_time = False
            print("\n".join(baseline_hwid))

        else:
            # Check if there's new device id's
            if hwid != baseline_hwid:
                for device in hwid:
                    # If there is a new device, lock it
                    if device not in baseline_hwid:
                        while findDevices() == hwid:
                            lockDevice(device)
                        baseline_hwid.append(device)
                        locked_devices.append(device)

                        smsclient = startclient()
            # If sms auth is good:
            try:
                if smsclient.auth:
                    for index, device in enumerate(locked_devices):
                        while findDevices() != hwid:
                            unlockDevice(device)
                        del locked_devices[index]
            except UnboundLocalError:
                continue


if __name__ == "__main__":
    main()
                   
            

    
