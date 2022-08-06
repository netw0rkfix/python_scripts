#!/home/serveradmin/Desktop/security/DEV/pyhton/environments/bin/ python3

#%%
### Importing librairies
import optparse
import scapy.all as scapy


#%%
### Deal with arguments passed in
def get_arguments():

    ### Set a parser object
    parser = optparse.OptionParser()
    
    ### Define options and their help message 
    parser.add_option("-t", "--target", dest="target", help="Type IPV4 single host or ip range. EX 192.168.1.1 or 192.168.1.1/24")
    
    ### Set options enter by the user to variables
    options = parser.parse_args()[0]
    
    ### Perform verification on user input
    if not options.target:
        parser.error("[*] - Please specify a ip or ip range, use --help for more info")
    
    ### If no error found, return user input options
    return options


#%%
### Perform an arp broadcast on the ip ou ip range passed in and return a list of dictionnary with the results
def arpscan(ip):

    ### Create an ARP packet with desired IP
    arp_request = scapy.ARP(pdst=ip)
    
    ### Create a braodcast packet sent to broadcast address
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")    
    
    ### Combine both variable to build a the complete packet
    arp_resquest_broadcast = broadcast/arp_request
    
    ### Set a variable with results
    answered_list  = scapy.srp(arp_resquest_broadcast, timeout=1, verbose=False)[0]
    
    ### Create empty list to store client mac-ip value
    client_list = []
    
    ### Add value as dictionnarie in client_list
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
    
    ### Return a list of dictionnary with IP and MAC
    return client_list


#%%
### Show results of arpscan if needed
def print_scan_result(results_list):
    print("\nIP\t\t\tMAC Address\n-------------------------------------------")   
    for client in results_list:
        print(client["ip"] + "\t\t" + client["mac"] ) 

#%%
##############################################
### Main program executing on file read ######
##############################################


arguments = get_arguments()
scan_result = arpscan(arguments.target)
print_scan_result(scan_result)


# %%
