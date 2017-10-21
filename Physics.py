import numpy as np
from Forces import Forces 


def doTheThing():
    print("howdy")

    force1 = Forces()

    testMass = 23.0 #in kg

    gForce = force1.getGravitationalForce(testMass)

    print('A ' + str(testMass) + ' kg person on earth experiences a gravitational force of ' + str(gForce) + ' m/s^2')

    force1.setGravity(10.0)
    gForce = force1.getGravitationalForce(testMass)
    print('A ' + str(testMass) + ' kg person on earth experiences a gravitational force of ' + str(gForce) + ' m/s^2')

      
    tension = 45.0 #in N

    force1.setTensionForce(tension)
    result = force1.getTensionForce()

    print('The dog pulled with ' + str(result) + ' N of force')






doTheThing()
