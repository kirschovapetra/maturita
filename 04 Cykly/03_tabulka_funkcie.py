"""
 Zostavte tabuľku funkcie y = x^2 + 4x +1 pre x < 1, 20 > s krokom 0,5.
"""

x = 1.0
while x <= 20.0:
    y = x**2 + 4*x + 1
    print("x:", x, "y:", y)
    x += 0.5
