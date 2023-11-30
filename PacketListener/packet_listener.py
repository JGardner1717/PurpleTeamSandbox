import scapy.all as scapy
#from scapy_http import http

def listen_packets(interface):

    scapy.sniff(iface=interface,store=False,prn=analyze_packets)
    #prn = callback function

def analyze_packets(packet):
    #packet.show()
    if packet.haslayer(scapy.TCP) and packet.haslayer(scapy.Raw):
        # Attempt to decode HTTP content from the Raw layer
        try:
            http_payload = packet[scapy.Raw].load.decode('utf-8')
            if "HTTP" in http_payload:  # Simple check for HTTP content
                print(http_payload)
        except UnicodeDecodeError:
            pass  # Ignore decode errors

listen_packets("eth0")
