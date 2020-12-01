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
    def create(self):
        self.advance()
        self.center.x = 300
        self.center.y = 200
        self.alive = True
    def advance(self):
        self.angle = math.degrees(math.atan2(self.velocity.dy, self.velocity.dx))
        self.speed = 0
        self.reverse = 0
        self.forward = 0
        self.dy = self.velocity.dy
        self.dx = self.velocity.dx
        self.dx = -math.sin(math.radians(self.angle)) * self.center.x
        self.dy = math.cos(math.radians(self.angle)) * self.center.y
    """
    #- This sets the accelaration of an object to 0.25 per iteration:
    @property
    def dy(self):
        return self._dy
    @dy.setter
    def dy(self, dy):
        if dy == 0.0:
            self._dy = 0.0
        elif dy > 0.25:
            self._dy += 0.25
        elif dy < -0.25:
            self._dy += -0.25
        else:
            self._dy = dy
    """
    def draw(self):
        self.sprite = arcade.load_texture("ship.png")
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.sprite.width, self.sprite.height, self.sprite, self.angle)

        if self.center.y < 0:
            self.center.y = SCREEN_HEIGHT
        if self.center.y > SCREEN_HEIGHT:
            self.center.y = 0
        if self.center.x < 0:
            self.center.x = SCREEN_WIDTH
        if self.center.x > SCREEN_WIDTH:
            self.center.x = 0

    def move_forward(self):
        self.velocity.dy += 0.25

    def move_backwards(self):
        self.velocity.dy -= 0.25

    def rotate_right(self):
        self.velocity.dy += 0.25

    def rotate_left(self):
        self.velocity.dy -= 0.25

    def death_event(self):
        self.alive = False

    def display(self):
        print("Moved: {}".format(self.dy))


def main():
    thrust = Ship()
    thrust.dy = 1
    thrust.dy = 1
    thrust.display()
    thrust.dy = -1
    thrust.display()
    thrust.dy = -2
    thrust.display()
    thrust.dy = 39
    thrust.display()

if __name__ == "__main__":
    main()
