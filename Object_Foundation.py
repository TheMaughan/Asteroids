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
        self.max = self.velocity.max
        self.create()

    @abstractmethod
    def create(self):
        pass
   

    @abstractmethod
    def draw(self): #- Establish the physical properties:
        pass #- Place the rotation angle progression here

    def advance(self): #- Progress/move in a straight line:
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    