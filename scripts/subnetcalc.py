#%%
import socket


def ip_valid(add, sub):
    # ip_valid fonction will validate format and validity of the string type by the user for IP Address
    # Return valid or invalid
    val = add.split('.', maxsplit=4)
    try:
        if val[1]:
            if len(val) == 4:
                if (len(val[0]) <= 3) and (len(val[1]) <= 3) and (len(val[2]) <= 3) and (len(val[3]) <= 3):
                    if (int(val[0]) <= 255) and (int(val[1]) <= 255) and (int(val[2]) <= 255) and (int(val[3]) <= 255):
                        return "valid"
                    else:
                        return "invalid" 
                else:
                    return "invalid"
            else:
                return "invalid"
        else:
            return "invalid"
    except IndexError:
        return "invalid"

def ip_class(add, sub):
    # fonction ip_class will return the class of the ip address input by user
    # Return A,B,C,D or E/invalid
    c = ip_valid(add, sub)
    if (c == "valid"):
        val = add.split('.', maxsplit=4)
        if (int(val[0]) <= 126):
            return "A"
        elif (int(val[0]) >= 128) and (int(val[0]) <= 191):
            return "B"
        elif (int(val[0]) >= 192) and (int(val[0]) <= 223):
            return "C"
        elif (int(val[0]) >= 224) and (int(val[0]) <= 239):
            return 'D, Multi-cast address'
        elif (int(val[0]) >= 240) and (int(val[0]) <= 255):
            return 'E, INVALID address range'
        else:
            return 'Invalid'
    else:
        return 'invalid'

def ip_priv(add, sub):
    # Fonction ip_priv will return the privacy of the address passed-in
    # return private or public
    c = ip_valid(add, sub)
    if (c == 'valid'):
        c = ip_class(add, sub)
        val = add.split('.', maxsplit=4)
        if (c == 'A'):
            if (int(val[0]) == 10):
                return 'private'
            else:
                return 'public'
        elif (c == 'B'):
            if (int(val[0]) == 172) and (int(val[1]) >= 16) and (int(val[1]) <= 31):
                return 'private'
            else:
                return 'public'
        elif (c == 'C'):
            if (int(val[0]) == 192) and (int(val[1]) == 168):
                return 'private'
            else:
                return 'public'
        elif (c == 'D, Multi-cast address'):
            return 'Multi-cast'
        elif (c == 'E, INVALID address range'):
            return 'Test and special use, invalid address range'
        else:
            return 'invalid'
    else:
        return 'invalid'

def subnet_valid(add, sub):
    # Fonction subnet_valid will check validity of the subnet input by user
    # return 'valid' or 'invalid'
    # CIDR notation can be passed in or standard address format
    sub_cidrls = ['/1', '/2', '/3', '/4', '/5', '/6', '/7', '/8', '/9', '/10', '/11', '/12', '/13', '/14', '/15', '/16',
                  '/17', '/18', '/19', '/20', '/21', '/22', '/23', '/24', '/25', '/26', '/27', '/28', '/29', '/30',
                  '/31', '/32']
    sub_addls1 = ['255.0.0.0', '255.128.0.0', '255.192.0.0', '255.252.0.0', '255.255.0.0', '255.240.0.0', '255.224.0.0',
                  '255.248.0.0', '255.254.0.0']
    sub_addls2 = ['255.255.192.0', '255.255.224.0', '255.255.240.0', '255.255.248.0', '255.255.252.0', '255.255.254.0',
                  '255.255.255.0', '255.255.128.0']
    sub_addls3 = ['255.255.255.128', '255.255.255.192', '255.255.255.224', '255.255.255.240', '255.255.255.248',
                  '255.255.255.252', '255.255.255.254', '255.255.255.255']
    sub_addls4 = ['128.0.0.0', '192.0.0.0', '224.0.0.0', '240.0.0.0', '248.0.0.0', '252.0.0.0', '254.0.0.0']
    sub_cidr = {
        '/1': '128.0.0.0',
        '/2': '192.0.0.0',
        '/3': '224.0.0.0',
        '/4': '240.0.0.0',
        '/5': '248.0.0.0',
        '/6': '252.0.0.0',
        '/7': '254.0.0.0',
        '/8': '255.0.0.0',
        '/9': '255.128.0.0',
        '/10': '255.192.0.0',
        '/11': '255.224.0.0',
        '/12': '255.240.0.0',
        '/13': '255.248.0.0',
        '/14': '255.252.0.0',
        '/15': '255.254.0.0',
        '/16': '255.255.0.0',
        '/17': '255.255.128.0',
        '/18': '255.255.192.0',
        '/19': '255.255.224.0',
        '/20': '255.255.240.0',
        '/21': '255.255.248.0',
        '/22': '255.255.252.0',
        '/23': '255.255.254.0',
        '/24': '255.255.255.0',
        '/25': '255.255.255.128',
        '/26': '255.255.255.192',
        '/27': '255.255.255.224',
        '/28': '255.255.255.240',
        '/29': '255.255.255.248',
        '/30': '255.255.255.252',
        '/31': '255.255.255.254',
        '/32': '255.255.255.255',
    }
    if (add in sub_cidrls) or (add in sub_addls1) or (add in sub_addls2) or (add in sub_addls3) or (add in sub_addls4):
        if (add in sub_cidrls):
            return sub_cidr[add]
        else:
            return add
    else:
        return 'invalid'

