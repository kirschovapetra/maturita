"""
Vytvorte program na výpočet mocniny x^n, x reálne číslo, n prirodzené číslo
"""

while True:
    x = float(input("Zadajte cislo (realne cislo): "))
    n = int(input("Zadajte mocninu (prirodzene cislo): "))

    if n <= 0:
        print("zadajte prirodzene cislo!")
    else:
        mocnina = 1
        for i in range(1, n + 1):
            mocnina *= x
        print(str(x) + "^" + str(n) + " = " + str(mocnina))
