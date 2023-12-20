from tabulate import tabulate
from json_TFL import Connection

class Display:
    def __init__(self, station_id, line_ids, time_for_arrival, direction):
        self.connection = Connection(station_id, line_ids, direction)
        self.time_for_arrival = time_for_arrival

    def display_timetable(self, table_data, station):
        headers = ["Train", f"Time for {station}"]
        print(f"{station} Timetable:")
        print(tabulate(table_data, headers=headers, tablefmt="plain"))

    def get_timetable(self, station):
            data = self.connection.call()
            if data:
                table_data = self.process_data(data)
                self.display_timetable(table_data, station)

    def process_data(self, data):
        if not data:
            return []

        table_data = []

        for entry in data.values():
            line = entry.get('line')
            towards_str = entry.get('towards_station')
            time_to_station = entry.get('time_to_station')
            towards_float = float(time_to_station)
            towards_min = round(towards_float / 60)

            # Order arrivals and append
            if time_to_station < self.time_for_arrival:
                table_data.append([line +" "+ towards_str, towards_min])

        # Sort based on time_to_station
        table_data.sort(key=lambda x: x[1])

        return table_data

if __name__ == "__main__":
    station_id = "940GZZLUHBN"
    line_ids = "central,piccadilly"
    time_for_arrival = 600 # Adjust as needed
    direction = "all"  # Replace with the actual direction

    display_instance = Display(station_id, line_ids, time_for_arrival, direction)
    display_instance.get_timetable("Holborn stations")

#Gray Inn's Road
    station_id = "490008165B"
    line_ids = "17,46"
    time_for_arrival = 6000 # Adjust as needed
    direction = "all"  # Replace with the actual direction

    display_instance = Display(station_id, line_ids, time_for_arrival, direction)
    display_instance.get_timetable("Gray Inn's Road, North to South")

#Gray Inn's Road
    station_id = "490008165B"
    line_ids = "17,46"
    time_for_arrival = 6000 # Adjust as needed
    direction = "all"  # Replace with the actual direction

    display_instance = Display(station_id, line_ids, time_for_arrival, direction)
    display_instance.get_timetable("Gray Inn's Road, North to South")
