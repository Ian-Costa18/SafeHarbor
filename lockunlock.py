import subprocess

def lockDevice(device_id):

    # Make sure ID is formatted correctly
    if device_id[1] != @:
        id_format = ['"', '@']

        for letter in device_id:
            id_format.append(letter)
        id_format.append('"')

        device_id = ''.join(id_format)

    subprocess.run(['devcon', 'disable', device_id])


def unlockDevice(device_id):

    # Make sure ID is formatted correctly
    if device_id[1] != @:
        id_format = ['"', '@']

        for letter in device_id:
            id_format.append(letter)
        id_format.append('"')

        device_id = ''.join(id_format)

    subprocess.run(['devcon', 'enable', device_id])
