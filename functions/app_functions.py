import sys
import pygame
from functions import vehicle_functions as vf, infrastructure_functions as inf


def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, buses, tubes):
    """Update images on the screen, and flip to the new screen."""
    screen.fill(settings.bg_color)

    # Update vehicles
    vf.update_vehicles(settings, tubes, buses)

    # Draw all sprites
    buses.draw(screen)
    tubes.draw(screen)
    inf.create_infratructrure(screen)

    pygame.display.flip()

