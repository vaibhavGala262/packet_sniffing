from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())  # Show a one-line summary for each packet

# Capture packets on the default interface
sniff(prn=packet_callback, store=0 , iface="eth0")
