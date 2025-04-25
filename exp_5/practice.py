import socket
import uuid


def getIp():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception as e:
        print(f"error: {e}")


def getMac():
    mac = uuid.getnode()
    macAddress = ':'.join(['{:02x}'.format((mac >> ele) & 0xff)
                          for ele in range(40, -1, -8)])
    return macAddress.upper()


print(getIp())
print(getMac())
