import pygame
from classes.settings import Settings
from functions import app_functions as af, vehicle_functions as vf


class TflApp:
    """Overall class to manage app assets and behavior."""

    def __init__(self):
        """Initialize the app, and create app resources."""
        pygame.init()
        pygame.display.set_caption("Tfl App")
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bus_dict_items = self.settings.bus_groups_dict.items()
        self.tube_dict_items = self.settings.tube_groups_dict.items()

        # Bus Sprite Groups
        self.bus_sprite_groups = {}
        self.tube_sprite_groups = {}

        for group_name, group_data in self.bus_dict_items:
            self.bus_sprite_groups[group_name] = pygame.sprite.Group()

        for group_name, group_data in self.tube_dict_items:
            self.tube_sprite_groups[group_name] = pygame.sprite.Group()

        vf.create_vehicle(self.settings, self.bus_sprite_groups, self.tube_sprite_groups)


    def _run_game(self):
        """Start the main loop for the app."""
        while True:
            af.check_events()
            af.update_screen(self.screen, self.settings, self.bus_sprite_groups, self.tube_sprite_groups)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ta = TflApp()
    ta._run_game()