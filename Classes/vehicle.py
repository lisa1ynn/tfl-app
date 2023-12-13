import pygame
from pygame.sprite import Sprite
from settings import Settings


class Vehicle(Sprite):
    """A class to represent a single vehicle."""

    def __init__(self, image, rotation_angle):
        super().__init__()
        self.image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(image), (80, 80)), rotation_angle)
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

    #def update(self, settings, start_station_time, end_station_time):
        # Update logic for movement or other behaviors
        """Move the vehicle."""
        #time_difference = (end_station_time - start_station_time).total_seconds()
        #speed = settings.screen_width / time_difference

        #if self.rect.x < settings.startstop2_x - self.rect.width:
            #elapsed_time = (pygame.time.get_ticks() - start_station_time) / 1000  # Convert to seconds
            #distance = speed * elapsed_time
            #self.rect.x = settings.startstop1_x + distance


# Subclasses for Bus and Train inheriting from Vehicle
class Bus(Vehicle):
    def __init__(self):
        super().__init__(image='images/bus1_100.bmp', rotation_angle=0)
        # Bus-specific attributes or behaviors can be added here


class Tube(Vehicle):
    def __init__(self):
        super().__init__(image='images/tube1.bmp', rotation_angle=180)
        # Tube-specific attributes or behaviors can be added here
