import pygame
from pygame.sprite import Sprite
from classes.settings import Settings


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

    def update(self, settings, direction_x=1, direction_y=0):
        """Move the vehicle."""
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        '''for group_name, group_data in settings.tube_groups_dict.items():
            if group_name == "central_east" and self.x <= group_data['second_station_x']:
                group_data['direction_x'] = 1
                group_data['direction_y'] = 1
            elif group_name == "central_west" and self.x >= group_data['second_station_x']:
                group_data['direction_x'] = 1
                group_data['direction_y'] = 0'''

        # Move the vehicle based on updated directions
        self.x += (self.settings.vehicle_speed * direction_x)
        self.y += (self.settings.vehicle_speed * direction_y)
        self.rect.x = self.x
        self.rect.y = self.y



# Subclasses for Bus and Train inheriting from Vehicle
class Bus(Vehicle):
    def __init__(self, rotation_angle):
        super().__init__(image='images/bus1_100.bmp', rotation_angle=rotation_angle)

class Tube(Vehicle):
    def __init__(self, rotation_angle):
        super().__init__(image='images/tube1.bmp', rotation_angle=rotation_angle)


