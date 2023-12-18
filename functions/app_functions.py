import sys
import pygame
from functions import vehicle_functions as vf, infrastructure_functions as inf



def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, bus17_north,bus17_south,bus46_north,bus46_south,bus19_north,bus19_south,
                  bus38_north,bus38_south,bus55_north,bus55_south,bus243_north,bus243_south,picadilly_north,
                  picadilly_south,central_east,central_west):
    """Update images on the screen, and flip to the new screen."""
    screen.fill(settings.bg_color)

    # Update vehicles
    vf.update_vehicles(screen, bus17_north, bus17_south,bus46_north,bus46_south,bus19_north,bus19_south,bus38_north,
                       bus38_south,bus55_north,bus55_south,bus243_north,bus243_south,picadilly_north,picadilly_south,
                       central_east,central_west)

    # Draw all sprites
    bus17_north.draw(screen)
    bus17_south.draw(screen)
    bus46_north.draw(screen)
    bus46_south.draw(screen)
    bus19_north.draw(screen)
    bus19_south.draw(screen)
    bus38_north.draw(screen)
    bus38_south.draw(screen)
    bus55_north.draw(screen)
    bus55_south.draw(screen)
    bus243_north.draw(screen)
    bus243_south.draw(screen)
    picadilly_north.draw(screen)
    picadilly_south.draw(screen)
    central_east.draw(screen)
    central_west.draw(screen)

    inf.create_infratructrure(screen, settings)
    pygame.display.flip()

