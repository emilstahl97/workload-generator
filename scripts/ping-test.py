from scapy.all import IP, ICMP, sr1

def simple_ping(target_ip):
    # Craft an ICMP echo request packet
    packet = IP(dst=target_ip) / ICMP()

    # Send the packet and receive the response
    response = sr1(packet, timeout=2, verbose=False)

    # Check if a response was received
    if response:
        print(f"Response received from {target_ip}")
        response.show()
    else:
        print(f"No response received from {target_ip}")

# Target IP address (1.1.1.1 in this case)
target_ip = "1.1.1.1"

# Call the function to send the ping and print the response
simple_ping(target_ip)
