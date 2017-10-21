
class Forces(object):
    import numpy as np


    """This is a class that will handle the forces.  It will have
        getters and setters.  It will also return the sumation of forces

        Attributes:
        gravity: A float representing the gravitational force of the planet
        tension: A float representing the tension in a massless/weightless rope

    """

    def __init__(self):
        self.gravity = 9.8 #initialized as earth's gravity in m/s^2
        self.tension = 0.0 #in N

    def getGravitationalForce(self, mass):
        """Returns the gravitational force on an object"""
        return self.gravity*mass

    def setGravity(self, inGravity):
        """Sets the gravitational force of a planet"""
        self.gravity = inGravity

    def setTensionForce(self, inTension):
        """Sets the tension force of a massless/weightless rope"""
        self.tension = inTension

    def getTensionForce(self):
        """Returns the tension force of a massless/weightless rope"""
        return self.tension


