"""
Zo vstupného zariadenia načítajte postupnosť celých kladných čísel ukončenú nulou.
Zostavte program, ktorý vypíše počet párnych a počet nepárnych čísel danej postupnosti.
"""

# ############### verzia 1 - nacitanie cisel po jednom ###############
parne = 0
neparne = 0
while True:
    cislo = int(input("Zadajte cislo: "))

    if cislo == 0:
        break
    else:
        if cislo % 2 == 0:
            parne += 1
        else:
            neparne += 1

print("Parnych: ", parne)
print("Neparnych: ", neparne)

# ############### verzia 2 - nacitanie cisel naraz ################

parne = 0
neparne = 0
postupnost = input("Zadajte postupnost celých kladných čísel ukončenú nulou: ")
postupnost_cisel = postupnost.split(" ")  # spravi sa pole

if int(postupnost_cisel[-1]) != 0:
    print("Neukoncil si postupnost nulou!")
else:
    for cislo in postupnost_cisel:
        if int(cislo) == 0:
            break
        if int(cislo) % 2 == 0:
            parne += 1
        else:
            neparne += 1

print("Parnych: ", parne)
print("Neparnych: ", neparne)

# ############### verzia 3 - najprv si nacitam pole a potom idem pocitat parne a neparne ################

postupnost_cisel = []
cislo_zo_vstupu = int(input("Zadajte cislo: "))
while cislo_zo_vstupu != 0:
    postupnost_cisel.append(cislo_zo_vstupu)
    cislo_zo_vstupu = int(input("Zadajte cislo: "))

parne = 0
neparne = 0
for cislo in postupnost_cisel:
    if cislo % 2 == 0:
        parne += 1
    else:
        neparne += 1

print("Parnych: ", parne)
print("Neparnych: ", neparne)