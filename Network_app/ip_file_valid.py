import os.path
import sys



def clear_screen():
    for i in range(5):
        print('#')




#####Function to check validity of the path and the existance of a .txt file with host IP
def ip_file_valid():
    #Prompt user to input path and file name
    hostfile = input('\n# Enter full path and file name of the file with hosts Ip\'s : ')

    #Perfrom checking wether the path and filename is correct
    #If file entered by user is true program will continue, if not program stop and user need to relaunch
    if os.path.isfile(hostfile) == True :
        #clear_screen()
        print('#',( '-' * 57 ), '\n# OK - File contening the ip addresses is VALID \n#',( '-' * 57 ))
    else :
        #clear_screen()
        print('\n# ',hostfile , 'Is not a valid file, Please type the correct path and name')
        sys.exit()

    #open user's file for reading
    selected_ip_file = open(hostfile, 'r')

    #Put the cursor at the start of the file
    selected_ip_file.seek(0)

    #Reading all the lines of the txt file and append them to a list
    ip_list = selected_ip_file.readlines()

    #Closing the file
    selected_ip_file.close()

    #returning the list of IP address
    return ip_list






