"""
Zostavte program na zistenie minimálneho a maximálneho čísla zo zadaných n čísel..
"""

cisla = [0, 1, 2, 5, -5, 4, 10, 100, -50, 2, 0, 0]

max_cislo = cisla[0]
min_cislo = cisla[0]

for cislo in cisla:
    if cislo > max_cislo:
        max_cislo = cislo
    if cislo < min_cislo:
        min_cislo = cislo

print("Maximum:", max_cislo)
print("Minimum:", min_cislo)
