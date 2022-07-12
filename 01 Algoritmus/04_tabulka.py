"""
Zostavte program na generovanie a výpis tabuľky.
Maximálny rozmer tabuľky je 20 X 20, čísla sa generujú z intervalu <0, 100)
"""
import random

velkost = int(input("Velkost tabulky: "))

if velkost > 20:
    print("velkost moze byt max 20")
elif velkost < 0:
    print("velkost nemoze byt zaporne")
else:
    for riadok in range(velkost):
        for stlpec in range(velkost):
            cislo = random.randint(0, 99)
            print(cislo, end=' ')
        print()
