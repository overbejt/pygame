import numpy as np
from Forces import Forces

class Physics(object):
    """This is the class that will act as the physics engine for the game.
        It will wrap all of the physics classes into one.

        Attributes:
        force: A Forces object that will perform the logic for forces
    """

    def __init__(self):
        self.force = Forces()


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


    def getMotion():
        """This is the function that will get the sum of forces and calculate the
            motion of the object"""

        
        self.force.setMass(25)
        
        motion = self.force.getSumofForces()
        
        return (motion)



    ##doTheThing()


