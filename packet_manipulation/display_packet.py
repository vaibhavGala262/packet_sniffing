from scapy.all import *

# Create packets
ping = IP(dst="8.8.8.8")/ICMP()
web = IP(dst="google.com")/TCP(dport=80)

# Display them
print("Ping packet:")
ping.show()

print("\nWeb packet:")  
web.show()
