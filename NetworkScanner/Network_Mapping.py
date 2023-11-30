import scapy.all as scapy
import ipaddress

def scan(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

count = 0
def print_result(results_list):
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"])
        count = count + 1

# Use ipaddress module to generate all IPs in the subnet
network = ipaddress.ip_network('10.0.0.0/24', strict=False)
all_ips = [str(ip) for ip in network.hosts()]


print("IP\t\t\tMAC Address\n------------------------------------------")
# Scan each IP in the subnet
for ip in all_ips:
    scan_result = scan(ip)
    print_result(scan_result)
