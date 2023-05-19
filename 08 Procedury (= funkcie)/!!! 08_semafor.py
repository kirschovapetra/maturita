"""
Napíšte program, ktorý bude simulovať striedanie svetiel semafora na križovatke.
Vytvorte štyri procedúry, ktoré budú prekresľovať vtej istej pozícii
4 fázy svetiel -stoj, priprav sa, choď, zastav.
"""
import time
import turtle

t = turtle.Turtle()

radius = 30


def stoj():
    t.fillcolor("red")
    t.penup()
    t.goto(10, 170)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    print("stoj")


def priprav_sa():
    t.fillcolor("orange")
    t.penup()
    t.goto(10, 100)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    print("priprav sa")


def chod():
    t.fillcolor("green")
    t.penup()
    t.goto(10, 30)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    print("chod")


def zastav():
    t.fillcolor("orange")
    t.penup()
    t.goto(10, 100)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    print("zastav")


counter = 0
while True:
    stav = counter % 4

    if stav == 0:
        stoj()
    elif stav == 1:
        priprav_sa()
    elif stav == 2:
        chod()
    elif stav == 3:
        zastav()

    counter += 1

    time.sleep(3)
