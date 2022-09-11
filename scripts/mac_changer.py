# importing needed librairies
import subprocess
import optparse
import re
import random

# Return the list of interface on the host
def get_host_int():
    # define interface empty list
    intrf = []
    # Store ifconfig to interface.txt
    subprocess.call("ifconfig > interface.txt", shell=True)
    # open user's file for reading
    interface_raw = open("interface.txt", 'r')
    # Put the cursor at the start of the file
    interface_raw.seek(0)
    # Reading all the lines of the txt file and append them to a list
    interface_lines = interface_raw.readlines()
    # Closing the file
    interface_raw.close()
    # iterate over every line to keep only line with interface name
    # Append to intrf list names of every interfaces on host system
    for i in interface_lines:
        if "flag" in i:
            interface_split = i.split()
            intrf.append(interface_split[0].replace(':', ''))
    # return the complete list of every interface when fonction is called
    return intrf

# return mac address of the host
def get_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"..:..:..:..:..:..", str(ifconfig_result))
    if mac_address_search_result.group(0):
        return mac_address_search_result.group(0)
    else:
        print("[-] - Could not get MAC Address")
        quit()

# Deal with arguments passed in
def get_arguments():
    # set a parser object
    parser = optparse.OptionParser()
    # define options and their help message
    parser.add_option("-i", "--interface", dest="interface", help="Enter the interface name")
    parser.add_option("-a", "--address", dest="new_mac", help="Manualy define the new mac for interface")
    parser.add_option("-r", "--random", dest="random_mac", help="yes/no to generate and set random mac address")
    # set options enter by the user to variables
    options = parser.parse_args()[0]
    # verify user input argument and return value accordingly
    if not options.interface or options.interface not in str(get_host_int()):
        parser.error("[*] - Please specify a valid network interface interface, use --help for more info")
    elif not options.new_mac and not options.random_mac or options.random_mac != "yes":
        parser.error("[*] - Please specify a MAC address, use --help for more info")
    elif not options.random_mac and options.new_mac:
        return options
    elif not options.new_mac and options.random_mac == "yes":
        options.new_mac = random_mac()
        return options

# Return a randomized MAC address
def random_mac():
    myhexdigits = []
    for x in range(6):
        # x will be set to the values 0 to 5
        a = random.randint(0, 255)
        # hex will be 2 hexadecimal digits with a leading 0 if necessary
        # you need 2 hexadecimal digits to represent 8 bits
        hex = '%02x' % a
        # save for after the loop ends
        myhexdigits.append(hex)
    # using : as the delimiter, join the 2-digit hex strings together into a single string
    rand_mac = str(':'.join(myhexdigits))
    return rand_mac

# fonction to perform mac address changing
def change_mac(interface, new_mac):
    # print on user screen confirmation message
    # print("[+] - Changing " + interface + " MAC address to : " + new_mac)
    # send bash command to turn down selected interface
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    # send bash command to modify mac address
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    # send bash command to turn on selected interface
    subprocess.call(["sudo", "ifconfig", interface, "up"])

if __name__ == '__main__':
    # set options variable to the arguments typed by the user
    options = get_arguments()

    # excute the code and remove .txt file
    change_mac(options.interface, options.new_mac)
    subprocess.call(["sudo", "rm", "interface.txt"])

    # verification to make shure new mac is set to interface
    modified_mac = get_mac_address(options.interface)
    if modified_mac == options.new_mac:
        print("[+] -  Mac Address successfully changed to : " + modified_mac)
    else:
        print("[-] -  Mac Address could not be modified")
