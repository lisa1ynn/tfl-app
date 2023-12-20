import sys
import pygame
from functions import vehicle_functions as vf, infrastructure_functions as inf



def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(screen, settings, bus_sprite_groups, tube_sprite_groups):
    """Update images on the screen, and flip to the new screen."""
    screen.fill(settings.bg_color)

    # Update vehicles
    vf.update_vehicles(screen, settings, bus_sprite_groups, tube_sprite_groups)

    # Draw all sprites
    for group_name, group in bus_sprite_groups.items():
        group.draw(screen)

    for group_name, group in tube_sprite_groups.items():
        group.draw(screen)

    inf.create_infratructrure(screen, settings)
    pygame.display.flip()


