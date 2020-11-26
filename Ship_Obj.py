import arcade, math, random 
from abc import abstractmethod
from abc import ABC
import Object_Foundation #- Main Parent Module

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

class Ship(Object_Foundation.Object):
    """
    The ship is a rectangle that tracks the mouse.
    """
    def __init__(self):
        super().__init__()
        
        

    def create(self):
        self.alive = True
        self.center.x = 300
        self.center.y = 200
        self.velocity.dy = self.advance_up = []
        self.velocity.dy = self.advance_down = []
        self.velocity.dx = self.advance_right = []
        self.velocity.dx = self.advance_left = []
        self.angle = 90

        
    def draw(self):

        texture = arcade.load_texture("ship.png")
        
        arcade.draw_texture_rectangle(self.center.x, self.center.y, texture.width, texture.height, texture, 360 - self.angle)

    def death_event(self):
        self.alive = False