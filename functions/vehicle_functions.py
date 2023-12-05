from classes.vehicle import Bus300East, TubeNorthernNorth

def create_bus(settings, buses):
    """Create a bus and place it in the row."""
    bus1 = Bus300East()
    bus1.rect.x = settings.station1_x
    bus1.rect.y = settings.station1_y
    buses.add(bus1)

def create_tube(settings, tubes):
    """Create a bus and place it in the row."""
    tube1 = TubeNorthernNorth()
    tube1.rect.x = settings.station2_x
    tube1.rect.y = settings.station2_y
    tubes.add(tube1)

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
        if bus.rect.right >= settings.station2_x:
            buses.remove(bus)

    # Get rid of vehicles that have arrived.
    for tube in tubes.copy():
        if tube.rect.left <= settings.station1_x:
            tubes.remove(tube)