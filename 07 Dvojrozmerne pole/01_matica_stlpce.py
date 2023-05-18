"""
Daná je matica A(m, n).Zostavte program na výmenu k-teho a l-teho stĺpca matice A.
"""

def vypis_matice(matica_fun):
    for riadok in matica_fun:
        for cislo in riadok:
            print(cislo, end=' ')
        print()


matica = [ 
    [1,2,3,4,5],    # [0][0] [0][1=k] [0][2] [0][3=l] [0][4]
    [1,2,3,4,5],    # [1][0] [1][1=k] [1][2] [1][3=l] [1][4]
    [1,2,3,4,5],    # [2][0] [2][1=k] [2][2] [2][3=l] [2][4]
]

print("pred vymenou")
vypis_matice(matica)

k = int(input("zadaj cislo (index) 1. stlpca: "))
l = int(input("zadaj cislo (index) 2. stlpca: "))

for index_riadku in range(len(matica)):
        matica[index_riadku][k], matica[index_riadku][l] = matica[index_riadku][l], matica[index_riadku][k]
 

print("po vymene")
vypis_matice(matica)