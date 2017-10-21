import numpy as np

gravity = 9.8 #initialized as earth's gravity in m/s^2

def getGravitationalForce(mass):
    return gravity*mass

def setGravitation(inGravity):
    gravity = inGravity
