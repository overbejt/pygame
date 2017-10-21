import numpy as np
import Forces as force


def doTheThing():
    print("howdy")

    testMass = 23.0 #in kg

    gForce = force.getGravitationalForce(testMass)

    print('A ' + str(testMass) + ' kg person on earth experiences a gravitational force of ' + str(gForce) + ' m/s^2')
    







doTheThing()
