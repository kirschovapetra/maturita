"""
Napíšte funkciu na výpočet ciferného súčtu daného čísla.
"""

cislo_str = input("zadaj cislo: ")

sucet = 0
for znak in cislo_str:
    sucet += int(znak)

print("ciferny sucet:", sucet)