#algorithme division successive/euclide
# programme classique:

#-----------------------------
"""
a = int(input("saisir le premier nombre entier"))
b = int(input("saisir le deuxième nombre entier"))
r = b
print(a,b,r)
while r != 0:
    r = a % b
    a = b
    b = r
    print(a,b,r)
"""
#-----------------------------

# création de la fonction de la division successive/euclide:

def euclide(a,b):
    r=b
    while r != 0:
        r = a % b
        a = b
        b = r
        print(a,b,r)
    return a
print(euclide(128,78))