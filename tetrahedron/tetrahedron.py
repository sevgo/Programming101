import math


class Tetrahedron(object):
    """A tetrahedron class that has just an init and volume method
       for now
    """

    def __init__(self, side):
        self.side = side

    def tetrahedron_fill(self):
        """A method that calculate the volume of the regular
        tetrahedron. It uses the following formula:
        V = (math.pow(a,3) * sqrt(2)) / 12) / 1000
        and returns the volume in liters
        """
        side = self.side
        return ((math.pow(side, 3) * math.sqrt(2)) / 12) / 1000
