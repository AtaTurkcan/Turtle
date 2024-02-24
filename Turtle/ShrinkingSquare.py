# İç içe kareler çizdirmek

import turtle

ekran = turtle.Screen()
ekran.bgcolor("orange")
ekran.title("İç İçe Kare")

imlec = turtle.Turtle()
imlec.color("blue")

def shrinking_square(size):
    for i in range(4):
        imlec.forward(size)
        imlec.left(90)
        size = size-5


for i in range(10):
    shrinking_square(150-i*20)

turtle.done()