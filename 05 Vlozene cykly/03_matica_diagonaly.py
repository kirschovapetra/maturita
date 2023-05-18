"""
Daná je štvorcová matica A. Zostavte program, ktorý vymení prvky vedľajšej
diagonály s prvkami hlavnej diagonály.
"""

matica = [
        [0,1,2,3],
        [0,4,5,6],
        [0,0,7,8],
        [0,0,0,9]
    ]

for i_r in range(len(matica)):
    for i_s in range(len(matica[i_r])):
        if i_r<i_s:
            matica[i_r][i_s], matica[i_s][i_r] = matica[i_s][i_r], matica[i_r][i_s]
        print(matica[i_r][i_s], end=' ')
    print()
