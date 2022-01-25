# Forth practical work
# 2021.12.29
# Andris Jenerts
# Group 1


import turtle
from object import Object
from sun import Sun
import time


class SolarSystem:
    def __init__(self, aSun: Sun):
        """
        Parameters
        ----------
        aSun : Sun
            Sun object for this solar system
        """

        self.__theSun = aSun
        self.__planets = []
        self.__objects = []

        # solar system is our screen
        # draw a black screen with fixed sized
        # tracer is used so that screen is updated only
        # after update method is called
        self._screen = turtle.Screen()
        self._screen.setup(1000, 600)
        self._screen.bgcolor('black')
        self._screen.tracer(0)

    def getPlanet(self, name):
        for aPlanet in self.__planets:
            if(aPlanet.__str__() == name):
                return aPlanet
        return self.__theSun

    def addPlanet(self, aPlanet: Object):
        """Adds planet to the solar system

        Parameters
        ----------
        aPlanet : Object
            Planet object to add
        """

        self.__planets.append(aPlanet)

    def addObject(self, aObject: Object):
        """Adds object to the solar system

        Parameters
        ----------
        aPlanet : Object
            Object object to add
        """

        self.__objects.append(aObject)

    def showPlanets(self):
        for aPlanet in self.__planets:
            print(aPlanet)

    def printSystemPlanets(self):
        """Prints all planet in the solar system
        from furthest to closes to the Sun.
        At the end prints name of the Sun.
        """

        if not self.__planets:
            print("Solar system has no planets")

        # create new list with all planets
        planetList = self.__planets.copy()

        # function that returns key for sorting
        # see python doc: https://docs.python.org/3/library/stdtypes.html#list.sort
        def getSortingKey(obj: Object):
            return obj.getDistance()

        # sort our local list
        planetList.sort(reverse=True, key=getSortingKey)

        # for debugging
        # for aPlanet in planetList:
        #     print(str(aPlanet) + ": " + str(aPlanet.getDistance()))

        # start by printing list
        for aPlanet in planetList:
            print(aPlanet)

        # print name of the sun
        print(self.__theSun)

    def simulate(self):
        while True:
            for aPlanet in self.__planets:
                aPlanet.move()
                aPlanet.increaseAngle()
            for aObject in self.__objects:
                aObject.move()
                aObject.increaseAngle()

            time.sleep(0.01)

            self._screen.update()
