"""
Je daná obdĺžniková matica A (m, n). Zostavte program, ktorý zistí
počet nulových prvkov matice A.
"""

matica = [
    [0, 2, 3, 4],
    [1, 2, 0, 4],
    [1, 0, 3, 4],
    [1, 2, 3, 4],
    [0, 2, 0, 4],
]

pocet_nul = 0
for riadok in matica:
    for cislo_v_stlpci in riadok:
        if cislo_v_stlpci == 0:
            pocet_nul += 1

print("pocet nulovych prvkov: ", pocet_nul)