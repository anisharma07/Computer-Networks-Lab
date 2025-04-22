# Practical 6: Simulate ARP and RARP Protocol
# Define a table for IP-MAC mappings
arp_table = {
    '192.168.1.1': '00:0a:95:9d:68:16',
    '192.168.1.2': '00:0a:95:9d:68:17',
    '192.168.1.3': '00:0a:95:9d:68:18',
    '192.168.1.4': '00:0a:95:9d:68:19'
}

# Generate reverse mapping for RARP
rarp_table = {v: k for k, v in arp_table.items()}

# ARP function
def arp(ip_address):
    print("\n[ARP Request]")
    if ip_address in arp_table:
        print(f"ARP Reply: MAC address for IP {ip_address} is {arp_table[ip_address]}")
    else:
        print(f"No entry found for IP address: {ip_address}")

# RARP function
def rarp(mac_address):
    print("\n[RARP Request]")
    if mac_address in rarp_table:
        print(f"RARP Reply: IP address for MAC {mac_address} is {rarp_table[mac_address]}")
    else:
        print(f"No entry found for MAC address: {mac_address}")

# Main function
def main():
    while True:

        print("\n--- CSE LAN Protocol Menu ---")
        print("1. ARP (IP to MAC)")
        print("2. RARP (MAC to IP)")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            ip = input("Enter IP Address: ")
            arp(ip)
        elif choice == '2':
            mac = input("Enter MAC Address: ")
            rarp(mac)
        elif choice == '3':
            print("Exiting ARP/RARP Simulator...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()