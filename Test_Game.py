"""
File: asteroids.py
Original Author: Br. Burton
Co-Author: Bryce Maughan

This program implements a version of the asteroids game.
"""
import arcade, math, random
from abc import abstractmethod
from abc import ABC
import Object_Foundation
import Asteroid_Obj
import Ship_Obj
from Ship_Obj import Ship

# These are Global constants to use throughout the game:
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

#---------------------------------Ship:
SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

# Speed limit
MAX_SPEED = 3.0

# How fast we accelerate
ACCELERATION_RATE = 0.1

# How fast to slow down after we letr off the key
FRICTION = 0.02

#--------------------------------Asteroid:
INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2

 
class Ship(Object_Foundation.Object):
    """
    The ship is a rectangle that tracks the mouse.
    """
    def __init__(self, val):
        super().__init__()
        #self.sprite = arcade.load_texture("Ship.png")
        #self.x = 300
        #self.center_y = 200
        self.dx = self.velocity.dx
        self.dy = self.velocity.dy

    def create(self):
        self.center.x = 300
        self.center.y = 200
        self.velocity.dy = 0.0
        self.velocity.dx = 0.0
        self.alive = True
        
        self.dx = self.velocity.dx
        
        self.dy = self.velocity.dy
        
        self.angle = 90

    @property
    def move_up(self):
        return self._dy
    
    
    def move_up(self, val):
        #val += SHIP_THRUST_AMOUNT

        if val < 0.0:
            self._dy = 0.0
            
        elif val > 3.0:
            self._dy = 3.0
        else:
            self._dy = val
        
    @property
    def move_down(self):
        return self.dy
    @move_down.setter
    def move_down(self, val):
        if val < -5:
            self.dy = 0.0
            
        elif val > 3.0:
            self.dy = 3.0
        else:
            self.dy = val       
    
    @property
    def move_left(self):
        return self.dx
    @move_left.setter
    def move_left(self, val):
        if val < -5:
            self.dy = 0.0
            
        elif val > 3.0:
            self.dy = 3.0
        else:
            self.dy = val

    @property
    def move_right(self):
        return self.dx
    @move_right.setter
    def move_right(self, val):
        if val < -5:
            self.dy = 0.0
            
        elif val > 3.0:
            self.dy = 3.0
        else:
            self.dy = val


    def draw(self):

        self.sprite = arcade.load_texture("ship.png")
        
        arcade.draw_texture_rectangle(self.center.x, self.center.y, self.sprite.width, self.sprite.height, self.sprite, 360 - self.angle)

    def death_event(self):
        self.alive = False

class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction

    This class will then call the appropriate functions of
    each of the above classes.

    You are welcome to modify anything in this class.
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        
        self.held_keys = set()

        self.ship = Ship_Obj.Ship(0.25)

        self.rocks = []
        self.create_asteroids()

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False

        # TODO: declare anything here you need the game class to track

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """
        
        # clear the screen to begin drawing
        arcade.start_render()

        #self.rock.draw()

        for rock in self.rocks:
            rock.draw()

        self.ship.draw()

        # TODO: draw each object

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        self.check_keys()

        self.ship.advance()

        for rock in self.rocks:
            rock.advance()


        # TODO: Tell everything to advance or move forward one step in time

        # TODO: Check for collisions

    def create_asteroids(self):
        #import Asteroid_Obj
        lrg = Asteroid_Obj.Rock_Lrg()
        #med = Asteroid_Obj.Rock_Med()
        #sml = Asteroid_Obj.Rock_Sml()

        lrg.create()
        #med.Asteroid_Obj.create
        #sml.Asteroid_Obj.create

        self.rocks.append(lrg)
        #self.asteroids.append(med)
        #self.asteroids.append(sml)

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        
        if arcade.key.LEFT in self.held_keys:
            self.ship.move_left
            
        if arcade.key.RIGHT in self.held_keys:
            self.ship.move_right
            
        if arcade.key.UP in self.held_keys:
            self.ship.dy
            
        if arcade.key.DOWN in self.held_keys:
            self.ship.move_down
            
        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                # TODO: Fire the bullet here!
                pass

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()