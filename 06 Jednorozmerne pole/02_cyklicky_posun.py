"""
Cyklický posun prvkov poľa o jeden a) doprava b) doľava
"""


def posun_o_1_dolava(pole):
    return pole[1:] + [pole[0]]


def posun_o_1_doprava(pole):
    return [pole[-1]] + pole[:-1]


pole_vstup = [1, 2, 3, 4, 5]
print("original", pole_vstup, "\n")

# posun --> o 1 prvok: [5, 1, 2, 3, 4]
print("doprava 1 krat:", posun_o_1_doprava(pole_vstup))

# posun <-- o 1 prvok: [2, 3, 4, 5, 1]
print("dolava 1 krat:", posun_o_1_dolava(pole_vstup))
print()

# ak by sme chceli posunut o viac
pocet_posunov = int(input("Zadaj kolkokrat chces posunut pole: "))

pole1 = pole_vstup
pole2 = pole_vstup

for x in range(pocet_posunov):
    pole1 = posun_o_1_doprava(pole1)
    pole2 = posun_o_1_dolava(pole2)

print("doprava", pocet_posunov, "krat:", pole1)
print("dolava", pocet_posunov, "krat:", pole2)
