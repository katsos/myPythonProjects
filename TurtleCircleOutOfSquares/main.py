import turtle

def draw_square(myTurtle):
    for i in range(0,4):
        myTurtle.forward(100)
        myTurtle.right(90)

def draw_scene():
    # set window
    window = turtle.Screen()
    window.bgcolor("orange")
    # create first turtle
    myTurtle = turtle.Turtle()
    myTurtle.hideturtle()
    myTurtle.speed(30)
    for i in range(1,74):
        draw_square(myTurtle)
        myTurtle.right(5)

    window.exitonclick()

# main
draw_scene()

