"""
Daná je matica A(M,N),ktorej každý prvok je reálne číslo z intervalu (-100, 100).
Napíšte program pre výpis matice A tak, aby každý prvok bol vypísaný s dvoma
platnými desatinnými číslami.
"""

A = [
    [1.12345, 2.12345, 3.12345, 4.12345, 5.12345],
    [-1.12345, -2.12345, -3.12345, -4.12345, -5.12345],
    [1.12345, 2.12345, 3.12345, 4.12345, 5.12345],
    [-1.12345, -2.12345, -3.12345, -4.12345, -5.12345],
    [1.12345, 2.12345, 3.12345, 4.12345, 5.12345],
    [-1.12345, -2.12345, -3.12345, -4.12345, -5.12345],
]

''' vypis matice '''

for riadok in range(len(A)):
    for stlpec in range(len(A[riadok])):
        print(round(A[riadok][stlpec], 2), end=' ')
    print()
