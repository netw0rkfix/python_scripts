from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
from ssh_connection import *
from create_threads import create_threads
import sys



#Calling ip_file_valid look into the system to find the file user passed in to make shure it actually exist
#Calling ip_address_valid perform a basic verification to see if addresses in the file are correct
#Calling ip_reach will try to ping all the addresses in the file to test network connectivity
#Will return False and auto-exit or return true 
try :
    ip_list = ip_reach(ip_addr_valid(ip_file_valid()))
    if ip_list == True :
        lf = loginfile()
        cf = commandfile()
        if lf != False and cf != False : 
            print('# Starting SSH Connect , Please wait \n#',( '-' * 57 ))
            ssh_connect("172.17.0.4")
           


except KeyboardInterrupt:
    print('\n# Program aborted by user')
    sys.exit()
    













#Verifying validity of each address in the list
#try:
#    ip_addr_valid(ip_list)
#except KeyboardInterrupt:
#    print('\n# Program aborted by user')
#    sys.exit()

#Verifying the reachability of each IP address in the list
#try:
#    ip_reach(ip_list)

#except KeyboardInterrupt:
#        print('\n# Program aborted by user')
#        sys.exit()



#Calling threads creation function for one or more ssh connections
#create_threads(ip_list, ssh_connect)

