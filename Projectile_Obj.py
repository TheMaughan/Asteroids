import arcade, math, random
from abc import abstractmethod
from abc import ABC
import Object_Foundation #- Main Parent Module
import Ship_Obj


BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60


class Bullet(Object_Foundation.Object):
    def __init__(self):
        super().__init__()
        #- Call the ceation of the bullet:
        self.create()

    def draw(self): #- Draw Ball with radius of 10 px:
        self.sprite = arcade.load_texture("laser.png")
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.sprite.width / 2, self.sprite.height / 2, self.sprite, self.angle)

    #- Sets the angle of the bullet tragectory and initiates the creation of the bullet.
    def fire(self):
        self.create()
        self.alive = True
        self.velocity.dx = self.ship.velocity.dx
        self.velocity.dy = self.ship.velocity.dy
        #self.angle = math.degrees(math.atan2(self.velocity.dy, self.velocity.dx))
    
    #- Create the Bullet in the Rifle
    def create(self): #- Set the perameters for the bullet
        self.ship = Ship_Obj.Ship()
        self.center.x = self.ship.center.x
        self.center.y = self.ship.center.y
        self.angle = math.atan2(self.velocity.y, self.velocity.x)
        self.speed = BULLET_SPEED
        self.radius = BULLET_RADIUS
        self.alive = True
