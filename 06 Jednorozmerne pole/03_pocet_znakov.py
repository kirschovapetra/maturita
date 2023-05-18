"""
Zostavte program na zistenie počtu výskytov jednotlivých znakov od  a...z
v postupnosti znakov ukončenej bodkou

poznamka:

ord(pismenko) --> dostaneme ascii cislo pismenka
print(ord("a")) vypise 98

chr(cislo) --> presne naopak, dostaneme pismenko z ascii cisla
print(chr(98)) vypise "a"

"""

def kolkokrat_je_tam_znak(znak_ktory_hladam, retazec):
    pocet = 0
    for symbol in retazec:
        if symbol == znak_ktory_hladam:
            pocet += 1
    return pocet

retazec_vstup = input("Zadaj znaky ukoncene bodkou: ")
for ascii_cislo_pismenka in range(ord('a'), ord('z')+1): # v range mozu byt iba cisla, teda ideme cez ascii cisla pre a-z
    pismenko = chr(ascii_cislo_pismenka)
    print(pismenko,":", kolkokrat_je_tam_znak(pismenko, retazec_vstup) ,"krat")
