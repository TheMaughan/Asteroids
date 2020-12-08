"""
File: asteroids.py
Original Author: Br. Burton
Co-Author: Bryce Maughan

This program implements a version of the asteroids game.
"""
import arcade
import Asteroid_Obj
import Ship_Obj
import Projectile_Obj

# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2

 
#import Object_Foundation
#from Object_Foundation import *
#from Asteroid_Obj import Rock_Lrg

#import Ship_Obj
#import Projectile_Obj


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
        
        self.bullets = []
        self.ship = Ship_Obj.Ship()
        self.rocks = []
        for i in range(5):
            self.create_asteroids()
        
        # TODO: declare anything here you need the game class to track

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """
        
        # clear the screen to begin drawing
        arcade.start_render()

        for rock in self.rocks:
            rock.draw()
        
        for bullet in self.bullets:
            bullet.draw()

        self.ship.draw()

        # TODO: draw each object

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """

        self.check_keys()
        self.ship.advance()
        self.cleanup_zombies()
        #self.ship.move()

        for rock in self.rocks:
            rock.advance()
            rock.rotate()

        for bullet in self.bullets:
            bullet.advance()
            bullet.set_life()


        # TODO: Tell everything to advance or move forward one step in time

        # TODO: Check for collisions

    def cleanup_zombies(self):
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)


    def create_asteroids(self):
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
            self.ship.rotate_left()
            
        if arcade.key.RIGHT in self.held_keys:
            self.ship.rotate_right()
            
        if arcade.key.UP in self.held_keys:
            self.ship.move_forward()
            
        if arcade.key.DOWN in self.held_keys:
            self.ship.move_backwards()
            
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
            #self.ship.move()
            
            if key == arcade.key.SPACE:
                bullet = Projectile_Obj.Bullet()
                bullet.fire(self.ship.center.x, self.ship.center.y, self.ship.angle)
                self.bullets.append(bullet)
                # TODO: Fire the bullet here!
                

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()