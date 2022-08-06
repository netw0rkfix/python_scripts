
#%%

def generate_key(n):
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    count = 0
    for i in letter: 
        key[i] = letter[(count + n) % (len(letter))]
        count += 1
    return key

def generate_dkey(key):
    inv_map = {v: k for k, v in key.items()}
    return inv_map

def encrypt(key, message):
    secret = ""
    for i in message:
        if i in key: secret += key[i]
        else: secret += i
    return secret

def brute_force(secret):
    for i in range(26):
        dkey = generate_key(i)
        potential_msg = encrypt(dkey, secret)
        print(potential_msg)



# Set parameters
key_num = 3
key = generate_key(key_num)
message = "MAXIME"
secret = encrypt(key, message)

#Decrypt with decryption key
#
#dkey = generate_dkey(key)
#secret = encrypt(dkey, secret)


#Decrypt by brute forcing
#
#brute_force(secret)




# %%
