"""
File: asteroids.py
Original Author: Br. Burton
Co-Author: Bryce Maughan

This program implements a version of the asteroids game.
"""
import arcade
import math
import random
from abc import abstractmethod
from abc import ABC

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


class Point: #- Object Location
    def __init__(self):
        self.x = 0
        self.y = 0

class Velocity: #- Object progression
    def __init__(self):
        self.dx = 0
        self.dy = 0

class Place_Obj(ABC): #- All travling objects share these same atrabutes:
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.alive = True
        self.size = None
        self.create()

    @abstractmethod
    def draw(self): #- Draw the physical properties:
        pass

    def advance(self): #- Progress/move in a straight line:
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy

    
    def is_off_screen(self, SCREEN_WIDTH, SCREEN_HEIGHT): #- If event where object leaves the window, kill the object:
        if (self.center.x < 0.0 or self.center.x > SCREEN_WIDTH):
            return True
        if (self.center.y < 0.0 or self.center.y > SCREEN_HEIGHT):
            return True
        return False

    @abstractmethod
    def create(self): #- Set dementions for the target to draw at a location:
        pass

class Asteroids(Place_Obj, ABC): #- Sets the design for the Asteroid template
    def __init__(self): #- Set perameters
        super().__init__()
        self.size = None
        self.angle = 0
    @abstractmethod
    def draw(self): #- Draw
        pass

    def rotate(self):
        pass

    @abstractmethod
    def hit(self): #- Kill on event
        pass
    @abstractmethod
    def create(self): #- Create at location based on random generator perameters:
        pass

class Asteroid_Sml(Target):
    def __init__(self):
        super().__init__()
        self.angle = 0
    #- Set dementions for the Safe_Target to draw:
    def draw(self):
        # This will load the graphics file into an arcade texture object
		texture = arcade.load_texture("small.png")
        	
		# This will draw the texture object.  The first 2 parameters describe where the
		# object should be drawn.  The next 2 parameters describe the width and height of
		# the object.  In this program, we want to draw the actual size of the picture.
		# We can do this by using the width and height member data in the texture object.
		# The next parameter specifies the texture object we are drawing.  Since we have to
		# rotate the object during game play, we will specify an additional rotation parameter.
		arcade.draw_texture_rectangle(self.center.x, self.center.y, texture.width, texture.height, texture, self.angle)

    def rotate(self):
        self.angle += 5
        

    #- Kill the target on collision event.
    def hit(self):
        self.alive = False
        return 1
    
    #- Set dementions for the target to draw at a location.
    def create(self):
        self.center.x = SCREEN_WIDTH - self.radius
        self.center.y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT)
        self.velocity.dx = random.uniform(-1, -5) #- Manipulate speed of ball here (min speed, max speed)
        self.velocity.dy = random.uniform(-2, 5)
        self.angle += 1

"""
class Asteroid_Med(Target):
    def __init__(self):
        super().__init__()

    #- Set dementions for the target to draw:
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius / 2, arcade.color.GREEN)

    #- Kills target on collision event:
    def hit(self):
        self.alive = False
        return -10
    
    #- Set dementions for the target to draw at a location.
    def create(self):
        self.center.x = self.radius
        self.center.y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT)
        self.velocity.dx = random.uniform(1, 5) #- Manipulate speed of ball here (min speed, max speed)
        self.velocity.dy = random.uniform(-2, 5)

class Asteroid_Lrg(Target):
    def __init__(self):
        super().__init__()
        self.red = arcade.color.RASPBERRY
        self.purple = arcade.color.PURPLE_MOUNTAIN_MAJESTY
        self.orange = arcade.color.ORANGE_PEEL
        self.black = arcade.color.BLACK_OLIVE
        self.color_list = [self.red, self.purple, self.orange, self.black]

    #- Set dementions for the target to draw:
    def draw(self):
        
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color_list[self.animate()])
        #self.script.append(color_list)
        #return self.script
        

    #- Kill target on collision event:
    def hit(self):
        score = 0

        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, arcade.color.RED)

        self.radius -= 10

        if self.radius == 20:
            score += 1
        elif self.radius == 10:
            score += 1
        elif self.radius <= 0:
            score += 5
            self.alive = False

        return score
        
    #- Set dementions for the target to draw at a location:
    def create(self):
        self.alive = True
        self.center.x = SCREEN_WIDTH - self.radius
        self.center.y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT)
        self.velocity.dx = random.uniform(-1, -3) #- Manipulate speed of ball here (min speed, max speed)
        self.velocity.dy = random.uniform(-2, 3)

    def animate(self):
        pointer = 0
        for color in self.color_list:
            if pointer >= 4:
                pointer -= 1
            elif pointer <=  0:
                pointer += 1
        return pointer

class Bullet(Place_Obj):
    def __init__(self):
        super().__init__()
        #- Call the ceation of the bullet:
        self.create()

    def draw(self): #- Draw Ball with radius of 10 px:
        arcade.draw_circle_filled(self.center.x, self.center.y, self.radius, self.color)

    #- Sets the angle of the bullet tragectory and initiates the creation of the bullet.
    def fire(self, angle: float):
        self.alive = True
        self.velocity.dx = math.cos(math.radians(angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(angle)) * self.speed
    
    #- Create the Bullet in the Rifle
    def create(self): #- Set the perameters for the bullet
        self.center.x = 0
        self.center.y = 0
        self.speed = BULLET_SPEED
        self.radius = BULLET_RADIUS
        self.color = arcade.color.BLACK
        self.alive = True
"""

class Ship:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

        self.angle = 45

    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, 360 - self.angle)


 
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

        self.asteroids = Asteroids()

        self.held_keys = set()

        self.asteroids = []

        # TODO: declare anything here you need the game class to track

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        # clear the screen to begin drawing
        arcade.start_render()

        # TODO: draw each object

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()

        for A in self.asteroid:
            asteroid.advance
            asteroid.rotate


        # TODO: Tell everything to advance or move forward one step in time

        # TODO: Check for collisions

    def create_asteroids(self):
        small = Asteroid_Sml()

        small.create()

        self.asteroids.append(small)

    def check_keys(self):
        """
        This function checks for keys that are being held down.
        You will need to put your own method calls in here.
        """
        if arcade.key.LEFT in self.held_keys:
            pass

        if arcade.key.RIGHT in self.held_keys:
            pass

        if arcade.key.UP in self.held_keys:
            pass

        if arcade.key.DOWN in self.held_keys:
            pass

        # Machine gun mode...
        #if arcade.key.SPACE in self.held_keys:
        #    pass


    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        You will need to add things here to handle firing the bullet.
        """
        if self.ship.alive:
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