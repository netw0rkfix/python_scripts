def ping(): 
    addr = input('Address to ping : ')
    import os
    response = os.system("ping -c 100 " + str(addr))
