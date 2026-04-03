# =============================================================================
#  WAYA CHEMLA — BTS SIO SISR — 1ère ANNÉE
#  Récapitulatif complet des travaux Python en Mathématiques
#  Lycée Turgot, Paris — Année scolaire 2025-2026
# =============================================================================
#
#  TABLE DES MATIÈRES
#  ─────────────────────────────────────────────────────────────────────────────
#  PARTIE 1 : TRAVAUX PRATIQUES (TP)
#      TP 1  — Variables, types et opérateurs (08/09/2025)
#      TP 2  — Algorithmes : entrées/sorties, conversions, gestion espèces
#      TP 3  — Conversion décimale → binaire (22/09/2025 & 26/09/2025)
#      TP 4  — Structures conditionnelles (29/09/2025)
#      TP 5  — Boucle Pour (06/10/2025)
#      TP 6  — Boucle Tant que (10/11/2025 & 24/11/2025)
#      TP 7  — Chaînes de caractères (24/11/2025 & 08/12/2025)
#      TP 8  — Les listes (15/12/2025 & 12/01/2026)
#      TP 9  — Fonctions (19/01/2026 & 03/02/2026)
#
#  PARTIE 2 : ENTRAÎNEMENTS CCF
#      Entraînement tri à bulle
#      Entraînement TP 8 — Listes
#      Entraînement TP 9 — Fonctions
#      Entraînement CCF — Tirage du loto (31/01/2026)
#      Révision totale (02/02/2026)
#
#  PARTIE 3 : CCF RÉALISÉS
#      CCF — Tirage du loto (26/01/2026)
#      CCF Blanc — Mastermind (23/03/2026)
# =============================================================================


# =============================================================================
# PARTIE 1 — TRAVAUX PRATIQUES
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# TP 1 — Variables, types et opérateurs (08/09/2025)
# ─────────────────────────────────────────────────────────────────────────────

# Code exécutable : opérations de base entre variables
a = 3
b = 5
c = a - b
d = c * a
print("Résultat TP1 :", d)

"""
# Version avec saisies (commentée pour GitHub) :
a = 3                                        # valeur donnée en dur
b = int(input("quel est votre âge? "))        # saisie entière
c = float(input("quelle est votre taille? ")) # saisie réelle
d = eval(input("saisir une valeur de d: "))   # saisie n'importe quel numérique
"""

# ─────────────────────────────────────────────────────────────────────────────
# TP 2 — Algorithmes : entrées/sorties, conversions, gestion d'espèces (15/09)
# ─────────────────────────────────────────────────────────────────────────────

# TP 2 — II) Conversions
"""
# 1) Conversion temporelle : heures/minutes/secondes → secondes
heures, minutes, secondes = int(input("Heures? ")), int(input("minutes? ")), int(input("secondes? "))
d = (heures * 3600) + (minutes * 60) + (secondes)
print("Durée en secondes :", d)

# 2) Conversion binaire → décimal sur un octet
a = int(input("bit 1: ")); b = int(input("bit 2: ")); c = int(input("bit 3: "))
d = int(input("bit 4: ")); e = int(input("bit 5: ")); f = int(input("bit 6: "))
g = int(input("bit 7: ")); h = int(input("bit 8: "))
i = (a*128) + (b*64) + (c*32) + (d*16) + (e*8) + (f*4) + (g*2) + (h*1)
print("Conversion binaire -> décimal :", i)
"""

# TP 2 — III) Gestion d'espèces
"""
montant = int(input("saisir le montant: "))
q1 = montant // 50; r1 = montant % 50
q2 = r1 // 20; r2 = r1 % 20
q3 = r2 // 10; r3 = r2 % 10
q4 = r3 // 5; r4 = r3 % 5
print("Billets - 50€:", q1, "| 20€:", q2, "| 10€:", q3, "| 5€:", q4)
"""

# ─────────────────────────────────────────────────────────────────────────────
# TP 3 — Conversion décimale → binaire (22/09/2025 & 26/09/2025)
# ─────────────────────────────────────────────────────────────────────────────

# Conversion par boucle (version finale)
"""
a_nb = int(input("Entrer le nombre entier à convertir : "))
bits = []
temp = a_nb
while temp > 0:
    bits.append(temp % 2)
    temp //= 2
resultat_bin = ''.join([str(bit) for bit in bits[::-1]])
print("Résultat binaire :", resultat_bin)
"""

# ─────────────────────────────────────────────────────────────────────────────
# TP 4 — Structures conditionnelles (if / elif / else) (29/09/2025)
# ─────────────────────────────────────────────────────────────────────────────

# Exercice télésiège
"""
age = int(input("saisir l'age : "))
taille = float(input("saisir la taille : "))
if age < 7 or taille < 1.25:
    print("ne peut pas monter seule")
else:
    print("peut monter seule")
"""

# Exercice 3 — places de concert avec réduction
"""
n = int(input("nombre de places : "))
etudiant = input("étudiant ? (Oui/Non) : ")
prix = n * 20
if etudiant == "Oui":
    prix = prix * 0.75
elif n >= 3:
    prix = prix * 0.9
print("Prix total :", prix)
"""

# ─────────────────────────────────────────────────────────────────────────────
# TP 5 — Boucle Pour (for) (06/10/2025)
# ─────────────────────────────────────────────────────────────────────────────

