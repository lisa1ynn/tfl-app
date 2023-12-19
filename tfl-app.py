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
        self.bus19_east = pygame.sprite.Group()
        self.bus19_west = pygame.sprite.Group()
        self.bus38_east = pygame.sprite.Group()
        self.bus38_west = pygame.sprite.Group()
        self.bus55_east = pygame.sprite.Group()
        self.bus55_west = pygame.sprite.Group()
        self.bus243_east = pygame.sprite.Group()
        self.bus243_west = pygame.sprite.Group()

        # Tube Sprite Groups
        self.piccadilly_north = pygame.sprite.Group()
        self.piccadilly_south = pygame.sprite.Group()
        self.central_east = pygame.sprite.Group()
        self.central_west = pygame.sprite.Group()

        vf.create_vehicle(self.settings,self.bus17_north, self.bus17_south, self.bus46_north, self.bus46_south, self.bus19_east,
              self.bus19_west, self.bus38_east, self.bus38_west, self.bus55_east, self.bus55_west,
              self.bus243_east, self.bus243_west, self.piccadilly_north, self.piccadilly_south, self.central_east,
              self.central_west)


    def _run_game(self):
        """Start the main loop for the app."""
        while True:
            af.check_events()
            af.update_screen(self.settings, self.screen, self.bus17_north, self.bus17_south, self.bus46_north,
                             self.bus46_south, self.bus19_east, self.bus19_west, self.bus38_east, self.bus38_west,
                             self.bus55_east, self.bus55_west, self.bus243_east, self.bus243_west,
                             self.piccadilly_north, self.piccadilly_south, self.central_east, self.central_west)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ta = TflApp()
    ta._run_game()