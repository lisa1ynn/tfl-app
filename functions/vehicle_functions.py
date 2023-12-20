from classes.vehicle import Bus, Tube
from classes.json_TFL import Connection

def continuously_create_vehicles(settings, bus_sprite_groups, tube_sprite_groups, added_tubes, added_buses):
    """Continuously update vehicles based on live data."""
    # Logic to fetch live data and create vehicles
    for group_name, group_data in settings.tube_groups_dict.items():
        if group_name in tube_sprite_groups:
            conn = Connection(group_data['third_station_id'], group_data['lineID'], group_data['direction'])
            api_dict = conn.call()
            print(f"{group_name} data: {api_dict} ")
            for vehicle_id, api_data in api_dict.items():
                if api_data["current_location"].startswith(f"At {group_data['first_station_name']}"):
                    print(f"if 1 - vehicle at station: {vehicle_id}")
                    if vehicle_id not in added_tubes:
                        tube_group = tube_sprite_groups[group_name]
                        new_tube = Tube(rotation_angle=group_data['rotation_angle'])
                        new_tube.rect.x = group_data['first_station_x']
                        new_tube.rect.y = group_data['first_station_y']
                        tube_group.add(new_tube)
                        added_tubes.add(vehicle_id)

    # Logic to fetch live data and create vehicles
    for group_name, group_data in settings.bus_groups_dict.items():
        if group_name in bus_sprite_groups:
            conn = Connection(group_data['first_station_id'], group_data['lineID'], group_data['direction'])
            api_dict = conn.call()
            print(f"{group_name} data: {api_dict} ")
            for vehicle_id, api_data in api_dict.items():
                if api_data["time_to_station"] <= 30:
                    print(f"if 1 - vehicle close to station: {vehicle_id}")
                    if vehicle_id not in added_buses:
                        bus_group = bus_sprite_groups[group_name]
                        new_bus = Bus(rotation_angle=group_data['rotation_angle'])
                        new_bus.rect.x = group_data['first_station_x']
                        new_bus.rect.y = group_data['first_station_y']
                        bus_group.add(new_bus)
                        added_buses.add(vehicle_id)


def update_vehicles(settings, bus_sprite_groups, tube_sprite_groups):
    for group_name, group_data in settings.bus_groups_dict.items():
        if group_name in bus_sprite_groups:
            direction_x = group_data['direction_x']
            direction_y = group_data['direction_y']
            bus_sprite_groups[group_name].update(settings, direction_x, direction_y)

    # Update vehicles based on tube_groups_dict
    for group_name, group_data in settings.tube_groups_dict.items():
        if group_name in tube_sprite_groups:
            for tube in tube_sprite_groups[group_name].sprites():  # Iterate through the sprites in the group
                if group_name == "central_east" and tube.rect.x >= group_data['second_station_x']:
                    direction_x = 1
                    direction_y = 1
                    tube.change_rotation_angle(315)
                elif group_name == "central_west" and tube.rect.x <= group_data['second_station_x']:
                    direction_x = -1
                    direction_y = 0
                    tube.change_rotation_angle(180)
                else:
                    direction_x = group_data['direction_x']
                    direction_y = group_data['direction_y']
                tube.update(settings, direction_x, direction_y)


    # Remove vehicle from sprite group when done.
    for group_name, group_data in settings.bus_groups_dict.items():
        if group_name in bus_sprite_groups:
            for bus in bus_sprite_groups[group_name].copy():
                if bus.rect.x == group_data['third_station_x'] and bus.rect.y == group_data['third_station_y']:
                    bus_sprite_groups[group_name].remove(bus)

    for group_name, group_data in settings.tube_groups_dict.items():
        if group_name in tube_sprite_groups:
            for tube in tube_sprite_groups[group_name].copy():
                if tube.rect.x == group_data['third_station_x'] and tube.rect.y == group_data['third_station_y']:
                    tube_sprite_groups[group_name].remove(tube)

