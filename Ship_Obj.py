import arcade, math, random, arcade
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
        #self.sprite = arcade.load_texture("Ship.png")
        #self.x = 300
        #self.center_y = 200
        self.dx = self.velocity.dx
        self.dy = self.velocity.dy

    def create(self):
        self.center.x = 300
        self.center.y = 200
        self.velocity.dx = 0.0
        self.velocity.dy = 0.0
        self.alive = True
        
        self.dx = self.velocity.dx
        
        self.dy = self.velocity.dy
        
        self.angle = 90

    @property
    def move_y(self):
        return self._dy
    
    @move_y.setter
    def move_y(self, val):

        if val < 0.0:
            self._dy = 0.0
            
        elif val > 3.0:
            self._dy = 3.0
        else:
            self._dy = val
    
    @property
    def move_x(self):
        return self._dx
        
    @move_x.setter
    def move_x(self, val):
        if val < 0.0:
            self._dx = 0.0
            
        elif val > 3.0:
            self._dx = 3.0
        else:
            self._dx = val


    def draw(self):

        self.sprite = arcade.load_texture("ship.png")
        
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.sprite.width, self.sprite.height, self.sprite, 360 - self.angle)

    def death_event(self):
        self.alive = False


def main():
    thrust = Ship(SHIP_THRUST_AMOUNT)
    print(thrust.dy)

if __name__ == "__main__":
    main()