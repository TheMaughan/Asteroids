import arcade
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
