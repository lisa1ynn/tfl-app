from classes.vehicle import Bus, Tube

def create_vehicle(settings, bus17_north, bus17_south, bus46_north, bus46_south, bus19_east, bus19_west, bus38_east,
                    bus38_west, bus55_east, bus55_west, bus243_east, bus243_west, piccadilly_north, piccadilly_south,
                    central_east, central_west):

    bus_groups = [bus17_north, bus17_south, bus46_north, bus46_south, bus19_east, bus19_west, bus38_east,
                    bus38_west, bus55_east, bus55_west, bus243_east, bus243_west]

    tube_groups = [piccadilly_north, piccadilly_south, central_east, central_west]

    """Create a bus and place it in the row."""
    # !!! use a dictionary to store group with corresponding???
    for bus_group in bus_groups:
        bus = Bus()
        bus.rect.x = settings.busstop_y_w_x
        bus.rect.y = settings.busstop_y_w_y
        bus_group.add(bus)

    for tube_group in tube_groups:
        tube = Tube()
        tube.rect.x = settings.tubestop_coventgarden_x
        tube.rect.y = settings.tubestop_coventgarden_y
        tube_group.add(tube)

def create_tube(settings, tubes):
    """Create a bus and place it in the row."""
    tube_northern_nort = Tube()
    tube_northern_nort.rect.x = settings.tubestop_holborn_x
    tube_northern_nort.rect.y = settings.tubestop_holborn_y
    tubes.add(tube_northern_nort)


def update_vehicles(screen, bus17_north, bus17_south, bus46_north, bus46_south, bus19_east, bus19_west, bus38_east,
                    bus38_west, bus55_east, bus55_west, bus243_east, bus243_west, piccadilly_north, piccadilly_south,
                    central_east, central_west):

    groups = [bus17_north, bus17_south, bus46_north, bus46_south, bus19_east, bus19_west, bus38_east,
              bus38_west, bus55_east, bus55_west, bus243_east, bus243_west, piccadilly_north,
              piccadilly_south, central_east, central_west]

    """Update the positions of all vehicles."""
    bus17_north.update(1, 0)
    bus17_south.update(1, 0)
    bus46_north.update(1, 0)
    bus46_south.update(1, 0)
    bus19_east.update(1, 0)
    bus19_west.update(1, 0)
    bus38_east.update(1, 0)
    bus38_west.update(1, 0)
    bus55_east.update(1, 0)
    bus55_west.update(1, 0)
    bus243_east.update(1, 0)
    bus243_west.update(1, 0)
    piccadilly_north.update(1, 0)
    piccadilly_south.update(1, 0)
    central_east.update(1, 0)
    central_west.update(1, 0)

    # Get rid of vehicles that disappear from the screen.
    for group in groups:
        for vehicle in group.copy():
            if not screen.get_rect().colliderect(vehicle.rect):
                group.remove(vehicle)