def ip_to_bin(add, sub):
    ##Fonction ip_to_bin will change the address into is binnary values
    ##return a string wich is the binary equivalent 'xxxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx'
    ##only valid ipv4 adress format can be passed-in
    octet = 0
    op_t = 1
    op_bv = 128
    subnet = add.split('.', maxsplit=4)
    subval = ip_valid(add, sub)
    binary_oct1 = ''
    fin = {}
    while (octet <= 3):
        test = {'octets': subnet[octet]}
        testvar = int(test['octets'])
        while (op_t < 9):
            testvar = testvar - int(op_bv)
            if (testvar >= 0):
                oct1_binval = {'bit' + str(op_t): '1'}
            else:
                testvar = testvar + int(op_bv)
                oct1_binval = {'bit' + str(op_t): '0'}
            binary_oct1 = binary_oct1 + oct1_binval['bit' + str(op_t)]
            op_t += 1
            op_bv /= 2
            fin[octet] = binary_oct1
        binary_oct1 = ''
        op_t = 1
        op_bv = 128
        octet += 1
    add_fin = fin[0] + '.' + fin[1] + '.' + fin[2] + '.' + fin[3]
    return (add_fin)

def bin_to_ip(add, sub):
    # Fonction bin_to_ip will change a binnary ipaddress into his regular ipv4 value
    # return a string 'xxx.xxx.xxx.xxx'
    n1 = add.split('.', maxsplit=4)
    b1 = 128
    d1 = 0
    d2 = 0
    octet = {}
    id = {}
    for p in n1:
        addr = 0
        for t in p:
            if (t == '1'):
                octet[d2] = int(b1)
                addr = addr + octet[d2]
                b1 /= 2
                d2 += 1
            else:
                octet[d2] = 0
                addr = addr + octet[d2]
                b1 /= 2
                d2 += 1
        id[d1] = addr
        d1 += 1
        d2 = 0
        b1 = 128
        octet = {}
    ipv4_add = str(id[0]) + '.' + str(id[1]) + '.' + str(id[2]) + '.' + str(id[3])
    return ipv4_add

def network_id(add, sub):
    # network_id fonction will apply subnet mask to address input by user using binary boolean algebra
    # Return a string, wich is the ip address corresponding to the network id
    t1 = ip_valid(add, sub)
    t2 = ip_valid(sub, sub)
    if (t1 == 'valid') and (t2 == 'valid'):
        fin_id = ''
        net_id = ''
        fin = {}
        t3 = ip_to_bin(add, sub)
        t4 = ip_to_bin(sub, sub)
        subnet = t4.split('.', maxsplit=4)
        address = t3.split('.', maxsplit=4)
        b_time = 0
        o_time = 0
        while (o_time < 4):
            a_octet = {'oct': address[o_time]}
            s_octet = {'oct': subnet[o_time]}
            add_oct = list(a_octet['oct'])
            sub_oct = list(s_octet['oct'])
            while (b_time < 8):
                if (add_oct[b_time] == '1') and (sub_oct[b_time] == '1'):
                    netid_b = {'bit': '1'}
                    net_id = net_id + netid_b['bit']
                else:
                    netid_b = {'bit': '0'}
                    net_id = net_id + netid_b['bit']
                b_time += 1
            fin[o_time] = fin_id + net_id
            net_id = ''
            o_time += 1
            b_time = 0
        fin_id = fin[0] + '.' + fin[1] + '.' + fin[2] + '.' + fin[3]
        return fin_id