# Application 6 — Randonnée
print("\n--- TP 5 : Randonnée ---")
parcours = 30
for i in range(1, 10):
    parcours = parcours + 10
print("Après 10 jours :", parcours, "km")

# Application 8 — Jeu de dés (5 parties)
from random import *
print("Scores des 5 parties de dés :")
for p in range(5):
    scorepartieencours = 10
    for i in range(10):
        resultat = randint(1, 6)
        if (resultat % 2) == 0:
            scorepartieencours = scorepartieencours + 1
        else:
            scorepartieencours = scorepartieencours - 2
    print("Partie", p+1, ":", scorepartieencours)

# ─────────────────────────────────────────────────────────────────────────────
# TP 6 — Boucle Tant que (while) (10/11/2025)
# ─────────────────────────────────────────────────────────────────────────────

# I) Ticket-resto
n_annee = 2018
ticket = 8.9
menu = 11
while ticket < menu:
    n_annee = n_annee + 1
    ticket = ticket * 1.05
    menu = menu + 0.10
print("\n--- TP 6 ---")
print("C'est en", n_annee, "que le ticket couvrira le menu.")

# II) Algorithme d'Euclide — version avec modulo
"""
a_euc = int(input("Nombre A : ")); b_euc = int(input("Nombre B : "))
while b_euc != 0:
    r = a_euc % b_euc
    a_euc = b_euc; b_euc = r
print("Le PGCD est :", a_euc)
"""

# ─────────────────────────────────────────────────────────────────────────────
# TP 7 — Chaînes de caractères (24/11/2025 & 08/12/2025)
# ─────────────────────────────────────────────────────────────────────────────

# Application 3 — décodage d'un code employé
"""
code = input("Code employé (ex: 2304513) : ")
annee_embauche = code[0:2]
numero_embauche = code[2:5]
titre = code[5] if len(code) > 5 else "?"
domaine = code[6] if len(code) > 6 else "?"
"""

# Exercice 4 — chiffrement de César (+3)
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"
mot_cesar = input("Mot à chiffrer : ")
nouveau_mot = ""
for lettre in mot_cesar:
    if lettre in alphabet:
        indice = alphabet.index(lettre)
        nouveau_mot += alphabet[(indice + 3) % 26]
print("Chiffré :", nouveau_mot)
"""

# ─────────────────────────────────────────────────────────────────────────────
# TP 8 — Les listes (15/12/2025 & 12/01/2026)
# ─────────────────────────────────────────────────────────────────────────────

# Exercice 2 — maximum d'une liste
print("\n--- TP 8 : Listes ---")
L_test = [12, 13, 45, 25, 56, 7]
M_max = L_test[0]
for i in range(len(L_test)):
    if L_test[i] > M_max:
        M_max = L_test[i]
print("Maximum trouvé :", M_max)

# ─────────────────────────────────────────────────────────────────────────────
# TP 9 — Fonctions (19/01/2026 & 03/02/2026)
# ─────────────────────────────────────────────────────────────────────────────

print("\n--- TP 9 : Fonctions ---")

def generer_liste_des():
    liste_des = [0] * 8
    for i in range(0, 8):
        liste_des[i] = randint(1, 6)
    return liste_des

def etendue(L):
    return max(L) - min(L)

def ma_somme(L):
    s = 0
    for val in L: s += val
    return s

ma_liste = generer_liste_des()
print("Liste :", ma_liste, "| Somme :", ma_somme(ma_liste))


# =============================================================================
# PARTIE 2 — ENTRAÎNEMENTS CCF
# =============================================================================

# Entraînement CCF — Tirage du loto (31/01/2026)
def tirage_loto():
    tab = [0] * 6
    for i in range(5): tab[i] = randint(1, 49)
    tab[5] = randint(1, 10)
    return tab

def estvalable(tab):
    for i in range(4):
        for j in range(i + 1, 5):
            if tab[i] == tab[j]: return False
    return True


# =============================================================================
# PARTIE 3 — CCF RÉALISÉS
# =============================================================================

# ─────────────────────────────────────────────────────────────────────────────
# CCF BLANC — Mastermind (23/03/2026)
# ─────────────────────────────────────────────────────────────────────────────

# --- Les fonctions (Archives) ---
"""
def c(): # Génère combinaison
    p = [0] * 3
    for i in range(3): p[i] = randint(1, 5)
    return p

def f(n): # Convertit entier en liste
    p2 = [0] * 3
    for i in range(3):
        p2[2 - i] = n % 10
        n = (n - p2[2 - i]) // 10
    return p2
"""

# --- Programme principal (Limite 12 essais) ---
from random import *

p = [0] * 3
p2 = [0] * 1 
essai = 0

for i in range(3):
    p[i] = randint(1, 5)

print("\n--- Mastermind (CCF Blanc) ---")

while p != p2 and essai < 12:
    n = int(input("Saisir 3 chiffres (1-5) : "))
    p2 = [0] * 3 
    temp_n = n 
    
    for i in range(3):
        p2[2 - i] = temp_n % 10
        temp_n = (temp_n - p2[2 - i]) // 10
    
    essai += 1 
    
    if p == p2:
        print("Gagné en", essai, "coups !")
    else:
        if essai == 12:
            print("Perdu ! Solution :", p)
        else:
            print("Essai n°", essai, "/ 12. Continuez...")

# Fin du fichier.