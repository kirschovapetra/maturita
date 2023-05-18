"""
Napíšte funkciu, ktorá prevedie prirodzené číslo z dvojkovej
pozičnej sústavy do desiatkovej
"""

binarne_cislo = input("zadaj binarne cislo: ")

desiatkove_cislo = 0
for index in range(len(binarne_cislo)):

    index_odzadu = -1-index
    bin_cislica = binarne_cislo[index_odzadu]

    desiatkove_cislo += int(bin_cislica) * (2 ** index)


print(desiatkove_cislo)