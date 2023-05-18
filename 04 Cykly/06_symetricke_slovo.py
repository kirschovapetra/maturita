"""
Vytvorte program, ktorý zistí, či zadané slovo je symetrické, t.j. či sa rovnako číta zľava aj sprava
"""

slovo = input("Zadajte slovo: ")

je_symetricke = True
# staci prechadzat do polovice slova, lebo porovnavam naraz odpredu aj odzadu
for index_odpredu in range(len(slovo) // 2):
    index_odzadu = -1 - index_odpredu
    if slovo[index_odpredu] != slovo[index_odzadu]:
        je_symetricke = False
        break

if je_symetricke:
    print("Je symetricke")
else:
    print("Nie je symetricke")
