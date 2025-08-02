from scapy.all import *

# stack using 
# Create a simple ICMP ping packet
ping_packet = IP(dst="8.8.8.8")/ICMP()

# Create a TCP SYN packet
syn_packet = IP(dst="192.168.1.1")/TCP(dport=80, flags="S")

# Create an ARP request
arp_request = ARP(pdst="192.168.1.0/24")

# Display packet structure
print("ICMP Packet:")
ping_packet.show()

print("\nTCP SYN Packet:")
syn_packet.show()

print("\nARP Request:")
arp_request.show()
