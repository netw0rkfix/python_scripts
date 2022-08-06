import sys

def clear_screen():
    for i in range(5):
        print('#')


#Checkin validity of the address in the file input by the user
def ip_addr_valid(iplist):
    

    print('# Checking addresses format \n#',( '-' * 57 ))
    #Iterating over Ip address in the file
    for ip in iplist: 
        #set value of the first address to the ip variable
        ip = ip.rstrip('\n')

        #Create a list of 4 values, representing the octet of the ip address 
        octet_list = ip.split('.')

        #Cheking if address is within range of a valid ip address to be use
        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):                                             
            continue
        else:
            print('\n# There was an invalid ip address in the file \n#', ip)
            sys.exit()
    print('# OK - All Ip addresses are VALID \n#',( '-' * 57 ))
    return iplist

