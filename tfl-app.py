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

        self.buses = pygame.sprite.Group()
        self.tubes = pygame.sprite.Group()

        vf.create_vehicles(self.settings, self.tubes, self.buses)

    def _run_game(self):
        """Start the main loop for the app."""
        while True:
            af.check_events()
            af.update_screen(self.settings, self.screen, self.buses, self.tubes)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ta = TflApp()
    ta._run_game()