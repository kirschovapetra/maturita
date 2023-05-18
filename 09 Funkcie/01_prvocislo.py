"""
Napíšte funkciu na zistenie, či dané číslo kje prvočíslo
"""

def zisti_ci_je_prvocislo(cislo):
    je_prvocislo = True
    for delitel in range(2, cislo):
        if cislo % delitel == 0:
            je_prvocislo = False
            break

    return je_prvocislo


cislo_vstup = int(input("Cislo: "))
print("Je prvocislo?", zisti_ci_je_prvocislo(cislo_vstup))