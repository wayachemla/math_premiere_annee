
#pgcd décomposition en facteur premier
# programme classique:
"""
n = int(input("un nombre entier"))
p = [2, 3, 5, 7, 9, 11, 13] # les nombres premier
exp = [0] * 7 #les exposants
for i in range(7): #parcours la liste p
    while n % p[i] == 0: #tant que n est divisible par l'indice de p
        n = n // p[i]
        exp[i] = exp[i] + 1
print(exp)

"""
# création de la fonction de la décomposition par facteur premier
def decprem(n):
    p = [2, 3, 5, 7, 9, 11, 13]
    exp = [0] * 7
    for i in range (7):
        while n % p[i] == 0:
            n = n // p[i]
            exp[i] = exp[i] + 1
    return exp
print(decprem(128))