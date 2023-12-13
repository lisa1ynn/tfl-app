import pygame
from classes.roads import Roads
from classes.stops import TubeStops, BusStops
from classes.hult import Hult

def create_infratructrure(screen):
    """Create infrastructure"""
    # Roads
    roads = Roads(screen)
    #Hult
    hult = Hult(screen)
    # Tube stops
    tubestop_stpauls = TubeStops(screen, x=690, y=830, text="St. Paul's")
    tubestop_holborn = TubeStops(screen, x=380, y=560, text="Holborn")
    tubestop_tottenhamcourtroad = TubeStops(screen, x=40, y=540, text="Tottenham Court Road")
    tubestop_russlesquare = TubeStops(screen, x=340, y=20, text="Rusell Square")
    tubestop_coventgarden = TubeStops(screen, x=340, y=850, text="Covent Garden")
    # Bus stops
    busstop_x = BusStops(screen, x=980, y=200, text="Stop X")
    busstop_other1 = BusStops(screen, x=980, y=50, text="Stop other 1")
    busstop_other2 = BusStops(screen, x=980, y=600, text="Stop other 2")

    busstop_y = BusStops(screen, x=800, y=360, text="Stop Y")
    busstop_other3 = BusStops(screen, x=500, y=360, text="Stop other 3")
    busstop_other4 = BusStops(screen, x=1300, y=360, text="Stop other 4")

    # build
    roads.draw_roads()
    hult.blitme()

    tubestop_stpauls.blitme()
    tubestop_holborn.blitme()
    tubestop_tottenhamcourtroad.blitme()
    tubestop_russlesquare.blitme()
    tubestop_coventgarden.blitme()

    busstop_x.blitme()
    busstop_other1.blitme()
    busstop_other2.blitme()
    busstop_y.blitme()
    busstop_other3.blitme()
    busstop_other4.blitme()







