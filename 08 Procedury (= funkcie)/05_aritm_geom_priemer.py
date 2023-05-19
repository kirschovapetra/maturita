"""
Na vstupe je N celých kladných čísel. Napíšte procedúru pre výpočet
aritmetického a geometrického priemeru
"""


def aritmeticky(pole):
    pocet_cisel = len(pole)
    sucet = 0
    for cislo in pole:
        sucet += cislo
    return sucet / pocet_cisel


# geometricky priemer - vzorec: https://sk.economy-pedia.com/11037000-geometric-mean#menu-1
def geometricky(pole):
    pocet_cisel = len(pole)
    sucin = 1  # !!!!!!!!!!!!!!!!!!!!!!!!! nem 0 ale 1, lebo ked robis sucin 0*hocico tak bude 0.
    for cislo in pole:
        sucin *= cislo
    return sucin ** (1 / pocet_cisel)  # n-ta odmocnina


pole_vstup = [1, 2, 3, 4, 5]
print(aritmeticky(pole_vstup))
print(geometricky(pole_vstup))
