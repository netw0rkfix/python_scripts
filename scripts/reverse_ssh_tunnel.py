### Importing libs
import subprocess

### Modify this section to match your connection needs
target = ""
target_ssh_port = ""
local_port = ""
remote_port = ""

### Fonction to perform verification if local host is already connected to the target or not
def host_is_connect():
    subprocess.call("ss -tnap | grep -i estab > /tmp/call_home/active_connections.txt", shell=True)
    act_con = open("/tmp/call_home/active_connections.txt", 'r')
    act_con.seek(0)
    act_con_line = act_con.readlines()
    for i in act_con_line :
        if target not in i :
            continue 
        else :
            return True  
        
### Fonction to connect localhost to target and make an ssh reverse tunel
def connect_to_jump():
     subprocess.call("autossh -M 0 -o \"ServerAliveInterval 30\" -o \"ServerAliveCountMax 3\" -p {} -R {}:localhost:{} root@{}".format(target_ssh_port,local_port,remote_port,target), shell=True)

### Run when called 
if __name__ == '__main__':
    if host_is_connect() == True :
        pass
    else :
        connect_to_jump()
        
        
