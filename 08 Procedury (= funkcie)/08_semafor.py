"""
Napíšte program, ktorý bude simulovať striedanie svetiel semafora na križovatke.
Vytvorte štyri procedúry, ktoré budú prekresľovať vtej istej pozícii
4 fázy svetiel -stoj, priprav sa, choď, zastav.
"""

import turtle

t = turtle.Turtle()

polomer = 30
cervena_y = 170
oranzova_y = 100
zelena_y = 30

def cierny_kruh(y):
    t.fillcolor("black")
    t.penup()
    t.goto(10, y)
    t.pendown()
    t.begin_fill()
    t.circle(polomer)
    t.end_fill()
 
def cerveny_kruh(y):
    t.fillcolor("red")
    t.penup()
    t.goto(10, y)
    t.pendown()
    t.begin_fill()
    t.circle(polomer)
    t.end_fill()


def oranzovy_kruh(y):
    t.fillcolor("orange")
    t.penup()
    t.goto(10, y)
    t.pendown()
    t.begin_fill()
    t.circle(polomer)
    t.end_fill()


def zeleny_kruh(y):
    t.fillcolor("green")
    t.penup()
    t.goto(10, y)
    t.pendown()
    t.begin_fill()
    t.circle(polomer)
    t.end_fill()


counter = 0
while True:
    stav = counter % 4

    if stav == 0:
        cerveny_kruh(cervena_y)
        cierny_kruh(oranzova_y)
        cierny_kruh(zelena_y)
    elif stav == 1:
        cierny_kruh(cervena_y)
        oranzovy_kruh(oranzova_y)
        cierny_kruh(zelena_y)
    elif stav == 2:
        cierny_kruh(cervena_y)
        cierny_kruh(oranzova_y)
        zeleny_kruh(zelena_y)
    elif stav == 3:
        cierny_kruh(cervena_y)
        oranzovy_kruh(oranzova_y)
        cierny_kruh(zelena_y)

    counter += 1
