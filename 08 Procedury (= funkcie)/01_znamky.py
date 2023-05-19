"""
Zostavte program na vyhodnotenie jednej písomnej práce v triede.
Mená žiakov sa nachádzajú vo vstupnom súbore dosiahnutá známka sa načítava z klávesnice.
Program má vypísať počet jednotiek, dvojok, trojok...atď
aj s menami žiakov a nakoniec vypíše aritmetický priemer triedy .
"""


def ziaci_so_znamkou(znamka_ktoru_hladam, pole_znamok, pole_mien):
    ziaci = []

    for index in range(len(pole_znamok)):
        if pole_znamok[index] == znamka_ktoru_hladam:
            ziaci.append(pole_mien[index])

    return ziaci


# step 1 - nacitame zo suboru a hodime do 2 poli - jedno pole pre mena a druhe pre znamky
subor = open("01_znamky.txt", "r")
znamky = []
mena = []
for riadok in subor.readlines():
    meno = riadok.strip()
    mena.append(meno)
    znamka_vstup = int(input("Zadaj aku znamku ma " + meno + ": "))
    znamky.append(znamka_vstup)

# step 2 - zistit pre kazdu znamku ktori ziaci ju dostali
for znamka in range(1, 6):  # alebo for znamka in [1,2,3,4,5]
    vysledny_ziaci = ziaci_so_znamkou(znamka, znamky, mena)
    print("Znamku", znamka, "ma", len(vysledny_ziaci), "ziakov:", vysledny_ziaci)

# step 3 - aritmeticky priemer
aritmeticky_priemer = sum(znamky) / len(znamky)
print("Priemer:", aritmeticky_priemer)
