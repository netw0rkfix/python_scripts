from os import PathLike
from pydoc import plain
import random

def xor(x, y):
    result = (bin(x ^ y))
    return result

#print(xor(4, 8))
#print(xor(4, 4))
#print(xor(255, 1))
#print(xor(255, 128))

def generate_key_stream(n):
    return bytes([random.randrange(0, 256) for i in range(n)])


def xor_bytes(key_stream, texte):
    length = min(len(key_stream), len(texte))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])



message = "UNE ATTAQUE"
message = message.encode()

key_stream = generate_key_stream(len(message))
print(key_stream)
secret = xor_bytes(key_stream, message)
print(secret)

message = "PAS ATTAQUE"
message = message.encode()
guess_key_stream = xor_bytes(message, secret)
print("La clé de chiffrement 1 : ", guess_key_stream)
plain_text = xor_bytes(guess_key_stream, secret)
print("Le texte original de l'équipe 1 : ", plain_text)

message = "DES SURPRIS"
message = message.encode()
guess_key_stream = xor_bytes(message, secret)
print("La clé de chiffrement 2 : ", guess_key_stream)
plain_text = xor_bytes(guess_key_stream, secret)
print("Le texte original de l'équipe 2 : ", plain_text)



#onetimepad1
#message = "TEST"
#message= message.encode()
#key_stream = generate_key_stream(len(message))
#print(key_stream)
#secret = xor_bytes(key_stream, message)
#print(secret)
#plain_text = xor_bytes(key_stream, secret)
#print(plain_text)