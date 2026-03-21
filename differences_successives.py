#pgcd différence successive:
# programme classique:

#-----------------------------
"""
a = 128
b = 78

print(a,b)
while a!=b:
    if a > b:
        a = a - b
        print(a,b)
    else:
        b = b - a
        print(a,b)
        
"""
#-----------------------------

# création de la fonction de la différence successive:

#-----------------------------

def diffsuc(a,b):
    while a != b:
        if a > b:
            a = a -b
            print(a,b)
        else:
            b = b -a
            print(a,b)
    return a,b

print(diffsuc(128,78))


