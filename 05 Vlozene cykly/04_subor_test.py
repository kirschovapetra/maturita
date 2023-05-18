"""
Textový súbor obsahuje  meno žiaka a počet dosiahnutých bodov z výstupného testu.
Zostavte program, ktorý vypíše na obrazovku mená žiakov usporiadané podľa
dosiahnutých bodov.
"""


subor = open("04_subor_test.txt", "r")

riadky = subor.readlines()

mena_zoznam = []
body_zoznam = []
for riadok in riadky:
    riadok_pole = riadok.strip().split(" ")
    mena_zoznam.append(riadok_pole[0])
    body_zoznam.append(int(riadok_pole[1]))

print(mena_zoznam)
print(body_zoznam)


# utriedime body od najvacieho po najmensie
# algoritmus bubble sort - vymiename pozicie aj v body_zoznam aj mena_zoznam

for i in range(len(body_zoznam)):
    for j in range(len(body_zoznam)):
        if body_zoznam[i] > body_zoznam[j]:
           body_zoznam[i], body_zoznam[j] = body_zoznam[j], body_zoznam[i]
           mena_zoznam[i], mena_zoznam[j] = mena_zoznam[j], mena_zoznam[i]

print(body_zoznam)
           
# pekne vypiseme
for i in range(len(body_zoznam)):
    print("meno:",mena_zoznam[i], "body:", body_zoznam[i])
