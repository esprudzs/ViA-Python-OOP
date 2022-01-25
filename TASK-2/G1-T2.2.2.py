# Second practical work: drawing function x/2+5
# 2021.12.05
# Group 1

import turtle
import timeit

#starts timer, when program is started
start = timeit.default_timer()

wn=turtle.Screen()
#sets screen width and height; later used to draw axis
w=50
h=50
wn.setworldcoordinates(-w, -h, w, h)
t=turtle.Turtle()
t.position()
t.heading()
#function to draw axis
def drawAxis(turtle, distance, mark):
    position = turtle.position()
    turtle.pendown()
    turtle.dot()

    for i in range(0, distance, mark):
        turtle.forward(mark)
        turtle.dot() #makes rundown slower, but makes axis easier to read 

    turtle.setposition(position)

    for i in range(0, distance, mark):
        turtle.backward(mark)
        turtle.dot()
#draws x-axis
t.penup()
t.home()
drawAxis(t, w, 1)
#draws y-axis 
t.penup()
t.home()
t.setheading(90)
drawAxis(t, h, 1)
#function to draw y = x / 2 + 5
def drawFunction(turtle, range):
    turtle.penup()
    turtle.pencolor("red")

    for x in range:
            y = x / 2 + 5
            t.goto(x, y)
            turtle.pendown()
#draws mathematical function in given range
drawFunction(t, range(-50, 50))
#stops the timer and prints out runtime
stop = timeit.default_timer()
print('Time: ', stop - start) 

input("Press any key to exit")
