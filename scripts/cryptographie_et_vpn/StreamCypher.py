import random
from webbrowser import get

class KeyStream:

    def __init__(self, key=2):
        self.next = key

    def rand(self):
        self.next = (1103515245 * self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return self.rand() % 256

def encryptDecrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])

def transmit(secret, tauxErreurs):
    # Contiens le message modifié
    b = []
    # On passe chaque octet du message et
    # l'ajoute à b
    for c in secret:
        # Selon notre taux d'erreur, on
        # flip un bit dans l'octet
        if random.randrange(0, tauxErreurs) == 0:
            c = c ^ 2**random.randrange(0, 8)
        b.append(c)
    return bytes(b)


def modification(secret):
    # On créer une liste de zéro de la même
    # longueur que le secret
    mod = [0] * len(secret)
    mod[18] = ord(' ') ^ ord('1')
    mod[19] = ord(' ') ^ ord('0')
    mod[20] = ord('1') ^ ord('0')

    # On fait la même opération que pour chiffrer
    return bytes([mod[i] ^ secret[i] for i in range(len(secret))])


def get_key(message, secret):
    return bytes([message[i] ^ secret[i] for i in range(len(secret))])



key = KeyStream()

for i in range(10):
    print(key.get_key_byte())




# On chiffre le message
# Notre objet clé de flux
key = KeyStream(23)
# Notre message à chiffrer
# Il doit être binaire
message = "Nous allons attaquer a 12 h, par le cote Est de la prairie".encode()
secret = encryptDecrypt(key, message)

# On voit voir le message original
print("Notre message est : ", message)
# On génère les erreurs tous les 6 octets
secret = transmit(secret, 6)

# On déchiffre le message
# On doit initialiser notre objet clé de flux de nouveau
# Notre clé seed
key = KeyStream(23)
# On déchiffre comme on chiffre avec un XOR
message = encryptDecrypt(key, secret)
print("Notre message en texte : ", message)




# Alice envoie son message à la banque
# Les deux se sont accordé pour la clé 10
key = KeyStream(10)
# Notre message à chiffrer
message = "Transfert a Bob :   10$".encode()
print("Alice : ", message)
secret = encryptDecrypt(key, message)
print("Le secret : ", secret)

# Bob intercepte le message ici
mod_sec = modification(secret)
print(mod_sec)


# La banque reçoit le message
# La banque connait la clé d'Alice
key = KeyStream(10)
message = encryptDecrypt(key, mod_sec)
print("La banque : ", message)


message_Eve = "Ceci est un message super hyper important".encode()

# Alice communique avec Bob
# Les deux se sont accordé pour la clé 33
key = KeyStream(33)
message = message_Eve
print("Alice : ", message)
secret = encryptDecrypt(key, message)
print("Le secret : ", secret)

eves_key_stream = get_key(message, secret)
print("eve stream = ", eves_key_stream)

# Voilà Bob
key = KeyStream(33)
message = encryptDecrypt(key, secret)
print("Bob : ", message)
