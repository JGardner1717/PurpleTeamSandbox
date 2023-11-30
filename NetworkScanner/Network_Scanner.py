import scapy.all as scapy
import optparse
import argparse

#1)arp_request
#2)broadcast
#3)response

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", dest="ip_address", help="IP Address or IP range to scan")
    options = parser.parse_args()

    if not options.ip_address:
        parser.error("[-] Please specify an IP address or range, use --help for more info.")
    return options

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet/arp_request_packet
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    answered_list.summary()

user_ip_address = get_arguments()
scan_my_network(user_ip_address.ip_address)
