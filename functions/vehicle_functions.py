from classes.vehicle import Bus, Tube

def create_bus(settings, buses):
    """Create a bus and place it in the row."""
    bus_300_east = Bus()
    bus_300_east.rect.x = settings.busstop_other3_x
    bus_300_east.rect.y = settings.busstop_other3_y
    buses.add(bus_300_east)

def create_tube(settings, tubes):
    """Create a bus and place it in the row."""
    tube_northern_nort = Tube()
    tube_northern_nort.rect.x = settings.tubestop_holborn_x
    tube_northern_nort.rect.y = settings.tubestop_holborn_y
    tubes.add(tube_northern_nort)

def create_vehicles(settings, tubes, buses):
    """Update the positions of all vehicles."""
    create_bus(settings, buses)
    create_tube(settings, tubes)

def update_vehicles(settings, tubes, buses):
    """Update the positions of all vehicles."""
    buses.update(1, 0)
    tubes.update(-1, 0)

    # Get rid of vehicles that have arrived.
    for bus in buses.copy():
        if bus.rect.right >= settings.busstop_other4_x:
            buses.remove(bus)

    # Get rid of vehicles that have arrived.
    for tube in tubes.copy():
        if tube.rect.left <= settings.tubestop_tottenhamcourtroad_x:
            tubes.remove(tube)