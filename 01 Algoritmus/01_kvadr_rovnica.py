"""
Napíšte program  na riešenie rovnice typu ax2 + bx + c = 0
"""

a = int(input("Zadajte a: "))
b = int(input("Zadajte b: "))
c = int(input("Zadajte c: "))

print("Rovnica: " + str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0")

D = b ** 2 - 4 * a * c

if D < 0:
    print("Korene neexistuju")

elif D == 0:
    x = -b / (2 * a)
    print("Koren: x=" + str(x))

else:
    x1 = (-b + D ** 0.5) / (2 * a)
    x2 = (-b - D ** 0.5) / (2 * a)
    print("Korene: x1=" + str(x1) + " x2=" + str(x2))
