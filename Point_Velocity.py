import arcade, math
from abc import abstractmethod
from abc import ABC

INPUT_DATA = 0.0

class Point: #- Object Location
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

class Velocity: #- Object progression
    def __init__(self):
        self.dx = 0.0
        self.dy = 0.0
    
    #- This sets the accelaration of an object to 0.25 per iteration:
    @property
    def dy(self):
        return self._dy
    @dy.setter
    def dy(self, dy):
        if dy < 0.0:
            self._dy = 0.0
        elif dy < -0.25:
            self._dy += -0.25
        elif dy > 0.25:
            self._dy += 0.25
        else:
            self._dy = dy

    @property
    def dx(self):
        return self._dx
    @dx.setter
    def dx(self, dx):
        if dx < 0.0:
            self._dx = 0.0
        elif dx < -0.25:
            self._dx += -0.25
        elif dx > 0.25:
            self._dx += 0.25
        else:
            self._dx = dx
    
    """
    def display(self):
        print("move: {}".format(self.dy))
    """

"""
def main():
    move = Velocity()
    #move.dy
    move.display()
    move.dy = 5
    print()
    move.display()
    move.dy = 15
    move.display()


if __name__ == "__main__":
    main()
"""