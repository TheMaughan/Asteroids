import arcade, math, random 
from abc import abstractmethod
from abc import ABC
import Object_Foundation #- Main Parent Module




class Bullet(Place_Obj):
    def __init__(self):
        super().__init__()
        #- Call the ceation of the bullet:
        self.create()

    def draw(self): #- Draw Ball with radius of 10 px:
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color)

    #- Sets the angle of the bullet tragectory and initiates the creation of the bullet.
    def fire(self, angle: float):
        self.alive = True
        self.velocity.dx = math.cos(math.radians(angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(angle)) * self.speed
    
    #- Create the Bullet in the Rifle
    def create(self): #- Set the perameters for the bullet
        self.center.x = 0
        self.center.y = 0
        self.speed = BULLET_SPEED
        self.radius = BULLET_RADIUS
        self.color = arcade.color.BLACK
        self.alive = True
