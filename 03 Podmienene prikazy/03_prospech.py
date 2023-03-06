"""
Zostavte program na určenie celkového prospechu žiaka

- prospel s vyznamenaním, ak ani v jednom povinnom vyučovacom predmete nemá stupeň prospechu horší ako chválitebný,
  priemerný stupeň prospechu z povinných vyučovacích predmetov nemá horší ako 1,5 a jeho správanie je hodnotené ako "veľmi dobré".
- Žiak prospel veľmi dobre, ak ani v jednom povinnom vyučovacom predmete nemá stupeň prospechu horší ako dobrý, priemerný
  stupeň prospechu z povinných vyučovacích predmetov nemá horší ako 2,0 a jeho správanie je hodnotené ako "veľmi dobré"
- Žiak prospel, ak nemá stupeň prospechu nedostatočný ani v jednom povinnom vyučovacom predmete.
- Žiak neprospel, ak má z niektorého povinného vyučovacieho predmetu aj po opravnej skúške stupeň prospechu nedostatočný.
"""

znamky = [1, 2, 1, 1, 2, 1, 3, 4, 1, 2, 1, 3, 3, 3]

# priemer
pocet_znamok = len(znamky)
sucet = 0
for znamka in znamky:
    sucet += znamka
priemer = sucet/pocet_znamok
print("Priemer: ", priemer)

# prospech
if 5 in znamky:
    print("Neprospel")
elif 4 in znamky or priemer > 2.0:
    print("Prospel")
elif 3 in znamky or priemer > 1.5:
    print("Prospel veľmi dobre")
else:
    print("Prospel s vyznamenaním")





