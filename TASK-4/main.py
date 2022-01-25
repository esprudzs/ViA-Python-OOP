# Forth practical work
# 2021.12.29
# Andris Jenerts
# Group 1

# import classes from local project folder
from sun import Sun
from object import Object
from solarsystem import SolarSystem


sun = Sun("Sun")  # create sun
ss = SolarSystem(sun)  # cerate solar system of our sun

planet = Object("Mercury", 0.15, 75, 0.5, "blue", sun)
ss.addPlanet(planet)

planet = Object("Earth", 1, 150, 1, "red", sun)
ss.addPlanet(planet)

planet = Object("Mars", 0.5,  200, 1.5, "white", sun)
ss.addPlanet(planet)

planet = Object("Jupiter", 2, 250, 2, "green", sun)

ss.addPlanet(planet)

moon = Object("Moon", 0.25, 30, (1 / 10), "green", ss.getPlanet("Earth"))
ss.addObject(moon)


ss.printSystemPlanets()
ss.simulate()
