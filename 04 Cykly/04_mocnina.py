"""
Vytvorte program na výpočet mocniny x^n, x reálne číslo, n prirodzené číslo
"""

while True:
    x_zaklad = float(input("Zadajte cislo (realne cislo): "))
    n_mocnina = int(input("Zadajte mocninu (prirodzene cislo): "))

    if n_mocnina <= 0:
        print("zadajte prirodzene cislo!")
    else:
        vysledok = 1
        for i in range(1, n_mocnina + 1):
            vysledok *= x_zaklad
        print(str(x_zaklad) + "^" + str(n_mocnina) + " = " + str(vysledok))
