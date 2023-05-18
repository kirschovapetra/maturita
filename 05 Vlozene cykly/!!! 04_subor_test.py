"""
Textový súbor obsahuje  meno žiaka a počet dosiahnutých bodov z výstupného testu.
Zostavte program, ktorý vypíše na obrazovku mená žiakov usporiadané podľa
dosiahnutých bodov.
"""


subor = open("04_subor_test.txt", "r")

riadky = subor.readlines()

for riadok in riadky:
    riadok_pole = riadok.strip().split(" ")
    meno = riadok_pole[0]
    body = riadok_pole[1]
    # todo