def magic_number(add, sub):
    # Fonction magic_number will return the magic number of the typed-in subnet
    # return a string wich is the last 'on' octet of the subnet
    t1 = ip_valid(add, sub)
    t2 = subnet_valid(add, sub)
    if (t1 == 'valid') and (t2 != 'invalid'):
        mgnb = {}
        subnet = ip_to_bin(add, sub)
        oct = subnet.split('.', maxsplit=4)
        for o in oct:
            if (o == '11111111') or (o == '00000000'):
                pass
            else:
                op_t = 0
                bin_val = 128
                for b in o:
                    if (b == '1'):
                        mgnb[op_t] = int(bin_val)
                        bin_val /= 2
                        op_t += 1
                    else:
                        mgnb[op_t] = 0
                        bin_val /= 2
                        op_t += 1
        try:
            for p in mgnb:
                if (mgnb[p] != 0):
                    magic_number = mgnb[p]

            return magic_number
        except UnboundLocalError:
            return 'none'

def subnet_bit(add, sub):
    # fonction subnet_bit will return de number of barrowed subnet bits to host portion
    # return a string wich is a number between 1 and 7
    count1 = ''
    count0 = ''
    n1 = ip_to_bin(add, sub)
    n2 = ip_to_bin(sub, sub)
    n3 = network_id(add, sub)
    sbit = n2.split('.', maxsplit=4)
    c = 0
    for o in sbit:
        if (o == '11111111') or (o == '00000000'):
            pass
        else:
            for b in o:
                if (b == '1'):
                    count1 = count1 + '1'
                elif (b == '0'):
                    count0 = count0 + '0'
            return len(count1)

def network_bit(add, sub):
    # Fonction network_bit will return the number of ''on'' byte in the netmask
    # Return a string wich is a number between 8 and 30
    nbits = ''
    n1 = ip_to_bin(add, sub)
    n2 = ip_to_bin(sub, sub)
    n3 = network_id(add, sub)
    sbit = n2.split('.', maxsplit=4)
    for o in sbit:
        if (o == '11111111'):
            nbits = nbits + '11111111'
        elif (o == '00000000'):
            pass
        else:
            for b in o:
                if (b == '1'):
                    nbits = nbits + '1'
                else:
                    pass
    return  str(len(nbits))

def host_bit(add, sub):
    # fonction host_bit will return the number of ''OFF'' byte in the netmask
    # return a string wich is an number between 24 an 2
    b = int(network_bit(add, sub))
    c = 32 - b
    return c

def first_address(add, sub):
    # first address fonction will return the first address of the network
    # return string wich is a decimal value ip adresse
    b = bin_to_ip(network_id(add, sub), sub)
    o = b.split('.', maxsplit=4)
    c = int(o[3]) + 1
    return o[0] + '.' + o[1] + '.' + o[2] + '.' + str(c)

def sub_network(add, sub):
    # sub_network fonction will list all the other netwokr based on subnet mask
    # Return a list of network ID address
    v1 = magic_number(sub, add)
    if (v1 != 'none'):
        octet = ''
        run = 0
        networks = []
        fin_add = []
        v2 = bin_to_ip(network_id(add, sub), sub)
        v3 = sub.split('.', maxsplit=4)
        v4 = v2.split('.', maxsplit=4)
        address = {
            1: v4[0],
            2: v4[1],
            3: v4[2],
            4: v4[3],
        }
        for o in v3:
            if (o != '0'):
                octet = octet + '1'
            elif (o == '0'):
                pass
        octet = len(octet)
        oct = octet - 1
        t = int(v4[oct])
        while (run < 255):
            networks.append(run)
            address[octet] = run
            add = str(address[1]) + '.' + str(address[2]) + '.' + str(address[3]) + '.' + str(address[4])
            fin_add.append(add)
            run = run + int(v1)
        return fin_add
    else:
        return 'none'

