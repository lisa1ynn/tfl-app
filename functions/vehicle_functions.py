from classes.vehicle import Bus, Tube

def create_vehicle(settings, vehicle_group):
    """Create a bus and place it in the row."""
    bus = Bus()
    bus.rect.x = settings.busstop_other3_x
    bus.rect.y = settings.busstop_other3_y
    vehicle_group.add(bus)

def create_tube(settings, tubes):
    """Create a bus and place it in the row."""
    tube_northern_nort = Tube()
    tube_northern_nort.rect.x = settings.tubestop_holborn_x
    tube_northern_nort.rect.y = settings.tubestop_holborn_y
    tubes.add(tube_northern_nort)


def update_vehicles(screen, bus17_north, bus17_south, bus46_north, bus46_south, bus19_north, bus19_south, bus38_north,
                    bus38_south, bus55_north, bus55_south, bus243_north, bus243_south, picadilly_north, picadilly_south,
                    central_east, central_west):
    """Update the positions of all vehicles."""
    bus17_north.update(1, 0)
    bus17_south.update(1, 0)
    bus46_north.update(1, 0)
    bus46_south.update(1, 0)
    bus19_north.update(1, 0)
    bus19_south.update(1, 0)
    bus38_north.update(1, 0)
    bus38_south.update(1, 0)
    bus55_north.update(1, 0)
    bus55_south.update(1, 0)
    bus243_north.update(1, 0)
    bus243_south.update(1, 0)
    picadilly_north.update(1, 0)
    picadilly_south.update(1, 0)
    central_east.update(1, 0)
    central_west.update(1, 0)

    groups = [bus17_north, bus17_south, bus46_north, bus46_south, bus19_north, bus19_south, bus38_north,
              bus38_south, bus55_north, bus55_south, bus243_north, bus243_south, picadilly_north,
              picadilly_south, central_east, central_west]

    # Get rid of vehicles that disappear from the screen.
    for group in groups:
        for vehicle in group.copy():
            if not screen.get_rect().colliderect(vehicle.rect):
                group.remove(vehicle)
