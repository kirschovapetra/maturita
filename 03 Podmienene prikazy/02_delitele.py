"""
 Zostavte program na zistenie všetkých deliteľov daného čísla.
"""

cislo = int(input("Zadajte cislo: "))

for delitel in range(1, cislo + 1):  # zacinam od 1 lebo 0 sa neda delit
    if cislo % delitel == 0:
        print("Delitel: ", delitel)
