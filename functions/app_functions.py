import sys
import pygame
from functions import vehicle_functions as vf, infrastructure_functions as inf



def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, bus17_north,bus17_south,bus46_north,bus46_south,bus19_east,bus19_west,
                  bus38_east,bus38_west,bus55_east,bus55_west,bus243_east,bus243_west,piccadilly_north,
                  piccadilly_south,central_east,central_west):

    """Update images on the screen, and flip to the new screen."""
    screen.fill(settings.bg_color)

    # Update vehicles
    vf.update_vehicles(screen, bus17_north, bus17_south,bus46_north,bus46_south,bus19_east,bus19_west,bus38_east,
                       bus38_west,bus55_east,bus55_west,bus243_east,bus243_west,piccadilly_north,piccadilly_south,
                       central_east,central_west)

    # Draw all sprites
    bus17_north.draw(screen)
    bus17_south.draw(screen)
    bus46_north.draw(screen)
    bus46_south.draw(screen)
    bus19_east.draw(screen)
    bus19_west.draw(screen)
    bus38_east.draw(screen)
    bus38_west.draw(screen)
    bus55_east.draw(screen)
    bus55_west.draw(screen)
    bus243_east.draw(screen)
    bus243_west.draw(screen)
    piccadilly_north.draw(screen)
    piccadilly_south.draw(screen)
    central_east.draw(screen)
    central_west.draw(screen)

    inf.create_infratructrure(screen, settings)
    pygame.display.flip()

