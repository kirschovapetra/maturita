"""
Daná je postupnosť n celých čísel. Zostavte program na zistenie najdlhšieho rastúceho úseku danej
postupnosti.
"""

vstupne_pole = [1, 2, 3, 4, 5, 2, 4, 6, 1, 2]

# sem sa budu ukladat vsetky rastuce postupnosti a nakoniec pozrieme ktora je najdlhsia
postupnosti = []  
temp_postupnost = []
for i in range(len(vstupne_pole)-1):
    temp_postupnost.append(vstupne_pole[i]) # pridame do nasej temp postupnosti
    
    if vstupne_pole[i+1] < vstupne_pole[i]: # nasledujuci prvok [i+1] je mensi ako ten predosly [i] --> teda koniec rastucej postupnosti
        postupnosti.append(temp_postupnost) # temp postupnost je hotova, pridame ju do pola postupnosti 
        temp_postupnost = [] # vymazeme, dalsia postupnost sa bude naplnat od zaciatku

# chybal nam tam posledny prvok, treba ho doplnit. uvidela by si to, keby si das na tomto mieste print(postupnosti)
temp_postupnost.append(vstupne_pole[-1])
postupnosti.append(temp_postupnost)

print(postupnosti)

# najdeme najdlhsiu postupnost, teda tu ktora ma max dlzku

imax = 0
for i in range(len(postupnosti)):
    if len(postupnosti[i]) > len(postupnosti[imax]):
        imax = i

print("najdlhsia postupnost:", postupnosti[imax], "dlzka:", len(postupnosti[imax]))

