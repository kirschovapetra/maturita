"""
Zostavte  program, na zistenie, koľko z daných n celých nezáporných čísel
sa končí číslicou 0, 1, 2, 3, ... ,
"""


def kolko_konci_na_cislicu(cislica, zoznam_cisel):
    pocet = 0

    for cislo in zoznam_cisel:
        if str(cislo)[-1] == str(cislica):
            pocet += 1

    return pocet


zoznam = [111, 222, 333, 444, 555, 123, 456, 789, 234, 345, 456]
print(zoznam)

for number in range(0, 10):
    vysledok = kolko_konci_na_cislicu(number, zoznam)
    print("Na cislicu", number, "konci", vysledok, "cisel")
