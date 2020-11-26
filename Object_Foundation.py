import arcade
from abc import abstractmethod
from abc import ABC
import Point_Velocity


class Object(ABC): #- All travling objects share these same atrabutes:
    def __init__(self):
        self.center = Point_Velocity.Point()
        self.velocity = Point_Velocity.Velocity()
        self.create()

    @abstractmethod
    def create(self): #- Set dementions for the target to draw at a location:
        pass

    @abstractmethod
    def draw(self): #- Establish the physical properties:
        pass #- Place the rotation angle progression here
    
    def advance(self): #- Progress/move in a straight line:
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    