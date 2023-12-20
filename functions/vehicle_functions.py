from classes.vehicle import Bus, Tube
from classes.json_TFL import Connection

def create_vehicle(settings, bus_sprite_groups, tube_sprite_groups):
    """ Create buses based on bus_groups_dict"""
    # NEW DATA LOGIC
    # for group_name, group_data in settings.bus_groups_dict.items():
    #   if group_name in bus_sprite_groups:
    #       conn = Connection(group_data['last_station_i'], group_data['lineID'])
    #       conn.call()
    #           for entry, data in api_data_dict:
    #                if current_location == “At {first station}” and api_data_dict["vehicle_id"] not in bus_group:
    #                   bus_group = bus_sprite_groups[group_name]
    #                   api_data_dict["vehicle_id"] = Bus(rotation_angle=group_data['rotation_angle'])
    #                   bus.rect.x = group_data['first_station_x']
    #                   bus.rect.y = group_data['first_station_y']
    #                   bus_group.add(api_data_dict["vehicle_id"])

    for group_name, group_data in settings.bus_groups_dict.items():
        if group_name in bus_sprite_groups:
            bus_group = bus_sprite_groups[group_name]
            bus = Bus(rotation_angle=group_data['rotation_angle'])
            bus.rect.x = group_data['first_station_x']
            bus.rect.y = group_data['first_station_y']
            bus_group.add(bus)

    """ Create tubes based on tube_groups_dict"""
    for group_name, group_data in settings.tube_groups_dict.items():
        if group_name in tube_sprite_groups:
            tube_group = tube_sprite_groups[group_name]
            tube = Tube(rotation_angle=group_data['rotation_angle'])
            tube.rect.x = group_data['first_station_x']
            tube.rect.y = group_data['first_station_y']
            tube_group.add(tube)

def update_vehicles(screen, settings, bus_sprite_groups, tube_sprite_groups):
    for group_name, group_data in settings.bus_groups_dict.items():
        if group_name in bus_sprite_groups:
            direction_x = group_data['direction_x']
            direction_y = group_data['direction_y']
            bus_sprite_groups[group_name].update(settings, direction_x, direction_y)

        # Update vehicles based on tube_groups_dict
    for group_name, group_data in settings.tube_groups_dict.items():
        if group_name in tube_sprite_groups:
            direction_x = group_data['direction_x']
            direction_y = group_data['direction_y']
            tube_sprite_groups[group_name].update(settings, direction_x, direction_y)

    all_groups = [bus_sprite_groups, tube_sprite_groups]

    # Get rid of vehicles that disappear from the screen.
    # FIX!!!!
    for groups in all_groups:
        for group in groups.values():
            for vehicle in group.copy():
                if not screen.get_rect().colliderect(vehicle.rect):
                    group.remove(vehicle)
