"""
Vytvorte program, ktorý prečíta n celých čísel, nájde maximálny
a vypíše pôvodnú postupnosť s tým, že prvé a maximálne číslo budú vymenené.
"""

pocet_cisel = int(input("Zadaj kolko cisel chces napisat: "))
cisla = []
for i in range(pocet_cisel):
    cisla.append(int(input("Zadaj cislo: ")))

# najdeme maximum
max_index = 0
for i in range(pocet_cisel):
    if cisla[i] > cisla[max_index]:
        max_index = i

print("Maximum:", cisla[max_index], "je na indexe: ", max_index)

print("Pred vymenou:", cisla)

# vymenime prvy prvok a maximalny
cisla[0], cisla[max_index] = cisla[max_index], cisla[0]

print("Po vymene:", cisla)
