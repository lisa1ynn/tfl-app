import pygame
from settings import Settings
from functions import app_functions as af, vehicle_functions as vf


class TflApp:
    """Overall class to manage app assets and behavior."""

    def __init__(self):
        """Initialize the app, and create app resources."""
        pygame.init()
        pygame.display.set_caption("Tfl App")
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


        # Bus Sprite Groups
        self.bus17_north = pygame.sprite.Group()
        self.bus17_south = pygame.sprite.Group()
        self.bus46_north = pygame.sprite.Group()
        self.bus46_south = pygame.sprite.Group()
        self.bus19_north = pygame.sprite.Group()
        self.bus19_south = pygame.sprite.Group()
        self.bus38_north = pygame.sprite.Group()
        self.bus38_south = pygame.sprite.Group()
        self.bus55_north = pygame.sprite.Group()
        self.bus55_south = pygame.sprite.Group()
        self.bus243_north = pygame.sprite.Group()
        self.bus243_south = pygame.sprite.Group()

        # Tube Sprite Groups
        self.picadilly_north = pygame.sprite.Group()
        self.picadilly_south = pygame.sprite.Group()
        self.central_east = pygame.sprite.Group()
        self.central_west = pygame.sprite.Group()

        # Create vehicles
        for i in (self.bus17_north, self.bus17_south, self.bus46_north, self.bus46_south, self.bus19_north,
                  self.bus19_south, self.bus38_north, self.bus38_south, self.bus55_north, self.bus55_south,
                  self.bus243_north, self.bus243_south, self.picadilly_north, self.picadilly_south, self.central_east,
                  self.central_west):
            vf.create_vehicle(self.settings, i)


    def _run_game(self):
        """Start the main loop for the app."""
        while True:
            af.check_events()
            af.update_screen(self.settings, self.screen, self.bus17_north, self.bus17_south, self.bus46_north,
                             self.bus46_south, self.bus19_north, self.bus19_south, self.bus38_north, self.bus38_south,
                             self.bus55_north, self.bus55_south, self.bus243_north, self.bus243_south,
                             self.picadilly_north, self.picadilly_south, self.central_east, self.central_west)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ta = TflApp()
    ta._run_game()