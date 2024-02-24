import turtle

screen = turtle.Screen()
screen.bgcolor("violet")
screen.title("Renkli Çizdirme")

imlec = turtle.Turtle()

colors =["yellow","blue","red","pink","violet","green"]


for i in range(6):
    imlec.circle(50*i)
    imlec.circle(-50*i)
    imlec.color(colors[i])

turtle.mainloop()
#turtle.done()