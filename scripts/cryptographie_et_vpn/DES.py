# DES01.py

# Import l'implémentation de DES
# https://gist.github.com/eigenein/1275094
from operator import mod
from pyDes import *

def modification(secret):
    # On créer une liste de zéro de la même
    # longueur que le secret
    mod = [0] * len(secret)
    mod[8] = 1
#    mod[12] = ord(' ') ^ ord('0')
#    mod[23] = ord('1') ^ ord('0')
    return mod




# Notre message un peu spécial
message = "Vers bob:    10$"
# On utilise la même clé que dans les commentaires
# La clé doit avoir 8 octets, dont les 
# 8 caractères
key = "DESCRYPT"
# Un vecteur d’initialisation, encore comme
# dans les commentaires on utilise 8 zéros.
# Ce vecteur n'est pas utilisé dans le 
# mode ECB, notre premier mode utilisé.
iv = bytes([1]*8)
# On crée notre objet clé, on ne met pas de
# caractère de padding et on utilise
# le mode de padding recommandé
k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)

# On chiffre le  message
secret = k.encrypt(message)

# Alice envoie son message à la banque
secret = k.encrypt(message)
print("Longueur du texte plain : ", len(message))
print("Longueur du texte chiffré : ", len(secret))
print("Message chiffré d'Alice : ", secret)

# Bob se place entre Alice et la banque
bob_mod = modification(secret)
print(bob_mod)


# La banque déchiffre ici
message = k.decrypt(secret)
print("Notre message déchiffré : ", message)
