import turtle
from random import randint
import time

ekran = turtle.Screen()
ekran.setup(height=800,width=800)
ekran.bgcolor("light blue")
ekran.title("Catch the Turtle")

#kaplumbağayı ekranda gösterme
turtle_instance=turtle.Turtle()
turtle_instance.shape("turtle")

#scoru ekranda gösterme
score = 0
score_instance = turtle.Turtle()
score_instance.penup()
score_instance.hideturtle()
score_instance.goto(0,380)
score_instance.write("Score: {}".format(score),font='Courier',align='center')

#zamanı ekranda gösterme
game_duration= 10
time_instance = turtle.Turtle()
time_instance.penup()
time_instance.hideturtle()
time_instance.goto(0,360)
time_instance.write("Time: {}".format(game_duration),font='Courier',align='center')


def clicked_on_turtle(x,y):
    global score
    score +=1
    score_instance.clear()
    score_instance.write("Score: {}".format(score),font='Courier',align='center')


start_time =time.time()

#kaplumbağayı random olarak ekranda gösterme
while True:
    turtle_instance.penup()
    turtle_instance.goto(randint(-400,400),randint(-400,400))
    turtle_instance.speed('slowest')
    turtle_instance.onclick(clicked_on_turtle)
    elapsed_time = time.time()-start_time
    remaining_time = max(game_duration-elapsed_time,0)
    time_instance.clear()
    time_instance.write("Time: {}".format(int(remaining_time)),font='Courier',align='center')

    if remaining_time <= 0:
        time_instance.clear()
        time_instance.write("Game Over", font='Courier', align='center')

        break

    ekran.update()


turtle.mainloop()