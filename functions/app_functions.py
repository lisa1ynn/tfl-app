import sys
import pygame
from functions import vehicle_functions as vf, infrastructure_functions as inf
import time
import pygame.font


def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(screen, settings, bus_sprite_groups, tube_sprite_groups, display_instance1, display_instance2, display_instance3, font):
    """Update images on the screen, and flip to the new screen."""
    screen.fill(settings.bg_color)

    # Update vehicles
    vf.update_vehicles(settings, bus_sprite_groups, tube_sprite_groups)

    # Draw all sprites
    for group_name, group in bus_sprite_groups.items():
        group.draw(screen)
        for bus in group.sprites():
            bus.blitme_text(screen)

    for group_name, group in tube_sprite_groups.items():
        group.draw(screen)
        for tube in group.sprites():
            tube.blitme_text(screen)

    inf.create_infratructrure(screen)

    timetable_surface = display_instance1.get_timetable("Holborn", font)
    screen.blit(timetable_surface, (50, 250))  # Specify the position on the screen

    timetable_surface2 = display_instance2.get_timetable("Gray's Inn Road", font)
    screen.blit(timetable_surface2, (600, 450))  # Specify the position on the screen

    timetable_surface3 = display_instance3.get_timetable("Gray's Inn Road & Clerkenwell Road", font)
    screen.blit(timetable_surface3, (1070, 220))  # Specify the position on the screen


    pygame.display.flip()
    time.sleep(1.2)

    pygame.display.update()

