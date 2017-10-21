
class Forces(object):
    import numpy as np


    """This is a class that will handle the forces.  It will have
        getters and setters.  It will also return the sumation of forces

        Attributes:
        gravity: A float representing the gravitational force of the planet
        tension: A float representing the tension in a massless/weightless rope

    """

    def __init__(self):
        self.gravity = (0 - 9.8) #initialized as earth's gravity in m/s^2
        self.tension = 0.0 #in N
        self.mass = 0.0 #in kg

    def getGravitationalForce(self):
        """Returns the gravitational force on an object"""
        #self.mass = mass
        return self.gravity*self.mass

    def setGravity(self, inGravity):
        """Sets the gravitational force of a planet"""
        self.gravity = inGravity

    def setMass(self, inMass):
        self.mass = inMass

    def getMass(self):
        return self.mass

    def setTensionForce(self, inTension):
        """Sets the tension force of a massless/weightless rope"""
        self.tension = inTension

    def getTensionForce(self):
        """Returns the tension force of a massless/weightless rope"""
        return self.tension

    def getSumofForcesX(self):
        """This is the function that will return acceleration of the sum
            of forces in x-axis"""
        x = 0.0 #in m/s^2
        
        return x

    def getSumOfForcesY(self):
        """This is the function that will return acceleration of the sum of
            forces in the y-axis"""
        ##For now I will only apply gravitational force
        y = self.getGravitationalForce()
        return y


