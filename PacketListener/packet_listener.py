import scapy.all as scapy

def listen_packets(interface):

    scapy.sniff(iface=interface,store=False,prn=analyze_packets)

def analyze_packets(packet):
    if packet.haslayer(scapy.TCP) and packet.haslayer(scapy.Raw):
        # Decode HTTP content from the Raw layer
        try:
            http_payload = packet[scapy.Raw].load.decode('utf-8')
            # Printing http packets
            if "HTTP" in http_payload:  
                print(http_payload)
        except UnicodeDecodeError:
            # Ignorng Decode Errors
            pass  

listen_packets("eth0")
