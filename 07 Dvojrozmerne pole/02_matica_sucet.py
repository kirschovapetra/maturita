"""
Zostavte program na výpočet stĺpcových a riadkových súčtov matice A.
"""

def vypis_matice(matica_fun):
    for riadok in matica_fun:
        for cislo in riadok:
            print(cislo, end=' ')
        print()


matica = [ 
    [1,2,3,4,5],    # [0][0] [0][1] [0][2] [0][3] [0][4]
    [0,2,0,4,0],    # [1][0] [1][1] [1][2] [1][3] [1][4]
    [1,0,3,0,5],    # [2][0] [2][1] [2][2] [2][3] [2][4]
]

vypis_matice(matica)

# sucet po riadkoch
for index_riadku in range(len(matica)):
    sucet_riadku = 0
    for index_stlpca in range(len(matica[index_riadku])):
        sucet_riadku += matica[index_riadku][index_stlpca]
    print("riadok", index_riadku, ":", sucet_riadku)


# sucet po stlpcoch
for index_stlpca in range(len(matica[0])):
    sucet_stlpca = 0
    for index_riadku in range(len(matica)):
        sucet_stlpca += matica[index_riadku][index_stlpca]
    print("stlpec", index_stlpca, ":", sucet_stlpca)
