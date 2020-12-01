from Asteroid_Obj import SCREEN_HEIGHT, SCREEN_WIDTH
import arcade
from abc import abstractmethod
from abc import ABC
import Point_Velocity

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Object(ABC): #- All travling objects share these same atrabutes:
    def __init__(self):
        self.center = Point_Velocity.Point()
        self.velocity = Point_Velocity.Velocity()
        self.create()

    @abstractmethod
    def create(self): #- Set dementions for the target to draw at a location:
        if self.center.y < 0:
            self.center.y = SCREEN_HEIGHT
        elif self.center.y > SCREEN_HEIGHT:
            self.center.y = 0
        elif self.center.x < 0:
            self.center.x = SCREEN_WIDTH
        elif self.center.x > SCREEN_HEIGHT:
            self.center.x = 0


    @abstractmethod
    def draw(self): #- Establish the physical properties:
        pass #- Place the rotation angle progression here

    def advance(self): #- Progress/move in a straight line:
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    