import sys
import subprocess
import os

#Performing ping over all the ip address in the file input by the user
def ip_reach(iplist):
    print('# Trying to reach (ping) addresses \n#',( '-' * 57 ))
    for ip in iplist:

        #set value of the first address to the ip variable
        ip = ip.rstrip('\n')

        #Ping Ip address and exit program if on ip is not reachable
        try :
            ping_reply = subprocess.check_output(["ping", "-c", "1", ip])
            print('# PING -',ip,'- OK')
            continue
        except subprocess.CalledProcessError:
            print('# PING -', str(ip) + '- FAILED\n#',( '-' * 57 ))
            return False
            sys.exit()
    print('#',( '-' * 57 ), '\n# OK - All ip addresses are reachable\n#',( '-' * 57 ), end='')
    return True


          