def broadcast_address(add, sub):
    # fonction broadcast_address will return the last address of the current network
    # return a string wich is an xxx.xxx.xxx.xxx format ip address
    try:
        v1 = bin_to_ip(network_id(add, sub), sub)
        v2 = int(magic_number(sub, add))
        v3 = v1.split('.', maxsplit=4)
        v4 = sub.split('.', maxsplit=4)
        run = 0
        address = {
            1: v3[0],
            2: v3[1],
            3: v3[2],
            4: v3[3],
        }
        for o in v4:
            run += 1
            if (o == '255'):
                pass
            elif (o != '0'):
                t = int(address[run]) + v2
                if (t < 255):
                    address[run] = t - 1
                else:
                    address[run] = 255
            elif (o == '0'):
                address[run] = '255'
        add = str(address[1]) + '.' + str(address[2]) + '.' + str(address[3]) + '.' + str(address[4])
        return add
    except ValueError:
        v1 = bin_to_ip(network_id(add, sub),sub)
        v3 = v1.split('.', maxsplit=4)
        v4 = sub.split('.', maxsplit=4)
        run = 0
        address = {
            1: v3[0],
            2: v3[1],
            3: v3[2],
            4: v3[3],
        }
        for o in v4:
            run += 1
            if (o == '255'):
                pass
            elif (o == '0'):
                address[run] = '255'
        add = str(address[1]) + '.' + str(address[2]) + '.' + str(address[3]) + '.' + str(address[4])
        return add

def last_address(add, sub):
    # Fonction last_address will return the last usable host of your network
    # string, xxx.xxx.xxx.xxx
    v1 = broadcast_address(add, sub)
    v2 = v1.split('.', maxsplit=4)
    v3 = int(v2[3]) - 1
    return v2[0] + '.' + v2[1] + '.' + v2[2] + '.' + str(v3)

