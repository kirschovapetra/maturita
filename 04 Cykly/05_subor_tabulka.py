"""
Predpokladajte, že vstupný súbor sa skladá z trojíc tvaru: identifikačné číslo IC, jednotková cena C
a množstvo tovaru M (kde IC > 0, C > 0, M >= 0), za ktorými bude trojica začínajúca nulou.
Zostavte program na tlač tabuľky s vhodným záhlavím, kde každý bežný riadok obsahuje informácie o jednom tovare:
číslo, cena, množstvo a hodnota (= cena krát množstvo).
V poslednom riadku má byť informácia o počte druhov tovaru a o celkovej hodnote inventúry
"""


# IC    C   M
# 1  10.50  10
# 2  11.50  11
# 3  12.50  0
# 4  13.50  13
# 5  1.50   0


subor = open("05_subor_tabulka.txt", "r")

riadky = subor.readlines()

suma = 0
druhy = []
print("Identif. cislo  Cena  Mnozstvo  Hodnota")

for riadok in riadky:
    riadok_pole = riadok.strip().split(" ")

    # vytiahneme si veci z riadku
    identifikacne_cislo = int(riadok_pole[0])
    cena_za_1ks = float(riadok_pole[1])
    mnozstvo = int(riadok_pole[2])
    cena_komplet = cena_za_1ks * mnozstvo

    # pripocitame cenu k sume (co vypisujeme nakoniec)
    suma += cena_komplet

    # pridame IC do listu len ak tam neexistuje (aby sme vedeli kolko tam je roznych IC)
    if identifikacne_cislo not in druhy:
        druhy.append(identifikacne_cislo)

    print(identifikacne_cislo, "             ", cena_za_1ks, " ", mnozstvo, "     ", cena_komplet)

print("\nPocet druhov tovaru:", len(druhy), ", Celkova hodnota:", suma)
