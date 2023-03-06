"""
Zostavte program na výpočet aritmetického priemeru z n nameraných hodnôt.
"""

hodnoty = [1.1, 2.2, 3.3, 4.4, 5.5]
n = len(hodnoty)

sucet = 0
for cislo in hodnoty:
    sucet += cislo
priemer = sucet / n
print(priemer)
