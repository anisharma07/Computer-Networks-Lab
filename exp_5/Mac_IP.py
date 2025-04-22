import socket
import uuid

def get_ip_address():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google DNS
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address
    except Exception as e:
        return f"Unable to get IP address: {e}"

def get_mac_address():
    try:
        mac = uuid.getnode()
        mac_address = ':'.join(['{:02x}'.format((mac >> ele) & 0xff) 
                                for ele in range(40, -1, -8)])
        return mac_address.upper()
    except Exception as e:
        return f"Unable to get MAC address: {e}"

def main():
    ip = get_ip_address()
    mac = get_mac_address()

    print("Machine Network Information")
    print("===========================")
    print(f"IP Address : {ip}")
    print(f"MAC Address: {mac}")

if __name__ == "__main__":
    main()
