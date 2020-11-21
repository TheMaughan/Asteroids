import arcade, math, random 
from abc import abstractmethod
from abc import ABC

class Point: #- Object Location
    def __init__(self):
        self.x = 0
        self.y = 0

class Velocity: #- Object progression
    def __init__(self):
        self.dx = 0
        self.dy = 0

class Angle:
    def __init__(self):
        self.degrees = 90

class Object(ABC): #- All travling objects share these same atrabutes:
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.angle = Angle()
        self.alive = True
        self.size = None
        self.create()

    @abstractmethod
    def create(self): #- Set dementions for the target to draw at a location:
        pass

    @abstractmethod
    def draw(self): #- Establish the physical properties:
        pass
    
    def advance(self): #- Progress/move in a straight line:
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    
    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT): #- If event where object leaves the window, kill the object:
        if (self.center.x < 0.0 or self.center.x > SCREEN_WIDTH):
            return True
        if (self.center.y < 0.0 or self.center.y > SCREEN_HEIGHT):
            return True
        return False

    