"""
Daný je textový súbor. Zostavte program, ktorý obsah tohto súboru zobrazí na obrazovke
tak, že každý riadok daného textového súboru zobrazí na obrazovke od 10 –teho znaku
"""

# encoding tu je kvoli tomu, aby vedel precitat slovenske znaky (nepovinne)
subor = open("03_subor.txt", "r", encoding="utf8")
riadky = subor.readlines()


for riadok in riadky:
    riadok_od_10teho_znaku = riadok[9:]
    # end="" - nebude pridavat enter pri vypise, lebo v riadkoch uz enter na konci je (nepovinne)
    print(riadok_od_10teho_znaku, end="")
