from scapy.all import sniff, DNSQR

def dns_packet_callback(packet):
    if packet.haslayer(DNSQR):  # DNS question
        qry = packet[DNSQR]
        print(f"DNS Query: {qry.qname.decode()}   Type: {qry.qtype}")
        
sniff(filter="udp port 53", prn=dns_packet_callback, store=0, iface="eth0")
