import subprocess

def lockDevice(device_id):

    print(f"Locking {device_id}")

    # Get useable device_id
    device_id = '"' + device_id.split('&')[0] + '"'

    locker = subprocess.Popen(["locker.bat ", device_id], stdout=subprocess.PIPE)

    return locker.stdout


def unlockDevice(device_id):

    print(f"Unlocking {device_id}")

    # Get useable device_id
    device_id = '"' + device_id.split('&')[0] + '"'

    unlocker = subprocess.Popen(["unlocker.bat ", device_id], stdout=subprocess.PIPE)

    return unlocker.stdout
