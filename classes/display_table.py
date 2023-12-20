from tabulate import tabulate
from json_TFL import Connection

class Display:
    def __init__(self, station_id, line_ids, time_for_arrival):
        self.connections = [Connection(station_id, line_id) for line_id in line_ids]
        self.time_for_arrival = time_for_arrival

    def display_timetable(self, table_data):
        headers = ["Line", "Towards", "Time to Station"]
        print(tabulate(table_data, headers=headers, tablefmt="pretty"))

    def get_timetable(self):
        table_data = []

        for connection in self.connections:
            data = connection.call()
            if data:
                table_data.extend(self.process_data(data, line_ids))

        if table_data:
            self.display_timetable(table_data)

    def process_data(self, data, line_id):
        if not data:
            return []

        table_data = []

        for entry in data.values():
            line_name = entry.get('line')
            direction = entry.get('direction')
            towards_str = entry.get('towards')
            time_to_station = entry.get('time_to_station')
            towards_float = float(time_to_station)
            towards_min = round(towards_float / 60)

            # Order arrivals and append
            if time_to_station < self.time_for_arrival:
                table_data.append([line_name, direction, towards_min])
        table_data.sort(key=lambda x: x[2])

        return table_data


if __name__ == "__main__":
    # input
    station_id = "940GZZLUOXC"
    line_ids = ["central"]
    time_for_arrival = 600  # Adjust as as you want

    display_instance = Display(station_id, line_ids, time_for_arrival)
    display_instance.get_timetable()
