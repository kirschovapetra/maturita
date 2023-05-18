"""
Daná je štvorcová matica n x n celých kladných čísel.
Zistite, či je daná matica symetrická podľa hlavnej diagonály.
Čísla matice sa zadávajú po riadkoch.
"""

# poznamka - mozme si vygenerovat maticu n x n alebo zo vstupu nacitavat po riadkoch. take veci sme uz robili v inych prikladoch

def zisti_ci_je_symetricka(matica):

    for index_riadku in range(len(matica)):

        riadok = matica[index_riadku]
        for index_stlpca in range(len(riadok)):

            prvok_vlavo = matica[index_riadku][index_stlpca]
            prvok_vpravo = matica[index_stlpca][index_riadku]

            if prvok_vlavo != prvok_vpravo:
                return False

    return True


matica_symetricka = [
    [1, 2, 3],    # suradnice [0,0], [0,1], [0,2]
    [2, 1, 0],    # suradnice [1,0], [1,1], [1,2]
    [3, 0, 1]     # suradnice [2,0], [2,1], [2,2]
]
print(zisti_ci_je_symetricka(matica_symetricka))

matica_nesymetricka = [
    [1, 0, 0],
    [0, 1, 0],
    [5, 0, 1],
]
print(zisti_ci_je_symetricka(matica_nesymetricka))


