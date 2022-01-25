# Forth practical work
# 2021.12.29
# Andris Jenerts
# Group 1


import turtle


class Sun(turtle.Turtle):
    def __init__(self, iName):

        super().__init__(shape='circle')

        self.__name = iName
        self.shapesize(5, 5)
        self.color('yellow')

    def __str__(self):
        return self.__name

    def draw(self):
        sunTurtle = turtle.Turtle()
        sunTurtle.shape('circle')
        sunTurtle.shapesize(5, 5)
        sunTurtle.color('yellow')
