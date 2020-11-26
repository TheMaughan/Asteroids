import arcade, math, random 
from abc import abstractmethod
from abc import ABC
import Object_Foundation #- Main Parent Module

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Ship(Object_Foundation.Object):
    """
    The ship is a rectangle that tracks the mouse.
    """
    def __init__(self):
        super().__init__()
        self.sprite = arcade.load_texture("Ship.png")

    def create(self):
        self.alive = True
        self.center.x = 300
        self.center.y = 200
        self.velocity.dy = 0.0
        self.velocity.dx = 0.0
        self.angle = 90

    @property
    def move_up(self):
        return self.center.y
    @move_up.setter
    def move_up(self):
        if self.center.y < SCREEN_HEIGHT + 5:
            self.center.y += 0.25
    @property
    def move_down(self):
        return self.center.y
    @move_down.setter
    def move_down(self):
        if self.center.y > -5:
            self.center.y -= 0.25
    
    @property
    def move_left(self):
        return self.center.x
    @move_left.setter
    def move_left(self):
        if self.center.x > -5:
            self.center.x -= 0.25

    @property
    def move_right(self):
        return self.center.x
    @move_right.setter
    def move_right(self):
        if self.center.x < SCREEN_WIDTH + 5:
            self.center.x += 0.25


    def draw(self):

        self.sprite = arcade.load_texture("ship.png")
        
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.sprite.width, self.sprite.height, self.sprite, 360 - self.angle)

    def death_event(self):
        self.alive = False