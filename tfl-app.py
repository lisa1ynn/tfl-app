import pygame
from classes.settings import Settings
from functions import app_functions as af, vehicle_functions as vf
from classes.json_TFL import Connection
from classes.display_table import Display
import threading
import time


class TflApp:
    """Overall class to manage app assets and behavior."""

    def __init__(self):
        """Initialize the app, and create app resources."""
        pygame.init()
        pygame.display.set_caption("Tfl App")
        pygame.font.init()
        self.font = pygame.font.Font(None, 20)  # Adjust the font size as needed

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bus_dict_items = self.settings.bus_groups_dict.items()
        self.tube_dict_items = self.settings.tube_groups_dict.items()

        # Bus and Tube Sprite Groups
        self.bus_sprite_groups = {}
        self.tube_sprite_groups = {}

        # Dictionary to keep track of added vehicles that are already on the screen
        self.added_tubes = set()
        self.added_buses = set()

        for group_name, group_data in self.bus_dict_items:
            self.bus_sprite_groups[group_name] = pygame.sprite.Group()

        for group_name, group_data in self.tube_dict_items:
            self.tube_sprite_groups[group_name] = pygame.sprite.Group()

        self.display_instance_Holborn = Display("940GZZLUHBN", "central,piccadilly", 600, "all")
        self.display_instance_BUS_EW = Display("490007391E", "55,243,19,38", 1500, "all")
        self.display_instance_BUS_NS = Display("490008165B", "17,46", 1500, "all")

    def run_game(self):
        """Start the main loop for the app."""
        while True:
            af.check_events()
            af.update_screen(self.screen, self.settings, self.bus_sprite_groups, self.tube_sprite_groups, self.display_instance_Holborn, self.display_instance_BUS_EW, self.display_instance_BUS_NS, self.font)

    def run_vehicle_creation(self):
        while True:
            vf.continuously_create_vehicles(
                self.settings, self.bus_sprite_groups, self.tube_sprite_groups, self.added_tubes, self.added_buses
            )
            time.sleep(2.5)

if __name__ == '__main__':
    # Make a game instance
    ta = TflApp()

    # Start a new thread for continuously creating vehicles
    vehicle_thread = threading.Thread(target=ta.run_vehicle_creation)
    vehicle_thread.daemon = True  # Daemonize the thread to stop it when the main thread ends
    vehicle_thread.start()

    # Run the game
    ta.run_game()
