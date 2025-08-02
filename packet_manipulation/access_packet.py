from scapy.all import *

# Create a packet
packet = IP(src="192.168.1.1", dst="8.8.8.8")/TCP(sport=1234, dport=80)

# Access fields
print(f"Source IP: {packet[IP].src}")
print(f"Destination IP: {packet[IP].dst}")
print(f"Source Port: {packet[TCP].sport}")
print(f"Destination Port: {packet[TCP].dport}")


