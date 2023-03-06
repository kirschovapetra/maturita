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
        print("Parnych: ", parne)
        print("Neparnych: ", neparne)
        break
    else:
        if cislo % 2 == 0:
            parne += 1
        else:
            neparne += 1

# ############### verzia 2 - nacitanie cisel naraz ################

parne = 0
neparne = 0
postupnost = input("Zadajte postupnost celých kladných čísel ukončenú nulou: ")
postupnost_cisla = postupnost.split(" ")  # spravi sa pole

if int(postupnost_cisla[-1]) != 0:
    print("Neukoncil si postupnost nulou!")
else:
    for cislo in postupnost_cisla:
        if int(cislo) == 0:
            print("Parnych: ", parne)
            print("Neparnych: ", neparne)
            break
        if int(cislo) % 2 == 0:
            parne += 1
        else:
            neparne += 1