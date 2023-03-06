"""
Vytvorte program, ktorý zistí, či zadané slovo je symetrické, t.j. či sa rovnako číta zľava aj sprava
"""

slovo = input("Zadajte slovo: ")

je_symetricke = True
# staci prechadzat do polovice slova, lebo porovnavam naraz odpredu aj odzadu
for index_pred in range(len(slovo) // 2):
    index_zad = -1 - index_pred
    if slovo[index_pred] != slovo[index_zad]:
        je_symetricke = False
        break

if je_symetricke:
    print("Je symetricke")
else:
    print("Nie je symetricke")
