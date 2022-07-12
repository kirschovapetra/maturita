"""
Napíšte program na určenie najväčšieho spoločného deliteľa
a najmenšieho spoločného násobku.
"""

a_vstup = int(input("Cislo a: "))
b_vstup = int(input("Cislo b: "))

''' NSD '''
nsd = a_vstup
b = b_vstup
while b != 0:
    nsd, b = b, nsd % b
print("NSD: " + str(nsd))

''' NSN '''
a = a_vstup
b = b_vstup
nsn = a * b
while b != 0:
    a, b = b, a % b
nsn = nsn // a
print("NSN: " + str(nsn))
