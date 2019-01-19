from devicefunctions import findDevices, lockDevice, unlockDevice
from smsmessagingnogui import run
from time import sleep

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
            if hwid != baseline_hwid:
                smsclient = None
                for device in hwid:
                    # If there is a new device, lock it
                    if device not in baseline_hwid:
                        lockcheck = 0
                        while device not in baseline_hwid and lockcheck <= 15:
                            lockcheck += 1
                            lockDevice(device)
                        if device in findDevices() and smscheck == 0:
                            smsclient = run()
                            smscheck = 1
                        
                        baseline_hwid.append(device)
                        
                    if smsclient == "Pass":
                        unlockDevice('*')
                        
                        

if __name__ == "__main__":
    main()
                        
    
