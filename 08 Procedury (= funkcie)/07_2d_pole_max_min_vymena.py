"""
Dané je dvojrozmerné pole obsahujúce celé čísla.
Vytvoriť program, ktorý nájde maximálnu a minimálnu hodnotu
v poslednom stĺpci a vymení riadky s maximálnou a minimálnou hodnotou
v poslednom stĺpci.
( použite procedúry: na načítanie a výpis dvojrozmerného poľa,
na nájdenie max. a min. hodnoty vstĺpci, na výmenu dvoch riadkov)
"""

def vypis_matice(matica_fun):
    for riadok in matica_fun:
        for cislo in riadok:
            print(cislo, end=' ')
        print()


def max_indexy_2D(pole):
    max_index_riadku = 0
    for i in range(len(pole)):
        if pole[i][-1] > pole[max_index_riadku][-1]:
            max_index_riadku = i

    return max_index_riadku

def min_indexy_2D(pole):
    min_index_riadku = 0
    for i in range(len(pole)):
        if pole[i][-1] < pole[min_index_riadku][-1]:
            min_index_riadku = i

    return min_index_riadku

# -----------------------------------------------------

pole_vstup = [
    [1,2,3],
    [4,5,2],
    [7,8,9]
]

max_r = max_indexy_2D(pole_vstup)
print("Maximum:", pole_vstup[max_r][-1], "je na indexoch: [",max_r, ",", -1,"]")

min_r = min_indexy_2D(pole_vstup)
print("Minimum:", pole_vstup[min_r][-1], "je na indexoch: [",min_r, ",", -1,"]")

print("Pred vymenou:")
vypis_matice(pole_vstup)

# vymenime riadky v ktorych sa nachadza max a min
pole_vstup[max_r], pole_vstup[min_r] = pole_vstup[min_r], pole_vstup[max_r]

print("Po vymene:")
vypis_matice(pole_vstup)

