import arcade, math, random 
from abc import abstractmethod
from abc import ABC
import Object_Foundation #- Main Parent Module


class Ship:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):
        self.center = Object_Foundation.Point
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, 360 - self.angle)
