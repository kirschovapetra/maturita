"""
Napíšte funkciu TROJ(X1,Y1, X2,Y2, X3,Y3), ktorá vypočíta plošný obsah
trojuholníka s vrcholmi (x1, y1), (x2, y2), (x3, y3).
"""


def TROJ(X1, Y1, X2, Y2, X3, Y3):
    x_12 = X2 - X1
    y_12 = Y2 - Y1
    strana_a_12 = (x_12 ** 2 + y_12 ** 2) ** 0.5

    x_23 = X3 - X2
    y_23 = Y3 - Y2
    strana_b_23 = (x_23 ** 2 + y_23 ** 2) ** 0.5

    x_13 = X3 - X1
    y_13 = Y3 - Y1
    strana_c_13 = (x_13 ** 2 + y_13 ** 2) ** 0.5

    # neviem vzorec s 3 stranami, tak vyratam obvod fck it

    obvod = strana_a_12 + strana_b_23 + strana_c_13

    print(obvod)


TROJ(1, 1, 2, 2, 3, 3)
