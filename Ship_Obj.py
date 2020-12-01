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
        self.speed = 0
        self.thrust = 0
        self.drag = 0.01

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

    def move_forward(self):
        if self.speed > 0:
            self.speed -= self.drag
            if self.speed < 0:
                self.speed = 0
        if self.speed < 0:
            self.speed += self.drag
            if self.speed > 0:
                self.speed = 0
        
        self.speed += self.thrust


    def advance(self):

        self.velocity.dx = -math.sin(math.radians(self.angle)) * self.speed
        self.velocity.dy = math.cos(math.radians(self.angle)) * self.speed


    def death_event(self):
        self.alive = False

    def display(self):
        print("Moved: {}".format(self.velocity.dy))

"""
def main():
    thrust = Ship()
    thrust.velocity.dy = 1
    thrust.velocity.dy = 1
    thrust.display()
    thrust.velocity.dy = -1
    thrust.display()

if __name__ == "__main__":
    main()
"""