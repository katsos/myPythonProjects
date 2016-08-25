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
    myTurtle.shape("turtle")
    myTurtle.speed(1)
    draw_square(myTurtle)
    
    # create first turtle
    secTurtle = turtle.Turtle()
    secTurtle.shape("arrow")
    secTurtle.speed(1)
    secTurtle.circle(150)

    window.exitonclick()

# main
draw_scene()
