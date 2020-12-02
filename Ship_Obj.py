import arcade, math, arcade
from abc import abstractmethod
from abc import ABC
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
        #self.center = Point_Velocity.Point(MAX_SPEED)
        self.max = 10
        self.velocity = Point_Velocity.Velocity()
    def create(self):
        self.alive = True
        self.speed = 0
        self.angle = math.degrees(math.atan2(self.center.y, self.center.x))
        self.center.x = 300
        self.center.y = 200
        self.velocity.dx = -math.sin(self.angle) * self.speed
        self.velocity.dy = math.cos(self.angle) * self.speed
        
        #self.change_x += -math.sin(self.radians) * speed
        #self.change_y += math.cos(self.radians) * speed

    def advance(self):
        #(math.radians(self.angle)) * math.sin((math.radians(self.angle)))
        self.center.x += -self.speed
        self.center.y += self.speed
    """
    def rotate_point(x: float, y: float, cx: float, cy: float,
                 angle_degrees: float) -> List[float]:
    """
    """
    Rotate a point around a center.

    :param x: x value of the point you want to rotate
    :param y: y value of the point you want to rotate
    :param cx: x value of the center point you want to rotate around
    :param cy: y value of the center point you want to rotate around
    :param angle_degrees: Angle, in degrees, to rotate
    :return: Return rotated (x, y) pair
    :rtype: (float, float)
    """
    """
    temp_x = x - cx
    temp_y = y - cy

    # now apply rotation
    angle_radians = math.radians(angle_degrees)
    cos_angle = math.cos(angle_radians)
    sin_angle = math.sin(angle_radians)
    rotated_x = temp_x * cos_angle - temp_y * sin_angle
    rotated_y = temp_x * sin_angle + temp_y * cos_angle

    # translate back
    rounding_precision = 2
    x = round(rotated_x + cx, rounding_precision)
    y = round(rotated_y + cy, rounding_precision)

    return [x, y]
    """
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
        self.speed += 0.25

    def move_backwards(self):
        self.speed -= 0.25

    def rotate_right(self):
        self.angle -= 3

    def rotate_left(self):
        self.angle += 3

    def death_event(self):
        self.alive = False