def main():
    sub = ''
    print('')
    print('[@] -                Welcome to this IPv4 analyzer                - [@]')
    print('[@] -                                                             - [@]')
    print('[@] -      This software will analyze the ipv4 address/mask,      - [@]')
    print('[@] -      And return all the value related to your network       - [@]')
    print('[@] -                                                             - [@]')
    print('[@] -                                                             - [@]')
    while ('true'):
        add = input(
            '[@] -                   Type an IPV4 ip address                   - [@]\n[@] -                                                             - [@]\n[@] > ')
        sub = subnet_valid(input(
            '[@] -                                                             - [@]\n[@] -                     And the Subnet Mask                     - [@]\n[@] > '),
            sub)
        print('[@] -                                                             - [@]')
        print('[@] -                                                             - [@]')
        v1 = 36 - int(len(add))
        v2 = ' ' * v1
        v3 = str(add + v2)
        print('[@] = Adress               :', v3, '- [@]')
        v4 = 36 - int(len(sub))
        v5 = ' ' * v4
        v6 = str(sub + v5)
        print('[@] = Mask                 :', v6, '- [@]')
        p1 = 36 - int(len(str(socket.inet_aton(add))))
        p2 = ' ' * p1
        p3 = str(str(socket.inet_aton(add)) + p2)
        print('[@] = HEX address          :', p3, '- [@]')
        p4 = 36 - int(len(str(socket.inet_aton(sub))))
        p5 = ' ' * p4
        p6 = str(socket.inet_aton(sub)) + p5
        print('[@] = HEX mask             :', p6, '- [@]')
        v7 = 36 - int(len(ip_class(add, sub)))
        v8 = ' ' * v7
        v9 = str(ip_class(add, sub) + v8)
        print('[@] = IP Class             :', v9, '- [@]')
        v10 = 36 - int(len(ip_priv(add, sub)))
        v11 = ' ' * v10
        v12 = str(ip_priv(add, sub) + v11)
        print('[@] = Address range        :', v12, '- [@]')
        v13 = 36 - int(len(ip_to_bin(add, sub)))
        v14 = ' ' * v13
        v15 = str(ip_to_bin(add, sub) + v14)
        print('[@] = Binary address       :', v15, '- [@]')
        v16 = 36 - int(len(ip_to_bin(sub, sub)))
        v17 = ' ' * v16
        v18 = str(ip_to_bin(sub, sub + v17))
        print('[@] = Binary subnet        :', v18, ' - [@]')
        v19 = 36 - int(len(network_id(add, sub)))
        v20 = ' ' * v19
        v21 = str(network_id(add, sub))
        print('[@] = Binary network ID    :', v21, ' - [@]')
        v22 = 36 - int(len(bin_to_ip(network_id(add, sub), sub)))
        v23 = ' ' * v22
        v24 = str(bin_to_ip(network_id(add, sub), sub)) + v23
        print('[@] = Network ID           :', v24, '- [@]')
        v25 = 35 - int(len(first_address(add, sub)))
        v26 = ' ' * v25
        v27 = str(first_address(add, sub) + v26)
        print('[@] = First usable host    :', v27, ' - [@]')
        v28 = 36 - int(len(last_address(add, sub)))
        v29 = ' ' * v28
        v30 = str(last_address(add, sub) + v29)
        print('[@] = Last usable host     :', v30, '- [@]')
        v31 = 36 - int(len(broadcast_address(add, sub)))
        v32 = ' ' * v31
        v33 = str(broadcast_address(add, sub)) + v32
        print('[@] = Broadcast address    :', v33, '- [@]')
        v34 = 36 - int(len(network_bit(add, sub)))
        v35 = ' ' * v34
        v36 = str(network_bit(add, sub) + v35)
        print('[@] = Network bits         :', v36, '- [@]')
        t1 = str((2 ** int(network_bit(add, sub))) - 2)
        t2 = len(t1)
        v37 = 36 - int(t2)
        v38 = ' ' * v37
        v39 = str(2 ** int(network_bit(add, sub)) - 2) + v38
        print('[@] = Available networks   :', v39, '- [@]')
        tgv = subnet_bit(add, sub)
        if (tgv == None):
            v90 = 'None'
            v91 = 36 - int(len(v90))
            v92 = ' ' * v91
            v93 = str(v90 + v92)
            print('[@] = Subnet bits          :', v93, '- [@]')
        else:
            t4 = str(len(str(subnet_bit(add, sub))))
            t3 = len(t4)
            v40 = 35 - int(t3)
            v41 = ' ' * v40
            v42 = str(str(subnet_bit(add, sub)) + v41)
            print('[@] = Subnet bits          :', v42, ' - [@]')
        t5 = str(host_bit(add, sub))
        t6 = len(t5)
        v43 = 36 - int(t6)
        v44 = ' ' * v43
        v45 = str(host_bit(add, sub)) + v44
        print('[@] = Host bits            :', v45, '- [@]')
        t7 = str(((2 ** host_bit(add, sub)) - 2))
        t8 = len(t7)
        v46 = 36 - int(t8)
        v47 = ' ' * v46
        v48 = str(((2 ** host_bit(add, sub)) - 2)) + v47
        print('[@] = Available hosts      :', v48, '- [@]')
        t9 = str(magic_number(sub, add))
        t10 = len(t9)
        v49 = 36 - int(t10)
        v50 = ' ' * v49
        v51 = str(magic_number(sub, add)) + v50
        print('[@] = Magic number         :', v51, '- [@]')
        print('[@] = OTHER SUB-NETWORK    : FIRST ADD.      -   LAST ADD.        - [@]')
        print('[@] -                                                             - [@]')
        t = sub_network(add, sub)
        if (t != 'none'):
            for a in t:
                if (len(a) < 15):
                    b = 15 - int(len(a))
                    y = ' ' * b
                    x = str(a + y)

                    v1 = 15 - len(first_address(a, sub))
                    c = first_address(a, sub)
                    v2 = ' ' * v1
                    v3 = str(c + v2)

                    b1 = 16 - len(last_address(a, sub))
                    b2 = last_address(a, sub)
                    b3 = ' ' * b1
                    b4 = str(b2 + b3)
                    print('[@] =', x, '     :', v3, '-  ', b4, '- [@]')
        else:
            print('[@] = None                 : None            -   None             - [@]')
        print('[@] -                                                             - [@]')
        print('[@] -                                                             - [@]')
        t = input('[@] -                  PRESS ANY KEY TO RE-RUN                    - [@]\n[@] >')

main()
