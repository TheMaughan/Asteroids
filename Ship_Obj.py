import arcade, math
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
        
        self.max = 10
        self.drag = 1
        
    def create(self):
        self.alive = True
        self.speed = 0
        self.angle = 0
        self.center.x = 300
        self.center.y = 200
        self.velocity.dx = 0.0
        self.velocity.dy = 0.0

    
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
        self.speed += SHIP_THRUST_AMOUNT
        self.velocity.dx = (math.cos(math.radians(self.angle + 90)) * self.speed)
        self.velocity.dy = (math.sin(math.radians(self.angle + 90)) * self.speed)

    def move_backwards(self):
        self.speed -= SHIP_THRUST_AMOUNT
        self.center.x -= self.velocity.dx
        self.center.y -= self.velocity.dy
        self.velocity.dx = (math.cos(math.radians(self.angle - 90)) * -self.speed)
        self.velocity.dy = (math.sin(math.radians(self.angle - 90)) * -self.speed)

    def rotate_right(self):
        self.angle -= SHIP_TURN_AMOUNT

    def rotate_left(self):
        self.angle += SHIP_TURN_AMOUNT
    
    def death_event(self):
        self.alive = False

    @property
    def speed(self):
        return self._speed
    @speed.setter
    def speed(self, speed):
        if speed < 0:
            self._speed = 0
        elif speed > self.max:
            self._speed = self.max
        else:
            self._speed = speed
