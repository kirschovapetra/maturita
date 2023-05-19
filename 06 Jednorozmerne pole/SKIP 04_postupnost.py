"""
Zostavte program, ktorý z daných n celých čísel nájde najdlhší úsek
tvoriaci aritmetickú postupnosť.
"""

# podobne ako "03 Podmienene prikazy/01_postupnost.py" ale tuto musime zistit ci to je aritmeticka postupnost
# teda musime vypocitat "d" a musi platit ze an+1 = an + d


vstupne_pole = [1, 2, 3, 4, 5, 2, 4, 6, 8, 9, 1, 2]
postupnosti = []
temp_postupnost = []

i = 0
d = vstupne_pole[i+1] - vstupne_pole[i]
while i < len(vstupne_pole)-1:

    temp_postupnost.append(vstupne_pole[i])

    if (vstupne_pole[i+2] - vstupne_pole[i+1]) != d:
        print("postupnost konci na i+1 prvku")
        temp_postupnost.append(vstupne_pole[i+1])
        postupnosti.append(temp_postupnost)
        temp_postupnost = []
        i += 2
    else:
        i += 1
    
    if i == (len(vstupne_pole)-1):
        temp_postupnost.append(vstupne_pole[i])
        postupnosti.append(temp_postupnost)
        break
    elif i >= (len(vstupne_pole)-1):
        temp_postupnost.append(vstupne_pole[-1])
        postupnosti.append(temp_postupnost)
        break

    d = vstupne_pole[i+1] - vstupne_pole[i]

print(postupnosti)
    