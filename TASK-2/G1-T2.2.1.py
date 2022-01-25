# Second practical work: n-pointed star
# 2021.12.05
# Group 1


import turtle  # import turtle graphics module
import math
# turtle module documentation:
# https://docs.python.org/3/library/turtle.html


def drawStar(thisTurtle: turtle.Turtle, n:int, q:int):
    """ Draw a n-pointed star using q turing number.

     - thisTurtle - turtle module Turtle class object
     - n          - points of the star
     - q          - turning number (see Schläfli symbol for more info)    
    """
    starRadius = 100                                                  #this is fixed number
    vertexAngle = (180*(n-2*q))/n                                     #angle sum divided by no. of vertices
    centerAngle = 360/n                                               
    turnAngle = 360*q/n                                               #calculates turning angle at the vertex
    sideLength = starRadius * math.sin(math.radians(centerAngle*q)/2)     #calculates length of the edge if fixed R

    liftAngle = (vertexAngle/2 + (180-centerAngle)/2)                       #once pen is lifted turn this angle
    liftDistance = starRadius * math.sin(math.radians(centerAngle/2))     #this is distance to the next point
    liftBackAngle = (180+centerAngle)/2 + vertexAngle/2             #angle to turn back and start next figure

    #for debugging purposes
    print("radius: %d vertex: %f turning: %f lift: %f liftb: %f side: %f liftSide: %f"%(starRadius, vertexAngle, turnAngle, liftAngle, liftBackAngle, sideLength, liftDistance))
   
    if(n % q != 0):
        # these stars can be drawn without "lifting pen"
        for point in range(n):                                         
            thisTurtle.forward(sideLength)                     #draw a line
            thisTurtle.right(turnAngle)                        #turn to draw next line
    else:
        for lift in range(q):
            for point in range(int(n/q)):
                thisTurtle.forward(sideLength)                 #draw a line
                thisTurtle.right(turnAngle)                    #turn to draw next line

            thisTurtle.penup()                                 #lift up pen
            thisTurtle.right(liftAngle)                        #turn to the next point direction
            thisTurtle.forward(liftDistance)                   #go to the next point
            thisTurtle.left(liftBackAngle)                     #turn back to draw next edge of the star 
            thisTurtle.pendown()                               #prepare to draw

while True:
    try:
           
        vertices = int(input('Enter star vertices count: '))   #convert user input to int
        if((vertices % 2) == 0):
            print("I can draw only stars with odd number vertices")
            continue                                           #resume while loop to ask again
        if(vertices < 5):
            print("Star has at least 5 vertices")
            continue
        break                                                  #all test passed, break out
    except:
        print("Error, please enter integer value")             #most likely entered float or non-numeric
        continue


# knowing how many pointed star user wants to draw
# we calcaulate all possible variants for this star and 
# provide them so that user can choose from them

variant_count = int((vertices - 3)/2)                          # calculates and stores star variants
turningNumber = None                                           # this will be determined
drawAll = False                                                # if user wants to see all variants 
if(variant_count > 1):                                            
    print("""It is possible to draw %d-pointed star in %d differnet ways.
    They are listed below in Schläfli notation"""%(vertices, variant_count))

    selected_variant = None                                    # user will select one of the variants
    for variant in range(variant_count):
        print("%d: "%(variant+1), end="")
        print("{%d,%d}"%(vertices,(2+variant)))
    print("%d: all variants"%(variant_count+1))

    while True:
        try:
            selected_variant = int(input("Enter number of the variant you want to draw: "))
            if(selected_variant < 1  or selected_variant > (variant_count)):
                if(selected_variant == (variant_count +1)):
                    print("drawing all variants")
                    drawAll = True
                    break

                print("Error, please enter valid value")
                continue

            turningNumber = selected_variant + 1                                    # 1st variant q = 2, 2nd q = 3 etc
            break
        except:
            print("Error, please enter valid value")
            continue
    

else:
    turningNumber = 2                                                       # 5 pointed star 



myTurtle = turtle.Turtle()      # create turtle object instance
myTurtle.speed(5)               # sets turtle speed
myTurtle.pencolor("#33cc33")    # color of the line
myTurtle.penup()
myTurtle.setposition(-400,0)
myTurtle.pendown()

if(drawAll):
    for variant in range(variant_count):
        turningNumber = variant+2
        drawStar(myTurtle, vertices, turningNumber)
        
        myTurtle.penup()
        myTurtle.setposition(myTurtle.pos()[0]+100,0)
        myTurtle.setheading(0)
        myTurtle.pendown()
else:
    drawStar(myTurtle, vertices, turningNumber)

input("Press any key to exit")
