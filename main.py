""" Main module for *PROGRAM NAME HERE*
Run this file using "python main.py" to start the script
"""
from devicefunctions import find_devices, lock_device
from smsmessagingnogui import start_sms

def main():
    """ Main file for *PROGRAM NAME HERE*
    Detects if a new USB device gets plugged in, disables it and then sends an SMS
    """

    # Setup variables for checkers
    first_time = True
    smscheck = 0
    lock_device_lst = []

    while True:
        hwid = find_devices()

        # Setup first time variables
        if first_time:
            baseline_hwid = hwid
            first_time = False
            print("\n".join(baseline_hwid))

        else:
            # More checker variables
            lockcheck = 0
            # Check if there's new device id's
            if hwid != baseline_hwid:
                for device in hwid:
                    # More checker variables
                    lockcheck = 0
                    # If there is a new device, lock it
                    if device not in baseline_hwid:
                        lock_device_lst.append(device)
                        # Keep locking device until its gone or loops too much
                        while device not in baseline_hwid and lockcheck <= 15:
                            lockcheck += 1
                            lock_device(device)
                            # Delete from list only first time in loop
                            if lockcheck == 1:
                                lock_device_lst.remove(device)
                        baseline_hwid.append(device)
                # After all new devices are locked, start authentication
                if lock_device_lst == [] and smscheck == 0:
                    start_sms()
                    smscheck = 1


if __name__ == "__main__":
    main()
