import random

def generate_key():
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cletters = list(letter)
    key = {}
    for i in letter: 
        key[i] = cletters.pop(random.randint(0, len(cletters) -1))
    return key

key = generate_key()


def encrypt(key, message):
    secret = ""
    for i in message:
        if i in key: secret += key[i]
        else: secret += i
    return secret

def generate_dkey(key):
    inv_map = {v: k for k, v in key.items()}
    return inv_map



#message = "MAXIME TEST JO"
#secret = encrypt(key, message)
#print(secret)
#dkey = generate_dkey(key)
#secret2 = encrypt(dkey, secret)
#print(secret2)






