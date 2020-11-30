import arcade, math, random, arcade
from abc import abstractmethod
from abc import ABC

from arcade import texture
import Object_Foundation #- Main Parent Module

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

# Speed limit
MAX_SPEED = 3.0

# How fast we accelerate
ACCELERATION_RATE = 0.1

# How fast to slow down after we letr off the key
FRICTION = 0.02

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Ship(Object_Foundation.Object):
    """
    The ship is a rectangle that tracks the mouse.
    """
    def __init__(self):
        super().__init__()
        #self.sprite = arcade.load_texture("Ship.png")
        #self.x = 300
        #self.center_y = 200

    def create(self):
        self.center.x = 300
        self.center.y = 200
        self.velocity.dx = 0.0
        self.velocity.dy = 0.0
        self.alive = True        
        self.angle = 90

    def draw(self):

        self.sprite = arcade.load_texture("ship.png")
        
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.sprite.width, self.sprite.height, self.sprite, self.angle)

    def death_event(self):
        self.alive = False

    def display(self):
        print("Moved: {}".format(self.dy))


def main():
    thrust = Ship()
    thrust.dy
    thrust.display()

if __name__ == "__main__":
    main()