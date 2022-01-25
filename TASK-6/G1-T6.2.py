# Group 1
# Task-6.2
# A.Jenerts 2022.01.24

import math
import random
from typing import List #this is needed to strictly type polygon function
import turtle

class Canvas:
    def __init__(self, w, h):
        self.__visibleObjects = []   #list of shapes to draw
        self.__turtle = turtle.Turtle()
        self.__screen = turtle.Screen()
        self.__screen.setup(width = w, height = h)
        self.__turtle.hideturtle()

    def drawAll(self):
        self.__turtle.reset()
        self.__turtle.up()
        self.__screen.tracer(0)
        for shape in self.__visibleObjects: #draw all shapes in order
            shape._draw(self.__turtle)
        self.__screen.tracer(1)
        self.__turtle.hideturtle()

    def addShape(self, shape):
        self.__visibleObjects.append(shape)

    def draw(self, gObject):
        gObject.setCanvas(self)
        gObject.setVisible(True)
        self.__turtle.up()
        self.__screen.tracer(0)
        gObject._draw(self.__turtle)
        self.__screen.tracer(1)
        self.addShape(gObject)

    def freeze(self):
        self.__screen.exitonclick()

from abc import *
class GeometricObject(ABC):
    def __init__(self):
        self.__lineColor = 'black'
        self.__lineWidth = 1
        self.__visible = False
        self.__myCanvas = None

    def setColor(self, color):  #modified to redraw visible shapes
        self.__lineColor = color
        if self.__visible:
            self.__myCanvas.drawAll()

    def setWidth(self, width):  #modified to redraw visible shapes
        self.__lineWidth = width
        if self.__visible:
            self.__myCanvas.drawAll()

    def getColor(self):
        return self.__lineColor

    def getWidth(self):
        return self.__lineWidth

    @abstractmethod
    def _draw(self):
        pass

    def setVisible(self, vFlag):
        self.__visible = vFlag

    def getVisible(self):
        return self.__visible

    def setCanvas(self, theCanvas):
        self.__myCanvas = theCanvas

    def getCanvas(self):
        return self.__myCanvas

class Point(GeometricObject):
    def __init__(self, x, y):
        super().__init__()
        # position is now stored as tuple
        # first element is x coordinate and seconds is y
        # accessing x __pos[0]
        # accessing y __pos[1]
        self.__pos = (x,y)

    def getCoord(self):
        return (self.__pos[0], self.__pos[1])

    def setPos(self,x,y):
        self.__pos = (x, y)

    def getX(self):
        return self.__pos[0]

    def getY(self):
        return self.__pos[1]

    def _draw(self, turtle):
        turtle.goto(self.__pos[0], self.__pos[1])
       # turtle.dot(self.__lineWidth, self.__lineColor)
        turtle.dot(self.getWidth(), self.getColor())

class Line(GeometricObject):
    def __init__(self, p1, p2):
        super().__init__()
        self.__p1 = p1
        self.__p2 = p2

    def getP1(self):
        return self.__p1

    def getP2(self):
        return self.__p2

    def _draw(self, turtle):
        turtle.color(self.getColor())
        turtle.width(self.getWidth())
        turtle.up()
        turtle.goto(self.__p1.getCoord())
        turtle.down()
        turtle.goto(self.__p2.getCoord())






class Polygon(GeometricObject):
    """
    Polygon class that conects all points passed as list
    """
    def __init__(self, points:List[Point]):
        super().__init__()
        self.__points = points
    
    def _draw(self, turtle):
        turtle.color(self.getColor())
        turtle.width(self.getWidth())

        turtle.up()
        turtle.goto(self.__points[0].getCoord())
        turtle.down()

        for point in self.__points:
            turtle.goto(point.getCoord())
            
        turtle.goto(self.__points[0].getCoord())
        turtle.up()


class CenterPolygon(Polygon):
    """
    Specify center coordinate, number of points and radius
    """
    def __init__(self, center:Point, radius, n:int ):
        self.__r = radius
        self.__n = n
        self.__center = center
        self.__centerAngle = 360/n

        self.__points = []
        for n in range(self.__n):           # iterate trough all vertices
            self.__points.append(Point(     # add new point to the list
                # x coordinate of the point
                (math.sin(math.radians(self.__centerAngle*n))*self.__r + self.__center.getX()),
                # y coordinate of the point
                (math.cos(math.radians(self.__centerAngle*n))*self.__r + self.__center.getY())
                ))

        super().__init__(self.__points)


class Triangle(Polygon):
    """
    Triangle is same as polygon
    specify 3 points
    """
    def __init__(self, p1:Point, p2:Point, p3:Point):
        super().__init__([p1, p2, p3])


class Rectangle(Polygon):
    """
    Specify bottom left and top right points
    to draw a rectangle
    """
    def __init__(self, x0y0:Point, x1y1:Point):
        super().__init__(
            [
                x0y0,                               # bottom left
                Point(x0y0.getX(), x1y1.getY()),    # top left
                x1y1,                               # top right
                Point(x1y1.getX(), x0y0.getY())     # bottom right
            ]
        )

class Octagon(CenterPolygon):
    """ 
    Specify radius and center location
    it is the same center polygon only with specified
    number of vertices.  
    """
    def __init__(self, center: Point, radius):
        super().__init__(center, radius, 8)

def test():
    myCanvas = Canvas(1000, 1000)

    line1 = Line(Point(0, -500), Point(0, 500))
    line2 = Line(Point(-500, 0), Point(500, 0))

    myCanvas.draw(line1)
    myCanvas.draw(line2)


    triangle = Triangle(Point(-375, 125), Point(-375,375),Point(-125,125))

    rectangle = Rectangle(Point(50,100),Point(450,250))

    octagon = Octagon(Point(-250, -250), 100)

    randomRegularPoly = CenterPolygon(Point(250, -250), 100, random.randint(3, 7))
  
    myCanvas.draw(triangle)
    myCanvas.draw(rectangle)
    myCanvas.draw(octagon)
    myCanvas.draw(randomRegularPoly)

    myCanvas.freeze()


test()
