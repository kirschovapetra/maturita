"""
Zostavte program, ktorý bude čítať vstupný súbor a pre každý riadok vytlačí koľkokrát sa v ňom vyskytuje
jeho prvý znak.
"""

subor = open("01_subor_pocet_1_znaku.txt", "r")
riadky = subor.readlines()

for riadok in riadky:
    prvy_znak = riadok[0]

    # spocitame kolko krat sa "prvy_znak" nachadza v "riadok"
    pocet = 0
    for znak in riadok:
        if znak == prvy_znak:
            pocet += 1
    print("Prvy znak:", prvy_znak, "sa nachadza", pocet, "krat:", riadok[:-1])
