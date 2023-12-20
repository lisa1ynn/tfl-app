from classes.vehicle import Bus, Tube
from classes.json_TFL import Connection
import time

#def create_vehicle(settings, bus_sprite_groups, tube_sprite_groups):
    #""" Create buses based on bus_groups_dict"""
    # for group_name, group_data in settings.bus_groups_dict.items():
        # if group_name in bus_sprite_groups:
            # bus_group = bus_sprite_groups[group_name]
            # bus = Bus(rotation_angle=group_data['rotation_angle'])
            # bus.rect.x = group_data['first_station_x']
            # bus.rect.y = group_data['first_station_y']
            # bus_group.add(bus)

def continuously_create_vehicles(settings, bus_sprite_groups, tube_sprite_groups, added_tubes, added_buses):
    """Continuously update vehicles based on live data."""
    print('added_tubes: ', added_tubes)
    # Logic to fetch live data and create vehicles
    for group_name, group_data in settings.tube_groups_dict.items():
        if group_name in tube_sprite_groups:
            conn = Connection(group_data['third_station_id'], group_data['lineID'])
            api_dict = conn.call()
            for vehicle_id, api_data in api_dict.items():
                if api_data["current_location"].startswith(f"At {group_data['first_station_name']}"):
                    if vehicle_id not in added_tubes:
                        tube_group = tube_sprite_groups[group_name]
                        new_tube = Tube(rotation_angle=group_data['rotation_angle'])
                        new_tube.rect.x = group_data['first_station_x']
                        new_tube.rect.y = group_data['first_station_y']
                        tube_group.add(new_tube)
                        added_tubes.add(vehicle_id)

    print('added_buses: ', added_buses)
    # Logic to fetch live data and create vehicles
    for group_name, group_data in settings.bus_groups_dict.items():
        if group_name in bus_sprite_groups:
            conn = Connection(group_data['first_station_id'], group_data['lineID'])
            api_dict = conn.call()
            for vehicle_id, api_data in api_dict.items():
                if api_data["time_to_station"] <= 30:
                    if vehicle_id not in added_buses:
                        bus_group = bus_sprite_groups[group_name]
                        new_bus = Bus(rotation_angle=group_data['rotation_angle'])
                        new_bus.rect.x = group_data['first_station_x']
                        new_bus.rect.y = group_data['first_station_y']
                        bus_group.add(new_bus)
                        added_buses.add(vehicle_id)


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
