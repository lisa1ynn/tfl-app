import sys
import pygame
from settings import Settings
from classes.vehicle import Bus, Tube


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

        self._create_vehicles()

    def run_game(self):
        """Start the main loop for the app."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)

        # Update vehicles
        self._update_vehicles()

        # Draw all sprites
        self.buses.draw(self.screen)
        self.tubes.draw(self.screen)

        pygame.display.flip()

    def _create_bus(self):
        """Create a bus and place it in the row."""
        bus = Bus()
        bus.rect.x = self.settings.startstop1_x
        bus.rect.y = self.settings.startstop1_y
        self.buses.add(bus)

    def _create_tube(self):
        """Create a bus and place it in the row."""
        tube = Tube()
        tube.rect.x = self.settings.startstop2_x
        tube.rect.y = self.settings.startstop2_y
        self.tubes.add(tube)

    def _create_vehicles(self):
        """Update the positions of all vehicles."""
        self._create_bus()
        self._create_tube()

    def _update_vehicles(self):
        """Update the positions of all vehicles."""
        self.buses.update(1,0)
        self.tubes.update(-1,0)

        # Get rid of vehicles that have arrived.
        for bus in self.buses.copy():
            if bus.rect.right >= self.settings.startstop2_x:
                self.buses.remove(bus)

        # Get rid of vehicles that have arrived.
        for tube in self.tubes.copy():
            if tube.rect.left <= self.settings.startstop1_x:
                self.tubes.remove(tube)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ta = TflApp()
    ta.run_game()