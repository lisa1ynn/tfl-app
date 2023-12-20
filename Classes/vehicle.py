import pygame
from pygame.sprite import Sprite
from classes.settings import Settings
import math


class Vehicle(Sprite):
    """A class to represent a single vehicle."""

    def __init__(self, image, rotation_angle, text):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(image), (80, 80)), rotation_angle)
        self.rect = self.image.get_rect()
        self.settings = Settings()
        self.rotation_angle = rotation_angle
        self.font = pygame.font.SysFont("Arial", 10)
        self.text = text

        self.rect.x = 0
        self.rect.y = 0

        # Store the vehicle's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def get_distance(self, from_station_x, from_station_y, to_station_x, to_station_y):
        if from_station_x > to_station_x and from_station_y > to_station_y:
            distance = math.sqrt(abs((from_station_y - to_station_y)**2) + abs((from_station_x - to_station_x)**2))
            return distance
        elif from_station_x < to_station_x and from_station_y < to_station_y:
            distance = math.sqrt(abs((to_station_y - from_station_y) ** 2) + abs((to_station_x - from_station_x) ** 2))
        elif from_station_x > to_station_x:
            distance = from_station_x - to_station_x
        elif from_station_x < to_station_x:
            distance = to_station_x - from_station_x
        elif from_station_y > to_station_y:
            distance = from_station_y - to_station_y
        elif from_station_y < to_station_y:
            distance = to_station_y - from_station_y
        return distance

    def calc_speed(self, from_station_x, from_station_y, to_station_x, to_station_y, time_to_station):
        speed = self.get_distance(from_station_x, from_station_y, to_station_x, to_station_y) / time_to_station
        return speed

    def update(self, from_station_x, from_station_y, to_station_x, to_station_y, time_to_station,
               direction_x=1, direction_y=0):
        """Move the vehicle."""
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # Move the vehicle based on updated directions
        self.x += (self.calc_speed(from_station_x, from_station_y, to_station_x, to_station_y, time_to_station)
                   * direction_x)
        self.y += (self.calc_speed(from_station_x, from_station_y, to_station_x, to_station_y, time_to_station)
                   * direction_x)
        self.rect.x = self.x
        self.rect.y = self.y

    def change_rotation_angle(self, rotation_angle):
        self.rotation_angle = rotation_angle
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load('images/tube1.bmp'), (80, 80)), rotation_angle)

    def blitme_text(self, screen):
        txtsurf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = txtsurf.get_rect()
        text_rect.centerx = self.rect.x + self.rect.width // 2
        text_rect.y = self.rect.y - text_rect.height
        screen.blit(txtsurf, text_rect)

# Subclasses for Bus and Train inheriting from Vehicle
class Bus(Vehicle):
    def __init__(self, rotation_angle, text):
        super().__init__(image='images/bus1_100.bmp', rotation_angle=rotation_angle, text=text)

class Tube(Vehicle):
    def __init__(self, rotation_angle, text):
        super().__init__(image='images/tube1.bmp', rotation_angle=rotation_angle, text=text)

