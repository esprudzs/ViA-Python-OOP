# Forth practical work
# 2021.12.29
# Andris Jenerts
# Group 1


import turtle
from math import *

# https://www.jpl.nasa.gov/edu/pdfs/scaless_reference.pdf
# https://nssdc.gsfc.nasa.gov/planetary/factsheet/


class Object(turtle.Turtle):
    def __init__(self, iName, iRad, iDist, iYear, iColor, iCenter):
        """
        Parameters
        ----------
        iName : str
            Name of the planet
        iRad : float
            Scale factor fot the planet    
        iDist : float
            Distance from the center in px
        iYear : float
            How long one year is compared to reference (e.g. Earth = 1year in our system)
        iColor : str
            Display color for the planet
        iCenter : obj
            Center of rotation
        """

        # init turtle and set shape to circle
        super().__init__(shape='circle', visible=False)

        # save local variables
        self.__name = iName
        self.__radius = iRad
        self.__distance = iDist
        self.__year = iYear

        self.__color = iColor
        self.__center = iCenter
  
        # lift pen - we do not want trajectories
        self.up()

        # turtle parameters
        self.setx(x=self.__distance)
        self.color(self.__color)
        self.shapesize(self.__radius, self.__radius)
        self.showturtle()                # show turtle
        # attributes for drawing
        self.__angle = 0

    def increaseAngle(self):
        """Updates angle of the planet for specificied angle

        Parameters
        ----------
        angle : float
            Angle in radians
        """
        #self.__angle += angle
        self.__angle += ((3.14*2)/(360*self.__year))

    def move(self):
        """Moves to the the current angle 
        """
        xPos = self.__distance*cos(self.__angle)
        yPos = self.__distance*sin(self.__angle)

        # use turtle method  xcor anf ycor to get current position
        # of the rotation center add calculated coordinates to the center
        # to get our position
        self.goto(self.__center.xcor() + xPos,
                  self.__center.ycor() + yPos)

    def getRadius(self):
        return self.__radius

    def getDistance(self):
        return self.__distance

    def setName(self, newName):
        self.__name = newName

    def setRadius(self, newRadius):
        self.__radius = newRadius

    def setDistance(self, newDistance):
        self.__distance = newDistance

    def __str__(self):
        return self.__name