from classes.roads import Roads
from classes.stops import TubeStops, BusStops
from classes.hult import Hult
from classes.display_table import Display
import pygame

def create_infratructrure(screen):
    """Create infrastructure"""
    # Roads
    roads = Roads(screen)
    roads.draw_roads()

    # Hult
    hult = Hult(screen)
    hult.blitme()

    # Tube and bus stops data in a dictionary
    stops_data = {
        'tubestops': [
            {"name": "Chancery Lane", "x": 690, "y": 850},
            {"name": "Holborn", "x": 380, "y": 560},
            {"name": "Tottenham Court Road", "x": 40, "y": 540},
            {"name": "Russell Square", "x": 340, "y": 20},
            {"name": "Covent Garden", "x": 340, "y": 850}
        ],
        'busstops': [
            {"name": "Coley Street (HD & HC)", "x": 980, "y": 50},
            {"name": "Gray's Inn Road (B) & Clerkenwell Road (CD)", "x": 980, "y": 200},
            {"name": "Holborn Circus (H) & High Holborn (C)", "x": 980, "y": 850},
            {"name": "Red Lion Street (G & A)", "x": 500, "y": 360},
            {"name": "Gray's Inn Road (CA & CP)", "x": 800, "y": 360},
            {"name": "Rosebery Avenue (CE, CU, CW) & Clerkenwell Road (CN)", "x": 1300, "y": 360}
        ]
    }

    # Blit tube stops
    for stop in stops_data['tubestops']:
        TubeStops(screen, x=stop['x'], y=stop['y'], text=stop['name']).blitme()

    # Blit bus stops
    for stop in stops_data['busstops']:
        BusStops(screen, x=stop['x'], y=stop['y'], text=stop['name']).blitme()

    #visual for display table
    def display_table(station, line_ids,time_for_arrival,direction):
        display_instance = Display(station,line_ids,time_for_arrival,direction)
        display_instance.get_timetable(station)

"""Running example of display table if __name__ == "__main__":

    # Display timetable for Holborn station, Central and Piccadilly lines
    display_table("Holborn", ["central", "piccadilly"], 600, "all")

    pygame.display.flip()
    pygame.display.update()
    pygame.time.Clock().tick(30)"""







