import arcade, math, random
import Object_Foundation
from Object_Foundation import Object #- Main Parent Module
from abc import abstractmethod
from abc import ABC
 
# These are Global constants to use throughout the game
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2


class A_Foundation(Object, ABC): #- Sets the design for the Asteroid template
    def __init__(self): #- Set perameters
        super().__init__()
    
    @abstractmethod
    def draw(self): #- Draw
        pass

    def rotate(self): #- Rotate
        pass

    @abstractmethod
    def hit(self): #- Kill or React at event:
        pass

    @abstractmethod
    def create(self): #- Create at location based on random generator perameters:
        pass


class Rock_Lrg(A_Foundation):
    def __init__(self):
        super().__init__()
        

    #- Set dementions for the target to draw:
    def draw(self):
        # This will load the graphics file into an arcade texture object
        texture = arcade.load_texture("large.png")
        self.angle += 5
        
        # This will draw the texture object.  The first 2 parameters describe where the
        # object should be drawn.  The next 2 parameters describe the width and height of
        # the object.  In this program, we want to draw the actual size of the picture.
        # We can do this by using the width and height member data in the texture object.
        # The next parameter specifies the texture object we are drawing.  Since we have to
        # rotate the object during game play, we will specify an additional rotation parameter.
        arcade.draw_texture_rectangle(self.center.x, self.center.y, texture.width, texture.height, texture, self.angle)
        

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
        self.Object_Foundation.alive = True
        self.Object_Foundation.center.x = 400
        self.Object_Foundation.center.y = 300
        self.Object_Foundation.velocity.dx = 1.5 #- Manipulate speed of rock here
        self.Object_Foundation.velocity.dy = 1.5


"""
class Rock_Med(A_Foundation):
    def __init__(self):
        super().__init__()

    #- Set dementions for the target to draw:
    def draw(self):
        # This will load the graphics file into an arcade texture object
        texture = arcade.load_texture("medium.png")
        self.angle += 5
        
        # This will draw the texture object.  The first 2 parameters describe where the
        # object should be drawn.  The next 2 parameters describe the width and height of
        # the object.  In this program, we want to draw the actual size of the picture.
        # We can do this by using the width and height member data in the texture object.
        # The next parameter specifies the texture object we are drawing.  Since we have to
        # rotate the object during game play, we will specify an additional rotation parameter.
        arcade.draw_texture_rectangle(self.center.x, self.center.y, texture.width, texture.height, texture, self.angle)

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


class Rock_Sml(A_Foundation):
    def __init__(self):
        super().__init__()
        self.angle = 0
    #- Set dementions for the Safe_Target to draw:
    
    def draw(self):
        # This will load the graphics file into an arcade texture object
        texture = arcade.load_texture("small.png")
        self.angle += 5
        
        # This will draw the texture object.  The first 2 parameters describe where the
        # object should be drawn.  The next 2 parameters describe the width and height of
        # the object.  In this program, we want to draw the actual size of the picture.
        # We can do this by using the width and height member data in the texture object.
        # The next parameter specifies the texture object we are drawing.  Since we have to
        # rotate the object during game play, we will specify an additional rotation parameter.
        arcade.draw_texture_rectangle(self.center.x, self.center.y, texture.width, texture.height, texture, self.angle)

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