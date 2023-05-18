"""
Zostavte program, ktorý z daných n celých čísel nájde najdlhší úsek
tvoriaci aritmetickú postupnosť.
"""

# podobne ako "03 Podmienene prikazy/01_postupnost.py" ale tuto musime zistit ci to je aritmeticka postupnost
# teda musime vypocitat "d" a musi platit ze an+1 = an + d


vstupne_pole = [1, 2, 3, 4, 5, 2, 4, 6, 8, 9, 1, 2]

# sem sa budu ukladat vsetky postupnosti a nakoniec pozrieme ktora je najdlhsia
postupnosti = []  
temp_postupnost = []

d = vstupne_pole[0] - vstupne_pole[1]
for i in range(len(vstupne_pole)-1):
    temp_postupnost.append(vstupne_pole[i]) # pridame do nasej temp postupnosti
    if vstupne_pole[i+1] - vstupne_pole[i] != d: # ked sa nam zmeni dcko, to znamena ze uz nepokracuje postupnost
        postupnosti.append(temp_postupnost) # temp postupnost je hotova, pridame ju do pola postupnosti 
        temp_postupnost = [] # vymazeme, dalsia postupnost sa bude naplnat od zaciatku
    
    d = vstupne_pole[i+1] - vstupne_pole[i] 
    
# chybal nam tam posledny prvok, treba ho doplnit. uvidela by si to, keby si das na tomto mieste print(postupnosti)
temp_postupnost.append(vstupne_pole[-1])
print(temp_postupnost)
# postupnosti.append(temp_postupnost)

print(postupnosti)

# najdeme najdlhsiu postupnost, teda tu ktora ma max dlzku

imax = 0
for i in range(len(postupnosti)):
    if len(postupnosti[i]) > len(postupnosti[imax]):
        imax = i

print("najdlhsia postupnost:", postupnosti[imax], "dlzka:", len(postupnosti[imax]))

