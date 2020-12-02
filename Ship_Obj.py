import arcade, math, arcade
from abc import abstractmethod
from abc import ABC
import Object_Foundation #- Main Parent Module
import Point_Velocity

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

SCALE = 0.5

# Speed limit
MAX_SPEED = 30

# How fast we accelerate
ACCELERATION_RATE = 0.01

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
        #self.center = Point_Velocity.Point(MAX_SPEED)
        self.max = 10
        self.velocity = Point_Velocity.Velocity()
    def create(self):
        self.alive = True
        self.speed = 0
        self.angle = math.degrees(math.atan2(self.center.y, self.center.x))
        self.center.x = 300
        self.center.y = 200
        self.velocity.dx = -math.sin(math.radians(self.angle)) * self.speed
        self.velocity.dy = math.cos(math.radians(self.angle)) * self.speed

    def advance(self):
        #(math.radians(self.angle))
        self.center.x += -self.speed * math.sin((math.radians(self.angle)))
        self.center.y += self.speed * math.cos((math.radians(self.angle)))
   
    def draw(self):
        self.sprite = arcade.load_texture("ship.png")
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.sprite.width / 2, self.sprite.height / 2, self.sprite, self.angle)

        if self.center.y < 0:
            self.center.y = SCREEN_HEIGHT
        if self.center.y > SCREEN_HEIGHT:
            self.center.y = 0
        if self.center.x < 0:
            self.center.x = SCREEN_WIDTH
        if self.center.x > SCREEN_WIDTH:
            self.center.x = 0

    def move_forward(self):
        self.speed += 0.25

    def move_backwards(self):
        self.speed -= 0.25

    def rotate_right(self):
        self.angle -= 3

    def rotate_left(self):
        self.angle += 3

    def death_event(self):
        self.alive = False