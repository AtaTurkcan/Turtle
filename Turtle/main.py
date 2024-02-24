import turtle


drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Turtle")
turtle_instance = turtle.Turtle()

'''
#square
for i in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)
turtle.done()
'''
'''
#star
for i in range(5):
    turtle_instance.forward(100)
    turtle_instance.right(144)
turtle.done()
'''
#polygon
turtle_instance = turtle.Turtle()
num_sides = 5
angle = 360.0 / num_sides
side_lenght = 100

for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_lenght)

turtle.done()    