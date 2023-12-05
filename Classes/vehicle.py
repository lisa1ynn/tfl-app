import pygame
from pygame.sprite import Sprite
from settings import Settings


class Vehicle(Sprite):
    """A class to represent a single vehicle."""

    def __init__(self, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.settings = Settings()

        self.rect.x = 0
        self.rect.y = 0

        # Store the vehicle's exact horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self, direction_x=1, direction_y=0):
        # direction of 1 represents right and down; -1 represents left and up; 0 means no movement.
        # Update logic for movement or other behaviors
        """Move the vehicle."""
        self.x = self.rect.x
        self.y = self.rect.y
        self.x += (self.settings.vehicle_speed * direction_x)
        self.y += (self.settings.vehicle_speed * direction_y)
        self.rect.x = self.x
        self.rect.y = self.y
        pass


# Subclasses for Bus and Train inheriting from Vehicle
class Bus(Vehicle):
    def __init__(self):
        super().__init__('images/bus1_100.bmp')
        # Bus-specific attributes or behaviors can be added here


class Tube(Vehicle):
    def __init__(self):
        super().__init__('images/tube1.bmp')
        # Tube-specific attributes or behaviors can be added here

