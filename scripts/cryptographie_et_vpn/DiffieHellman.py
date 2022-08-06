import math
import random

def est_premier(p):
    for i in range(2, math.isqrt(p)+1):
        if p % i == 0:
            return False
    return True

def trouve_premier(size):
    while True:
        p = random.randrange(size, 2*size)
        if est_premier(p):
            return p


def is_generator(g, p):
    for i in range(1, p - 1):
        if(g**i) % p == 1:
            return False
    return True


def get_generator(p):
    for g in range(2, p):
        if is_generator(g, p):
            return g



print(get_generator(10000))

print("Nombre premier : ", trouve_premier(10000), "Generateur :", get_generator(trouve_premier(10000)))

#On vérifie avec un nombre non premier et un premier.
#print("46 est non premier : ", est_premier(46))
#print("23 est premier : ", est_premier(23))
# Informations publiques
# On génère un nombre premier aléatoire.
p = trouve_premier(10000)
# On génère un générateur
g = get_generator(p)
print("Nombre premier : ", p, "Générateur : ",g)

#On ajoute Alice 1.
# Alice 1
# Elle doit générer un nombre aléatoire.
# Normalement, on utiliserait un très
# grand nombre.
a = random.randrange(0, p)
# Elle calcule le nombre à envoyer à Bob
j = (g**a) % p
# Alice envoie son nombre à Bob
# Elle utilise un canal non sécurisé
print(" Alice j : ", j)

#On ajoute Bob 1.
# Bob 1
# Il doit générer un nombre aléatoire.
# Normalement, on utiliserait un très
# grand nombre.
b = random.randrange(0, p)
# Il calcule le nombre à envoyer à Alice
k = (g**b) % p
# Bob envoie son nombre à Alice
# Il utilise un canal non sécurisé
print(" Bob k : ", k)

#On veut vérifier si Alice et Bob peuvent générer un nombre identique
# Alice 2
g_ab = (k**a) % p
print("Alice g_ab : ", g_ab)

# Bob 2
g_ab = (j**b) % p
print("Bob g_ab : ", g_ab)




