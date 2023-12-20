from tabulate import tabulate
from classes.json_TFL import Connection
import pygame.font
import time


class Display:
    def __init__(self, station_id, line_ids, time_for_arrival, direction):
        self.connection = Connection(station_id, line_ids, direction)
        self.time_for_arrival = time_for_arrival
        self.visible = False



    def display_timetable(self, table_data, station):
        headers = ["Line", f"Time for {station}"]
        print(f"{station} Timetable:")
        # Calculate the maximum length of each column
        max_lengths = [len(str(max(row, key=lambda x: len(str(x))))) for row in zip(*table_data, headers)]

        # Print the header
        header_str = f"{max_lengths[0] * '-'}   {max_lengths[1] * '-'}"
        print(f"{max_lengths[0] * '-'}   {max_lengths[1] * '-'}")
        print(f"{headers[0]:<{max_lengths[0]}}   {headers[1]:<{max_lengths[1]}}")
        print(header_str)

        # Print each row
        for row in table_data:
            print(f"{row[0]:<{max_lengths[0]}}   {row[1]:<{max_lengths[1]}}")

        print(header_str)

        # print(tabulate(table_data, headers=headers, tablefmt="plain"))

    #def set_position(self,x,y):
        #self.x=x
        #self.y=y

    def get_timetable(self, station,font):
        data = self.connection.call()
        while data:
            table_data = self.process_data(data)
            print("count")
            time.sleep(3)
            return self.render_timetable(table_data, station, font)

        else:
            self.visible = False
            return None

    def render_timetable(self, table_data, station, font):
        headers = ["Line", f"Time for {station}"]
        timetable_text = tabulate(table_data, headers=headers, tablefmt="plain")

        # Split the timetable text into lines
        timetable_lines = timetable_text.split('\n')

        # Use Pygame's font module to render each line separately
        text_surfaces = [font.render(line, True, (255, 165, 0)) for line in timetable_lines]

        # Calculate the total height of the rendered text
        total_height = sum(surface.get_height() for surface in text_surfaces)
        max_width = max(surface.get_width() for surface in text_surfaces)

        # Create a new surface to hold the rendered text
        timetable_surface = pygame.Surface((max(surface.get_width() for surface in text_surfaces), total_height))
        timetable_surface.fill((0, 0, 0))  # Set background color to black

        # Blit each line onto the new surface
        y_offset = 0
        for surface in text_surfaces:
            x_offset = max_width - surface.get_width()  # Calculate x-coordinate for right alignment
            timetable_surface.blit(surface, (x_offset, y_offset))
            y_offset += surface.get_height()

        return timetable_surface
        # # Use Pygame's font module to render text
        # text_surface = font.render(timetable_text, True, (255, 165, 0))  # Orange color
        #
        # # Create a surface with a black background
        # background_surface = pygame.Surface(text_surface.get_size())
        # background_surface.fill((0, 0, 0))  # Black color
        #
        # # Blit the text surface onto the background surface
        # background_surface.blit(text_surface, (0, 0))
        #
        # return background_surface

    def get_timetable_surface_size(self, station, font):
        data = self.connection.call()
        if data:
            table_data = self.process_data(data)
            timetable_text = self.render_timetable(table_data, station, font)
            return timetable_text.get_size()
        else:
            self.visible = False
            return (0, 0)

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
    direction = "all"

    display_instance = Display(station_id, line_ids, time_for_arrival, direction)
    display_instance.get_timetable("Gray Inn's Road, North to South")
