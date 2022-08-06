import paramiko
import os.path
import time
import sys
import re
import builtins

login_file = ''
command_file = ''

def loginfile():
    global login_file
    #Prompt the user to enter valid path and file name
    #File should be already existing and populated with a username,password
    login_file = input('\n# Enter the path and the file name where login and password are stored : ')
    #Verifying if file path and file name are true
    if os.path.isfile(login_file) == True :
        print('#',( '-' * 57 ),'\n# OK - File contening login & password is VALID \n#',( '-' * 57 ))
        return True
    else : 
        print('# Login file is invalid, closing program \n#',( '-' * 57 ))
        return False
        sys.exit()
        
def commandfile():
    global command_file
    #Prompt the user to enter valid path and file name
    #File should be already existing and populated with a list of commands
    command_file = input('# Enter the path and the file name where commands are stored : ')
    #Verifying if file path and file name are true
    if os.path.isfile(command_file) == True :
        print('#',( '-' * 57 ),'\n# OK - File contening commands is VALID \n#',( '-' * 57 ))
        return True
    else : 
        print('#',( '-' * 57 ),'\n# OK - File contening commands is INVALID \n#',( '-' * 57 ))
        return False
        sys.exit()


#Open a SSHv2 conneection to the device
def ssh_connect(ip) :
    global login_file
    global command_file

    try: 
        #Define SSH parameters
        selected_user_file = open(login_file , 'r')

        #set cursor to the beginning of the file
        selected_user_file.seek(0)

        #Reading username from the file
        username = selected_user_file.readlines()[0].split(',')[0].rstrip('\n')

        #set cursor to the beginning of the file
        selected_user_file.seek(0)

        #Reading password from the file
        password = selected_user_file.readlines()[0].split(',')[1].rstrip('\n')

        #Logging into the device
        session = paramiko.SSHClient()

        #For test, auto-accept unknow host keys
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
      
        #Open ssh connection to the device using username and password        
        session.connect(ip.rstrip('\n'), username = username, password = password)

        #Start intercative shell session 
        connection = session.invoke_shell()

        #Send commands
        #connection.send('ip address\n')
        #connection.send('ping 172.16.0.1\n')

        #Open user selected commande file
        selected_cmd_file = open(command_file, 'r')

        #set cursor to the beginning of the file
        selected_cmd_file.seek(0)

        #sending ech line as a command to the device
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)

        #closing the login file
        selected_user_file.close()

        #closing the command file
        selected_cmd_file.close()

        #checking for syntax errors output
        router_output = connection.recv(65535)
        if re.search(b'% Invalid input', router_output):
            print('Syntax error for passing the command')
        else :
            print('\n' + 'Done for device : ', ip)

        #test reading command output
        print(str(router_output) + '\n')

        #Close the connection
        session.close()
    except paramiko.AuthenticationException:
       print('invalid username or password')