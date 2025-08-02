from scapy.all import *

# Send ping and get response
try:
    response = sr1(IP(dst="8.8.8.8")/ICMP(), timeout=2)
    if response:
        print(f"Ping successful! Response from {response[IP].src}")
    else:
        print("No response")
except Exception as e:
    print(f"Error: {e}")
